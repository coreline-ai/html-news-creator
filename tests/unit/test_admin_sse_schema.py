"""Unit tests for the structured SSE progress schema (Phase A).

We don't spin up the FastAPI route here — instead we drive the helper that
shapes runner queue payloads into the `{step, progress, message, raw_line}`
contract that the FE hook expects. This keeps the test fast and decoupled
from EventSource / sse_starlette plumbing.
"""
from __future__ import annotations

import json

import pytest

from app.admin.run_runner import RunState
from app.admin.sse import STEPS, _event_iter, _normalise_progress


def test_progress_payload_extracts_step_from_structlog_line():
    line = json.dumps(
        {
            "step": "collect",
            "event": "github_anonymous_fallback",
            "level": "warning",
            "timestamp": "2026-04-30T01:23:45Z",
        }
    )
    payload = _normalise_progress({"stream": "stdout", "line": line, "ts": "x"})

    assert payload["step"] == "collect"
    assert payload["progress"] == STEPS.index("collect") / (len(STEPS) - 1)
    assert payload["message"] == "github_anonymous_fallback"
    assert payload["raw_line"] == line


def test_progress_payload_marks_unknown_step_with_zero_progress():
    line = "raw text emitted by an external library, not JSON"
    payload = _normalise_progress({"stream": "stderr", "line": line, "ts": "x"})

    assert payload["step"] == "unknown"
    assert payload["progress"] == 0.0
    assert payload["message"] == ""
    assert payload["raw_line"] == line


def test_progress_payload_handles_invalid_json_with_brace_prefix():
    # Looks like JSON, isn't — the parser must fall back gracefully.
    line = "{not valid json"
    payload = _normalise_progress({"stream": "stdout", "line": line, "ts": "x"})

    assert payload["step"] == "unknown"
    assert payload["progress"] == 0.0
    assert payload["raw_line"] == line


def test_progress_payload_keys_are_stable_contract():
    """FE depends on the four-key shape — guard it explicitly."""
    payload = _normalise_progress({"stream": "stdout", "line": "{}", "ts": "x"})
    assert set(payload.keys()) == {"step", "progress", "message", "raw_line"}


def test_progress_payload_progress_is_full_at_notify_step():
    line = json.dumps({"step": "notify", "event": "slack_skipped"})
    payload = _normalise_progress({"stream": "stdout", "line": line, "ts": "x"})

    assert payload["step"] == "notify"
    assert payload["progress"] == 1.0
    assert payload["message"] == "slack_skipped"


def test_progress_payload_handles_empty_payload_dict():
    payload = _normalise_progress({})
    assert payload == {
        "step": "unknown",
        "progress": 0.0,
        "message": "",
        "raw_line": "",
    }


@pytest.mark.asyncio
async def test_event_iter_replays_done_for_terminal_late_subscriber(monkeypatch):
    """A completed run must still terminate late SSE subscribers."""
    state = RunState(run_id="run-1", options={"dry_run": True})
    state.status = "completed"
    state.started_at = "2026-05-01T00:00:00+00:00"
    state.completed_at = "2026-05-01T00:00:01+00:00"
    state.return_code = 0
    state.history.append(
        {
            "stream": "stdout",
            "line": json.dumps({"step": "render", "event": "rendered"}),
            "ts": state.started_at,
        }
    )

    monkeypatch.setattr(
        "app.admin.sse.get_run",
        lambda run_id: state if run_id == "run-1" else None,
    )

    frames = [frame async for frame in _event_iter("run-1")]

    assert [frame["event"] for frame in frames] == ["progress", "done"]
    done = json.loads(frames[-1]["data"])
    assert done["event"] == "done"
    assert done["status"] == "completed"
    assert done["return_code"] == 0
