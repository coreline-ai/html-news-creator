"""Unit tests for ``app.admin.render.render_published``.

Covers the contract that publish-time re-renders honour:
- DB Report + ReportSection rows (ordered by ``section_order``) feed Jinja.
- ``disabled_section_ids`` removes those rows before render.
- The renderer is invoked exactly once and the file write happens through
  the existing ``JinjaRenderer.render_to_file`` (template untouched).
- A ``ReportArtifact`` row is recorded with a project-root-relative path.
- ``ValueError`` on bad date, ``LookupError`` on missing report.
"""
from __future__ import annotations

import uuid
from datetime import date as date_cls
from pathlib import Path
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from app.admin.render import render_published


# ---------------------------------------------------------------------------
# Fakes
# ---------------------------------------------------------------------------

class _FakeSection:
    def __init__(self, sid: str, order: int, title: str = "S") -> None:
        self.id = uuid.UUID(sid)
        self.section_order = order
        self.title = title
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


class _FakeReport:
    def __init__(self, report_id: str, run_date: date_cls) -> None:
        self.id = uuid.UUID(report_id)
        self.report_date = run_date
        self.title = "Daily"
        self.status = "draft"
        self.summary_ko = "요약"
        self.stats_json = {
            "total_sources": 10,
            "ai_relevant": 5,
            "clusters": 3,
            "verified": 2,
        }
        self.method_json = {}
        self.created_at = None
        self.updated_at = None
        self.published_at = None


def _make_db(report: _FakeReport | None, sections: list[_FakeSection]):
    """Build an AsyncMock session whose ``execute`` dispenses queued results.

    The render helper issues two selects: the Report row, then the section
    list. ``add()`` and ``commit()`` are also recorded for assertions.
    """
    queue: list = []
    if report is not None:
        queue.append(report)
    else:
        queue.append(None)
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


# ---------------------------------------------------------------------------
# Happy path
# ---------------------------------------------------------------------------

@pytest.mark.asyncio
async def test_render_published_renders_all_enabled_sections(tmp_path):
    report_id = str(uuid.uuid4())
    s_ids = [str(uuid.uuid4()) for _ in range(3)]
    sections = [_FakeSection(s_ids[i], i, f"Title {i}") for i in range(3)]
    report = _FakeReport(report_id, date_cls.fromisoformat("2026-04-30"))
    db = _make_db(report, sections)

    fake_render = MagicMock(return_value=tmp_path / "out.html")
    with patch(
        "app.admin.render.JinjaRenderer"
    ) as MockRenderer:
        instance = MockRenderer.return_value
        instance.render_to_file = fake_render
        path = await render_published("2026-04-30", db, disabled_section_ids=None)

    # Renderer called once with all three sections in order.
    fake_render.assert_called_once()
    args, _kwargs = fake_render.call_args
    report_arg, sections_arg, output_arg = args
    assert isinstance(report_arg, dict) and report_arg["report_date"] == "2026-04-30"
    assert [s["title"] for s in sections_arg] == ["Title 0", "Title 1", "Title 2"]
    assert output_arg.endswith("public/news/2026-04-30-trend.html")

    # ReportArtifact stamped with relative path + commit issued.
    db.add.assert_called_once()
    artifact = db.add.call_args.args[0]
    assert artifact.artifact_type == "html"
    assert artifact.storage_path == "public/news/2026-04-30-trend.html"
    db.commit.assert_awaited_once()

    assert path == tmp_path / "out.html"


@pytest.mark.asyncio
async def test_render_published_drops_disabled_sections(tmp_path):
    report_id = str(uuid.uuid4())
    s_ids = [str(uuid.uuid4()) for _ in range(3)]
    sections = [_FakeSection(s_ids[i], i, f"Title {i}") for i in range(3)]
    report = _FakeReport(report_id, date_cls.fromisoformat("2026-04-30"))
    db = _make_db(report, sections)

    fake_render = MagicMock(return_value=tmp_path / "out.html")
    with patch("app.admin.render.JinjaRenderer") as MockRenderer:
        MockRenderer.return_value.render_to_file = fake_render
        await render_published(
            "2026-04-30",
            db,
            disabled_section_ids={s_ids[1]},  # drop the middle one
        )

    _, sections_arg, _ = fake_render.call_args.args
    assert [s["title"] for s in sections_arg] == ["Title 0", "Title 2"]


@pytest.mark.asyncio
async def test_render_published_empty_disabled_list_keeps_all(tmp_path):
    report_id = str(uuid.uuid4())
    sections = [_FakeSection(str(uuid.uuid4()), 0, "only")]
    report = _FakeReport(report_id, date_cls.fromisoformat("2026-04-30"))
    db = _make_db(report, sections)

    fake_render = MagicMock(return_value=tmp_path / "out.html")
    with patch("app.admin.render.JinjaRenderer") as MockRenderer:
        MockRenderer.return_value.render_to_file = fake_render
        await render_published("2026-04-30", db, disabled_section_ids=[])
    _, sections_arg, _ = fake_render.call_args.args
    assert len(sections_arg) == 1


# ---------------------------------------------------------------------------
# Error paths
# ---------------------------------------------------------------------------

@pytest.mark.asyncio
async def test_render_published_bad_date_raises_value_error():
    db = _make_db(None, [])
    with pytest.raises(ValueError):
        await render_published("not-a-date", db, disabled_section_ids=None)


@pytest.mark.asyncio
async def test_render_published_missing_report_raises_lookup_error():
    db = _make_db(None, [])
    with pytest.raises(LookupError):
        await render_published("2099-01-01", db, disabled_section_ids=None)


# ---------------------------------------------------------------------------
# Storage path is project-root relative
# ---------------------------------------------------------------------------

@pytest.mark.asyncio
async def test_render_published_storage_path_is_project_root_relative(tmp_path):
    report_id = str(uuid.uuid4())
    sections = [_FakeSection(str(uuid.uuid4()), 0)]
    report = _FakeReport(report_id, date_cls.fromisoformat("2026-04-30"))
    db = _make_db(report, sections)

    with patch("app.admin.render.JinjaRenderer") as MockRenderer:
        MockRenderer.return_value.render_to_file = MagicMock(
            return_value=tmp_path / "out.html"
        )
        await render_published("2026-04-30", db, disabled_section_ids=None)

    artifact = db.add.call_args.args[0]
    # No leading slash, no absolute prefix, normalized POSIX-style.
    p = Path(artifact.storage_path)
    assert not p.is_absolute()
    assert artifact.storage_path == "public/news/2026-04-30-trend.html"
