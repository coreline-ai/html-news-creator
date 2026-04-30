"""Sources registry admin helpers.

Reads/writes ``data/sources_registry.yaml`` to toggle ``enabled`` flags or
adjust ``priority`` for a single source. The registry is a small YAML file
operated by hand normally; the admin UI mutates it through these helpers so
``scripts/run_daily.py`` picks up changes on the next run.
"""
from __future__ import annotations

from copy import deepcopy
from pathlib import Path
from threading import RLock
from typing import Any

import yaml

DEFAULT_REGISTRY_PATH = (
    Path(__file__).resolve().parents[2] / "data" / "sources_registry.yaml"
)

_FILE_LOCK = RLock()
# Whitelist of fields the admin UI is allowed to modify
ALLOWED_UPDATE_FIELDS: tuple[str, ...] = (
    "enabled",
    "priority",
    "max_items",
    "trust_level",
    "source_tier",
    "category",
)


def _load_registry(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {"sources": []}
    with path.open("r", encoding="utf-8") as f:
        data = yaml.safe_load(f) or {}
    if not isinstance(data, dict):
        raise ValueError(f"sources registry must be a YAML mapping: {path}")
    data.setdefault("sources", [])
    if not isinstance(data["sources"], list):
        raise ValueError("sources registry 'sources' must be a list")
    return data


def _save_registry(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        yaml.safe_dump(data, f, allow_unicode=True, sort_keys=False)


def list_sources(path: str | Path | None = None) -> list[dict[str, Any]]:
    """Return all registered sources as plain dicts.

    A source's ``enabled`` flag defaults to ``True`` if missing — matching the
    DB schema (`Source.enabled` default).
    """
    registry_path = Path(path) if path else DEFAULT_REGISTRY_PATH
    with _FILE_LOCK:
        registry = _load_registry(registry_path)
    sources = []
    for raw in registry.get("sources", []):
        if not isinstance(raw, dict):
            continue
        item = deepcopy(raw)
        item.setdefault("enabled", True)
        sources.append(item)
    return sources


def update_source(
    name: str,
    fields: dict[str, Any],
    path: str | Path | None = None,
) -> dict[str, Any]:
    """Patch a single source by ``name`` and persist to YAML.

    Only fields in :data:`ALLOWED_UPDATE_FIELDS` are honored — unknown keys are
    rejected with ``ValueError`` to avoid silently accepting typos. Raises
    ``KeyError`` if the source name is not found.
    """
    if not isinstance(fields, dict) or not fields:
        raise ValueError("update fields must be a non-empty mapping")

    unknown = [k for k in fields if k not in ALLOWED_UPDATE_FIELDS]
    if unknown:
        raise ValueError(
            f"unsupported source fields: {unknown!r} (allowed: {ALLOWED_UPDATE_FIELDS})"
        )

    registry_path = Path(path) if path else DEFAULT_REGISTRY_PATH
    with _FILE_LOCK:
        registry = _load_registry(registry_path)
        target: dict[str, Any] | None = None
        for source in registry.get("sources", []):
            if isinstance(source, dict) and source.get("name") == name:
                target = source
                break
        if target is None:
            raise KeyError(f"source not found: {name!r}")

        for key, value in fields.items():
            target[key] = value

        _save_registry(registry_path, registry)

    updated = deepcopy(target)
    updated.setdefault("enabled", True)
    return updated
