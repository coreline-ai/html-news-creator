from __future__ import annotations
from datetime import date
from pathlib import Path
from typing import Any, Optional

from fastapi import Body, Depends, FastAPI, HTTPException, Path as PathParam, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field
from sqlalchemy import desc, func, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.admin.policy_admin import get_policy, set_policy_override
from app.admin.preview import render_preview
from app.admin.run_runner import get_run, start_run
from app.admin.sources_admin import (
    ALLOWED_UPDATE_FIELDS,
    list_sources as registry_list_sources,
    update_source as registry_update_source,
)
from app.admin.sse import stream_run
from app.config import settings
from app.db import get_db
from app.models.db_models import Cluster, JobLog, JobRun, RawItem, Report, ReportSection, Source
from app.utils.logger import get_logger

app = FastAPI(
    title="News Studio API",
    description="Admin + News Studio web UI for the AI Trend Report engine",
    version="0.2.0",
)

# CORS — Vite dev server lives at localhost:5173 by default; honor the
# configured origin for non-default deploys.
_allowed_origins = list({"http://localhost:5173", settings.ui_dev_origin})
app.add_middleware(
    CORSMiddleware,
    allow_origins=_allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

logger = get_logger(step="admin")


# ---------------------------------------------------------------------------
# Health + legacy v1 endpoints (kept as-is so existing tests still pass)
# ---------------------------------------------------------------------------

@app.get("/health")
async def health():
    return {"status": "ok", "service": "ai-trend-report-engine"}


@app.get("/api/v1/runs")
async def list_runs(
    limit: int = Query(default=20, le=100),
    db: AsyncSession = Depends(get_db),
):
    """List recent job runs (legacy v1)."""
    result = await db.execute(
        select(JobRun).order_by(desc(JobRun.started_at)).limit(limit)
    )
    runs = result.scalars().all()
    return {
        "runs": [
            {
                "id": str(r.id),
                "run_date": str(r.run_date) if r.run_date else None,
                "status": r.status,
                "started_at": str(r.started_at) if r.started_at else None,
                "completed_at": str(r.completed_at) if r.completed_at else None,
                "metadata_json": r.metadata_json,
            }
            for r in runs
        ]
    }


@app.get("/api/v1/runs/{run_id}/logs")
async def get_run_logs(
    run_id: str,
    limit: int = Query(default=100, le=500),
    db: AsyncSession = Depends(get_db),
):
    """Get logs for a specific job run (legacy v1)."""
    result = await db.execute(
        select(JobLog)
        .where(JobLog.job_run_id == run_id)
        .order_by(JobLog.created_at)
        .limit(limit)
    )
    logs = result.scalars().all()
    return {
        "run_id": run_id,
        "logs": [
            {
                "level": log.level,
                "step": log.step_name,
                "message": log.message,
                "created_at": str(log.created_at) if log.created_at else None,
            }
            for log in logs
        ],
    }


@app.get("/api/v1/reports")
async def list_reports_v1(
    limit: int = Query(default=10, le=50),
    db: AsyncSession = Depends(get_db),
):
    """List recent reports (legacy v1 — unchanged response shape)."""
    result = await db.execute(
        select(Report).order_by(desc(Report.created_at)).limit(limit)
    )
    reports = result.scalars().all()
    return {
        "reports": [
            {
                "id": str(r.id),
                "report_date": str(r.report_date) if r.report_date else None,
                "title": r.title,
                "status": r.status,
                "created_at": str(r.created_at) if r.created_at else None,
                "stats_json": r.stats_json,
            }
            for r in reports
        ]
    }


@app.get("/api/v1/stats/today")
async def today_stats(db: AsyncSession = Depends(get_db)):
    """Get today's pipeline statistics."""
    today = date.today()
    raw_count_result = await db.execute(
        select(func.count(RawItem.id)).where(
            func.date(RawItem.collected_at) == today
        )
    )
    raw_count = raw_count_result.scalar() or 0
    cluster_count_result = await db.execute(
        select(func.count(Cluster.id)).where(
            func.date(Cluster.created_at) == today
        )
    )
    cluster_count = cluster_count_result.scalar() or 0
    return {
        "date": str(today),
        "raw_items": raw_count,
        "clusters": cluster_count,
    }


@app.get("/api/v1/sources")
async def list_sources_v1(
    active_only: bool = True,
    db: AsyncSession = Depends(get_db),
):
    """List registered sources (legacy v1, DB-backed)."""
    query = select(Source)
    if active_only:
        query = query.where(Source.enabled.is_(True))
    result = await db.execute(query.order_by(Source.name))
    sources = result.scalars().all()
    return {
        "sources": [
            {
                "id": str(s.id),
                "name": s.name,
                "source_type": s.source_type,
                "url": s.url,
                "trust_level": s.trust_level,
                "is_active": s.enabled,
            }
            for s in sources
        ]
    }


# ---------------------------------------------------------------------------
# Phase 1 — News Studio API (8 endpoints, all under /api/)
# ---------------------------------------------------------------------------

class PreviewRequest(BaseModel):
    target_sections: Optional[int] = Field(default=None, ge=1, le=30)
    date_kst: Optional[str] = None
    # Free-form policy overrides — accepted as a nested dict.
    policy_override: Optional[dict] = None

    model_config = {"extra": "allow"}


class RunRequest(BaseModel):
    date: Optional[str] = None
    mode: Optional[str] = None
    from_step: Optional[str] = None
    to_step: Optional[str] = None
    dry_run: bool = False

    model_config = {"extra": "allow"}


class PolicyPatchRequest(BaseModel):
    patch: Optional[dict] = None


class SourcePatchRequest(BaseModel):
    enabled: Optional[bool] = None
    priority: Optional[int] = None
    max_items: Optional[int] = None
    trust_level: Optional[str] = None
    source_tier: Optional[str] = None
    category: Optional[str] = None

    def to_fields(self) -> dict[str, Any]:
        return {
            key: getattr(self, key)
            for key in ALLOWED_UPDATE_FIELDS
            if getattr(self, key, None) is not None
        }


# ---------------------------------------------------------------------------
# Phase 4 — Section editing / reorder / publish
# ---------------------------------------------------------------------------

class SectionPatchRequest(BaseModel):
    """Allowed editable fields on a single ReportSection.

    Maps to the existing DB columns:
      - title          → ReportSection.title
      - summary_ko     → ReportSection.fact_summary
      - implication_ko → ReportSection.inference_summary
      - image_url      → injected into image_evidence_json (first entry)
    """

    title: Optional[str] = None
    summary_ko: Optional[str] = None
    implication_ko: Optional[str] = None
    image_url: Optional[str] = None

    model_config = {"extra": "ignore"}

    def has_any(self) -> bool:
        return any(
            getattr(self, k) is not None
            for k in ("title", "summary_ko", "implication_ko", "image_url")
        )


class ReorderRequest(BaseModel):
    section_ids: list[str] = Field(default_factory=list)


class PublishRequest(BaseModel):
    publish_dir: Optional[str] = None
    dry_run: bool = False

    model_config = {"extra": "allow"}


# 1) GET /api/reports — recent reports (lightweight summary)
@app.get("/api/reports")
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


# 2) GET /api/reports/{date_kst} — single report + sections
@app.get("/api/reports/{date_kst}")
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


# 3) POST /api/preview — in-memory render with options override (NO DB writes)
@app.post("/api/preview")
async def api_preview(payload: PreviewRequest = Body(default_factory=PreviewRequest)):
    options: dict[str, Any] = payload.model_dump(exclude_none=True)
    date_kst = options.pop("date_kst", None)
    try:
        html = render_preview(options=options, date_kst=date_kst)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc))
    return {"html": html, "length": len(html)}


# 4) POST /api/runs — kick off a background run
@app.post("/api/runs")
async def api_start_run(payload: RunRequest = Body(default_factory=RunRequest)):
    options = payload.model_dump(exclude_none=True)
    run_id = await start_run(options)
    state = get_run(run_id)
    return {
        "run_id": run_id,
        "status": state.status if state else "queued",
        "options": options,
    }


# 5) GET /api/runs/{run_id}/stream — SSE progress stream
@app.get("/api/runs/{run_id}/stream")
async def api_stream_run(run_id: str):
    return stream_run(run_id)


# 6) GET /api/policy — yaml + runtime override merged
@app.get("/api/policy")
async def api_get_policy():
    return {"policy": get_policy()}


# 7) PUT /api/policy — replace runtime override (volatile)
@app.put("/api/policy")
async def api_put_policy(payload: PolicyPatchRequest = Body(default_factory=PolicyPatchRequest)):
    try:
        merged = set_policy_override(payload.patch or {})
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc))
    return {"policy": merged}


# 8a) GET /api/sources — registry sources (yaml-backed)
@app.get("/api/sources")
async def api_list_sources():
    return {"sources": registry_list_sources()}


# 8b) PUT /api/sources/{name} — patch enabled/priority/etc.
@app.put("/api/sources/{name}")
async def api_update_source(
    name: str,
    payload: SourcePatchRequest = Body(default_factory=SourcePatchRequest),
):
    fields = payload.to_fields()
    if not fields:
        raise HTTPException(status_code=400, detail="no updatable fields supplied")
    try:
        updated = registry_update_source(name, fields)
    except KeyError as exc:
        raise HTTPException(status_code=404, detail=str(exc))
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc))
    return {"source": updated}


# ---------------------------------------------------------------------------
# Phase 4 — Section editing / reorder / publish (4 new routes)
# ---------------------------------------------------------------------------


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


# 9) PATCH /api/sections/{id} — edit single section
@app.patch("/api/sections/{section_id}")
async def api_patch_section(
    section_id: str,
    payload: SectionPatchRequest = Body(default_factory=SectionPatchRequest),
    db: AsyncSession = Depends(get_db),
):
    if not payload.has_any():
        raise HTTPException(status_code=400, detail="no updatable fields supplied")

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


# 10) POST /api/sections/{id}/regenerate — single-section regen via LLM
@app.post("/api/sections/{section_id}/regenerate")
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


# 11) POST /api/reports/{date}/reorder — bulk reorder section_order
@app.post("/api/reports/{date_kst}/reorder")
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

    # All ids in payload must belong to this report
    unknown = [sid for sid in payload.section_ids if sid not in by_id]
    if unknown:
        raise HTTPException(
            status_code=400,
            detail=f"section_ids not part of report {date_kst}: {unknown}",
        )

    for new_pos, sid in enumerate(payload.section_ids):
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


# 12) POST /api/reports/{date}/publish — Netlify deploy trigger
@app.post("/api/reports/{date_kst}/publish")
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


# ---------------------------------------------------------------------------
# Phase 6 — Static SPA mount (MUST be last so it does not shadow /api routes)
# ---------------------------------------------------------------------------

_ui_dist = Path(settings.ui_dist_path)
if _ui_dist.is_dir():
    # Serve hashed assets out of /assets/* with proper caching headers via
    # StaticFiles. The SPA fallback below handles every other path so that
    # client-side routes (e.g. /sources, /reports/2026-04-30) survive a hard
    # refresh by rendering index.html.
    _assets_dir = _ui_dist / "assets"
    if _assets_dir.is_dir():
        app.mount(
            "/assets",
            StaticFiles(directory=str(_assets_dir)),
            name="ui-assets",
        )

    _index_html = _ui_dist / "index.html"

    @app.get("/{full_path:path}", include_in_schema=False)
    async def spa_fallback(full_path: str) -> Any:
        # Never shadow API routes — they are registered above and FastAPI's
        # router resolution would already have matched them. Defensive guard
        # in case of unknown /api/* requests so the user gets JSON 404 rather
        # than HTML.
        if full_path.startswith("api/") or full_path == "api":
            raise HTTPException(status_code=404, detail="Not Found")

        # Top-level static files (favicon.ico, robots.txt, etc.) ship straight
        # from disk when they exist.
        candidate = (_ui_dist / full_path).resolve()
        try:
            candidate.relative_to(_ui_dist.resolve())
        except ValueError:
            # Path traversal — fall through to index.html.
            candidate = None  # type: ignore[assignment]
        if candidate and candidate.is_file():
            return FileResponse(str(candidate))

        # All other paths render the SPA shell.
        return FileResponse(str(_index_html))

else:
    logger.info(
        "ui_dist_not_found",
        path=str(_ui_dist),
        note="run `make ui-build` to populate ui/dist before serving the SPA",
    )
