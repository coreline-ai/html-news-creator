"""Verify Publish re-renders the HTML from DB before deploying.

These tests focus on the contract introduced in Phase B:
- ``publish_report`` always invokes ``render_published`` first.
- ``disabled_section_ids`` is forwarded to the render helper.
- ``dry_run=True`` still renders (no Netlify call) and reports the count.
- The ``POST /api/reports/{date}/publish`` route accepts the new field
  without breaking existing callers.
- The new ``POST /api/reports/{date}/render`` route works in isolation.
"""
from __future__ import annotations

import uuid
from datetime import date as date_cls
from pathlib import Path
from unittest.mock import AsyncMock, MagicMock, patch

import pytest
from fastapi.testclient import TestClient

from app.admin.api import app
from app.db import get_db


# ---------------------------------------------------------------------------
# Shared DB stubs (mirrors test_admin_sections style)
# ---------------------------------------------------------------------------

class _ReportRow:
    def __init__(self, report_id: str, run_date: date_cls) -> None:
        self.id = report_id
        self.report_date = run_date
        self.title = "Daily"
        self.status = "draft"


class _SectionRow:
    def __init__(self, sid: str, report_id: str, order: int, title: str = "S") -> None:
        self.id = sid
        self.report_id = report_id
        self.section_order = order
        self.title = title


def _override_db(db_obj):
    async def _gen():
        yield db_obj

    app.dependency_overrides[get_db] = _gen


def _clear_override():
    async def _default():
        mock = AsyncMock()
        scalars_mock = MagicMock()
        scalars_mock.all.return_value = []
        scalars_mock.first.return_value = None
        execute_result = MagicMock()
        execute_result.scalars.return_value = scalars_mock
        execute_result.scalar.return_value = 0
        mock.execute.return_value = execute_result
        yield mock

    app.dependency_overrides[get_db] = _default


def _make_db(report=None, sections=None):
    sections = sections or []
    queue: list = []
    if report is not None:
        queue.append(report)
    if sections:
        queue.append(sections)

    def _make_result(payload):
        scalars_mock = MagicMock()
        if isinstance(payload, list):
            scalars_mock.all.return_value = payload
            scalars_mock.first.return_value = payload[0] if payload else None
        else:
            scalars_mock.all.return_value = [payload] if payload else []
            scalars_mock.first.return_value = payload
        execute_result = MagicMock()
        execute_result.scalars.return_value = scalars_mock
        return execute_result

    async def _execute(*_args, **_kwargs):
        if queue:
            return _make_result(queue.pop(0))
        return _make_result(None)

    db = AsyncMock()
    db.execute.side_effect = _execute
    db.add = MagicMock()
    db.commit = AsyncMock(return_value=None)
    return db


client = TestClient(app)


# ---------------------------------------------------------------------------
# publish_report() helper directly
# ---------------------------------------------------------------------------

@pytest.mark.asyncio
async def test_publish_report_dry_run_calls_render_with_disabled_ids():
    """dry_run still renders so disabled_section_ids must propagate."""
    from app.admin import publish as publish_module

    fake_render = AsyncMock(return_value=Path("public/news/2026-04-30-trend.html"))

    fake_session = AsyncMock()
    fake_session.__aenter__ = AsyncMock(return_value=fake_session)
    fake_session.__aexit__ = AsyncMock(return_value=None)

    with patch.object(publish_module, "render_published", fake_render), \
         patch("app.admin.publish.AsyncSessionLocal", return_value=fake_session):
        result = await publish_module.publish_report(
            "2026-04-30",
            dry_run=True,
            disabled_section_ids=["abc-123", "def-456"],
        )

    fake_render.assert_awaited_once()
    args, kwargs = fake_render.call_args
    # First positional arg is the date_kst, second is the session.
    assert args[0] == "2026-04-30"
    assert kwargs.get("disabled_section_ids") == ["abc-123", "def-456"]
    assert result["status"] == "dry_run"
    assert result["dry_run"] is True
    assert result["disabled_count"] == 2


@pytest.mark.asyncio
async def test_publish_report_real_deploy_renders_then_deploys():
    """Full path: render_published → NetlifyPublisher.deploy → status published."""
    from app.admin import publish as publish_module

    fake_render = AsyncMock(return_value=Path("public/news/2026-04-30-trend.html"))
    fake_deploy = AsyncMock(
        return_value={
            "status": "success",
            "deploy_url": "https://ai-news-5min-kr.netlify.app/2026-04-30-trend.html",
            "stdout": "",
        }
    )

    # Session for the publish step (after render): returns a Report row.
    publish_session = AsyncMock()
    publish_session.__aenter__ = AsyncMock(return_value=publish_session)
    publish_session.__aexit__ = AsyncMock(return_value=None)
    scalars_mock = MagicMock()
    scalars_mock.first.return_value = _ReportRow(
        str(uuid.uuid4()), date_cls.fromisoformat("2026-04-30")
    )
    exec_result = MagicMock()
    exec_result.scalars.return_value = scalars_mock
    publish_session.execute = AsyncMock(return_value=exec_result)
    publish_session.commit = AsyncMock(return_value=None)

    # Session for the render step (separate context manager open).
    render_session = AsyncMock()
    render_session.__aenter__ = AsyncMock(return_value=render_session)
    render_session.__aexit__ = AsyncMock(return_value=None)

    with patch.object(publish_module, "render_published", fake_render), \
         patch("app.admin.publish.AsyncSessionLocal",
               side_effect=[render_session, publish_session]), \
         patch("app.deployment.netlify.NetlifyPublisher.deploy", fake_deploy), \
         patch("app.admin.publish.settings") as mock_settings:
        mock_settings.netlify_auth_token = "tok"
        mock_settings.netlify_site_id = "site"
        result = await publish_module.publish_report(
            "2026-04-30",
            dry_run=False,
            disabled_section_ids=["x"],
        )

    fake_render.assert_awaited_once()
    fake_deploy.assert_awaited_once()
    assert result["status"] == "success"
    assert result["dry_run"] is False
    assert result["disabled_count"] == 1


# ---------------------------------------------------------------------------
# Route — POST /api/reports/{date}/publish accepts disabled_section_ids
# ---------------------------------------------------------------------------

def test_publish_route_forwards_disabled_section_ids():
    report_id = str(uuid.uuid4())
    report = _ReportRow(report_id, date_cls.fromisoformat("2026-04-30"))
    _override_db(_make_db(report=report))

    fake_publish = AsyncMock(
        return_value={
            "status": "dry_run",
            "deployed_url": "https://ai-news-5min-kr.netlify.app/2026-04-30-trend.html",
            "report_date": "2026-04-30",
            "dry_run": True,
            "rendered_path": "public/news/2026-04-30-trend.html",
            "disabled_count": 2,
        }
    )
    try:
        with patch("app.admin.publish.publish_report", fake_publish):
            resp = client.post(
                "/api/reports/2026-04-30/publish",
                json={
                    "dry_run": True,
                    "disabled_section_ids": ["a-1", "b-2"],
                },
            )
            assert resp.status_code == 200
            body = resp.json()
            assert body["status"] == "dry_run"
            assert body["disabled_count"] == 2
            fake_publish.assert_awaited_once()
            kwargs = fake_publish.call_args.kwargs
            assert kwargs["disabled_section_ids"] == ["a-1", "b-2"]
            assert kwargs["dry_run"] is True
    finally:
        _clear_override()


def test_publish_route_backwards_compatible_without_disabled_ids():
    """Old clients posting only ``{dry_run}`` still work — no field required."""
    report = _ReportRow(str(uuid.uuid4()), date_cls.fromisoformat("2026-04-30"))
    _override_db(_make_db(report=report))

    fake_publish = AsyncMock(
        return_value={
            "status": "dry_run",
            "deployed_url": "https://ai-news-5min-kr.netlify.app/2026-04-30-trend.html",
            "report_date": "2026-04-30",
            "dry_run": True,
        }
    )
    try:
        with patch("app.admin.publish.publish_report", fake_publish):
            resp = client.post(
                "/api/reports/2026-04-30/publish", json={"dry_run": True}
            )
            assert resp.status_code == 200
            kwargs = fake_publish.call_args.kwargs
            # Empty list is fine — the helper treats it the same as None.
            assert kwargs["disabled_section_ids"] == []
    finally:
        _clear_override()


# ---------------------------------------------------------------------------
# New route — POST /api/reports/{date}/render
# ---------------------------------------------------------------------------

def test_render_route_returns_path_sections_and_disabled_count():
    report_id = str(uuid.uuid4())
    s1 = _SectionRow(str(uuid.uuid4()), report_id, 0)
    s2 = _SectionRow(str(uuid.uuid4()), report_id, 1)
    report = _ReportRow(report_id, date_cls.fromisoformat("2026-04-30"))
    # Three execute() calls: render's two (Report + Sections), then route's
    # follow-up two (Report + Sections). _make_db replays them in order.
    db = AsyncMock()
    queue: list = [report, [s1, s2], report, [s1, s2]]
    db.add = MagicMock()
    db.commit = AsyncMock(return_value=None)

    def _make_result(payload):
        scalars_mock = MagicMock()
        if isinstance(payload, list):
            scalars_mock.all.return_value = payload
            scalars_mock.first.return_value = payload[0] if payload else None
        else:
            scalars_mock.all.return_value = [payload] if payload else []
            scalars_mock.first.return_value = payload
        execute_result = MagicMock()
        execute_result.scalars.return_value = scalars_mock
        return execute_result

    async def _execute(*_a, **_k):
        if queue:
            return _make_result(queue.pop(0))
        return _make_result(None)

    db.execute.side_effect = _execute
    _override_db(db)

    fake_render = AsyncMock(
        return_value=Path("/tmp/rendered/public/news/2026-04-30-trend.html")
    )
    try:
        with patch("app.admin.render.render_published", fake_render):
            resp = client.post(
                "/api/reports/2026-04-30/render",
                json={"disabled_section_ids": [s1.id]},
            )
            assert resp.status_code == 200
            body = resp.json()
            assert "rendered_path" in body
            # one of two sections survives the disabled filter
            assert body["sections"] == 1
            assert body["disabled_count"] == 1
            fake_render.assert_awaited_once()
    finally:
        _clear_override()


def test_render_route_bad_date_returns_400():
    _override_db(_make_db())
    try:
        resp = client.post("/api/reports/oops/render", json={})
        assert resp.status_code == 400
    finally:
        _clear_override()


def test_render_route_missing_report_returns_404():
    _override_db(_make_db(report=None))
    try:
        resp = client.post("/api/reports/2099-01-01/render", json={})
        assert resp.status_code == 404
    finally:
        _clear_override()
