"""Per-run options reach the pipeline (Phase F, bundle X).

Covers three layers of the contract that External Validation flagged as
broken:

1. ``run_runner._build_argv`` translates editorial knobs (target_sections,
   quotas, …) into a single ``--policy-override-json`` blob and the output
   theme into ``--output-theme``.
2. ``app.editorial.policy.load_policy`` honours the
   ``EDITORIAL_POLICY_OVERRIDE_JSON`` env var the run-script exports, deep-
   merging it on top of the YAML policy.
3. Bad JSON in the env var is logged and ignored — the run still produces a
   valid policy dict.
"""
from __future__ import annotations

import json

import pytest

from app.admin.run_runner import _build_argv
from app.editorial.policy import (
    POLICY_OVERRIDE_JSON_ENV,
    POLICY_PATH_ENV,
    load_policy,
)


# ---------------------------------------------------------------------------
# _build_argv — editorial / policy knobs
# ---------------------------------------------------------------------------

def _override_payload(argv: list[str]) -> dict:
    """Pull the JSON blob out of an argv list for assertions."""
    assert "--policy-override-json" in argv, argv
    idx = argv.index("--policy-override-json")
    return json.loads(argv[idx + 1])


def test_build_argv_target_sections_emits_policy_override():
    argv = _build_argv({"target_sections": 5})
    payload = _override_payload(argv)
    assert payload == {"report_selection": {"target_sections": 5}}


def test_build_argv_quotas_use_section_quotas_key():
    argv = _build_argv({"quotas": {"product": 3, "research": 2}})
    payload = _override_payload(argv)
    # ``quotas`` (FE shorthand) maps to ``section_quotas`` (policy schema).
    assert payload == {"section_quotas": {"product": 3, "research": 2}}


def test_build_argv_arxiv_and_community_caps_map_to_selection_keys():
    argv = _build_argv({"arxiv_max": 2, "community_max": 3})
    payload = _override_payload(argv)
    assert payload == {
        "report_selection": {
            "max_arxiv_only_sections": 2,
            "max_community_sections": 3,
        }
    }


def test_build_argv_image_required_maps_to_backfill_require_image():
    argv = _build_argv({"image_required": True})
    payload = _override_payload(argv)
    assert payload == {
        "report_selection": {"backfill_require_image": True}
    }


def test_build_argv_image_not_required_maps_to_generated_fallback_path():
    argv = _build_argv({"image_required": False})
    payload = _override_payload(argv)
    assert payload == {
        "report_selection": {"backfill_require_image": False}
    }


def test_build_argv_combines_multiple_keys_into_single_blob():
    argv = _build_argv(
        {
            "target_sections": 8,
            "min_section_score": 50,
            "quotas": {"product": 4},
            "cluster_bonus": 7,
        }
    )
    payload = _override_payload(argv)
    assert payload["report_selection"]["target_sections"] == 8
    assert payload["report_selection"]["min_section_score"] == 50
    assert payload["section_quotas"] == {"product": 4}
    assert payload["scoring_weights"]["cluster_size_boost_per_item"] == 7


def test_build_argv_no_policy_keys_skips_override_flag():
    """A vanilla run with only execution flags should not emit the JSON."""
    argv = _build_argv({"date": "2026-04-30", "mode": "full"})
    assert "--policy-override-json" not in argv


# ---------------------------------------------------------------------------
# _build_argv — output theme
# ---------------------------------------------------------------------------

def test_build_argv_output_theme_newsroom_white():
    argv = _build_argv({"output_theme": "newsroom-white"})
    assert "--output-theme" in argv
    idx = argv.index("--output-theme")
    assert argv[idx + 1] == "newsroom-white"


def test_build_argv_output_theme_dark():
    argv = _build_argv({"output_theme": "dark"})
    idx = argv.index("--output-theme")
    assert argv[idx + 1] == "dark"


def test_build_argv_invalid_output_theme_dropped():
    """Operator typo should not silently become a different theme."""
    argv = _build_argv({"output_theme": "rainbow"})
    assert "--output-theme" not in argv


def test_build_argv_source_types_carried_via_source_filter():
    argv = _build_argv({"source_types": ["rss", "github"]})
    payload = _override_payload(argv)
    assert payload == {"__source_filter": ["rss", "github"]}


# ---------------------------------------------------------------------------
# load_policy — JSON override env var
# ---------------------------------------------------------------------------

def test_load_policy_applies_override_json(monkeypatch):
    monkeypatch.delenv(POLICY_PATH_ENV, raising=False)
    monkeypatch.setenv(
        POLICY_OVERRIDE_JSON_ENV,
        '{"report_selection":{"target_sections":3}}',
    )
    policy = load_policy()
    assert policy["report_selection"]["target_sections"] == 3
    # Other keys from DEFAULT_POLICY should still be present.
    assert "section_quotas" in policy


def test_load_policy_override_deep_merges_with_yaml(tmp_path, monkeypatch):
    yaml_file = tmp_path / "p.yaml"
    yaml_file.write_text(
        "report_selection:\n  target_sections: 9\n  min_section_score: 40\n",
        encoding="utf-8",
    )
    monkeypatch.setenv(POLICY_PATH_ENV, str(yaml_file))
    monkeypatch.setenv(
        POLICY_OVERRIDE_JSON_ENV,
        '{"report_selection":{"target_sections":3}}',
    )
    policy = load_policy()
    # Override wins on the touched key,
    assert policy["report_selection"]["target_sections"] == 3
    # …but the YAML's other keys survive the deep-merge.
    assert policy["report_selection"]["min_section_score"] == 40


def test_load_policy_invalid_override_json_logged_and_ignored(
    monkeypatch, caplog
):
    monkeypatch.delenv(POLICY_PATH_ENV, raising=False)
    monkeypatch.setenv(POLICY_OVERRIDE_JSON_ENV, "not-json{")
    # Must not raise — bad JSON is a warning, not a fatal.
    policy = load_policy()
    assert isinstance(policy, dict)
    assert "report_selection" in policy


def test_load_policy_override_must_be_object(monkeypatch):
    """A JSON list / scalar at the top level is rejected, not deep-merged."""
    monkeypatch.delenv(POLICY_PATH_ENV, raising=False)
    monkeypatch.setenv(POLICY_OVERRIDE_JSON_ENV, "[1,2,3]")
    policy = load_policy()
    # Override skipped entirely → defaults survive untouched.
    assert isinstance(policy.get("report_selection"), dict)


@pytest.fixture(autouse=True)
def _scrub_override_env(monkeypatch):
    """Each test starts with a clean override env to avoid cross-test bleed."""
    monkeypatch.delenv(POLICY_OVERRIDE_JSON_ENV, raising=False)
    yield
