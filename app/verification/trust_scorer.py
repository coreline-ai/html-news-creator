from __future__ import annotations


def score(
    verification_status: str,
    source_type: str,
    evidence_count: int = 1,
) -> int:
    """
    Compute trust_score 0-100.

    Verification status tiers:
    - official_confirmed: 90-100
    - github_confirmed: 80-89
    - paper_confirmed: 75-84
    - trusted_media_only: 60-69
    - social_only: 30-39
    - unverified: 0-19
    """
    base_scores = {
        "official_confirmed": 90,
        "github_confirmed": 80,
        "paper_confirmed": 75,
        "trusted_media_only": 60,
        "community_only": 45,
        "social_only": 30,
        "unverified": 5,
    }
    base = base_scores.get(verification_status, 5)

    # Bonus for multiple evidence sources (max +10)
    evidence_bonus = min(10, (evidence_count - 1) * 3)

    # Source type adjustment
    type_bonus = {
        "official_site": 5,
        "official_docs": 5,
        "official_github": 3,
        "official_huggingface": 3,
        "paper_arxiv": 4,
        "trusted_media": 2,
        "community": 0,
        "unknown": -5,
    }.get(source_type, 0)

    return min(100, max(0, base + evidence_bonus + type_bonus))
