"""Unit tests for ``policy_admin.persist_runtime_override_to_yaml``.

Phase E — Policy persistence helper. These exercise the write path directly,
without the FastAPI layer, so we can verify atomicity and backup semantics in
isolation.
"""
from __future__ import annotations

import os
from pathlib import Path
from unittest.mock import patch

import pytest
import yaml

from app.admin import policy_admin


@pytest.fixture(autouse=True)
def _clear_override_between_tests():
    policy_admin.clear_policy_override()
    yield
    policy_admin.clear_policy_override()


def test_persist_raises_when_override_empty(tmp_path: Path) -> None:
    """No runtime override = nothing to persist."""
    target = tmp_path / "editorial_policy.yaml"
    with pytest.raises(ValueError, match="no runtime override to persist"):
        policy_admin.persist_runtime_override_to_yaml(target)
    # Side-effect free.
    assert not target.exists()
    assert not (tmp_path / "editorial_policy.yaml.bak").exists()


def test_persist_creates_yaml_when_missing(tmp_path: Path) -> None:
    """First-time persist: no prior yaml ⇒ no backup, fresh file written."""
    target = tmp_path / "editorial_policy.yaml"
    policy_admin.set_policy_override(
        {"section_quotas": {"product": 7}, "report_selection": {"target_sections": 5}}
    )

    result = policy_admin.persist_runtime_override_to_yaml(target)

    assert result["persisted_to"] == target
    assert result["backup"] is None
    assert target.exists()

    loaded = yaml.safe_load(target.read_text(encoding="utf-8"))
    assert loaded["section_quotas"]["product"] == 7
    assert loaded["report_selection"]["target_sections"] == 5
    # No backup created when the original didn't exist.
    assert not target.with_suffix(target.suffix + ".bak").exists()


def test_persist_merges_into_existing_yaml_and_creates_backup(tmp_path: Path) -> None:
    """Existing yaml is deep-merged, .bak preserves the prior contents verbatim."""
    target = tmp_path / "editorial_policy.yaml"
    original = {
        "section_quotas": {"product": 4, "tooling": 4, "research": 1},
        "report_selection": {"target_sections": 10, "max_sections": 10},
    }
    target.write_text(yaml.safe_dump(original), encoding="utf-8")
    original_text = target.read_text(encoding="utf-8")

    policy_admin.set_policy_override(
        {"section_quotas": {"product": 9}, "report_selection": {"target_sections": 6}}
    )

    result = policy_admin.persist_runtime_override_to_yaml(target)

    backup = target.with_suffix(target.suffix + ".bak")
    assert result["persisted_to"] == target
    assert result["backup"] == backup
    assert backup.exists()
    # Backup is byte-for-byte the previous file.
    assert backup.read_text(encoding="utf-8") == original_text

    merged = yaml.safe_load(target.read_text(encoding="utf-8"))
    # Override applied.
    assert merged["section_quotas"]["product"] == 9
    assert merged["report_selection"]["target_sections"] == 6
    # Untouched keys survived the deep merge.
    assert merged["section_quotas"]["tooling"] == 4
    assert merged["section_quotas"]["research"] == 1
    assert merged["report_selection"]["max_sections"] == 10


def test_persist_failure_leaves_original_untouched(tmp_path: Path) -> None:
    """If the dump step blows up, the target yaml must be intact (atomicity)."""
    target = tmp_path / "editorial_policy.yaml"
    original = {"section_quotas": {"product": 4}}
    target.write_text(yaml.safe_dump(original), encoding="utf-8")
    original_bytes = target.read_bytes()

    policy_admin.set_policy_override({"section_quotas": {"product": 9}})

    boom = RuntimeError("simulated dump failure")
    with patch("app.admin.policy_admin.yaml.safe_dump", side_effect=boom):
        with pytest.raises(RuntimeError, match="simulated dump failure"):
            policy_admin.persist_runtime_override_to_yaml(target)

    # Original intact byte-for-byte.
    assert target.read_bytes() == original_bytes
    # No leftover tempfile in the directory.
    leftovers = [
        p for p in target.parent.iterdir()
        if p.name.startswith(target.name + ".") and p.name.endswith(".tmp")
    ]
    assert leftovers == []


def test_persist_uses_os_replace_for_atomic_swap(tmp_path: Path) -> None:
    """Writing must go through os.replace (atomic rename), not a plain open()."""
    target = tmp_path / "editorial_policy.yaml"
    target.write_text(yaml.safe_dump({"section_quotas": {"product": 4}}), encoding="utf-8")

    policy_admin.set_policy_override({"section_quotas": {"product": 9}})

    real_replace = os.replace
    calls: list[tuple[str, str]] = []

    def _spy(src, dst):
        calls.append((str(src), str(dst)))
        return real_replace(src, dst)

    with patch("app.admin.policy_admin.os.replace", side_effect=_spy):
        result = policy_admin.persist_runtime_override_to_yaml(target)

    assert result["persisted_to"] == target
    # Exactly one replace call, and the destination is our target.
    assert len(calls) == 1
    src, dst = calls[0]
    assert dst == str(target)
    # The src is a tempfile in the same directory (so rename is atomic on POSIX).
    assert Path(src).parent == target.parent
