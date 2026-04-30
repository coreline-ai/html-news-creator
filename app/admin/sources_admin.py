"""Sources registry admin helpers.

Reads/writes ``data/sources_registry.yaml`` to toggle ``enabled`` flags or
adjust ``priority`` for a single source. The registry is a small YAML file
operated by hand normally; the admin UI mutates it through these helpers so
``scripts/run_daily.py`` picks up changes on the next run.

All write operations are atomic: we serialize to a tempfile in the same
directory and ``os.replace`` it onto the target. This avoids leaving the
registry truncated if the API process is killed mid-flush — the file is
either the old version or the new version, never a half-written one.
"""
from __future__ import annotations

import os
import re
import tempfile
from copy import deepcopy
from pathlib import Path
from threading import RLock
from typing import Any

import yaml

DEFAULT_REGISTRY_PATH = (
    Path(__file__).resolve().parents[2] / "data" / "sources_registry.yaml"
)

_FILE_LOCK = RLock()
# Whitelist of fields the admin UI is allowed to modify via PUT
ALLOWED_UPDATE_FIELDS: tuple[str, ...] = (
    "enabled",
    "priority",
    "max_items",
    "trust_level",
    "source_tier",
    "category",
)

# Whitelist + types for new entries (POST). ``name`` and ``source_type`` are
# required; everything else is optional and copied through verbatim.
SOURCE_TYPES: tuple[str, ...] = ("rss", "github", "arxiv", "website")
SOURCE_TIERS: tuple[str, ...] = (
    "official",
    "mainstream",
    "research",
    "developer_signal",
    "community",
)
# Allowed fields when adding a new source. Mirrors the existing yaml schema.
ALLOWED_CREATE_FIELDS: tuple[str, ...] = (
    "name",
    "source_type",
    "url",
    "homepage_url",
    "trust_level",
    "source_tier",
    "category",
    "priority",
    "max_items",
    "enabled",
    "org",
    "query",
    "listing_url",
    "sitemap_url",
    "include_url_patterns",
    "max_candidates",
    "collector_type",
    "content_category",
)

# A source ``name`` is the registry primary key — keep it conservative so it
# survives URL paths (PUT /api/sources/{name}) and yaml/json round-trips.
_NAME_PATTERN = re.compile(r"^[A-Za-z][A-Za-z0-9 _.\-]+$")


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
    """Atomic write: tempfile in the same dir + ``os.replace``.

    Same-filesystem replace is atomic on POSIX, so a crashed write never
    leaves a truncated registry on disk. The tempfile is created with
    ``delete=False`` so we can rename it; on any error we clean it up.
    """
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = tempfile.NamedTemporaryFile(
        mode="w",
        encoding="utf-8",
        dir=str(path.parent),
        prefix=f".{path.name}.",
        suffix=".tmp",
        delete=False,
    )
    tmp_path = Path(tmp.name)
    try:
        with tmp:
            yaml.safe_dump(data, tmp, allow_unicode=True, sort_keys=False)
            tmp.flush()
            os.fsync(tmp.fileno())
        os.replace(str(tmp_path), str(path))
    except Exception:
        # Best-effort cleanup of the orphaned tempfile.
        try:
            tmp_path.unlink()
        except FileNotFoundError:
            pass
        raise


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
    ``KeyError`` if the source name is not found. Write is atomic.
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


def add_source(
    fields: dict[str, Any],
    path: str | Path | None = None,
) -> dict[str, Any]:
    """Append a new source to the registry and persist atomically.

    Required fields:
      - ``name`` (matches :data:`_NAME_PATTERN`, unique in the registry)
      - ``source_type`` (one of :data:`SOURCE_TYPES`)

    Optional fields are filtered through :data:`ALLOWED_CREATE_FIELDS` so the
    UI cannot inject arbitrary YAML structure. Defaults applied:
      - ``enabled`` = True
      - ``priority`` = 50
      - ``max_items`` = 20

    Raises:
      ValueError — missing/invalid required field, duplicate name, unknown key.
    """
    if not isinstance(fields, dict) or not fields:
        raise ValueError("source fields must be a non-empty mapping")

    unknown = [k for k in fields if k not in ALLOWED_CREATE_FIELDS]
    if unknown:
        raise ValueError(
            f"unsupported source fields: {unknown!r} "
            f"(allowed: {ALLOWED_CREATE_FIELDS})"
        )

    name = fields.get("name")
    if not isinstance(name, str) or not name.strip():
        raise ValueError("'name' is required and must be a non-empty string")
    name = name.strip()
    if not _NAME_PATTERN.match(name):
        raise ValueError(
            "'name' must start with a letter and contain only letters, "
            "digits, spaces, underscores, dots, or hyphens"
        )

    source_type = fields.get("source_type")
    if not isinstance(source_type, str) or source_type not in SOURCE_TYPES:
        raise ValueError(
            f"'source_type' must be one of {SOURCE_TYPES} (got {source_type!r})"
        )

    if "source_tier" in fields and fields["source_tier"] is not None:
        if fields["source_tier"] not in SOURCE_TIERS:
            raise ValueError(
                f"'source_tier' must be one of {SOURCE_TIERS} "
                f"(got {fields['source_tier']!r})"
            )

    if "priority" in fields and fields["priority"] is not None:
        if not isinstance(fields["priority"], int) or isinstance(
            fields["priority"], bool
        ):
            raise ValueError("'priority' must be an integer")

    registry_path = Path(path) if path else DEFAULT_REGISTRY_PATH
    with _FILE_LOCK:
        registry = _load_registry(registry_path)
        for source in registry.get("sources", []):
            if isinstance(source, dict) and source.get("name") == name:
                raise ValueError(f"source already exists: {name!r}")

        new_entry: dict[str, Any] = {"name": name, "source_type": source_type}
        # Carry every other allowed field through verbatim, in declaration
        # order so the yaml stays readable.
        for key in ALLOWED_CREATE_FIELDS:
            if key in ("name", "source_type"):
                continue
            if key in fields and fields[key] is not None:
                new_entry[key] = fields[key]
        new_entry.setdefault("enabled", True)
        new_entry.setdefault("priority", 50)
        new_entry.setdefault("max_items", 20)

        registry.setdefault("sources", []).append(new_entry)
        _save_registry(registry_path, registry)

    return deepcopy(new_entry)
