"""Runtime policy admin helpers.

Loads the editorial policy from YAML and applies an in-memory override patch
that survives only for the lifetime of the FastAPI process. This keeps the
``data/editorial_policy.yaml`` file untouched while still letting operators
preview alternative settings via the News Studio UI.
"""
from __future__ import annotations

import os
import shutil
import tempfile
from copy import deepcopy
from pathlib import Path
from threading import RLock
from typing import Any

import yaml

from app.editorial.policy import DEFAULT_POLICY_PATH, _deep_merge, load_policy

# Module-level runtime override (volatile — cleared on process restart)
_OVERRIDE_LOCK = RLock()
_RUNTIME_OVERRIDE: dict[str, Any] = {}


def get_runtime_override() -> dict[str, Any]:
    """Return a deep copy of the current runtime override patch."""
    with _OVERRIDE_LOCK:
        return deepcopy(_RUNTIME_OVERRIDE)


def set_policy_override(patch: dict[str, Any] | None) -> dict[str, Any]:
    """Replace the runtime override with ``patch`` (deep-merged, volatile).

    Passing ``None`` or ``{}`` clears the override. Returns the new merged
    policy (yaml + override) so callers can show the operator the result.
    """
    global _RUNTIME_OVERRIDE
    with _OVERRIDE_LOCK:
        if not patch:
            _RUNTIME_OVERRIDE = {}
        else:
            if not isinstance(patch, dict):
                raise ValueError("policy override must be a mapping")
            _RUNTIME_OVERRIDE = deepcopy(patch)
    return get_policy()


def clear_policy_override() -> None:
    """Drop any in-memory override (used by tests)."""
    global _RUNTIME_OVERRIDE
    with _OVERRIDE_LOCK:
        _RUNTIME_OVERRIDE = {}


def get_policy() -> dict[str, Any]:
    """Return ``editorial_policy.yaml`` merged with the runtime override.

    The yaml file itself is never written; the override is purely in-memory.
    """
    base = load_policy()
    override = get_runtime_override()
    if not override:
        return base
    return _deep_merge(base, override)


def merge_with_options(options: dict[str, Any] | None) -> dict[str, Any]:
    """Merge the current policy with a per-request ``options`` patch.

    Used by the preview endpoint to render with one-off overrides without
    touching the runtime override. Unknown keys at the top level are kept so
    callers can pass additional rendering hints (e.g. ``target_sections``).
    """
    base = get_policy()
    if not options:
        return base
    if not isinstance(options, dict):
        raise ValueError("preview options must be a mapping")
    return _deep_merge(base, options)


def materialize_to(tmp_path: str | Path) -> Path:
    """Dump the current effective policy (yaml + runtime override) to a yaml file.

    Used by :mod:`app.admin.run_runner` to hand the runtime override to a
    subprocess via the ``EDITORIAL_POLICY_PATH`` env var. The resulting file is
    a complete, self-contained policy — :func:`app.editorial.policy.load_policy`
    will deep-merge it onto ``DEFAULT_POLICY`` exactly as it does for the
    repo-level yaml.

    Returns the resolved :class:`Path` so callers can pass it through env vars.
    """
    target = Path(tmp_path)
    target.parent.mkdir(parents=True, exist_ok=True)
    payload = get_policy()
    with target.open("w", encoding="utf-8") as f:
        yaml.safe_dump(payload, f, allow_unicode=True, sort_keys=False)
    return target


def persist_runtime_override_to_yaml(
    yaml_path: Path | str | None = None,
) -> dict[str, Path | None]:
    """Atomically write the current runtime override into the on-disk yaml.

    Steps:
      1. Refuse if there is no runtime override (``ValueError``) — the operator
         must explicitly tune something via :func:`set_policy_override` first.
      2. If the target yaml already exists, copy it to ``<yaml_path>.bak``
         (overwriting any stale backup).
      3. Load the existing yaml (or ``{}`` when missing), deep-merge the
         override on top, and dump the result to a tempfile in the target
         directory. ``os.replace`` then atomically swaps the tempfile in.

    Returns a mapping ``{"persisted_to": Path, "backup": Path | None}``. The
    backup key is ``None`` when the yaml didn't exist beforehand.
    """
    target = Path(yaml_path) if yaml_path is not None else Path(DEFAULT_POLICY_PATH)
    target = target.resolve() if target.exists() else target

    override = get_runtime_override()
    if not override:
        raise ValueError("no runtime override to persist")

    target.parent.mkdir(parents=True, exist_ok=True)

    backup_path: Path | None = None
    if target.exists():
        backup_path = target.with_suffix(target.suffix + ".bak")
        shutil.copy2(target, backup_path)
        with target.open("r", encoding="utf-8") as fh:
            existing = yaml.safe_load(fh) or {}
        if not isinstance(existing, dict):
            raise ValueError(f"existing policy yaml is not a mapping: {target}")
    else:
        existing = {}

    merged = _deep_merge(existing, override)

    # Atomic write: dump to a tempfile in the same directory, fsync, then
    # os.replace so a partial write can never corrupt the target.
    tmp_fd, tmp_name = tempfile.mkstemp(
        prefix=target.name + ".",
        suffix=".tmp",
        dir=str(target.parent),
    )
    tmp_path = Path(tmp_name)
    try:
        with os.fdopen(tmp_fd, "w", encoding="utf-8") as fh:
            yaml.safe_dump(merged, fh, allow_unicode=True, sort_keys=False)
            fh.flush()
            os.fsync(fh.fileno())
        os.replace(tmp_path, target)
    except Exception:
        # Best-effort cleanup; original file (if any) is untouched because we
        # never opened it for writing.
        try:
            tmp_path.unlink()
        except FileNotFoundError:
            pass
        raise

    return {"persisted_to": target, "backup": backup_path}
