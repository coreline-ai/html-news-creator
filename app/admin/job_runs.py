"""Minimal JobRun persistence helpers for admin-triggered pipeline runs.

This module intentionally stores only run lifecycle summaries. Full stdout /
stderr log persistence belongs to a later JobLog phase.
"""
from __future__ import annotations

import uuid
from datetime import date, datetime
from typing import Any

from sqlalchemy import desc, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.db import AsyncSessionLocal
from app.models.db_models import JobRun
from app.utils.logger import get_logger

logger = get_logger(step="admin.job_runs")

_JOB_NAME = "daily_report"
_RUNNER_NAME = "scripts/run_daily.py"
_TRACKABLE_STATUSES = {"queued", "running"}
_ALLOWED_STATUSES = {"queued", "running", "completed", "failed", "cancelled"}


def coerce_run_uuid(run_id: str) -> uuid.UUID | None:
    """Parse both hex and hyphenated UUID strings used by FE/DB."""
    try:
        return uuid.UUID(str(run_id))
    except (TypeError, ValueError, AttributeError):
        return None


def parse_report_date(options: dict[str, Any] | None) -> date | None:
    raw = (options or {}).get("date") or (options or {}).get("run_date")
    if not raw:
        return None
    try:
        return date.fromisoformat(str(raw))
    except ValueError:
        return None


def parse_iso_datetime(value: str | None) -> datetime | None:
    if not value:
        return None
    try:
        return datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return None


def normalise_status(status: str | None) -> str:
    if status in _ALLOWED_STATUSES:
        return status
    return "failed"


def build_job_metadata(state: Any) -> dict[str, Any]:
    options = dict(getattr(state, "options", {}) or {})
    return_code = getattr(state, "return_code", None)
    error = getattr(state, "error", None)
    metadata: dict[str, Any] = {
        "run_id": getattr(state, "run_id", None),
        "runner": _RUNNER_NAME,
        "options": options,
        "return_code": return_code,
    }
    if error:
        metadata["error"] = error
    return metadata


def error_code_for_state(state: Any) -> str | None:
    status = getattr(state, "status", None)
    error = getattr(state, "error", None)
    return_code = getattr(state, "return_code", None)
    if status != "failed":
        return None
    if error:
        return str(error).split(":", 1)[0][:80]
    if isinstance(return_code, int) and return_code != 0:
        return "nonzero_exit"
    return "runner_failed"


def job_run_to_summary(job: JobRun, *, trackable: bool) -> dict[str, Any]:
    metadata = job.metadata_json if isinstance(job.metadata_json, dict) else {}
    run_id = metadata.get("run_id") if isinstance(metadata.get("run_id"), str) else None
    if not run_id:
        run_id = job.id.hex if isinstance(job.id, uuid.UUID) else str(job.id)
    options = (
        metadata.get("options") if isinstance(metadata.get("options"), dict) else {}
    )
    status = normalise_status(str(job.status) if job.status is not None else None)
    error = job.error_message
    if not trackable and status in _TRACKABLE_STATUSES and not error:
        error = "server_restart_or_memory_state_lost: run is no longer stream-trackable"
    return {
        "id": str(job.id),
        "run_id": run_id,
        "status": status,
        "started_at": job.started_at.isoformat() if job.started_at else None,
        "completed_at": job.completed_at.isoformat() if job.completed_at else None,
        "return_code": metadata.get("return_code"),
        "error": error,
        "options": options,
        "report_date": job.report_date.isoformat() if job.report_date else None,
        "trackable": trackable,
        "source": "memory" if trackable else "db",
    }


def memory_run_to_summary(summary: dict[str, Any]) -> dict[str, Any]:
    return {**summary, "trackable": True, "source": "memory"}


async def persist_job_run_state(state: Any) -> None:
    """Best-effort upsert of a RunState into `job_runs`.

    Persistence must never fail the actual pipeline run. Any DB problem is
    logged and swallowed so local/offline runs continue to work.
    """
    run_id = getattr(state, "run_id", None)
    run_uuid = coerce_run_uuid(str(run_id)) if run_id else None
    if run_uuid is None:
        logger.warning("job_run_persist_skipped_bad_run_id", run_id=str(run_id))
        return

    try:
        async with AsyncSessionLocal() as session:
            job = await session.get(JobRun, run_uuid)
            if job is None:
                job = JobRun(
                    id=run_uuid,
                    job_name=_JOB_NAME,
                    report_date=parse_report_date(getattr(state, "options", None)),
                )
                session.add(job)

            job.status = normalise_status(getattr(state, "status", None))
            job.started_at = parse_iso_datetime(getattr(state, "started_at", None))
            job.completed_at = parse_iso_datetime(getattr(state, "completed_at", None))
            job.error_code = error_code_for_state(state)
            job.error_message = getattr(state, "error", None)
            job.metadata_json = build_job_metadata(state)
            await session.commit()
    except Exception as exc:  # pragma: no cover - depends on local DB availability
        logger.warning(
            "job_run_persist_failed",
            run_id=str(run_id),
            status=getattr(state, "status", None),
            error=str(exc),
        )


async def list_persisted_job_runs(
    db: AsyncSession,
    *,
    limit: int,
) -> list[dict[str, Any]]:
    try:
        result = await db.execute(
            select(JobRun)
            .order_by(desc(JobRun.started_at), desc(JobRun.created_at))
            .limit(limit)
        )
        return [
            job_run_to_summary(job, trackable=False)
            for job in result.scalars().all()
        ]
    except Exception as exc:
        logger.warning("job_run_list_failed", error=str(exc))
        return []


async def get_persisted_job_run(
    db: AsyncSession,
    run_id: str,
) -> dict[str, Any] | None:
    run_uuid = coerce_run_uuid(run_id)
    if run_uuid is None:
        return None
    try:
        result = await db.execute(select(JobRun).where(JobRun.id == run_uuid).limit(1))
        job = result.scalars().first()
        if job is None:
            return None
        summary = job_run_to_summary(job, trackable=False)
        return summary
    except Exception as exc:
        logger.warning("job_run_get_failed", run_id=run_id, error=str(exc))
        return None


__all__ = [
    "build_job_metadata",
    "coerce_run_uuid",
    "get_persisted_job_run",
    "job_run_to_summary",
    "list_persisted_job_runs",
    "memory_run_to_summary",
    "parse_report_date",
    "persist_job_run_state",
]
