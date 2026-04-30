"""Runtime policy override → subprocess env propagation (Phase C).

Covers three layers of the dispatch chain:

1. ``policy_admin.materialize_to`` writes a complete yaml file.
2. ``run_runner._materialize_policy_override`` returns ``None`` when no
   override is active and a real path when one is.
3. ``run_runner._supervise`` injects ``EDITORIAL_POLICY_PATH`` into the
   subprocess env when an override was materialized, and cleans the
   tempfile up afterwards.
4. ``app.editorial.policy.load_policy`` honors the env var.
"""
from __future__ import annotations

import asyncio
from pathlib import Path
from unittest.mock import MagicMock

import pytest
import yaml

from app.admin import policy_admin, run_runner
from app.admin.run_runner import RunState, _materialize_policy_override, _supervise
from app.editorial.policy import POLICY_PATH_ENV, load_policy


@pytest.fixture(autouse=True)
def _clear_override():
    policy_admin.clear_policy_override()
    yield
    policy_admin.clear_policy_override()


def test_materialize_to_writes_full_policy(tmp_path: Path) -> None:
    policy_admin.set_policy_override(
        {"report_selection": {"target_sections": 5}}
    )
    target = tmp_path / "p.yaml"
    policy_admin.materialize_to(target)

    on_disk = yaml.safe_load(target.read_text(encoding="utf-8"))
    assert on_disk["report_selection"]["target_sections"] == 5
    # Defaults from DEFAULT_POLICY survive the round-trip — the file is
    # complete, not just the override patch.
    assert "source_tiers" in on_disk
    assert "scoring_weights" in on_disk


def test_materialize_policy_override_returns_none_when_empty():
    assert _materialize_policy_override() is None


def test_materialize_policy_override_returns_path_and_cleans_up():
    policy_admin.set_policy_override({"section_quotas": {"product": 9}})
    path = _materialize_policy_override()
    assert path is not None
    assert path.exists()
    on_disk = yaml.safe_load(path.read_text(encoding="utf-8"))
    assert on_disk["section_quotas"]["product"] == 9
    # Best-effort cleanup so the tmpdir doesn't accumulate during tests.
    path.unlink()


def test_load_policy_uses_env_var(tmp_path: Path, monkeypatch):
    """``load_policy()`` reads ``$EDITORIAL_POLICY_PATH`` ahead of the default."""
    target = tmp_path / "p.yaml"
    target.write_text(
        yaml.safe_dump(
            {"report_selection": {"target_sections": 3, "max_sections": 4}},
            allow_unicode=True,
        ),
        encoding="utf-8",
    )
    monkeypatch.setenv(POLICY_PATH_ENV, str(target))
    loaded = load_policy()
    assert loaded["report_selection"]["target_sections"] == 3
    assert loaded["report_selection"]["max_sections"] == 4


def test_load_policy_explicit_path_wins_over_env(tmp_path: Path, monkeypatch):
    explicit = tmp_path / "explicit.yaml"
    explicit.write_text(
        yaml.safe_dump({"report_selection": {"target_sections": 8}}),
        encoding="utf-8",
    )
    env_target = tmp_path / "env.yaml"
    env_target.write_text(
        yaml.safe_dump({"report_selection": {"target_sections": 99}}),
        encoding="utf-8",
    )
    monkeypatch.setenv(POLICY_PATH_ENV, str(env_target))
    assert load_policy(explicit)["report_selection"]["target_sections"] == 8


def test_load_policy_falls_back_to_default_when_env_unset(monkeypatch):
    monkeypatch.delenv(POLICY_PATH_ENV, raising=False)
    # We don't assert on a specific value (data/editorial_policy.yaml may
    # or may not exist in CI) — we just check the call resolves without
    # consulting the env var.
    loaded = load_policy()
    assert isinstance(loaded, dict)
    assert "report_selection" in loaded


def test_supervise_passes_policy_path_to_subprocess(monkeypatch):
    """When an override is set, ``_supervise`` puts the path into env."""
    policy_admin.set_policy_override(
        {"report_selection": {"target_sections": 4}}
    )

    captured: dict = {}

    async def fake_create_subprocess_exec(*args, **kwargs):
        captured["env"] = kwargs.get("env", {})
        proc = MagicMock()

        async def _wait():
            return 0

        async def _readline():
            return b""

        proc.stdout = MagicMock()
        proc.stdout.readline = _readline
        proc.stderr = MagicMock()
        proc.stderr.readline = _readline
        proc.wait = _wait
        proc.returncode = 0
        return proc

    monkeypatch.setattr(
        run_runner.asyncio, "create_subprocess_exec", fake_create_subprocess_exec
    )

    async def _drive():
        state = RunState(run_id="t1", options={"dry_run": True})
        await _supervise(state)
        return state

    state = asyncio.run(_drive())

    assert state.status == "completed"
    env = captured.get("env") or {}
    policy_path = env.get(POLICY_PATH_ENV)
    assert policy_path, f"expected {POLICY_PATH_ENV} in subprocess env, got {env!r}"

    # ``_supervise`` cleans the tempfile up after the subprocess finishes —
    # operator inspection should never leave stragglers in /tmp.
    assert not Path(policy_path).exists()


def test_supervise_does_not_set_env_when_no_override(monkeypatch):
    policy_admin.clear_policy_override()
    captured: dict = {}

    async def fake_create_subprocess_exec(*args, **kwargs):
        captured["env"] = kwargs.get("env", {})
        proc = MagicMock()

        async def _wait():
            return 0

        async def _readline():
            return b""

        proc.stdout = MagicMock()
        proc.stdout.readline = _readline
        proc.stderr = MagicMock()
        proc.stderr.readline = _readline
        proc.wait = _wait
        proc.returncode = 0
        return proc

    monkeypatch.setattr(
        run_runner.asyncio, "create_subprocess_exec", fake_create_subprocess_exec
    )
    # Make sure the surrounding shell env doesn't leak through and produce a
    # false negative — we assert specifically that ``_supervise`` did NOT
    # add the key.
    monkeypatch.delenv(POLICY_PATH_ENV, raising=False)

    async def _drive():
        # ``RunState`` constructs an ``asyncio.Queue`` in its default factory,
        # which requires a running loop on Python 3.9 — build it inside the
        # coroutine that runs under ``asyncio.run``.
        state = RunState(run_id="t2", options={"dry_run": True})
        await _supervise(state)
        return state

    state = asyncio.run(_drive())
    assert state.status == "completed"

    env = captured.get("env") or {}
    assert POLICY_PATH_ENV not in env
