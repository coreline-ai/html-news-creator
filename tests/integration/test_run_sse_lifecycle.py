"""End-to-end SSE lifecycle: POST /api/runs → GET /stream → done event.

The pipeline subprocess (``scripts/run_daily.py``) is mocked at the
``asyncio.create_subprocess_exec`` boundary so the test never needs the
LLM proxy, network, or DB. We feed the runner a tiny script of stdout
lines (one structlog-shaped JSON record + EOF) so the SSE layer has
something realistic to normalize and surface.

Contract verified:
- 200 + a valid run_id from POST /api/runs
- At least one ``progress`` SSE event with the documented schema
  (``step``, ``progress``, optional ``message``/``raw_line``)
- A ``done`` event arrives within 30s and carries a terminal status
"""
from __future__ import annotations

import asyncio
import json
from typing import AsyncIterator
from unittest.mock import MagicMock

import pytest

from app.admin import run_runner

pytestmark = pytest.mark.asyncio

# How long to wait for the lifecycle as a whole. The runner itself has a
# `_DEFAULT_MAX_RUNTIME_SEC` of 300 but the mocked subprocess exits
# immediately, so 30s is *generous* — failure here means the SSE plumbing
# is wedged, not slow.
_LIFECYCLE_DEADLINE_SEC = 30.0


# ---------------------------------------------------------------------------
# Fake subprocess scaffolding
# ---------------------------------------------------------------------------

class _ScriptedReader:
    """Minimal asyncio.StreamReader stand-in.

    Yields each ``lines`` entry on successive ``readline()`` calls and then
    returns ``b""`` to signal EOF (matching the contract that
    ``run_runner._drain_stream`` relies on to exit its read loop).
    """

    def __init__(self, lines: list[bytes]) -> None:
        self._lines = list(lines)

    async def readline(self) -> bytes:
        if not self._lines:
            return b""
        return self._lines.pop(0)


def _make_fake_subprocess_factory(stdout_lines: list[bytes], rc: int = 0):
    """Return a coroutine compatible with ``asyncio.create_subprocess_exec``."""
    async def _factory(*_args, **_kwargs):
        proc = MagicMock()
        proc.stdout = _ScriptedReader(stdout_lines)
        proc.stderr = _ScriptedReader([])
        proc.returncode = rc

        async def _wait() -> int:
            return rc

        proc.wait = _wait
        return proc

    return _factory


# ---------------------------------------------------------------------------
# SSE parsing helper
# ---------------------------------------------------------------------------

async def _read_sse_until_done(
    stream_iter: AsyncIterator[bytes], deadline_sec: float
) -> list[dict]:
    """Read raw SSE bytes, return the list of decoded {event, data} frames.

    Stops as soon as a ``done`` frame is observed (or the deadline expires).
    Works against ``httpx.AsyncClient.stream(...).aiter_bytes()``.
    """
    buf = ""
    frames: list[dict] = []

    def _split_frames(blob: str) -> tuple[list[str], str]:
        """Pull complete SSE frames out of ``blob``; return (frames, leftover).

        sse-starlette emits CRLF line endings (``\\r\\n``) and frame
        separators of ``\\r\\n\\r\\n``. Be tolerant of bare ``\\n\\n`` too in
        case the framing changes upstream.
        """
        # Normalize line endings so a single split rule handles both styles.
        normalized = blob.replace("\r\n", "\n")
        chunks = normalized.split("\n\n")
        # The last chunk is whatever is left after the trailing separator —
        # if the blob ended on a frame boundary it's an empty string.
        complete = chunks[:-1]
        leftover = chunks[-1]
        return complete, leftover

    async def _consume() -> None:
        nonlocal buf
        async for chunk in stream_iter:
            buf += chunk.decode("utf-8", errors="replace")
            complete, buf = _split_frames(buf)
            for raw_frame in complete:
                event = "message"
                data_lines: list[str] = []
                for line in raw_frame.splitlines():
                    if line.startswith("event:"):
                        event = line[len("event:"):].strip()
                    elif line.startswith("data:"):
                        data_lines.append(line[len("data:"):].strip())
                    # ":" comments and other field types are ignored.
                if not data_lines:
                    continue
                data_str = "\n".join(data_lines)
                try:
                    data = json.loads(data_str) if data_str else {}
                except json.JSONDecodeError:
                    data = {"_raw": data_str}
                frames.append({"event": event, "data": data})
                if event == "done":
                    return

    try:
        await asyncio.wait_for(_consume(), timeout=deadline_sec)
    except asyncio.TimeoutError:
        # Caller decides whether the absence of `done` is a failure based on
        # the frames collected so far.
        pass
    return frames


# ---------------------------------------------------------------------------
# POST /api/runs — happy path
# ---------------------------------------------------------------------------

async def test_post_runs_returns_run_id(async_client, monkeypatch):
    """POST /api/runs accepts the documented body and returns a run_id."""
    run_runner.reset_for_tests()
    monkeypatch.setattr(
        "app.admin.run_runner.asyncio.create_subprocess_exec",
        _make_fake_subprocess_factory([], rc=0),
    )

    resp = await async_client.post(
        "/api/runs",
        json={"date": "2026-05-01", "mode": "full", "dry_run": True},
    )
    assert resp.status_code == 200, resp.text
    body = resp.json()
    assert "run_id" in body and body["run_id"]
    # The runner may already be finished by the time the response is built —
    # any of the four lifecycle states is acceptable here.
    assert body["status"] in {"queued", "running", "completed", "failed"}
    # Options round-tripped intact.
    assert body["options"]["dry_run"] is True
    assert body["options"]["mode"] == "full"


# ---------------------------------------------------------------------------
# Full lifecycle — progress → done within 30s
# ---------------------------------------------------------------------------

async def test_run_sse_lifecycle_progress_then_done(async_client, monkeypatch):
    """Spawn a fake subprocess, subscribe to /stream, assert lifecycle."""
    run_runner.reset_for_tests()

    structlog_line = json.dumps(
        {
            "step": "collect",
            "event": "github_anonymous_fallback",
            "level": "info",
            "timestamp": "2026-05-01T00:00:00Z",
        }
    ).encode("utf-8") + b"\n"
    monkeypatch.setattr(
        "app.admin.run_runner.asyncio.create_subprocess_exec",
        _make_fake_subprocess_factory([structlog_line], rc=0),
    )

    resp = await async_client.post(
        "/api/runs",
        json={
            "date": "2026-05-01",
            "mode": "full",
            "dry_run": True,
            # Tighten the runner's own wall-clock guard so a wedged test
            # fails fast instead of hanging the suite.
            "max_runtime_sec": 10,
        },
    )
    assert resp.status_code == 200, resp.text
    run_id = resp.json()["run_id"]

    async with async_client.stream(
        "GET", f"/api/runs/{run_id}/stream"
    ) as stream:
        assert stream.status_code == 200
        # sse-starlette uses text/event-stream — be tolerant of charset suffix.
        assert "text/event-stream" in stream.headers.get("content-type", "")
        frames = await _read_sse_until_done(
            stream.aiter_bytes(), deadline_sec=_LIFECYCLE_DEADLINE_SEC
        )

    # The replay loop emits a `progress` event for every queued line — at
    # least the one we scripted must be there.
    progress_frames = [f for f in frames if f["event"] == "progress"]
    assert progress_frames, f"no progress frames received; got {frames!r}"

    # Schema contract — keys the FE relies on.
    sample = progress_frames[0]["data"]
    assert isinstance(sample, dict)
    assert "step" in sample
    assert "progress" in sample
    # `message` and `raw_line` are documented but optional (empty string is
    # the canonical "absent" sentinel from sse._normalise_progress).
    assert "message" in sample or "raw_line" in sample

    # Lifecycle terminator with a known terminal status.
    done_frames = [f for f in frames if f["event"] == "done"]
    assert done_frames, f"no done frame within {_LIFECYCLE_DEADLINE_SEC}s"
    done = done_frames[-1]["data"]
    assert done.get("status") in {"completed", "failed", "error"}
