"""Runtime policy admin helpers.

Loads the editorial policy from YAML and applies an in-memory override patch
that survives only for the lifetime of the FastAPI process. This keeps the
``data/editorial_policy.yaml`` file untouched while still letting operators
preview alternative settings via the News Studio UI.
"""
from __future__ import annotations

from copy import deepcopy
from threading import RLock
from typing import Any

from app.editorial.policy import _deep_merge, load_policy

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
