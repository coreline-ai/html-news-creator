"""Report + section endpoints.

Routes:
  - GET   /api/reports
  - GET   /api/reports/{date_kst}
  - GET   /api/reports/{date_kst}/html
  - POST  /api/reports/{date_kst}/render
  - POST  /api/reports/{date_kst}/publish
  - POST  /api/reports/{date_kst}/reorder
  - PATCH /api/sections/{section_id}
  - POST  /api/sections/{section_id}/regenerate
"""

from __future__ import annotations
from datetime import date
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

from fastapi import APIRouter, Body, Depends, HTTPException, Path as PathParam, Query
from fastapi.responses import FileResponse
from sqlalchemy import desc, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.admin.routers._models import (
    PublishRequest,
    RenderRequest,
    ReorderRequest,
    SectionPatchRequest,
)
from app.db import get_db
from app.models.db_models import Report, ReportSection
from app.utils.logger import get_logger

logger = get_logger(step="admin")

router = APIRouter()


def _serialize_section(s: ReportSection) -> dict[str, Any]:
    return {
        "id": str(s.id),
        "section_order": s.section_order,
        "title": s.title,
        "lead": s.lead,
        "fact_summary": s.fact_summary,
        "social_signal_summary": s.social_signal_summary,
        "inference_summary": s.inference_summary,
        "caution": s.caution,
        "image_evidence_json": s.image_evidence_json,
        "sources_json": s.sources_json,
        "confidence": s.confidence,
        "importance_score": s.importance_score,
        "tags_json": s.tags_json,
    }


# 1) GET /api/reports — recent reports (lightweight summary)
@router.get("/api/reports")
async def api_list_reports(
    limit: int = Query(default=20, le=100),
    db: AsyncSession = Depends(get_db),
):
    result = await db.execute(
        select(Report).order_by(desc(Report.report_date)).limit(limit)
    )
    reports = result.scalars().all()
    return {
        "reports": [
            {
                "id": str(r.id),
                "report_date": str(r.report_date) if r.report_date else None,
                "title": r.title,
                "status": r.status,
                "summary_ko": r.summary_ko,
                "stats_json": r.stats_json,
                "created_at": str(r.created_at) if r.created_at else None,
                "updated_at": str(r.updated_at) if r.updated_at else None,
                "published_at": str(r.published_at) if r.published_at else None,
            }
            for r in reports
        ]
    }


# 2) GET /api/reports/{date_kst}/html — serve the published HTML file
@router.get("/api/reports/{date_kst}/html", include_in_schema=False)
async def api_get_report_html(
    date_kst: str = PathParam(..., description="KST date YYYY-MM-DD"),
):
    """Serve the published HTML file produced by the static publisher.

    Used by ReviewReport's "Live" preview pane so the operator can see the
    actual rendered output (not the synthetic preview used by NewReport).
    Returns 404 if the report has not been published yet. Cache-Control
    no-store so a republish is reflected immediately.
    """
    try:
        date.fromisoformat(date_kst)
    except ValueError as exc:
        raise HTTPException(
            status_code=400, detail=f"invalid date_kst (expected YYYY-MM-DD): {exc}"
        )
    project_root = Path(__file__).resolve().parents[3]
    html_path = (project_root / "public" / "news" / f"{date_kst}-trend.html").resolve()
    try:
        html_path.relative_to((project_root / "public" / "news").resolve())
    except ValueError:
        raise HTTPException(status_code=400, detail="invalid path")
    if not html_path.is_file():
        raise HTTPException(
            status_code=404, detail=f"published HTML not found for {date_kst}"
        )
    return FileResponse(
        str(html_path),
        media_type="text/html",
        headers={"Cache-Control": "no-store, must-revalidate"},
    )


# 3) GET /api/reports/{date_kst} — single report + sections
@router.get("/api/reports/{date_kst}")
async def api_get_report(
    date_kst: str = PathParam(..., description="KST date YYYY-MM-DD"),
    db: AsyncSession = Depends(get_db),
):
    try:
        run_date = date.fromisoformat(date_kst)
    except ValueError as exc:
        raise HTTPException(
            status_code=400, detail=f"invalid date_kst (expected YYYY-MM-DD): {exc}"
        )

    result = await db.execute(select(Report).where(Report.report_date == run_date))
    db_report = result.scalars().first()
    if db_report is None:
        raise HTTPException(status_code=404, detail=f"report not found: {date_kst}")

    sections_result = await db.execute(
        select(ReportSection)
        .where(ReportSection.report_id == db_report.id)
        .order_by(ReportSection.section_order)
    )
    sections = sections_result.scalars().all()

    return {
        "id": str(db_report.id),
        "report_date": str(db_report.report_date),
        "title": db_report.title,
        "status": db_report.status,
        "summary_ko": db_report.summary_ko,
        "stats_json": db_report.stats_json,
        "method_json": db_report.method_json,
        "created_at": str(db_report.created_at) if db_report.created_at else None,
        "updated_at": str(db_report.updated_at) if db_report.updated_at else None,
        "published_at": str(db_report.published_at) if db_report.published_at else None,
        "sections": [
            {
                "id": str(s.id),
                "section_order": s.section_order,
                "title": s.title,
                "lead": s.lead,
                "fact_summary": s.fact_summary,
                "social_signal_summary": s.social_signal_summary,
                "inference_summary": s.inference_summary,
                "caution": s.caution,
                "image_evidence_json": s.image_evidence_json,
                "sources_json": s.sources_json,
                "confidence": s.confidence,
                "importance_score": s.importance_score,
                "tags_json": s.tags_json,
            }
            for s in sections
        ],
    }


# 4) PATCH /api/sections/{id} — edit single section
@router.patch("/api/sections/{section_id}")
async def api_patch_section(
    section_id: str,
    payload: SectionPatchRequest = Body(default_factory=SectionPatchRequest),
    db: AsyncSession = Depends(get_db),
):
    if not payload.has_any():
        raise HTTPException(status_code=400, detail="no updatable fields supplied")

    # Validate image_url up-front (P1-1): only http(s) URLs with a non-empty
    # netloc are accepted. Empty strings are treated as "skip" so the FE can
    # send `image_url: ""` to clear an editing buffer without forcing a value.
    if payload.image_url is not None and payload.image_url != "":
        parsed = urlparse(payload.image_url)
        if parsed.scheme not in ("http", "https") or not parsed.netloc:
            raise HTTPException(
                status_code=400,
                detail=(
                    "invalid image_url: must be an absolute http(s) URL with a host "
                    f"(got {payload.image_url!r})"
                ),
            )

    result = await db.execute(
        select(ReportSection).where(ReportSection.id == section_id)
    )
    section = result.scalars().first()
    if section is None:
        raise HTTPException(status_code=404, detail=f"section not found: {section_id}")

    if payload.title is not None:
        section.title = payload.title
    if payload.summary_ko is not None:
        # `fact_summary` is the closest existing column for the editorial summary.
        section.fact_summary = payload.summary_ko
    if payload.implication_ko is not None:
        section.inference_summary = payload.implication_ko
    if payload.image_url is not None:
        # Replace / inject the primary image evidence entry.
        existing = section.image_evidence_json or []
        if isinstance(existing, list) and existing and isinstance(existing[0], dict):
            existing[0] = {**existing[0], "url": payload.image_url}
        else:
            existing = [{"url": payload.image_url}]
        section.image_evidence_json = existing

    await db.commit()
    await db.refresh(section)
    return {"section": _serialize_section(section)}


# 5) POST /api/sections/{id}/regenerate — single-section regen via LLM
@router.post("/api/sections/{section_id}/regenerate")
async def api_regenerate_section(section_id: str):
    """Regenerate a single section via SectionGenerator.

    The helper opens its own session so we can update only the target row
    without dragging the request-scoped session into LLM I/O.
    """
    from app.admin.section_regen import regenerate_section

    try:
        updated = await regenerate_section(section_id)
    except LookupError as exc:
        raise HTTPException(status_code=404, detail=str(exc))
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc))
    except Exception as exc:  # pragma: no cover — defensive
        logger.error("regenerate_section_failed", section_id=section_id, error=str(exc))
        raise HTTPException(
            status_code=500, detail=f"regenerate failed: {exc}"
        )

    return {
        "status": "ok",
        "section_id": section_id,
        "section": updated,
    }


# 6) POST /api/reports/{date}/reorder — bulk reorder section_order
@router.post("/api/reports/{date_kst}/reorder")
async def api_reorder_sections(
    date_kst: str,
    payload: ReorderRequest = Body(default_factory=ReorderRequest),
    db: AsyncSession = Depends(get_db),
):
    try:
        run_date = date.fromisoformat(date_kst)
    except ValueError as exc:
        raise HTTPException(
            status_code=400, detail=f"invalid date_kst (expected YYYY-MM-DD): {exc}"
        )

    if not payload.section_ids:
        raise HTTPException(status_code=400, detail="section_ids must not be empty")

    result = await db.execute(select(Report).where(Report.report_date == run_date))
    db_report = result.scalars().first()
    if db_report is None:
        raise HTTPException(status_code=404, detail=f"report not found: {date_kst}")

    sections_result = await db.execute(
        select(ReportSection).where(ReportSection.report_id == db_report.id)
    )
    sections = sections_result.scalars().all()
    by_id = {str(s.id): s for s in sections}

    # Exact-set check: payload must reference EVERY section of this report
    # exactly once — neither dropping known ids nor introducing foreign ones.
    # We normalise everything via ``str()`` so UUID vs str payloads compare
    # cleanly.
    payload_ids = [str(sid) for sid in payload.section_ids]
    payload_set = set(payload_ids)
    db_set = set(by_id.keys())
    missing = sorted(db_set - payload_set)
    unknown = sorted(payload_set - db_set)
    if missing or unknown or len(payload_ids) != len(db_set):
        raise HTTPException(
            status_code=400,
            detail=(
                "section_ids must exactly match the report's section set "
                f"(missing: {missing}, unknown: {unknown})"
            ),
        )

    for new_pos, sid in enumerate(payload_ids):
        by_id[sid].section_order = new_pos

    await db.commit()

    refreshed = await db.execute(
        select(ReportSection)
        .where(ReportSection.report_id == db_report.id)
        .order_by(ReportSection.section_order)
    )
    ordered = refreshed.scalars().all()
    return {
        "report_date": date_kst,
        "sections": [_serialize_section(s) for s in ordered],
    }


# 7) POST /api/reports/{date}/publish — Netlify deploy trigger
@router.post("/api/reports/{date_kst}/publish")
async def api_publish_report(
    date_kst: str,
    payload: PublishRequest = Body(default_factory=PublishRequest),
    db: AsyncSession = Depends(get_db),
):
    from app.admin.publish import publish_report

    # Validate date + report existence up-front using the request-scoped DB.
    # The helper opens its own session for the actual mutation so a long
    # Netlify deploy can't pin our HTTP connection.
    try:
        run_date = date.fromisoformat(date_kst)
    except ValueError as exc:
        raise HTTPException(
            status_code=400, detail=f"invalid date_kst (expected YYYY-MM-DD): {exc}"
        )

    result = await db.execute(select(Report).where(Report.report_date == run_date))
    db_report = result.scalars().first()
    if db_report is None:
        raise HTTPException(status_code=404, detail=f"report not found: {date_kst}")

    try:
        return await publish_report(
            date_kst,
            dry_run=payload.dry_run,
            publish_dir=payload.publish_dir,
            disabled_section_ids=payload.disabled_section_ids or [],
        )
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc))
    except LookupError as exc:
        raise HTTPException(status_code=404, detail=str(exc))
    except RuntimeError as exc:
        # Netlify config missing → 400 (operator action required).
        raise HTTPException(status_code=400, detail=str(exc))
    except Exception as exc:  # pragma: no cover — defensive
        logger.error("publish_failed", date_kst=date_kst, error=str(exc))
        raise HTTPException(status_code=500, detail=f"publish failed: {exc}")


# 8) POST /api/reports/{date}/render — re-render HTML from DB (no deploy)
@router.post("/api/reports/{date_kst}/render")
async def api_render_report(
    date_kst: str,
    payload: RenderRequest = Body(default_factory=RenderRequest),
    db: AsyncSession = Depends(get_db),
):
    """Re-render the published HTML from current DB state.

    Useful as a debug hook (no Netlify call) and as the first step the
    publish route performs internally. Returns the rendered file path,
    the number of sections actually rendered, and how many were dropped
    by the disabled-toggle list.
    """
    from app.admin.render import render_published

    try:
        rendered_path = await render_published(
            date_kst,
            db,
            disabled_section_ids=payload.disabled_section_ids or [],
        )
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc))
    except LookupError as exc:
        raise HTTPException(status_code=404, detail=str(exc))
    except Exception as exc:  # pragma: no cover — defensive
        logger.error("render_failed", date_kst=date_kst, error=str(exc))
        raise HTTPException(status_code=500, detail=f"render failed: {exc}")

    # Re-query for the section count after the render commit so callers can
    # see exactly how many sections survived the disabled filter.
    try:
        run_date = date.fromisoformat(date_kst)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc))
    report_row = (
        await db.execute(select(Report).where(Report.report_date == run_date))
    ).scalars().first()
    section_count = 0
    if report_row is not None:
        all_sections = (
            await db.execute(
                select(ReportSection).where(
                    ReportSection.report_id == report_row.id
                )
            )
        ).scalars().all()
        disabled_set = {sid for sid in (payload.disabled_section_ids or [])}
        section_count = sum(
            1 for s in all_sections if str(s.id) not in disabled_set
        )

    project_root = Path(__file__).resolve().parents[3]
    try:
        rel_path = str(rendered_path.resolve().relative_to(project_root))
    except ValueError:
        rel_path = str(rendered_path)

    return {
        "rendered_path": rel_path,
        "sections": section_count,
        "disabled_count": len(payload.disabled_section_ids or []),
    }
