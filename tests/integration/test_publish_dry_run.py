"""Render + Publish (dry-run) wired end-to-end through the ASGI app.

We seed a stub Report + ReportSection set into the request-scoped DB
session, and short-circuit the *expensive* parts:

- ``app.admin.render.render_published`` is patched at the module boundary
  so the Jinja renderer + ReportArtifact write don't need a real DB or
  a live Postgres.
- ``app.admin.publish.AsyncSessionLocal`` is patched to hand out the same
  session so ``publish_report`` doesn't open a real Postgres connection.
- Netlify is never reached because ``dry_run=True``.

Contract verified:
- ``POST /api/reports/{date}/render`` returns ``{rendered_path, sections,
  disabled_count}`` and the section count drops when ``disabled_section_ids``
  is supplied.
- ``POST /api/reports/{date}/publish`` with ``dry_run=True`` returns
  ``{deployed_url, dry_run: true}`` plus the propagated ``disabled_count``.
"""
from __future__ import annotations

import uuid
from datetime import date as date_cls
from pathlib import Path
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from app.admin.api import app
from app.db import get_db

pytestmark = pytest.mark.asyncio

REPORT_DATE = "2026-05-01"


# ---------------------------------------------------------------------------
# Lightweight ORM-shaped row stubs — match the attribute reads the routes do.
# ---------------------------------------------------------------------------

class _ReportRow:
    def __init__(self, report_id: str, run_date: date_cls) -> None:
        self.id = report_id
        self.report_date = run_date
        self.title = "Daily"
        self.status = "draft"
        self.summary_ko = "요약"
        self.stats_json = {}
        self.method_json = {}
        self.created_at = None
        self.updated_at = None
        self.published_at = None


class _SectionRow:
    def __init__(self, sid: str, report_id: str, order: int) -> None:
        self.id = sid
        self.report_id = report_id
        self.section_order = order
        self.title = f"Section {order}"
        self.lead = None
        self.fact_summary = f"fact-{order}"
        self.social_signal_summary = None
        self.inference_summary = None
        self.caution = None
        self.image_evidence_json = []
        self.sources_json = []
        self.confidence = None
        self.importance_score = 1.0
        self.tags_json = []


# ---------------------------------------------------------------------------
# DB override helper — replays a deterministic queue of execute() results.
# ---------------------------------------------------------------------------

def _install_db_override(payload_queue: list):
    """Override get_db so each ``execute()`` pops the next payload.

    Each entry in ``payload_queue`` is either a single row or a list. Tests
    reset by removing the override (the autouse fixture in conftest also
    cleans up after the test exits).
    """
    queue = list(payload_queue)

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

    async def _gen():
        yield db

    app.dependency_overrides[get_db] = _gen
    return db


# ---------------------------------------------------------------------------
# POST /api/reports/{date}/render
# ---------------------------------------------------------------------------

async def test_render_route_returns_path_and_section_counts(async_client):
    """Render with no disabled ids — sections count equals total rows."""
    report_id = str(uuid.uuid4())
    section_ids = [str(uuid.uuid4()) for _ in range(3)]
    sections = [_SectionRow(sid, report_id, i) for i, sid in enumerate(section_ids)]
    report = _ReportRow(report_id, date_cls.fromisoformat(REPORT_DATE))

    # The route's own follow-up query (after render_published commits) needs
    # the Report row + section list. render_published itself is mocked, so
    # only the trailing two execute() calls actually fire on this session.
    _install_db_override([report, sections])

    fake_render = AsyncMock(
        return_value=Path(f"/abs/public/news/{REPORT_DATE}-trend.html")
    )
    with patch("app.admin.render.render_published", fake_render):
        resp = await async_client.post(
            f"/api/reports/{REPORT_DATE}/render", json={}
        )

    assert resp.status_code == 200, resp.text
    body = resp.json()
    assert "rendered_path" in body and body["rendered_path"]
    assert body["sections"] == 3
    assert body["disabled_count"] == 0
    fake_render.assert_awaited_once()


async def test_render_route_drops_disabled_sections(async_client):
    """``disabled_section_ids`` shrinks the reported section count."""
    report_id = str(uuid.uuid4())
    section_ids = [str(uuid.uuid4()) for _ in range(3)]
    sections = [_SectionRow(sid, report_id, i) for i, sid in enumerate(section_ids)]
    report = _ReportRow(report_id, date_cls.fromisoformat(REPORT_DATE))

    _install_db_override([report, sections])

    fake_render = AsyncMock(
        return_value=Path(f"/abs/public/news/{REPORT_DATE}-trend.html")
    )
    disabled = [section_ids[0], section_ids[2]]
    with patch("app.admin.render.render_published", fake_render):
        resp = await async_client.post(
            f"/api/reports/{REPORT_DATE}/render",
            json={"disabled_section_ids": disabled},
        )

    assert resp.status_code == 200, resp.text
    body = resp.json()
    # 3 sections - 2 disabled = 1 surviving
    assert body["sections"] == 1
    assert body["disabled_count"] == 2
    # Render helper saw the disabled list verbatim.
    kwargs = fake_render.call_args.kwargs
    assert kwargs["disabled_section_ids"] == disabled


# ---------------------------------------------------------------------------
# POST /api/reports/{date}/publish — dry_run end-to-end
# ---------------------------------------------------------------------------

async def test_publish_dry_run_returns_deployed_url_without_netlify(
    async_client,
):
    """``dry_run=True`` skips Netlify entirely but still re-renders."""
    report_id = str(uuid.uuid4())
    report = _ReportRow(report_id, date_cls.fromisoformat(REPORT_DATE))

    # The publish route validates the report exists *before* delegating to
    # ``publish_report``, so we need the Report row available on the
    # request-scoped session at least once.
    _install_db_override([report])

    fake_render = AsyncMock(
        return_value=Path(f"public/news/{REPORT_DATE}-trend.html")
    )
    # publish_report opens its own AsyncSessionLocal — patch that too so the
    # render step inside publish doesn't hit Postgres.
    fake_session = AsyncMock()
    fake_session.__aenter__ = AsyncMock(return_value=fake_session)
    fake_session.__aexit__ = AsyncMock(return_value=None)

    with patch("app.admin.publish.render_published", fake_render), \
         patch("app.admin.publish.AsyncSessionLocal", return_value=fake_session):
        resp = await async_client.post(
            f"/api/reports/{REPORT_DATE}/publish",
            json={"dry_run": True},
        )

    assert resp.status_code == 200, resp.text
    body = resp.json()
    assert body["dry_run"] is True
    assert body["deployed_url"].endswith(f"{REPORT_DATE}-trend.html")
    # No disabled ids posted → empty list propagates.
    assert body["disabled_count"] == 0
    fake_render.assert_awaited_once()


async def test_publish_dry_run_propagates_disabled_section_ids(async_client):
    """``disabled_section_ids`` reaches the helper and inflates the count."""
    report_id = str(uuid.uuid4())
    report = _ReportRow(report_id, date_cls.fromisoformat(REPORT_DATE))
    _install_db_override([report])

    fake_render = AsyncMock(
        return_value=Path(f"public/news/{REPORT_DATE}-trend.html")
    )
    fake_session = AsyncMock()
    fake_session.__aenter__ = AsyncMock(return_value=fake_session)
    fake_session.__aexit__ = AsyncMock(return_value=None)

    disabled = ["sec-a", "sec-b", "sec-c"]
    with patch("app.admin.publish.render_published", fake_render), \
         patch("app.admin.publish.AsyncSessionLocal", return_value=fake_session):
        resp = await async_client.post(
            f"/api/reports/{REPORT_DATE}/publish",
            json={"dry_run": True, "disabled_section_ids": disabled},
        )

    assert resp.status_code == 200, resp.text
    body = resp.json()
    assert body["disabled_count"] == 3
    assert body["dry_run"] is True
    # render_published received the verbatim list (publish.publish_report
    # passes it as a positional kwarg).
    _, kwargs = fake_render.call_args
    assert kwargs["disabled_section_ids"] == disabled
