"""Run + preview endpoints.

Routes:
  - POST /api/preview          — in-memory render (no DB writes)
  - POST /api/runs             — kick off a background pipeline run
  - GET  /api/runs/{id}/stream — SSE progress stream
"""

from __future__ import annotations
from typing import Any

from fastapi import APIRouter, Body, HTTPException

from app.admin.preview import render_preview
from app.admin.routers._models import PreviewRequest, RunRequest
from app.admin.run_runner import get_run, start_run
from app.admin.sse import stream_run

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


@router.get("/api/runs/{run_id}/stream")
async def api_stream_run(run_id: str):
    return stream_run(run_id)
