"""Background pipeline runner.

Wraps ``scripts/run_daily.py`` in an asyncio subprocess so the FastAPI layer
can stream stdout lines as SSE progress events. State is held in-memory; if
the API process restarts, ongoing runs are lost (acceptable for a single-user
admin tool — the operator can always restart).
"""
from __future__ import annotations

import asyncio
import json
import os
import sys
import tempfile
import uuid
from collections import deque
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from app.admin import policy_admin
from app.editorial.policy import POLICY_PATH_ENV
from app.utils.logger import get_logger

PROJECT_ROOT = Path(__file__).resolve().parents[2]
RUN_DAILY_PATH = PROJECT_ROOT / "scripts" / "run_daily.py"

logger = get_logger(step="admin.run_runner")

# Run-option keys ``_build_argv`` knows how to forward to the CLI. Anything
# outside this set is currently a UI-only knob; we still accept it (so the FE
# can store it for previews / future phases) but log a warning so the gap is
# visible in operator logs instead of silently dropped.
_SUPPORTED_OPTION_KEYS: frozenset[str] = frozenset(
    {
        "date",
        "run_date",  # FE legacy alias for date
        "mode",
        "from_step",
        "to_step",
        "dry_run",
        # Runtime knobs consumed by ``_supervise`` (not forwarded as CLI flags
        # but explicitly handled — kept here so they don't trigger warnings).
        "max_runtime_sec",
        # Output-side knob — flows through ``--output-theme``.
        "output_theme",
        # Editorial policy knobs — folded into a single
        # ``--policy-override-json`` payload for the subprocess.
        "target_sections",
        "min_section_score",
        "quotas",
        "section_quotas",
        "image_required",
        "arxiv_max",
        "community_max",
        "cluster_bonus",
        # Collector-side knob — accepted but currently informational; the
        # collector phase doesn't yet honour per-run source filters. We carry
        # it through the policy override under ``__source_filter`` so a future
        # phase can pick it up without breaking the contract.
        "source_types",
    }
)

# Output theme values accepted by ``--output-theme``. Anything outside this
# set is dropped with a warning so a typo in the FE store doesn't quietly
# become the dark default.
_VALID_OUTPUT_THEMES: frozenset[str] = frozenset(
    {"light", "dark", "newsroom-white"}
)

# Per-line history retained per run (so a late SSE subscriber can replay)
_MAX_LINES_PER_RUN = 2000

# Hard wall-clock cap for a single run. A normal full run finishes in 1–3 min;
# anything over 5 min is almost always a hung external call (LLM proxy in
# CLOSE_WAIT, slow upstream RSS, etc.). Operator can override via the run
# options (`max_runtime_sec`) when intentionally launching a long backfill.
_DEFAULT_MAX_RUNTIME_SEC = 300
# How long to wait between SIGTERM and the escalation to SIGKILL.
_GRACE_PERIOD_SEC = 5


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


def _build_policy_override(options: dict[str, Any]) -> dict[str, Any]:
    """Project per-run options onto the editorial-policy schema.

    The keys on the FE side use shorthand (``arxiv_max``); the policy file
    uses fully qualified paths (``report_selection.max_arxiv_only_sections``).
    This helper performs the mapping so ``_build_argv`` can hand a single
    JSON blob to the child process via ``--policy-override-json``.

    Returns an empty dict when the operator did not touch any of the
    policy-shaped knobs — ``_build_argv`` then skips emitting the flag
    entirely so a vanilla "click run" still produces a flag-free argv.
    """
    override: dict[str, Any] = {}
    selection: dict[str, Any] = {}

    if "target_sections" in options and options["target_sections"] is not None:
        selection["target_sections"] = int(options["target_sections"])
    if "min_section_score" in options and options["min_section_score"] is not None:
        selection["min_section_score"] = int(options["min_section_score"])
    if "arxiv_max" in options and options["arxiv_max"] is not None:
        selection["max_arxiv_only_sections"] = int(options["arxiv_max"])
    if "community_max" in options and options["community_max"] is not None:
        selection["max_community_sections"] = int(options["community_max"])
    if "image_required" in options and options["image_required"] is not None:
        selection["backfill_require_image"] = bool(options["image_required"])

    if selection:
        override["report_selection"] = selection

    quotas = options.get("section_quotas") or options.get("quotas")
    if isinstance(quotas, dict) and quotas:
        # Coerce numeric values defensively — the FE may hand us strings from
        # an ``<input type=number>`` round-trip.
        override["section_quotas"] = {
            k: int(v) for k, v in quotas.items() if v is not None
        }

    if "cluster_bonus" in options and options["cluster_bonus"] is not None:
        override.setdefault("scoring_weights", {})[
            "cluster_size_boost_per_item"
        ] = int(options["cluster_bonus"])

    source_types = options.get("source_types")
    if isinstance(source_types, list) and source_types:
        override["__source_filter"] = list(source_types)

    return override


def _build_argv(options: dict[str, Any]) -> list[str]:
    """Translate UI options dict into ``run_daily.py`` CLI flags.

    The handful of execution flags map 1:1 to CLI options. Everything else
    that's still policy-shaped (target_sections, quotas, score thresholds,
    …) is folded into a single ``--policy-override-json`` blob the
    subprocess deep-merges on top of the resolved YAML policy. Output theme
    rides on its own ``--output-theme`` flag because it doesn't live in the
    policy schema.

    Keys outside ``_SUPPORTED_OPTION_KEYS`` are logged via
    ``logger.warning("ignored_run_option")`` so the operator can see what
    isn't wired through yet (publish-side knobs like ``deploy_target``,
    ``slack_notify``, ``publish_at``, ``format`` are all in this bucket).
    """
    argv: list[str] = [sys.executable, str(RUN_DAILY_PATH)]
    date_value = options.get("date") or options.get("run_date")
    if date_value:
        argv += ["--date", str(date_value)]
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

    output_theme = options.get("output_theme")
    if output_theme:
        if str(output_theme) in _VALID_OUTPUT_THEMES:
            argv += ["--output-theme", str(output_theme)]
        else:
            logger.warning(
                "invalid_output_theme",
                value=str(output_theme),
                allowed=sorted(_VALID_OUTPUT_THEMES),
            )

    policy_override = _build_policy_override(options)
    if policy_override:
        argv += [
            "--policy-override-json",
            json.dumps(policy_override, ensure_ascii=False, sort_keys=True),
        ]

    for key in options:
        if key not in _SUPPORTED_OPTION_KEYS:
            logger.warning("ignored_run_option", key=key)
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


async def _terminate(proc: asyncio.subprocess.Process) -> None:
    """Send SIGTERM, give the child a grace period, then SIGKILL if needed."""
    if proc.returncode is not None:
        return
    try:
        proc.terminate()
    except ProcessLookupError:
        return
    try:
        await asyncio.wait_for(proc.wait(), timeout=_GRACE_PERIOD_SEC)
        return
    except asyncio.TimeoutError:
        pass
    try:
        proc.kill()
    except ProcessLookupError:
        return
    try:
        await asyncio.wait_for(proc.wait(), timeout=_GRACE_PERIOD_SEC)
    except asyncio.TimeoutError:
        pass


def _materialize_policy_override() -> Path | None:
    """If a runtime policy override exists, dump it to a tempfile and return path.

    Returns ``None`` when no override is active so callers can skip the env-var
    plumbing entirely. The caller is responsible for unlinking the file once
    the subprocess has exited.
    """
    override = policy_admin.get_runtime_override()
    if not override:
        return None
    fd, tmp_name = tempfile.mkstemp(suffix=".yaml", prefix="news-studio-policy-")
    os.close(fd)
    try:
        policy_admin.materialize_to(tmp_name)
    except Exception:
        # Failed to dump — clean up the empty placeholder before re-raising.
        try:
            os.unlink(tmp_name)
        except FileNotFoundError:
            pass
        raise
    return Path(tmp_name)


async def _supervise(state: RunState) -> None:
    state.status = "running"
    state.started_at = datetime.now(timezone.utc).isoformat()
    argv = _build_argv(state.options)
    env = os.environ.copy()
    env.setdefault("PYTHONPATH", str(PROJECT_ROOT))

    # If the operator tweaked the policy via the UI (PUT /api/policy), the
    # override lives only in this process's memory — the subprocess wouldn't
    # see it. Materialize it to a tempfile and pass the path through env so
    # ``app.editorial.policy.load_policy`` picks it up inside the child.
    policy_tmp_path: Path | None = None
    try:
        policy_tmp_path = _materialize_policy_override()
    except Exception as exc:
        # Policy override is an explicit operator intent (PUT /api/policy).
        # Silent fallback to the default would silently regress that intent,
        # so we fail the run loud and skip the subprocess entirely.
        logger.error("policy_override_materialize_failed", error=str(exc))
        state.status = "failed"
        state.error = f"policy_override_materialize_failed: {exc}"
        state.completed_at = datetime.now(timezone.utc).isoformat()
        await state.queue.put(
            {
                "stream": "control",
                "event": "done",
                "status": "failed",
                "return_code": None,
                "error": state.error,
                "ts": state.completed_at,
            }
        )
        return
    if policy_tmp_path is not None:
        env[POLICY_PATH_ENV] = str(policy_tmp_path)
        logger.info(
            "policy_override_passed_to_subprocess",
            path=str(policy_tmp_path),
        )

    max_runtime = float(state.options.get("max_runtime_sec") or _DEFAULT_MAX_RUNTIME_SEC)
    try:
        proc = await asyncio.create_subprocess_exec(
            *argv,
            cwd=str(PROJECT_ROOT),
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
            env=env,
        )
        state.process = proc
        try:
            await asyncio.wait_for(
                asyncio.gather(
                    _drain_stream(state, proc.stdout, "stdout"),
                    _drain_stream(state, proc.stderr, "stderr"),
                ),
                timeout=max_runtime,
            )
            state.return_code = await proc.wait()
            state.status = "completed" if state.return_code == 0 else "failed"
        except asyncio.TimeoutError:
            await _terminate(proc)
            state.return_code = proc.returncode
            state.status = "failed"
            state.error = f"max_runtime_exceeded: {max_runtime}s"
    except FileNotFoundError as exc:
        state.error = f"runner_not_found: {exc}"
        state.status = "failed"
    except Exception as exc:  # pragma: no cover — defensive
        state.error = repr(exc)
        state.status = "failed"
    finally:
        # Best-effort cleanup of the temp policy file. We only emit a debug
        # log on failure — losing a tempfile in /tmp is harmless.
        if policy_tmp_path is not None:
            try:
                policy_tmp_path.unlink()
            except FileNotFoundError:
                pass
            except Exception as exc:  # pragma: no cover
                logger.warning(
                    "policy_override_tmp_cleanup_failed",
                    path=str(policy_tmp_path),
                    error=str(exc),
                )
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
