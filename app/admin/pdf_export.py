"""PDF export helper for published AI trend reports.

The report HTML is browser-first, so this helper converts the current rendered
HTML with Playwright/Chromium instead of introducing a second layout engine.
"""
from __future__ import annotations

import hashlib
from datetime import date as date_cls
from pathlib import Path
from typing import Any

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.admin.render import render_published
from app.models.db_models import Report, ReportArtifact
from app.rendering.playwright_renderer import PlaywrightRenderer
from app.utils.logger import get_logger

logger = get_logger(step="admin.pdf")

_PROJECT_ROOT = Path(__file__).resolve().parents[2]


def _validate_report_date(date_kst: str) -> date_cls:
    try:
        return date_cls.fromisoformat(date_kst)
    except ValueError as exc:
        raise ValueError(f"invalid date_kst (expected YYYY-MM-DD): {exc}") from exc


def pdf_storage_path(date_kst: str) -> Path:
    """Return the project-relative PDF artifact path for a report date."""
    _validate_report_date(date_kst)
    return Path("public") / "news" / f"{date_kst}-trend.pdf"


def html_storage_path(date_kst: str) -> Path:
    """Return the project-relative HTML artifact path for a report date."""
    _validate_report_date(date_kst)
    return Path("public") / "news" / f"{date_kst}-trend.html"


async def export_report_pdf(
    date_kst: str,
    db: AsyncSession,
    *,
    fresh: bool = False,
    output_theme: str = "dark",
    pdf_options: dict[str, Any] | None = None,
) -> Path:
    """Export a report HTML file to PDF.

    By default, this converts the existing published HTML as-is so the PDF
    matches the report the operator sees in the live iframe, including its
    selected theme. When ``fresh=True`` or the HTML file is missing, the helper
    first re-renders from DB rows.
    """
    run_date = _validate_report_date(date_kst)
    report = (
        await db.execute(select(Report).where(Report.report_date == run_date))
    ).scalars().first()
    if report is None:
        raise LookupError(f"report not found: {date_kst}")

    html_rel = html_storage_path(date_kst)
    html_path = _PROJECT_ROOT / html_rel
    if fresh or not html_path.is_file():
        html_path = await render_published(date_kst, db, output_theme=output_theme)

    output_rel = pdf_storage_path(date_kst)
    output_path = _PROJECT_ROOT / output_rel

    renderer = PlaywrightRenderer()
    pdf_path = await renderer.export_pdf(
        str(html_path),
        str(output_path),
        **(pdf_options or {}),
    )

    pdf_bytes = pdf_path.read_bytes()
    db.add(
        ReportArtifact(
            report_id=report.id,
            artifact_type="pdf",
            storage_path=str(output_rel),
            sha256=hashlib.sha256(pdf_bytes).hexdigest(),
        )
    )
    await db.commit()

    logger.info(
        "report_pdf_exported",
        date_kst=date_kst,
        fresh=fresh,
        html_path=str(html_rel),
        path=str(output_rel),
        size_bytes=pdf_path.stat().st_size,
    )
    return pdf_path


__all__ = ["export_report_pdf", "html_storage_path", "pdf_storage_path"]
