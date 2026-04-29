from __future__ import annotations

from copy import deepcopy
from math import ceil
from typing import Any


def _score(editorial: dict[str, Any]) -> float:
    try:
        return float(editorial.get("editorial_score", 0.0) or 0.0)
    except (TypeError, ValueError):
        return 0.0


def _source_tiers(editorial: dict[str, Any]) -> list[str]:
    """Return normalized source tiers from either source_tier or source_tiers."""
    tiers = editorial.get("source_tiers")
    if tiers is None:
        tiers = [editorial.get("source_tier", "unknown")]
    elif isinstance(tiers, str):
        tiers = [tiers]

    normalized = [str(tier or "unknown") for tier in tiers if tier is not None]
    return normalized or ["unknown"]


def _is_arxiv_only(source_tiers: list[str]) -> bool:
    """A cluster is arXiv-only when every known source tier is research."""
    tiers = set(source_tiers)
    return bool(tiers) and (source_tiers == ["research"] or tiers <= {"research"})


def summarize_cluster_editorial(
    items: list[dict], policy: dict | None = None
) -> dict:
    """Summarize item-level editorial ranks into cluster-level metadata.

    The function is intentionally pure and serializable so the daily runner can
    reuse it without depending on database or pipeline state.
    """
    ranks = [item.get("editorial", {}) for item in items if item.get("editorial")]
    if not ranks:
        return {
            "editorial_score": 0.0,
            "topic_type": "industry",
            "eligible_for_main": False,
            "rejected": True,
            "rejection_reason": "no_ranked_items",
            "source_tiers": [],
            "arxiv_only": False,
        }

    usable = [rank for rank in ranks if not rank.get("rejected")]
    best = max(ranks, key=_score)
    source_tiers = sorted({tier for rank in ranks for tier in _source_tiers(rank)})

    # Cluster size boost: more sources covering the same topic → trending signal.
    weights = (policy or {}).get("scoring_weights", {})
    size_per = _float_cfg(weights, "cluster_size_boost_per_item", 5.0)
    size_max = _float_cfg(weights, "cluster_size_boost_max", 20.0)
    size_bonus = min((len(items) - 1) * size_per, size_max)
    final_score = min(100.0, _score(best) + size_bonus)

    return {
        "editorial_score": final_score,
        "topic_type": best.get("topic_type", "industry"),
        "eligible_for_main": any(bool(rank.get("eligible_for_main")) for rank in ranks),
        "rejected": not usable,
        "rejection_reason": "all_items_rejected" if not usable else None,
        "source_tiers": source_tiers,
        "arxiv_only": _is_arxiv_only(source_tiers),
        "best_item": deepcopy(best),
    }


def _candidate_editorial(candidate: dict[str, Any]) -> dict[str, Any]:
    editorial = candidate.get("editorial")
    if isinstance(editorial, dict) and editorial:
        normalized = deepcopy(editorial)
        source_tiers = sorted(set(_source_tiers(normalized)))
        normalized.setdefault("source_tiers", source_tiers)
        normalized.setdefault("arxiv_only", _is_arxiv_only(source_tiers))
        return normalized
    return summarize_cluster_editorial(candidate.get("items") or [])


def _int_cfg(mapping: dict[str, Any], key: str, default: int) -> int:
    try:
        return int(mapping.get(key, default))
    except (TypeError, ValueError):
        return default


def _float_cfg(mapping: dict[str, Any], key: str, default: float) -> float:
    try:
        return float(mapping.get(key, default))
    except (TypeError, ValueError):
        return default


def _iter_values(value: Any) -> list[Any]:
    if value is None:
        return []
    if isinstance(value, (list, tuple, set)):
        return [item for item in value if item is not None]
    return [value]


def _first_mapping_value(mapping: dict[str, Any], keys: tuple[str, ...]) -> list[Any]:
    values: list[Any] = []
    for key in keys:
        values.extend(_iter_values(mapping.get(key)))
    return values


def _candidate_source_keys(candidate: dict[str, Any]) -> set[str]:
    """Return source identity keys without mutating heterogeneous candidates."""
    mappings: list[dict[str, Any]] = []
    for value in (candidate, candidate.get("editorial"), candidate.get("cluster")):
        if isinstance(value, dict):
            mappings.append(value)

    for item in candidate.get("items") or []:
        if isinstance(item, dict):
            mappings.append(item)
            editorial = item.get("editorial")
            if isinstance(editorial, dict):
                mappings.append(editorial)

    source_ids: set[str] = set()
    source_names: set[str] = set()
    for mapping in mappings:
        source_ids.update(
            str(value)
            for value in _first_mapping_value(mapping, ("source_id", "source_ids"))
            if str(value).strip()
        )
        source_names.update(
            str(value)
            for value in _first_mapping_value(mapping, ("source_name", "source_names"))
            if str(value).strip()
        )

    return {f"id:{value}" for value in source_ids} | {
        f"name:{value}" for value in source_names
    }


def _ratio_cap(mapping: dict[str, Any], key: str, max_sections: int) -> int | None:
    if key not in mapping:
        return None
    ratio = _float_cfg(mapping, key, 0.0)
    if ratio <= 0:
        return None
    return max(1, ceil(max_sections * min(ratio, 1.0)))


def select_editorial_clusters(candidates: list[dict], policy: dict) -> list[dict]:
    """Select report clusters according to editorial policy.

    Accepts candidates shaped as ``{cluster, items, editorial}`` or
    ``{id, editorial}``. Returned candidates are shallow copies with normalized
    ``editorial`` metadata, leaving caller-owned input dicts untouched.
    """
    selection_cfg = policy.get("report_selection", {}) or {}
    quotas = policy.get("section_quotas", {}) or {}
    max_sections = _int_cfg(selection_cfg, "max_sections", 6)
    min_score = _float_cfg(selection_cfg, "min_section_score", 35.0)
    max_arxiv_only = _int_cfg(selection_cfg, "max_arxiv_only_sections", 1)
    max_community = _int_cfg(selection_cfg, "max_community_sections", max_sections)
    max_same_source = _int_cfg(selection_cfg, "max_same_source_name", max_sections)
    max_same_tier = _ratio_cap(
        selection_cfg, "max_same_source_tier_ratio", max_sections
    )

    normalized_candidates: list[dict[str, Any]] = []
    for candidate in candidates:
        editorial = _candidate_editorial(candidate)
        normalized = dict(candidate)
        normalized["editorial"] = editorial
        normalized_candidates.append(normalized)

    def sort_key(candidate: dict[str, Any]) -> tuple[int, float]:
        editorial = candidate["editorial"]
        return (
            1 if editorial.get("eligible_for_main") else 0,
            _score(editorial),
        )

    selected: list[dict] = []
    topic_counts: dict[str, int] = {}
    arxiv_only_count = 0
    community_count = 0
    source_counts: dict[str, int] = {}
    tier_counts: dict[str, int] = {}

    for candidate in sorted(normalized_candidates, key=sort_key, reverse=True):
        editorial = candidate["editorial"]
        topic = str(editorial.get("topic_type", "industry") or "industry")
        score = _score(editorial)

        if editorial.get("rejected") or score < min_score:
            continue
        if topic_counts.get(topic, 0) >= _int_cfg(quotas, topic, max_sections):
            continue
        source_tiers = _source_tiers(editorial)
        if editorial.get("arxiv_only") and arxiv_only_count >= max_arxiv_only:
            continue
        if "community" in source_tiers and community_count >= max_community:
            continue
        source_keys = _candidate_source_keys(candidate)
        if source_keys and any(
            source_counts.get(key, 0) >= max_same_source for key in source_keys
        ):
            continue
        if max_same_tier is not None and any(
            tier_counts.get(tier, 0) >= max_same_tier for tier in set(source_tiers)
        ):
            continue

        selected.append(candidate)
        topic_counts[topic] = topic_counts.get(topic, 0) + 1
        if editorial.get("arxiv_only"):
            arxiv_only_count += 1
        if "community" in source_tiers:
            community_count += 1
        for key in source_keys:
            source_counts[key] = source_counts.get(key, 0) + 1
        for tier in set(source_tiers):
            tier_counts[tier] = tier_counts.get(tier, 0) + 1
        if len(selected) >= max_sections:
            break

    return selected
