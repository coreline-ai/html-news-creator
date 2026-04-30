"""Background pipeline runner.

Wraps ``scripts/run_daily.py`` in an asyncio subprocess so the FastAPI layer
can stream stdout lines as SSE progress events. State is held in-memory; if
the API process restarts, ongoing runs are lost (acceptable for a single-user
admin tool — the operator can always restart).
"""
from __future__ import annotations

import asyncio
import os
import sys
import uuid
from collections import deque
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

PROJECT_ROOT = Path(__file__).resolve().parents[2]
RUN_DAILY_PATH = PROJECT_ROOT / "scripts" / "run_daily.py"

# Per-line history retained per run (so a late SSE subscriber can replay)
_MAX_LINES_PER_RUN = 2000


@dataclass
class RunState:
    run_id: str
    options: dict[str, Any]
    status: str = "queued"  # queued | running | completed | failed
    started_at: str | None = None
    completed_at: str | None = None
    return_code: int | None = None
    error: str | None = None
    queue: asyncio.Queue = field(default_factory=asyncio.Queue)
    history: deque = field(default_factory=lambda: deque(maxlen=_MAX_LINES_PER_RUN))
    process: asyncio.subprocess.Process | None = None
    task: asyncio.Task | None = None

    def to_summary(self) -> dict[str, Any]:
        return {
            "run_id": self.run_id,
            "status": self.status,
            "started_at": self.started_at,
            "completed_at": self.completed_at,
            "return_code": self.return_code,
            "error": self.error,
            "options": self.options,
        }


_RUNS: dict[str, RunState] = {}
_RUNS_LOCK = asyncio.Lock()


def _build_argv(options: dict[str, Any]) -> list[str]:
    """Translate UI options dict into ``run_daily.py`` CLI flags."""
    argv: list[str] = [sys.executable, str(RUN_DAILY_PATH)]
    if options.get("date") or options.get("run_date"):
        argv += ["--date", str(options.get("date") or options.get("run_date"))]
    mode = options.get("mode")
    if mode:
        argv += ["--mode", str(mode)]
    from_step = options.get("from_step")
    if from_step:
        argv += ["--from-step", str(from_step)]
    to_step = options.get("to_step")
    if to_step:
        argv += ["--to-step", str(to_step)]
    if options.get("dry_run"):
        argv += ["--dry-run"]
    return argv


async def _drain_stream(state: RunState, stream: asyncio.StreamReader, label: str) -> None:
    """Pump subprocess output into the in-memory queue + replay history."""
    while True:
        line = await stream.readline()
        if not line:
            break
        text = line.decode("utf-8", errors="replace").rstrip("\n")
        event = {
            "stream": label,
            "line": text,
            "ts": datetime.now(timezone.utc).isoformat(),
        }
        state.history.append(event)
        await state.queue.put(event)


async def _supervise(state: RunState) -> None:
    state.status = "running"
    state.started_at = datetime.now(timezone.utc).isoformat()
    argv = _build_argv(state.options)
    env = os.environ.copy()
    env.setdefault("PYTHONPATH", str(PROJECT_ROOT))
    try:
        proc = await asyncio.create_subprocess_exec(
            *argv,
            cwd=str(PROJECT_ROOT),
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
            env=env,
        )
        state.process = proc
        await asyncio.gather(
            _drain_stream(state, proc.stdout, "stdout"),
            _drain_stream(state, proc.stderr, "stderr"),
        )
        state.return_code = await proc.wait()
        state.status = "completed" if state.return_code == 0 else "failed"
    except FileNotFoundError as exc:
        state.error = f"runner_not_found: {exc}"
        state.status = "failed"
    except Exception as exc:  # pragma: no cover — defensive
        state.error = repr(exc)
        state.status = "failed"
    finally:
        state.completed_at = datetime.now(timezone.utc).isoformat()
        await state.queue.put(
            {
                "stream": "control",
                "event": "done",
                "status": state.status,
                "return_code": state.return_code,
                "error": state.error,
                "ts": state.completed_at,
            }
        )


async def start_run(options: dict[str, Any] | None = None) -> str:
    """Spawn ``scripts/run_daily.py`` in the background, return the run_id."""
    opts = dict(options or {})
    run_id = uuid.uuid4().hex
    state = RunState(run_id=run_id, options=opts)
    async with _RUNS_LOCK:
        _RUNS[run_id] = state
    state.task = asyncio.create_task(_supervise(state))
    return run_id


def get_run(run_id: str) -> RunState | None:
    return _RUNS.get(run_id)


def list_runs() -> list[dict[str, Any]]:
    return [state.to_summary() for state in _RUNS.values()]


def reset_for_tests() -> None:
    """Test helper — clear the in-memory run registry."""
    _RUNS.clear()


__all__ = [
    "RunState",
    "start_run",
    "get_run",
    "list_runs",
    "reset_for_tests",
]
