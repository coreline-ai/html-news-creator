"""Server-Sent Events helpers for streaming pipeline progress."""
from __future__ import annotations

import asyncio
import json
from typing import Any, AsyncIterator

from fastapi import HTTPException
from sse_starlette.sse import EventSourceResponse

from app.admin.run_runner import get_run

# How long to wait between polls when re-checking run state if the queue is idle.
_HEARTBEAT_INTERVAL_SEC = 15


async def _event_iter(run_id: str) -> AsyncIterator[dict[str, Any]]:
    state = get_run(run_id)
    if state is None:
        # The route layer already rejects unknown runs; this is defense in depth.
        return

    # Replay everything observed so far so a late subscriber sees the full log.
    for past in list(state.history):
        yield {
            "event": "progress",
            "data": json.dumps(past, ensure_ascii=False),
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
            "data": json.dumps(payload, ensure_ascii=False),
        }


def stream_run(run_id: str) -> EventSourceResponse:
    """Return an SSE response that streams progress lines for ``run_id``."""
    if get_run(run_id) is None:
        raise HTTPException(status_code=404, detail=f"unknown run_id: {run_id}")
    return EventSourceResponse(_event_iter(run_id))


__all__ = ["stream_run"]
