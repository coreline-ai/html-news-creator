"""Server-Sent Events helpers for streaming pipeline progress.

The progress event payload is a stable, FE-facing contract:

    {
      "step": "collect",       # one of STEPS or "unknown"
      "progress": 0.11,        # step_index / len(STEPS); float 0..1
      "message": "github_anonymous_fallback",  # event / status string
      "raw_line": "{...}"      # original stdout line (untouched)
    }

When the runner stdout line is not structured JSON we still emit the same
shape with ``step="unknown"`` so the FE never has to special-case raw text.
"""
from __future__ import annotations

import asyncio
import json
from typing import Any, AsyncIterator

from fastapi import HTTPException
from sse_starlette.sse import EventSourceResponse

from app.admin.run_runner import get_run

# How long to wait between polls when re-checking run state if the queue is idle.
_HEARTBEAT_INTERVAL_SEC = 15

# Pipeline step ordering — used to compute a 0..1 progress fraction.
# Keep in sync with scripts/run_daily.py::PIPELINE_STEPS / dev-plan.
STEPS: list[str] = [
    "collect",
    "extract",
    "classify",
    "cluster",
    "verify",
    "image_analyze",
    "generate",
    "render",
    "publish",
    "notify",
]
_STEP_INDEX: dict[str, int] = {name: i for i, name in enumerate(STEPS)}
_STEP_DENOM = max(len(STEPS) - 1, 1)


def _normalise_progress(payload: dict[str, Any]) -> dict[str, Any]:
    """Translate a runner queue payload into the FE-facing progress schema.

    ``payload`` is what ``run_runner._drain_stream`` puts on the queue:
    ``{"stream": "stdout"|"stderr", "line": "...", "ts": "..."}``.
    The runner emits structlog JSON lines (one log record per line), so we
    try to parse and pull ``step``/``event``/``level`` out. Plain text lines
    fall back to ``step="unknown"``.
    """
    raw_line = payload.get("line", "") if isinstance(payload, dict) else ""
    step = "unknown"
    message = ""
    parsed: dict[str, Any] | None = None
    if isinstance(raw_line, str) and raw_line.strip().startswith("{"):
        try:
            obj = json.loads(raw_line)
            if isinstance(obj, dict):
                parsed = obj
        except (json.JSONDecodeError, ValueError):
            parsed = None

    if parsed is not None:
        step_val = parsed.get("step")
        if isinstance(step_val, str) and step_val:
            step = step_val if step_val in _STEP_INDEX else step_val
        event_val = parsed.get("event")
        if isinstance(event_val, str) and event_val:
            message = event_val
        elif isinstance(parsed.get("message"), str):
            message = parsed["message"]
        # If the log record didn't carry ``step`` but its event matches a
        # known pipeline step (e.g. ``"step_start"`` with step= field), we
        # still default to "unknown" — the FE only needs the broad bucket.

    if step in _STEP_INDEX:
        progress = _STEP_INDEX[step] / _STEP_DENOM
    else:
        progress = 0.0

    return {
        "step": step,
        "progress": progress,
        "message": message,
        "raw_line": raw_line if isinstance(raw_line, str) else "",
    }


async def _event_iter(run_id: str) -> AsyncIterator[dict[str, Any]]:
    state = get_run(run_id)
    if state is None:
        # The route layer already rejects unknown runs; this is defense in depth.
        return

    # Replay everything observed so far so a late subscriber sees the full log.
    for past in list(state.history):
        yield {
            "event": "progress",
            "data": json.dumps(_normalise_progress(past), ensure_ascii=False),
        }

    while True:
        try:
            payload = await asyncio.wait_for(
                state.queue.get(), timeout=_HEARTBEAT_INTERVAL_SEC
            )
        except asyncio.TimeoutError:
            # SSE comment line keeps proxies happy without polluting client data.
            yield {"event": "heartbeat", "data": "{}"}
            if state.status in {"completed", "failed"}:
                break
            continue

        if payload.get("event") == "done":
            yield {"event": "done", "data": json.dumps(payload, ensure_ascii=False)}
            break
        yield {
            "event": "progress",
            "data": json.dumps(_normalise_progress(payload), ensure_ascii=False),
        }


def stream_run(run_id: str) -> EventSourceResponse:
    """Return an SSE response that streams progress lines for ``run_id``."""
    if get_run(run_id) is None:
        raise HTTPException(status_code=404, detail=f"unknown run_id: {run_id}")
    return EventSourceResponse(_event_iter(run_id))


__all__ = ["stream_run", "STEPS"]
