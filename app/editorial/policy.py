from __future__ import annotations

from copy import deepcopy
from pathlib import Path
from typing import Any

import yaml

DEFAULT_POLICY_PATH = Path(__file__).resolve().parents[2] / "data" / "editorial_policy.yaml"


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

    The returned object is a plain dict to keep tests and downstream code simple.
    Missing sections are filled from ``DEFAULT_POLICY`` so partial test fixtures are
    valid and production behavior remains stable if the YAML is edited.
    """
    policy_path = Path(path) if path is not None else DEFAULT_POLICY_PATH
    if not policy_path.exists():
        return deepcopy(DEFAULT_POLICY)

    with policy_path.open("r", encoding="utf-8") as f:
        loaded = yaml.safe_load(f) or {}
    if not isinstance(loaded, dict):
        raise ValueError(f"Editorial policy must be a YAML mapping: {policy_path}")
    return _deep_merge(DEFAULT_POLICY, loaded)
