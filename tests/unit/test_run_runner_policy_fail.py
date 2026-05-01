"""Phase F 묶음 Z — policy materialize hard-fail.

When the runtime policy override is set but materializing it to disk fails
(disk full, perms, yaml dump bug, …), the operator's explicit intent would
silently regress to the default policy if we swallowed the error. Instead,
``_supervise`` must:

1. mark the run as ``failed`` with an explanatory ``error`` string,
2. emit a ``control:done`` SSE event so the FE useRunStream flips to error,
3. NOT spawn the ``run_daily.py`` subprocess at all.
"""
from __future__ import annotations

import asyncio
from unittest.mock import MagicMock

import pytest

from app.admin import run_runner
from app.admin.run_runner import RunState, _supervise


@pytest.fixture(autouse=True)
def _reset_runs():
    run_runner.reset_for_tests()
    yield
    run_runner.reset_for_tests()


def test_supervise_marks_run_failed_when_materialize_raises(monkeypatch):
    """``_materialize_policy_override`` raising ⇒ run fails, no subprocess."""
    def _boom() -> None:
        raise RuntimeError("disk full")

    monkeypatch.setattr(
        run_runner, "_materialize_policy_override", _boom
    )

    spawn_calls: list = []

    async def fake_create_subprocess_exec(*args, **kwargs):  # pragma: no cover
        spawn_calls.append((args, kwargs))
        proc = MagicMock()
        proc.returncode = 0
        return proc

    monkeypatch.setattr(
        run_runner.asyncio,
        "create_subprocess_exec",
        fake_create_subprocess_exec,
    )

    async def _drive():
        state = RunState(run_id="z1", options={"dry_run": True})
        await _supervise(state)
        return state

    state = asyncio.run(_drive())

    assert state.status == "failed"
    assert state.error is not None
    assert "policy_override_materialize_failed" in state.error
    assert "disk full" in state.error
    assert state.completed_at is not None
    assert state.return_code is None

    # Subprocess must NOT have been started — fail-loud, fail-fast.
    assert spawn_calls == [], (
        f"expected zero subprocess spawns, got {len(spawn_calls)}"
    )


def test_supervise_emits_control_done_failed_event(monkeypatch):
    """The FE listens on ``control:done`` to flip useRunStream → error.

    Even when we abort before subprocess spawn, the queue must receive the
    terminal event or the operator's UI hangs in ``running`` forever.
    """
    def _boom() -> None:
        raise OSError("permission denied")

    monkeypatch.setattr(run_runner, "_materialize_policy_override", _boom)

    async def fake_create_subprocess_exec(*args, **kwargs):  # pragma: no cover
        raise AssertionError("subprocess must not start on materialize fail")

    monkeypatch.setattr(
        run_runner.asyncio,
        "create_subprocess_exec",
        fake_create_subprocess_exec,
    )

    async def _drive():
        state = RunState(run_id="z2", options={"dry_run": True})
        await _supervise(state)
        # Drain the queue so we can assert on the terminal event.
        events: list = []
        while not state.queue.empty():
            events.append(state.queue.get_nowait())
        return state, events

    state, events = asyncio.run(_drive())

    assert state.status == "failed"
    assert events, "expected at least one queue event (control:done)"
    done_events = [e for e in events if e.get("event") == "done"]
    assert len(done_events) == 1, f"expected exactly one done event, got {events!r}"
    done = done_events[0]
    assert done["stream"] == "control"
    assert done["status"] == "failed"
    assert done["return_code"] is None
    assert "policy_override_materialize_failed" in (done.get("error") or "")
    assert "permission denied" in done["error"]
