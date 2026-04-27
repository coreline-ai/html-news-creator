from __future__ import annotations
from datetime import date
from typing import Optional
from fastapi import FastAPI, Depends, HTTPException, Query
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func, desc
from app.db import get_db
from app.models.db_models import JobRun, JobLog, Report, ReportSection, Source, RawItem, Cluster
from app.utils.logger import get_logger

app = FastAPI(
    title="AI Trend Report Engine — Admin API",
    description="Internal admin dashboard for monitoring the pipeline",
    version="0.1.0",
)
logger = get_logger(step="admin")


@app.get("/health")
async def health():
    return {"status": "ok", "service": "ai-trend-report-engine"}


@app.get("/api/v1/runs")
async def list_runs(
    limit: int = Query(default=20, le=100),
    db: AsyncSession = Depends(get_db),
):
    """List recent job runs."""
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
                # JobRun uses metadata_json (not stats_json)
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
    """Get logs for a specific job run."""
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
                "level": l.level,
                # JobLog uses step_name (not step)
                "step": l.step_name,
                "message": l.message,
                "created_at": str(l.created_at) if l.created_at else None,
            }
            for l in logs
        ],
    }


@app.get("/api/v1/reports")
async def list_reports(
    limit: int = Query(default=10, le=50),
    db: AsyncSession = Depends(get_db),
):
    """List recent reports."""
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

    # Count raw items today
    raw_count_result = await db.execute(
        select(func.count(RawItem.id)).where(
            func.date(RawItem.collected_at) == today
        )
    )
    raw_count = raw_count_result.scalar() or 0

    # Count clusters today
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
async def list_sources(
    active_only: bool = True,
    db: AsyncSession = Depends(get_db),
):
    """List registered sources."""
    query = select(Source)
    if active_only:
        # Source uses `enabled` column (not `is_active`)
        query = query.where(Source.enabled == True)
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
                # Source uses `enabled` column (not `is_active`)
                "is_active": s.enabled,
            }
            for s in sources
        ]
    }
