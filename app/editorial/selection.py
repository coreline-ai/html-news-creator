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
        "has_complete_main_image": any(
            bool(rank.get("has_complete_main_image")) for rank in ranks
        ),
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


def _bool_cfg(mapping: dict[str, Any], key: str, default: bool) -> bool:
    value = mapping.get(key, default)
    if isinstance(value, bool):
        return value
    if isinstance(value, str):
        return value.strip().lower() in {"1", "true", "yes", "on"}
    return bool(value)


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


def _has_nonempty_image_value(value: Any) -> bool:
    return any(str(item or "").strip() for item in _iter_values(value))


def _mapping_has_complete_image(mapping: dict[str, Any]) -> bool:
    if bool(mapping.get("has_complete_main_image")):
        return True

    editorial = mapping.get("editorial")
    if isinstance(editorial, dict):
        if bool(editorial.get("has_complete_main_image")):
            return True
        best_item = editorial.get("best_item")
        if isinstance(best_item, dict) and _mapping_has_complete_image(best_item):
            return True

    image_keys = (
        "image_url",
        "og_image_url",
        "representative_image_url",
        "thumbnail_url",
    )
    if any(_has_nonempty_image_value(mapping.get(key)) for key in image_keys):
        return True

    image_list_keys = ("content_image_urls", "image_urls", "images")
    return any(_has_nonempty_image_value(mapping.get(key)) for key in image_list_keys)


def _candidate_has_complete_image(candidate: dict[str, Any]) -> bool:
    if _mapping_has_complete_image(candidate):
        return True
    return any(
        isinstance(item, dict) and _mapping_has_complete_image(item)
        for item in candidate.get("items") or []
    )


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
    target_sections = min(
        _int_cfg(selection_cfg, "target_sections", max_sections),
        max_sections,
    )
    backfill_min_score = _float_cfg(
        selection_cfg, "backfill_min_section_score", min_score
    )
    backfill_require_image = _bool_cfg(
        selection_cfg, "backfill_require_image", True
    )
    backfill_relax_topic_quotas = _bool_cfg(
        selection_cfg, "backfill_relax_topic_quotas", False
    )
    backfill_max_community = _int_cfg(
        selection_cfg, "backfill_max_community_sections", max_community
    )
    backfill_max_same_source = _int_cfg(
        selection_cfg, "backfill_max_same_source_name", max_same_source
    )
    backfill_max_same_tier = _ratio_cap(
        selection_cfg, "backfill_max_same_source_tier_ratio", max_sections
    )
    if backfill_max_same_tier is None:
        backfill_max_same_tier = max_same_tier

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
    selected_ids: set[int] = set()
    topic_counts: dict[str, int] = {}
    arxiv_only_count = 0
    community_count = 0
    source_counts: dict[str, int] = {}
    tier_counts: dict[str, int] = {}

    def can_select(
        candidate: dict[str, Any],
        *,
        min_allowed_score: float,
        enforce_topic_quotas: bool,
        community_limit: int,
        same_source_limit: int,
        same_tier_limit: int | None,
        require_image: bool,
    ) -> bool:
        if id(candidate) in selected_ids:
            return False
        editorial = candidate["editorial"]
        topic = str(editorial.get("topic_type", "industry") or "industry")
        score = _score(editorial)

        if editorial.get("rejected"):
            return False
        if score < min_allowed_score:
            return False
        if require_image and not _candidate_has_complete_image(candidate):
            return False
        if enforce_topic_quotas and topic_counts.get(topic, 0) >= _int_cfg(
            quotas, topic, max_sections
        ):
            return False
        source_tiers = _source_tiers(editorial)
        if editorial.get("arxiv_only") and arxiv_only_count >= max_arxiv_only:
            return False
        if "community" in source_tiers and community_count >= community_limit:
            return False
        source_keys = _candidate_source_keys(candidate)
        if source_keys and any(
            source_counts.get(key, 0) >= same_source_limit for key in source_keys
        ):
            return False
        if same_tier_limit is not None and any(
            tier_counts.get(tier, 0) >= same_tier_limit for tier in set(source_tiers)
        ):
            return False
        return True

    def add_candidate(candidate: dict[str, Any]) -> None:
        nonlocal arxiv_only_count, community_count
        editorial = candidate["editorial"]
        topic = str(editorial.get("topic_type", "industry") or "industry")
        source_tiers = _source_tiers(editorial)
        source_keys = _candidate_source_keys(candidate)
        selected.append(candidate)
        selected_ids.add(id(candidate))
        topic_counts[topic] = topic_counts.get(topic, 0) + 1
        if editorial.get("arxiv_only"):
            arxiv_only_count += 1
        if "community" in source_tiers:
            community_count += 1
        for key in source_keys:
            source_counts[key] = source_counts.get(key, 0) + 1
        for tier in set(source_tiers):
            tier_counts[tier] = tier_counts.get(tier, 0) + 1

    sorted_candidates = sorted(normalized_candidates, key=sort_key, reverse=True)

    for candidate in sorted_candidates:
        if not can_select(
            candidate,
            min_allowed_score=min_score,
            enforce_topic_quotas=True,
            community_limit=max_community,
            same_source_limit=max_same_source,
            same_tier_limit=max_same_tier,
            require_image=False,
        ):
            continue

        add_candidate(candidate)
        if len(selected) >= max_sections:
            break

    if len(selected) < target_sections:
        backfill_candidates = sorted(
            normalized_candidates,
            key=lambda candidate: (
                1 if _candidate_has_complete_image(candidate) else 0,
                1 if candidate["editorial"].get("eligible_for_main") else 0,
                _score(candidate["editorial"]),
            ),
            reverse=True,
        )

        for candidate in backfill_candidates:
            if not can_select(
                candidate,
                min_allowed_score=backfill_min_score,
                enforce_topic_quotas=not backfill_relax_topic_quotas,
                community_limit=backfill_max_community,
                same_source_limit=backfill_max_same_source,
                same_tier_limit=backfill_max_same_tier,
                require_image=backfill_require_image,
            ):
                continue

            add_candidate(candidate)
            if len(selected) >= target_sections:
                break

    return selected
