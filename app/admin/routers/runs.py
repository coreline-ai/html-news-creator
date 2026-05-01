"""Run + preview endpoints.

Routes:
  - POST /api/preview          — in-memory render (no DB writes)
  - GET  /api/runs             — list in-memory background runs
  - POST /api/runs             — kick off a background pipeline run
  - GET  /api/runs/{id}        — inspect one in-memory background run
  - GET  /api/runs/{id}/stream — SSE progress stream
"""

from __future__ import annotations
from typing import Any

from fastapi import APIRouter, Body, Depends, HTTPException, Query
from sqlalchemy.ext.asyncio import AsyncSession

from app.admin.job_runs import (
    get_persisted_job_run,
    list_persisted_job_runs,
    memory_run_to_summary,
)
from app.admin.preview import render_preview
from app.admin.routers._models import PreviewRequest, RunRequest
from app.admin.run_runner import get_run, list_runs, start_run
from app.admin.sse import stream_run
from app.db import get_db

router = APIRouter()


@router.post("/api/preview")
async def api_preview(payload: PreviewRequest = Body(default_factory=PreviewRequest)):
    options: dict[str, Any] = payload.model_dump(exclude_none=True)
    date_kst = options.pop("date_kst", None)
    try:
        html = render_preview(options=options, date_kst=date_kst)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc))
    return {"html": html, "length": len(html)}


@router.post("/api/runs")
async def api_start_run(payload: RunRequest = Body(default_factory=RunRequest)):
    options = payload.model_dump(exclude_none=True)
    run_id = await start_run(options)
    state = get_run(run_id)
    return {
        "run_id": run_id,
        "status": state.status if state else "queued",
        "options": options,
    }


@router.get("/api/runs")
async def api_list_runs(
    limit: int = Query(default=20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
):
    memory_runs = [memory_run_to_summary(run) for run in reversed(list_runs())]
    persisted_runs = await list_persisted_job_runs(db, limit=limit)

    seen: set[str] = set()
    merged: list[dict[str, Any]] = []
    for run in [*memory_runs, *persisted_runs]:
        key = str(run.get("run_id") or run.get("id") or "")
        if key in seen:
            continue
        seen.add(key)
        merged.append(run)
        if len(merged) >= limit:
            break
    return {"runs": merged}


@router.get("/api/runs/{run_id}")
async def api_get_run(
    run_id: str,
    db: AsyncSession = Depends(get_db),
):
    state = get_run(run_id)
    if state is not None:
        return {"run": memory_run_to_summary(state.to_summary())}

    persisted = await get_persisted_job_run(db, run_id)
    if persisted is not None:
        return {"run": persisted}
    raise HTTPException(status_code=404, detail=f"unknown run_id: {run_id}")


@router.get("/api/runs/{run_id}/stream")
async def api_stream_run(run_id: str):
    return stream_run(run_id)
