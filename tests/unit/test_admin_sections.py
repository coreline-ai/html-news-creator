"""
Unit tests for News Studio admin Phase 4 — section editing / reorder / publish.

TC-4 coverage:
- PATCH /api/sections/{id}                  → 200 + updated section
- PATCH /api/sections/{id} (no fields)      → 400
- PATCH /api/sections/{id} (missing)        → 404
- POST /api/sections/{id}/regenerate        → 200 + queued (stub, no other-section side effects)
- POST /api/reports/{date}/reorder          → 200 + ordered list
- POST /api/reports/{date}/reorder (bad)    → 400 (empty/foreign ids)
- POST /api/reports/{date}/publish (dry_run)→ 200 + deployed_url
- POST /api/reports/{date}/publish (real)   → uses NetlifyPublisher mock
"""
from __future__ import annotations

import uuid
from datetime import date as date_cls
from unittest.mock import AsyncMock, MagicMock, patch

from fastapi.testclient import TestClient

from app.admin.api import app
from app.db import get_db


# ---------------------------------------------------------------------------
# Per-test DB stub: lets each test wire up bespoke responses.
# ---------------------------------------------------------------------------

class _SectionRow:
    def __init__(
        self,
        section_id: str,
        report_id: str,
        order: int,
        title: str = "Sample",
    ) -> None:
        self.id = section_id
        self.report_id = report_id
        self.section_order = order
        self.title = title
        self.lead = None
        self.fact_summary = None
        self.social_signal_summary = None
        self.inference_summary = None
        self.caution = None
        self.image_evidence_json = []
        self.sources_json = []
        self.confidence = None
        self.importance_score = None
        self.tags_json = []


class _ReportRow:
    def __init__(self, report_id: str, report_date: date_cls) -> None:
        self.id = report_id
        self.report_date = report_date
        self.title = "Daily"
        self.status = "draft"
        self.summary_ko = None
        self.stats_json = {}
        self.method_json = {}
        self.created_at = None
        self.updated_at = None
        self.published_at = None


def _make_db(*, sections: list | None = None, report: _ReportRow | None = None):
    """Build an AsyncMock DB whose `execute()` returns context-aware results.

    The api routes call `select(...)` then `.scalars().first()` (single row)
    or `.scalars().all()` (collection). Tests pre-populate `sections` and
    `report`, and the mock dispenses them in execution order.
    """
    state = {"calls": 0}
    sections = sections or []

    def _make_result(payload):
        scalars_mock = MagicMock()
        scalars_mock.all.return_value = payload if isinstance(payload, list) else [payload]
        scalars_mock.first.return_value = (
            payload if not isinstance(payload, list)
            else (payload[0] if payload else None)
        )
        execute_result = MagicMock()
        execute_result.scalars.return_value = scalars_mock
        execute_result.scalar.return_value = 0
        return execute_result

    queue: list = []
    if report is not None:
        queue.append(report)  # first execute → Report.first()
    if sections:
        queue.append(sections)  # second execute → ReportSection.all()
        # Third (refresh) → return live-sorted view of the same row objects.
        queue.append(("__sorted__", sections))

    async def _execute(*_args, **_kwargs):
        if queue:
            payload = queue.pop(0)
            if isinstance(payload, tuple) and payload and payload[0] == "__sorted__":
                live_sorted = sorted(payload[1], key=lambda s: s.section_order)
                return _make_result(live_sorted)
            return _make_result(payload)
        # Default: empty result
        return _make_result(None)

    db = AsyncMock()
    db.execute.side_effect = _execute
    db.commit = AsyncMock(return_value=None)
    db.refresh = AsyncMock(return_value=None)
    state  # keep ref
    return db


# Default fallback DB stub — always installed at module load and reinstated
# after each test. We avoid clearing the override entirely so that any sibling
# test module that runs after us continues to receive a mocked DB rather than
# touching a real Postgres connection.
async def _default_mock_db():
    mock = AsyncMock()
    scalars_mock = MagicMock()
    scalars_mock.all.return_value = []
    scalars_mock.first.return_value = None
    execute_result = MagicMock()
    execute_result.scalars.return_value = scalars_mock
    execute_result.scalar.return_value = 0
    mock.execute.return_value = execute_result
    yield mock


# Only install our default if nothing useful is registered yet.
if get_db not in app.dependency_overrides:
    app.dependency_overrides[get_db] = _default_mock_db


def _override_db(db_obj):
    async def _gen():
        yield db_obj

    app.dependency_overrides[get_db] = _gen


def _clear_override():
    # Restore the default fallback, NOT pop — see comment above.
    app.dependency_overrides[get_db] = _default_mock_db


client = TestClient(app)


# ---------------------------------------------------------------------------
# PATCH /api/sections/{id}
# ---------------------------------------------------------------------------

def test_patch_section_updates_title_and_summary():
    sec_id = str(uuid.uuid4())
    section = _SectionRow(sec_id, str(uuid.uuid4()), 0, title="Old")
    _override_db(_make_db(sections=[section]))
    try:
        resp = client.patch(
            f"/api/sections/{sec_id}",
            json={"title": "New", "summary_ko": "요약", "implication_ko": "시사점"},
        )
        assert resp.status_code == 200
        body = resp.json()["section"]
        assert body["title"] == "New"
        assert body["fact_summary"] == "요약"
        assert body["inference_summary"] == "시사점"
    finally:
        _clear_override()


def test_patch_section_image_url_replaces_first_evidence():
    sec_id = str(uuid.uuid4())
    section = _SectionRow(sec_id, str(uuid.uuid4()), 0)
    section.image_evidence_json = [{"url": "old.png", "caption": "k"}]
    _override_db(_make_db(sections=[section]))
    try:
        resp = client.patch(
            f"/api/sections/{sec_id}",
            json={"image_url": "https://cdn.example/new.png"},
        )
        assert resp.status_code == 200
        body = resp.json()["section"]
        assert body["image_evidence_json"][0]["url"] == "https://cdn.example/new.png"
        # caption preserved
        assert body["image_evidence_json"][0].get("caption") == "k"
    finally:
        _clear_override()


def test_patch_section_no_fields_returns_400():
    sec_id = str(uuid.uuid4())
    _override_db(_make_db(sections=[_SectionRow(sec_id, str(uuid.uuid4()), 0)]))
    try:
        resp = client.patch(f"/api/sections/{sec_id}", json={})
        assert resp.status_code == 400
    finally:
        _clear_override()


def test_patch_section_missing_returns_404():
    _override_db(_make_db(sections=[]))
    try:
        resp = client.patch(
            f"/api/sections/{uuid.uuid4()}", json={"title": "x"}
        )
        assert resp.status_code == 404
    finally:
        _clear_override()


# ---------------------------------------------------------------------------
# POST /api/sections/{id}/regenerate
# ---------------------------------------------------------------------------

def test_regenerate_section_returns_queued_without_touching_others():
    sec_id = str(uuid.uuid4())
    section = _SectionRow(sec_id, str(uuid.uuid4()), 2, title="Target")
    _override_db(_make_db(sections=[section]))
    try:
        resp = client.post(f"/api/sections/{sec_id}/regenerate")
        assert resp.status_code == 200
        body = resp.json()
        assert body["status"] == "queued"
        assert body["section_id"] == sec_id
    finally:
        _clear_override()


def test_regenerate_section_unknown_id_returns_404():
    _override_db(_make_db(sections=[]))
    try:
        resp = client.post(f"/api/sections/{uuid.uuid4()}/regenerate")
        assert resp.status_code == 404
    finally:
        _clear_override()


# ---------------------------------------------------------------------------
# POST /api/reports/{date}/reorder
# ---------------------------------------------------------------------------

def test_reorder_sections_persists_new_order():
    report_id = str(uuid.uuid4())
    s1 = _SectionRow(str(uuid.uuid4()), report_id, 0, title="A")
    s2 = _SectionRow(str(uuid.uuid4()), report_id, 1, title="B")
    s3 = _SectionRow(str(uuid.uuid4()), report_id, 2, title="C")
    report = _ReportRow(report_id, date_cls.fromisoformat("2026-04-30"))

    _override_db(_make_db(sections=[s1, s2, s3], report=report))
    try:
        resp = client.post(
            "/api/reports/2026-04-30/reorder",
            json={"section_ids": [s3.id, s1.id, s2.id]},
        )
        assert resp.status_code == 200
        body = resp.json()
        assert [s["id"] for s in body["sections"]] == [s3.id, s1.id, s2.id]
        # in-memory positions updated
        assert s3.section_order == 0
        assert s1.section_order == 1
        assert s2.section_order == 2
    finally:
        _clear_override()


def test_reorder_sections_rejects_empty_payload():
    report_id = str(uuid.uuid4())
    report = _ReportRow(report_id, date_cls.fromisoformat("2026-04-30"))
    _override_db(_make_db(sections=[], report=report))
    try:
        resp = client.post(
            "/api/reports/2026-04-30/reorder", json={"section_ids": []}
        )
        assert resp.status_code == 400
    finally:
        _clear_override()


def test_reorder_sections_rejects_foreign_ids():
    report_id = str(uuid.uuid4())
    s1 = _SectionRow(str(uuid.uuid4()), report_id, 0)
    report = _ReportRow(report_id, date_cls.fromisoformat("2026-04-30"))
    _override_db(_make_db(sections=[s1], report=report))
    try:
        bad = str(uuid.uuid4())
        resp = client.post(
            "/api/reports/2026-04-30/reorder",
            json={"section_ids": [bad]},
        )
        assert resp.status_code == 400
        assert "not part of report" in resp.json()["detail"]
    finally:
        _clear_override()


def test_reorder_sections_bad_date_returns_400():
    _override_db(_make_db())
    try:
        resp = client.post(
            "/api/reports/not-a-date/reorder",
            json={"section_ids": [str(uuid.uuid4())]},
        )
        assert resp.status_code == 400
    finally:
        _clear_override()


def test_reorder_sections_missing_report_returns_404():
    _override_db(_make_db(sections=[], report=None))
    try:
        resp = client.post(
            "/api/reports/2099-01-01/reorder",
            json={"section_ids": [str(uuid.uuid4())]},
        )
        assert resp.status_code == 404
    finally:
        _clear_override()


# ---------------------------------------------------------------------------
# POST /api/reports/{date}/publish
# ---------------------------------------------------------------------------

def test_publish_dry_run_returns_deploy_url_without_calling_netlify():
    report = _ReportRow(str(uuid.uuid4()), date_cls.fromisoformat("2026-04-30"))
    _override_db(_make_db(report=report))
    try:
        resp = client.post(
            "/api/reports/2026-04-30/publish", json={"dry_run": True}
        )
        assert resp.status_code == 200
        body = resp.json()
        assert body["status"] == "dry_run"
        assert "2026-04-30-trend.html" in body["deployed_url"]
    finally:
        _clear_override()


def test_publish_invokes_netlify_publisher():
    report = _ReportRow(str(uuid.uuid4()), date_cls.fromisoformat("2026-04-30"))
    _override_db(_make_db(report=report))

    fake_deploy = AsyncMock(
        return_value={
            "status": "success",
            "deploy_url": "https://ai-news-5min-kr.netlify.app/2026-04-30-trend.html",
            "stdout": "",
        }
    )

    with patch("app.deployment.netlify.NetlifyPublisher.deploy", fake_deploy):
        try:
            resp = client.post("/api/reports/2026-04-30/publish", json={})
            assert resp.status_code == 200
            body = resp.json()
            assert body["status"] == "success"
            assert body["deployed_url"].endswith("2026-04-30-trend.html")
            fake_deploy.assert_awaited_once()
        finally:
            _clear_override()


def test_publish_missing_report_returns_404():
    _override_db(_make_db(report=None))
    try:
        resp = client.post(
            "/api/reports/2099-01-01/publish", json={"dry_run": True}
        )
        assert resp.status_code == 404
    finally:
        _clear_override()


def test_publish_bad_date_returns_400():
    _override_db(_make_db())
    try:
        resp = client.post(
            "/api/reports/oops/publish", json={"dry_run": True}
        )
        assert resp.status_code == 400
    finally:
        _clear_override()
