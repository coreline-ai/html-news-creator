from __future__ import annotations
from datetime import date
from pathlib import Path
from typing import Any, Optional
from urllib.parse import urlparse

from fastapi import Body, Depends, FastAPI, HTTPException, Path as PathParam, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field
from sqlalchemy import desc, func, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.admin.policy_admin import (
    get_policy,
    persist_runtime_override_to_yaml,
    set_policy_override,
)
from app.admin.preview import render_preview
from app.admin.run_runner import get_run, start_run
from app.admin.sources_admin import (
    ALLOWED_UPDATE_FIELDS,
    add_source as registry_add_source,
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


class AddSourceRequest(BaseModel):
    """Body for ``POST /api/sources`` — append a new yaml registry entry.

    ``name`` and ``source_type`` are required; everything else is optional and
    validated/whitelisted by :func:`app.admin.sources_admin.add_source`. The
    pydantic layer is intentionally permissive (no ``Literal`` enums) so
    domain-level errors come through as HTTP 400 with a readable message.
    """

    name: str
    source_type: str
    url: Optional[str] = None
    homepage_url: Optional[str] = None
    trust_level: Optional[str] = None
    source_tier: Optional[str] = None
    category: Optional[str] = None
    priority: Optional[int] = None
    max_items: Optional[int] = None
    enabled: Optional[bool] = None
    org: Optional[str] = None
    query: Optional[str] = None
    listing_url: Optional[str] = None
    sitemap_url: Optional[str] = None
    include_url_patterns: Optional[list[str]] = None
    max_candidates: Optional[int] = None
    collector_type: Optional[str] = None
    content_category: Optional[str] = None

    model_config = {"extra": "ignore"}

    def to_fields(self) -> dict[str, Any]:
        return {k: v for k, v in self.model_dump().items() if v is not None}


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
    # Section UUIDs the operator toggled OFF in Review. The DB row has no
    # `enabled` column — re-render time is the only place we apply this.
    disabled_section_ids: Optional[list[str]] = None

    model_config = {"extra": "allow"}


class RenderRequest(BaseModel):
    """Body for ``POST /api/reports/{date}/render`` — render-only debug hook."""

    disabled_section_ids: Optional[list[str]] = None

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
@app.get("/api/reports/{date_kst}/html", include_in_schema=False)
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
    project_root = Path(__file__).resolve().parents[2]
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


# 7b) POST /api/policy/persist — flush the volatile override into yaml.
# Errors:
#   400 — runtime override is empty (nothing to persist).
#   500 — atomic write failed (disk full, permissions, etc.).
@app.post("/api/policy/persist")
async def api_persist_policy():
    """Atomically write the in-memory runtime override into ``editorial_policy.yaml``.

    Creates a ``*.yaml.bak`` next to the target on success so the operator can
    recover the previous policy. Body is intentionally empty — the helper uses
    the project-default yaml path.
    """
    try:
        result = persist_runtime_override_to_yaml()
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc))
    except Exception as exc:  # pragma: no cover — defensive
        logger.error("policy_persist_failed", error=str(exc))
        raise HTTPException(status_code=500, detail=f"policy persist failed: {exc}")

    project_root = Path(__file__).resolve().parents[2]
    persisted = result["persisted_to"]
    backup = result["backup"]

    def _to_rel(path: Path | None) -> str | None:
        if path is None:
            return None
        try:
            return str(Path(path).resolve().relative_to(project_root))
        except ValueError:
            return str(path)

    return {
        "persisted_to": _to_rel(persisted),
        "backup": _to_rel(backup),
    }


# 8a) GET /api/sources — registry sources (yaml-backed)
@app.get("/api/sources")
async def api_list_sources():
    return {"sources": registry_list_sources()}


# 8b) POST /api/sources — append a new entry to the registry yaml.
# Errors:
#   400 — missing/invalid required field, duplicate name, unknown key,
#         malformed url (when supplied).
@app.post("/api/sources", status_code=201)
async def api_add_source(
    payload: AddSourceRequest = Body(...),
):
    fields = payload.to_fields()

    # Validate URL eagerly when supplied — the registry layer accepts
    # arbitrary strings, but the FE always sends a value so we want a clear
    # error here rather than at collect-time.
    url = fields.get("url")
    if url is not None:
        parsed = urlparse(str(url))
        if parsed.scheme not in ("http", "https") or not parsed.netloc:
            raise HTTPException(
                status_code=400,
                detail="'url' must be an http(s) URL with a host",
            )

    try:
        created = registry_add_source(fields)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc))
    return {"source": created}


# 8c) PUT /api/sources/{name} — patch enabled/priority/etc.
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


# 13) POST /api/reports/{date}/render — re-render HTML from DB (no deploy)
@app.post("/api/reports/{date_kst}/render")
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

    project_root = Path(__file__).resolve().parents[2]
    try:
        rel_path = str(rendered_path.resolve().relative_to(project_root))
    except ValueError:
        rel_path = str(rendered_path)

    return {
        "rendered_path": rel_path,
        "sections": section_count,
        "disabled_count": len(payload.disabled_section_ids or []),
    }


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

        # index.html and SPA fallback responses must NEVER be cached, otherwise
        # users keep loading old chunk hashes after a fresh build (the symptom
        # was 404 on Sources-XXXX.js after rebuilding tokens.css). /assets/* is
        # already content-hashed by Vite so the StaticFiles mount above can
        # cache long-term — this only applies to the shell.
        no_store = {"Cache-Control": "no-store, must-revalidate"}

        # Top-level static files (favicon.ico, robots.txt, etc.) ship straight
        # from disk when they exist.
        candidate = (_ui_dist / full_path).resolve()
        try:
            candidate.relative_to(_ui_dist.resolve())
        except ValueError:
            # Path traversal — fall through to index.html.
            candidate = None  # type: ignore[assignment]
        if candidate and candidate.is_file():
            # Top-level non-hashed files (favicon, robots) get default caching
            # via FileResponse, but if the request is for an unhashed JS/CSS
            # at the root we still want freshness. Apply no-store only to the
            # shell entry.
            return FileResponse(str(candidate))

        # All other paths render the SPA shell — must always be fresh.
        return FileResponse(str(_index_html), headers=no_store)

else:
    logger.info(
        "ui_dist_not_found",
        path=str(_ui_dist),
        note="run `make ui-build` to populate ui/dist before serving the SPA",
    )
