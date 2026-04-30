from __future__ import annotations

from dataclasses import dataclass, asdict
from typing import Any
from urllib.parse import urlparse

from app.editorial.policy import load_policy
from app.utils.source_images import is_complete_main_image_url


@dataclass(frozen=True)
class RankedItem:
    editorial_score: float
    topic_type: str
    source_tier: str
    eligible_for_main: bool
    has_complete_main_image: bool = False
    rejected: bool = False
    rejection_reason: str | None = None
    score_breakdown: dict[str, float] | None = None


def _get(obj: Any, key: str, default: Any = None) -> Any:
    if obj is None:
        return default
    if isinstance(obj, dict):
        return obj.get(key, default)
    return getattr(obj, key, default)


def _text(item: Any, *keys: str) -> str:
    return " ".join(str(_get(item, key, "") or "") for key in keys).lower()


def _domain(url: str | None) -> str:
    if not url:
        return ""
    return urlparse(url.lower()).netloc.removeprefix("www.")


def _is_arxiv(item: Any, source: Any) -> bool:
    url = str(_get(item, "url", "") or _get(item, "canonical_url", "") or "").lower()
    source_type = str(_get(item, "source_type", "") or _get(source, "source_type", "") or "").lower()
    source_id = str(_get(item, "source_id", "") or _get(source, "source_id", "") or _get(source, "name", "") or "").lower()
    return source_type == "arxiv" or "arxiv.org" in url or "arxiv" in source_id


def _normalize_source_tier(item: Any, source: Any, policy: dict[str, Any]) -> str:
    source_type = str(_get(item, "source_type", "") or _get(source, "source_type", "") or "").lower()
    explicit_values = [
        _get(source, "tier"),
        _get(source, "source_tier"),
        _get(item, "source_tier"),
    ]
    for value in explicit_values:
        normalized_value = str(value or "").lower()
        if normalized_value in policy.get("source_tiers", {}):
            return normalized_value

    if _is_arxiv(item, source):
        return "research"
    if source_type == "github":
        return "developer_signal"

    raw_values = [
        *explicit_values,
        _get(source, "trust_level"),
        _get(source, "source_type"),
        _get(item, "trust_level"),
        _get(item, "source_type"),
    ]
    aliases = policy.get("source_aliases", {})
    normalized = [str(v).lower() for v in raw_values if v]

    for tier, tier_aliases in aliases.items():
        if any(value == str(alias).lower() for value in normalized for alias in tier_aliases):
            return tier
    if any(v in {"official", "verified"} for v in normalized):
        return "official"
    return "unknown"


_OSS_DEV_KEYS = (
    "open source", "open weight", "open-weight", "open model",
    "quantiz", "gguf", "ggml", "vllm", "ollama", "llama.cpp",
    "lora", "qlora", "finetun", "fine-tun",
    "hugging face", "huggingface",
    "inference engine", "inference server",
)


def _classify_topic(item: Any, source: Any, source_tier: str) -> str:
    blob = _text(item, "title", "raw_text", "summary", "description", "url")
    if _is_arxiv(item, source):
        return "research"
    # GitHub / developer sources are always tooling regardless of title content.
    if source_tier == "developer_signal":
        return "tooling"
    # OSS / local inference / fine-tuning content → tooling before product check.
    if any(k in blob for k in _OSS_DEV_KEYS):
        return "tooling"
    if any(k in blob for k in ["release", "launch", "announc", "model", "api", "product", "preview", "generally available", "new app"]):
        return "product" if source_tier == "official" else "industry"
    if any(k in blob for k in ["paper", "benchmark", "dataset", "research", "eval"]):
        return "research"
    if any(k in blob for k in ["github", "open source", "sdk", "tool", "library", "repo", "plugin", "extension"]):
        return "tooling"
    if any(k in blob for k in ["policy", "regulation", "safety", "copyright", "court"]):
        return "policy"
    return "industry"


def _source_present(item: Any, source: Any) -> bool:
    return bool(
        source
        or _get(item, "source_id")
        or _get(item, "source_type")
        or _get(item, "source_tier")
        or _get(item, "trust_level")
    )


def _metrics_score(item: Any, weight: float) -> float:
    metrics = _get(item, "metrics_json", None) or _get(item, "metrics", None) or {}
    if not isinstance(metrics, dict):
        return 0.0
    total = 0.0
    for key in ("stars", "score", "points", "likes", "retweets", "citations"):
        try:
            total += float(metrics.get(key, 0) or 0)
        except (TypeError, ValueError):
            continue
    return min(total * weight, 10.0)


def _dict_value(obj: Any, key: str) -> Any:
    return obj.get(key) if isinstance(obj, dict) else None


def _main_image_url(item: Any) -> str:
    candidates = [
        _get(item, "image_url"),
        _get(item, "og_image_url"),
        _get(item, "representative_image_url"),
    ]

    raw_json = _get(item, "raw_json", None)
    metadata_json = _get(item, "metadata_json", None)
    for mapping in (raw_json, metadata_json):
        if isinstance(mapping, dict):
            candidates.extend(
                [
                    _dict_value(mapping, "image_url"),
                    _dict_value(mapping, "og_image_url"),
                    _dict_value(mapping, "representative_image_url"),
                ]
            )

    for candidate in candidates:
        image_url = str(candidate or "")
        if is_complete_main_image_url(image_url):
            return image_url
    return ""


class EditorialRanker:
    """Pure, deterministic ranker for raw collected AI-news items."""

    def __init__(self, policy: dict[str, Any] | None = None):
        self.policy = policy or load_policy()

    def rank(self, item: Any, source: Any | None = None) -> dict[str, Any]:
        policy = self.policy
        weights = policy.get("scoring_weights", {})
        penalties = policy.get("penalties", {})
        gates = policy.get("quality_gates", {})
        main_cfg = policy.get("main_headline", {})

        title = str(_get(item, "title", "") or "").strip()
        url = str(_get(item, "url", "") or _get(item, "canonical_url", "") or "").strip()
        source_tier = _normalize_source_tier(item, source, policy)
        topic_type = _classify_topic(item, source, source_tier)
        arxiv_only = _is_arxiv(item, source)
        has_complete_main_image = bool(_main_image_url(item)) and not arxiv_only

        rejection_reason = None
        if gates.get("require_source", True) and not _source_present(item, source):
            rejection_reason = "no_source"
        elif gates.get("require_url", True) and not url:
            rejection_reason = "missing_url"
        elif len(title) < int(gates.get("min_title_length", 0)):
            rejection_reason = "title_too_short"
        elif gates.get("reject_unknown_source_without_url", True) and source_tier == "unknown" and not _domain(url):
            rejection_reason = "unknown_source"

        breakdown: dict[str, float] = {"base": float(weights.get("base_score", 50))}
        tier_boost = float(policy.get("source_tiers", {}).get(source_tier, {}).get("boost", 0))
        breakdown["source_tier"] = tier_boost * float(weights.get("source_tier", 1.0))
        if source_tier == "official":
            breakdown["official_source_boost"] = float(weights.get("official_source_boost", 0))
        if source_tier == "mainstream":
            breakdown["mainstream_source_boost"] = float(weights.get("mainstream_source_boost", 0))
        if topic_type == "product":
            breakdown["product_signal"] = float(weights.get("product_signal", 0))
        if topic_type == "research":
            breakdown["research_signal"] = float(weights.get("research_signal", 0))
        breakdown["metrics_signal"] = _metrics_score(item, float(weights.get("metrics_signal", 0)))
        breakdown["main_image_signal"] = (
            float(weights.get("main_image_signal", 0))
            if has_complete_main_image
            else 0.0
        )

        penalty_total = 0.0
        if arxiv_only:
            penalty_total += float(penalties.get("obscure_research_penalty", 0))
        if source_tier == "community":
            penalty_total += float(penalties.get("community_penalty", 0))
        if not url:
            penalty_total += float(penalties.get("missing_url_penalty", 0))
        if not title:
            penalty_total += float(penalties.get("missing_title_penalty", 0))
        if rejection_reason:
            penalty_total += 100.0
        breakdown["penalties"] = -penalty_total

        score = max(0.0, min(100.0, sum(breakdown.values())))
        tier_main_ok = bool(policy.get("source_tiers", {}).get(source_tier, {}).get("eligible_for_main", False))
        eligible_for_main = (
            not rejection_reason
            and score >= float(main_cfg.get("minimum_score", 55))
            and tier_main_ok
            and (bool(main_cfg.get("allow_arxiv_only", False)) or not arxiv_only)
        )

        result = RankedItem(
            editorial_score=round(score, 2),
            topic_type=topic_type,
            source_tier=source_tier,
            eligible_for_main=eligible_for_main,
            has_complete_main_image=has_complete_main_image,
            rejected=bool(rejection_reason),
            rejection_reason=rejection_reason,
            score_breakdown={k: round(v, 2) for k, v in breakdown.items()},
        )
        return asdict(result)


def rank_item(item: Any, source: Any | None = None, policy: dict[str, Any] | None = None) -> dict[str, Any]:
    """Rank a raw item/source pair and return serializable editorial metadata."""
    return EditorialRanker(policy=policy).rank(item, source=source)
