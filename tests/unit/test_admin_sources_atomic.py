"""Atomic write semantics for ``sources_admin`` (Phase C / TC-1.4).

We can't easily simulate a real crash in unit tests, but we can:

  1. Verify a successful write left no leftover ``.tmp`` siblings (the
     ``NamedTemporaryFile`` was renamed, not orphaned).
  2. Force ``yaml.safe_dump`` to raise mid-write and assert the original
     yaml is untouched and no ``.tmp`` file leaked.

Together these establish the "always old-or-new, never half" invariant that
the rest of the system relies on.
"""
from __future__ import annotations

from pathlib import Path

import pytest
import yaml

from app.admin import sources_admin


@pytest.fixture
def registry(tmp_path: Path) -> Path:
    path = tmp_path / "sources_registry.yaml"
    path.write_text(
        yaml.safe_dump(
            {
                "sources": [
                    {
                        "name": "Existing",
                        "source_type": "rss",
                        "url": "https://example.com/feed",
                        "enabled": True,
                        "priority": 50,
                    }
                ]
            },
            allow_unicode=True,
            sort_keys=False,
        ),
        encoding="utf-8",
    )
    return path


def _list_tmp_siblings(path: Path) -> list[Path]:
    """Return any ``.<basename>.*.tmp`` files left next to ``path``."""
    return sorted(
        p
        for p in path.parent.iterdir()
        if p.name.startswith(f".{path.name}.") and p.suffix == ".tmp"
    )


def test_update_source_leaves_no_orphan_tmp(registry: Path) -> None:
    sources_admin.update_source(
        "Existing", {"enabled": False, "priority": 10}, path=registry
    )
    assert _list_tmp_siblings(registry) == []
    on_disk = yaml.safe_load(registry.read_text(encoding="utf-8"))
    assert on_disk["sources"][0]["enabled"] is False
    assert on_disk["sources"][0]["priority"] == 10


def test_add_source_leaves_no_orphan_tmp(registry: Path) -> None:
    sources_admin.add_source(
        {
            "name": "New One",
            "source_type": "rss",
            "url": "https://example.org/feed",
        },
        path=registry,
    )
    assert _list_tmp_siblings(registry) == []
    on_disk = yaml.safe_load(registry.read_text(encoding="utf-8"))
    names = [s["name"] for s in on_disk["sources"]]
    assert "New One" in names
    assert "Existing" in names


def test_update_source_keeps_old_yaml_when_dump_fails(
    registry: Path, monkeypatch
) -> None:
    """If ``yaml.safe_dump`` blows up the rename never happens — old file stays.

    We monkey-patch the symbol the helper imports (``sources_admin.yaml``) so
    the failure surfaces inside the tempfile-write block. The expected
    invariant: original yaml untouched + no leftover tempfile siblings.
    """
    original = registry.read_bytes()

    def _boom(*_args, **_kwargs):
        raise RuntimeError("simulated disk failure")

    monkeypatch.setattr(sources_admin.yaml, "safe_dump", _boom)

    with pytest.raises(RuntimeError, match="simulated disk failure"):
        sources_admin.update_source("Existing", {"enabled": False}, path=registry)

    assert registry.read_bytes() == original
    assert _list_tmp_siblings(registry) == []


def test_add_source_keeps_old_yaml_when_dump_fails(
    registry: Path, monkeypatch
) -> None:
    original = registry.read_bytes()

    def _boom(*_args, **_kwargs):
        raise RuntimeError("simulated disk failure")

    monkeypatch.setattr(sources_admin.yaml, "safe_dump", _boom)

    with pytest.raises(RuntimeError, match="simulated disk failure"):
        sources_admin.add_source(
            {
                "name": "WontPersist",
                "source_type": "rss",
                "url": "https://example.org/x",
            },
            path=registry,
        )

    assert registry.read_bytes() == original
    assert _list_tmp_siblings(registry) == []
