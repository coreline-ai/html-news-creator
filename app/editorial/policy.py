from __future__ import annotations

import json
import os
from copy import deepcopy
from pathlib import Path
from typing import Any

import yaml

from app.utils.logger import get_logger

DEFAULT_POLICY_PATH = Path(__file__).resolve().parents[2] / "data" / "editorial_policy.yaml"

# Env var that lets the API hand a temporary policy file to a subprocess.
# When set, ``load_policy()`` reads from this path instead of the repo-level
# yaml — see ``app/admin/run_runner.py`` for the producer side.
POLICY_PATH_ENV = "EDITORIAL_POLICY_PATH"

# Env var carrying a JSON-encoded deep-merge override applied **after** the
# YAML policy is loaded. Used by the run-runner to forward per-run editorial
# knobs (target_sections, quotas, …) the operator picked in the UI for this
# specific run without mutating the on-disk policy file.
POLICY_OVERRIDE_JSON_ENV = "EDITORIAL_POLICY_OVERRIDE_JSON"

_logger = get_logger(step="editorial.policy")


DEFAULT_POLICY: dict[str, Any] = {
    "source_tiers": {
        "official": {"boost": 18, "eligible_for_main": True},
        "mainstream": {"boost": 12, "eligible_for_main": True},
        "research": {"boost": 4, "eligible_for_main": False},
        "developer_signal": {"boost": 14, "eligible_for_main": True},
        "community": {"boost": -4, "eligible_for_main": False},
        "unknown": {"boost": -18, "eligible_for_main": False},
    },
    "section_quotas": {"product": 4, "research": 1, "industry": 1, "tooling": 4, "policy": 1},
    "report_selection": {
        "max_sections": 10,
        "target_sections": 10,
        "min_section_score": 35,
        "max_arxiv_only_sections": 1,
        "max_community_sections": 1,
        "max_same_source_name": 2,
        "max_same_source_tier_ratio": 0.75,
        "backfill_min_section_score": 35,
        "backfill_require_image": True,
        "backfill_relax_topic_quotas": True,
        "backfill_max_community_sections": 2,
        "backfill_max_same_source_name": 5,
        "backfill_max_same_source_tier_ratio": 0.9,
        "prefer_mainstream_first": True,
    },
    "scoring_weights": {
        "base_score": 50,
        "source_tier": 1.0,
        "official_source_boost": 10,
        "mainstream_source_boost": 6,
        "product_signal": 8,
        "research_signal": 3,
        "main_image_signal": 8,
        "metrics_signal": 0.25,
        "cluster_size_boost_per_item": 5,
        "cluster_size_boost_max": 20,
    },
    "penalties": {
        "obscure_research_penalty": 22,
        "arxiv_only_main_penalty": 100,
        "community_penalty": 8,
        "missing_url_penalty": 40,
        "missing_title_penalty": 30,
    },
    "quality_gates": {
        "require_source": True,
        "require_url": True,
        "min_title_length": 8,
        "reject_unknown_source_without_url": True,
    },
    "main_headline": {"allow_arxiv_only": False, "minimum_score": 55},
    "source_aliases": {
        "official": ["official", "official_site", "official_docs", "official_github", "official_huggingface"],
        "mainstream": ["mainstream", "trusted_media", "media"],
        "research": ["research", "paper_arxiv", "arxiv"],
        "developer_signal": ["developer_signal", "github", "official_github", "developer"],
        "community": ["community"],
    },
}


def _deep_merge(base: dict[str, Any], override: dict[str, Any]) -> dict[str, Any]:
    merged = deepcopy(base)
    for key, value in (override or {}).items():
        if isinstance(value, dict) and isinstance(merged.get(key), dict):
            merged[key] = _deep_merge(merged[key], value)
        else:
            merged[key] = value
    return merged


def load_policy(path: str | Path | None = None) -> dict[str, Any]:
    """Load editorial ranking policy from YAML.

    Resolution order for the source file:
      1. Explicit ``path`` argument (used by tests and one-off callers).
      2. ``$EDITORIAL_POLICY_PATH`` environment variable. The admin API sets
         this when handing a runtime-override-materialized yaml down to the
         ``scripts/run_daily.py`` subprocess so operator-tuned policies actually
         drive the pipeline.
      3. ``DEFAULT_POLICY_PATH`` (``data/editorial_policy.yaml``).

    Missing sections are filled from ``DEFAULT_POLICY`` so partial fixtures and
    materialized override files remain valid.

    After the YAML resolution, ``$EDITORIAL_POLICY_OVERRIDE_JSON`` (if set) is
    parsed and deep-merged on top so per-run knobs (target_sections, quotas,
    …) the operator picked in the UI for THIS run can override the persisted
    policy without writing a tempfile. Bad JSON is logged as
    ``policy_override_json_parse_failed`` and skipped — the run still gets a
    valid policy dict from the YAML/default layer.

    Returns a plain dict.
    """
    if path is not None:
        policy_path = Path(path)
    else:
        env_value = os.environ.get(POLICY_PATH_ENV)
        if env_value:
            policy_path = Path(env_value)
        else:
            policy_path = DEFAULT_POLICY_PATH

    if not policy_path.exists():
        merged = deepcopy(DEFAULT_POLICY)
    else:
        with policy_path.open("r", encoding="utf-8") as f:
            loaded = yaml.safe_load(f) or {}
        if not isinstance(loaded, dict):
            raise ValueError(
                f"Editorial policy must be a YAML mapping: {policy_path}"
            )
        merged = _deep_merge(DEFAULT_POLICY, loaded)

    # Per-run JSON override (deep-merged on top). Failing to parse should not
    # poison the entire policy load — the run can still proceed against the
    # YAML/default policy, just without the requested per-run knobs. The
    # error is logged so the operator can spot it in run logs.
    override_json = os.environ.get(POLICY_OVERRIDE_JSON_ENV)
    if override_json:
        try:
            override_dict = json.loads(override_json)
            if not isinstance(override_dict, dict):
                raise ValueError("policy override must decode to a JSON object")
            merged = _deep_merge(merged, override_dict)
        except (json.JSONDecodeError, ValueError) as exc:
            _logger.error(
                "policy_override_json_parse_failed",
                error=str(exc),
                preview=override_json[:200],
            )

    return merged
