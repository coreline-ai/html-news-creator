from __future__ import annotations

import uuid
from datetime import date as date_cls
from pathlib import Path
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from app.admin.pdf_export import (
    export_report_pdf,
    html_storage_path,
    pdf_storage_path,
)


class _FakeReport:
    def __init__(self, report_id: str, run_date: date_cls) -> None:
        self.id = uuid.UUID(report_id)
        self.report_date = run_date


def _make_db(report: _FakeReport | None):
    scalars = MagicMock()
    scalars.first.return_value = report
    result = MagicMock()
    result.scalars.return_value = scalars
    db = AsyncMock()
    db.execute.return_value = result
    db.add = MagicMock()
    db.commit = AsyncMock(return_value=None)
    return db


def test_pdf_storage_path_is_project_relative():
    assert pdf_storage_path("2026-05-01") == Path("public/news/2026-05-01-trend.pdf")
    assert html_storage_path("2026-05-01") == Path("public/news/2026-05-01-trend.html")


def test_pdf_storage_path_rejects_bad_date():
    with pytest.raises(ValueError):
        pdf_storage_path("not-a-date")


@pytest.mark.asyncio
async def test_export_report_pdf_uses_existing_html_by_default(tmp_path):
    report = _FakeReport(str(uuid.uuid4()), date_cls.fromisoformat("2026-05-01"))
    db = _make_db(report)
    html_path = tmp_path / "public/news/2026-05-01-trend.html"
    html_path.parent.mkdir(parents=True)
    html_path.write_text("<html>ok</html>", encoding="utf-8")
    pdf_path = tmp_path / "report.pdf"
    pdf_path.write_bytes(b"%PDF fake")

    with patch("app.admin.pdf_export._PROJECT_ROOT", tmp_path), patch(
        "app.admin.pdf_export.render_published",
        new=AsyncMock(return_value=html_path),
    ) as render_mock, patch("app.admin.pdf_export.PlaywrightRenderer") as Renderer:
        Renderer.return_value.export_pdf = AsyncMock(return_value=pdf_path)
        result = await export_report_pdf("2026-05-01", db)

    assert result == pdf_path
    render_mock.assert_not_awaited()
    Renderer.return_value.export_pdf.assert_awaited_once()
    export_args = Renderer.return_value.export_pdf.await_args.args
    assert export_args == (
        str(html_path),
        str(tmp_path / "public/news/2026-05-01-trend.pdf"),
    )

    db.add.assert_called_once()
    artifact = db.add.call_args.args[0]
    assert artifact.report_id == report.id
    assert artifact.artifact_type == "pdf"
    assert artifact.storage_path == "public/news/2026-05-01-trend.pdf"
    assert artifact.sha256
    db.commit.assert_awaited_once()


@pytest.mark.asyncio
async def test_export_report_pdf_can_force_fresh_render(tmp_path):
    report = _FakeReport(str(uuid.uuid4()), date_cls.fromisoformat("2026-05-01"))
    db = _make_db(report)
    html_path = tmp_path / "fresh.html"
    html_path.write_text("<html>fresh</html>", encoding="utf-8")
    pdf_path = tmp_path / "fresh.pdf"
    pdf_path.write_bytes(b"%PDF fresh")

    with patch("app.admin.pdf_export._PROJECT_ROOT", tmp_path), patch(
        "app.admin.pdf_export.render_published",
        new=AsyncMock(return_value=html_path),
    ) as render_mock, patch("app.admin.pdf_export.PlaywrightRenderer") as Renderer:
        Renderer.return_value.export_pdf = AsyncMock(return_value=pdf_path)
        await export_report_pdf(
            "2026-05-01",
            db,
            fresh=True,
            output_theme="newsroom-white",
        )

    render_mock.assert_awaited_once_with(
        "2026-05-01",
        db,
        output_theme="newsroom-white",
    )


@pytest.mark.asyncio
async def test_export_report_pdf_missing_report_raises_lookup_error():
    db = _make_db(None)

    with pytest.raises(LookupError):
        await export_report_pdf("2099-01-01", db)
