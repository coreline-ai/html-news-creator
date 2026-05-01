"""Legacy v1 endpoints + /health.

Kept as-is so existing tests continue to pass against the same response
shapes. Routes registered here:

  - GET /health
  - GET /api/v1/runs
  - GET /api/v1/runs/{run_id}/logs
  - GET /api/v1/reports
  - GET /api/v1/stats/today
  - GET /api/v1/sources
"""

from __future__ import annotations
from datetime import date

from fastapi import APIRouter, Depends, Query
from sqlalchemy import desc, func, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.db import get_db
from app.models.db_models import Cluster, JobLog, JobRun, RawItem, Report, Source

router = APIRouter()


@router.get("/health")
async def health():
    return {"status": "ok", "service": "ai-trend-report-engine"}


@router.get("/api/v1/runs")
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


@router.get("/api/v1/runs/{run_id}/logs")
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


@router.get("/api/v1/reports")
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


@router.get("/api/v1/stats/today")
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


@router.get("/api/v1/sources")
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
