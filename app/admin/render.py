"""Re-render a published Report from the live DB state.

This module is the missing link between Review (DB edits) and Publish
(static deploy). Calling ``render_published`` reads the latest
``Report``/``ReportSection`` rows for ``date_kst``, drops any sections
listed in ``disabled_section_ids`` (a client-only toggle — the DB row
itself has no ``enabled`` column), and rewrites
``public/news/{date_kst}-trend.html`` via the existing
``JinjaRenderer.render_to_file``. A ``ReportArtifact`` row is recorded
so operators can see exactly which HTML was deployed.

The renderer defaults to the existing newsstream template, but honours
``Report.method_json.output_style`` so a report generated as a signal briefing
keeps that structure when operators re-render or publish it.
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
from app.utils.source_images import is_usable_representative_image_url

logger = get_logger(step="admin")


# Project root — keep storage_path stable as ``public/news/<date>-trend.html``
# regardless of where the API process was launched from.
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
_DEFAULT_OUTPUT_STYLE = "newsstream"
_SIGNAL_BRIEFING_OUTPUT_STYLE = "signal_briefing"


def _normalize_output_style(value: str | None) -> str:
    return (
        _SIGNAL_BRIEFING_OUTPUT_STYLE
        if value == _SIGNAL_BRIEFING_OUTPUT_STYLE
        else _DEFAULT_OUTPUT_STYLE
    )


def _unique_source_count(sections: list[ReportSection]) -> int:
    seen: set[str] = set()
    for section in sections:
        sources = section.sources_json or []
        if not isinstance(sources, list):
            continue
        for src in sources:
            if not isinstance(src, dict):
                continue
            key = str(src.get("url") or src.get("name") or "").strip()
            if key:
                seen.add(key)
    return len(seen)


def _stats_with_section_fallbacks(
    raw_stats: dict[str, Any],
    sections: list[ReportSection],
) -> dict[str, Any]:
    stats = dict(raw_stats or {})
    section_count = len(sections)
    if section_count <= 0:
        return stats
    source_count = _unique_source_count(sections) or section_count
    stats["clusters"] = stats.get("clusters") or section_count
    stats["total_sources"] = stats.get("total_sources") or source_count
    stats["ai_relevant"] = stats.get("ai_relevant") or source_count
    return stats


def _section_to_render_dict(s: ReportSection) -> dict[str, Any]:
    """Convert an ORM ``ReportSection`` into the dict shape the template expects.

    Mirrors ``scripts/run_daily.py::run_render`` so the published HTML stays
    visually identical between a fresh pipeline run and a re-render after
    operator edits.

    Image evidence is filtered through ``is_usable_representative_image_url``
    so journalist headshots, logos, tracking pixels, and decorative SVGs from
    upstream collectors never reach the rendered HTML — even when an operator
    accepted them at section-edit time.
    """
    image_evidence = s.image_evidence_json or []
    content_images = [
        e["url"]
        for e in image_evidence
        if isinstance(e, dict)
        and e.get("url")
        and e.get("source") == "content"
        and is_usable_representative_image_url(e["url"])
    ]
    fallback_image = next(
        (
            e["url"]
            for e in image_evidence
            if isinstance(e, dict)
            and e.get("url")
            and e.get("source") != "content"
            and is_usable_representative_image_url(e["url"])
        ),
        "",
    )
    output_meta = _extract_section_output_meta(s.tags_json)
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
        "key_updates": output_meta["key_updates"],
        "image_detail_hint": output_meta["image_detail_hint"],
        "tags": output_meta["tags"],
        "category": "other",
    }


def _extract_section_output_meta(tags_json: Any) -> dict[str, Any]:
    result: dict[str, Any] = {
        "key_updates": [],
        "image_detail_hint": None,
        "tags": [],
    }
    if not isinstance(tags_json, list):
        return result
    for entry in tags_json:
        if not isinstance(entry, dict):
            continue
        if "key_updates" in entry and isinstance(entry["key_updates"], list):
            result["key_updates"] = entry["key_updates"]
        if "image_detail_hint" in entry:
            result["image_detail_hint"] = entry["image_detail_hint"]
        if "tags" in entry and isinstance(entry["tags"], list):
            result["tags"] = entry["tags"]
    return result


def _report_to_render_dict(
    report: Report,
    section_count: int,
    output_style: str,
) -> dict[str, Any]:
    stats = report.stats_json or {}
    total_sources = stats.get("total_sources", 0) or 0
    ai_relevant = stats.get("ai_relevant", 0) or 0
    clusters = stats.get("clusters", 0) or section_count
    if section_count > 0:
        total_sources = total_sources or section_count
        ai_relevant = ai_relevant or section_count
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
            **stats,
            "total_sources": total_sources,
            "ai_relevant": ai_relevant,
            "clusters": clusters,
            "verified": stats.get("verified", 0),
            "output_style": output_style,
        },
    }


async def render_published(
    date_kst: str,
    db: AsyncSession,
    disabled_section_ids: Optional[Iterable[str]] = None,
    output_theme: str = "dark",
    output_style: str | None = None,
) -> Path:
    """Re-render the published HTML for ``date_kst`` from current DB state.

    Args:
        date_kst: report date in ``YYYY-MM-DD`` (KST).
        db: an open ``AsyncSession`` (the caller decides whether it commits).
        disabled_section_ids: section UUIDs (str) to skip. ``None`` or empty
            renders every section in ``section_order``.
        output_theme: ``dark`` (default), ``light``, or ``newsroom-white``.
            Forwarded to ``JinjaRenderer.render_to_file`` so the per-run theme
            picked in the UI ends up in the deployed HTML instead of always
            shipping dark.
        output_style: ``newsstream`` or ``signal_briefing``. When omitted, the
            value persisted in ``Report.method_json.output_style`` is used.

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
    stored_output_style = (
        (db_report.method_json or {}).get("output_style")
        if isinstance(db_report.method_json, dict)
        else None
    )
    resolved_output_style = _normalize_output_style(
        output_style or stored_output_style
    )

    sections_result = await db.execute(
        select(ReportSection)
        .where(ReportSection.report_id == db_report.id)
        .order_by(ReportSection.section_order)
    )
    all_sections = list(sections_result.scalars().all())
    kept_sections = [s for s in all_sections if str(s.id) not in disabled_set]

    report_data = _report_to_render_dict(
        db_report,
        len(kept_sections),
        resolved_output_style,
    )
    sections_data = [_section_to_render_dict(s) for s in kept_sections]
    normalized_stats = _stats_with_section_fallbacks(
        db_report.stats_json or {},
        kept_sections,
    )
    if normalized_stats != (db_report.stats_json or {}):
        db_report.stats_json = normalized_stats
        report_data = _report_to_render_dict(
            db_report,
            len(kept_sections),
            resolved_output_style,
        )

    output_rel = Path("public") / "news" / f"{date_kst}-trend.html"
    output_path = _PROJECT_ROOT / output_rel

    renderer = JinjaRenderer(templates_dir=str(_PROJECT_ROOT / "templates"))
    written_path = renderer.render_to_file(
        report_data,
        sections_data,
        str(output_path),
        output_theme=output_theme,
        output_style=resolved_output_style,
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
        output_theme=output_theme,
        output_style=resolved_output_style,
        path=str(output_rel),
    )
    return written_path
