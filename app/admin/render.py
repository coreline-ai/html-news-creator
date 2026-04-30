"""Re-render a published Report from the live DB state.

This module is the missing link between Review (DB edits) and Publish
(static deploy). Calling ``render_published`` reads the latest
``Report``/``ReportSection`` rows for ``date_kst``, drops any sections
listed in ``disabled_section_ids`` (a client-only toggle — the DB row
itself has no ``enabled`` column), and rewrites
``public/news/{date_kst}-trend.html`` via the existing
``JinjaRenderer.render_to_file``. A ``ReportArtifact`` row is recorded
so operators can see exactly which HTML was deployed.

The Jinja template (`templates/report_newsstream.html.j2`) and the
``JinjaRenderer`` signature are intentionally untouched — this helper
only changes which section rows feed the renderer.
"""
from __future__ import annotations

from datetime import date as date_cls
from pathlib import Path
from typing import Any, Iterable, Optional

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.db_models import Report, ReportArtifact, ReportSection
from app.rendering.jinja_renderer import JinjaRenderer
from app.utils.logger import get_logger

logger = get_logger(step="admin")


# Project root — keep storage_path stable as ``public/news/<date>-trend.html``
# regardless of where the API process was launched from.
_PROJECT_ROOT = Path(__file__).resolve().parents[2]


def _section_to_render_dict(s: ReportSection) -> dict[str, Any]:
    """Convert an ORM ``ReportSection`` into the dict shape the template expects.

    Mirrors ``scripts/run_daily.py::run_render`` so the published HTML stays
    visually identical between a fresh pipeline run and a re-render after
    operator edits.
    """
    image_evidence = s.image_evidence_json or []
    content_images = [
        e["url"]
        for e in image_evidence
        if isinstance(e, dict) and e.get("url") and e.get("source") == "content"
    ]
    fallback_image = next(
        (
            e["url"]
            for e in image_evidence
            if isinstance(e, dict) and e.get("url") and e.get("source") != "content"
        ),
        "",
    )
    return {
        "title": s.title or "",
        "summary_ko": s.fact_summary or "",
        "fact_summary": s.fact_summary,
        "social_signal_summary": s.social_signal_summary,
        "inference_summary": s.inference_summary,
        "importance_score": s.importance_score or 0.0,
        "sources_json": s.sources_json or [],
        "content_image_urls": content_images,
        "og_image_url": fallback_image,
        "category": "other",
    }


def _report_to_render_dict(report: Report, section_count: int) -> dict[str, Any]:
    stats = report.stats_json or {}
    return {
        "title": report.title,
        "report_date": str(report.report_date),
        "summary_ko": report.summary_ko or "",
        "created_at": (
            report.updated_at.strftime("%Y-%m-%d %H:%M")
            if report.updated_at is not None
            else ""
        ),
        "stats": {
            "total_sources": stats.get("total_sources", 0),
            "ai_relevant": stats.get("ai_relevant", 0),
            "clusters": stats.get("clusters", section_count),
            "verified": stats.get("verified", 0),
        },
    }


async def render_published(
    date_kst: str,
    db: AsyncSession,
    disabled_section_ids: Optional[Iterable[str]] = None,
) -> Path:
    """Re-render the published HTML for ``date_kst`` from current DB state.

    Args:
        date_kst: report date in ``YYYY-MM-DD`` (KST).
        db: an open ``AsyncSession`` (the caller decides whether it commits).
        disabled_section_ids: section UUIDs (str) to skip. ``None`` or empty
            renders every section in ``section_order``.

    Returns:
        Path to the freshly written HTML file.

    Raises:
        ValueError: invalid ``date_kst`` format.
        LookupError: no Report row exists for that date.
    """
    try:
        run_date = date_cls.fromisoformat(date_kst)
    except ValueError as exc:
        raise ValueError(f"invalid date_kst (expected YYYY-MM-DD): {exc}")

    disabled_set: set[str] = (
        {str(sid) for sid in disabled_section_ids}
        if disabled_section_ids
        else set()
    )

    result = await db.execute(select(Report).where(Report.report_date == run_date))
    db_report = result.scalars().first()
    if db_report is None:
        raise LookupError(f"report not found: {date_kst}")

    sections_result = await db.execute(
        select(ReportSection)
        .where(ReportSection.report_id == db_report.id)
        .order_by(ReportSection.section_order)
    )
    all_sections = list(sections_result.scalars().all())
    kept_sections = [s for s in all_sections if str(s.id) not in disabled_set]

    report_data = _report_to_render_dict(db_report, len(kept_sections))
    sections_data = [_section_to_render_dict(s) for s in kept_sections]

    output_rel = Path("public") / "news" / f"{date_kst}-trend.html"
    output_path = _PROJECT_ROOT / output_rel

    renderer = JinjaRenderer(templates_dir=str(_PROJECT_ROOT / "templates"))
    written_path = renderer.render_to_file(
        report_data, sections_data, str(output_path)
    )

    artifact = ReportArtifact(
        report_id=db_report.id,
        artifact_type="html",
        storage_path=str(output_rel),
    )
    db.add(artifact)
    await db.commit()

    logger.info(
        "render_published_done",
        date_kst=date_kst,
        sections_total=len(all_sections),
        sections_rendered=len(kept_sections),
        disabled_count=len(disabled_set),
        path=str(output_rel),
    )
    return written_path
