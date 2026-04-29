from __future__ import annotations

from app.editorial.selection import (
    select_editorial_clusters,
    summarize_cluster_editorial,
)


def _policy(**selection_overrides):
    selection = {
        "max_sections": 6,
        "min_section_score": 35,
        "max_arxiv_only_sections": 1,
    }
    selection.update(selection_overrides)
    return {
        "report_selection": selection,
        "section_quotas": {
            "product": 4,
            "research": 4,
            "industry": 4,
            "tooling": 4,
            "policy": 4,
        },
    }


def _candidate(
    id_: str,
    score: float,
    topic: str = "industry",
    *,
    eligible=True,
    tiers=None,
    rejected=False,
):
    return {
        "id": id_,
        "editorial": {
            "editorial_score": score,
            "topic_type": topic,
            "eligible_for_main": eligible,
            "source_tiers": tiers or ["mainstream"],
            "arxiv_only": set(tiers or ["mainstream"]) <= {"research"},
            "rejected": rejected,
        },
    }


def test_summarize_cluster_editorial_uses_best_score_topic_and_arxiv_only():
    summary = summarize_cluster_editorial(
        [
            {
                "editorial": {
                    "editorial_score": 44,
                    "topic_type": "industry",
                    "source_tier": "research",
                }
            },
            {
                "editorial": {
                    "editorial_score": 72,
                    "topic_type": "research",
                    "source_tier": "research",
                    "eligible_for_main": False,
                }
            },
        ]
    )

    # 2 items → size bonus = (2-1) * 5 = 5; 72 + 5 = 77
    assert summary["editorial_score"] == 77.0
    assert summary["topic_type"] == "research"
    assert summary["source_tiers"] == ["research"]
    assert summary["arxiv_only"] is True
    assert summary["rejected"] is False


def test_select_editorial_clusters_orders_by_eligible_then_score():
    candidates = [
        _candidate("low", 50),
        _candidate("high", 80),
        _candidate("ineligible_top_score", 95, eligible=False),
    ]

    selected = select_editorial_clusters(candidates, _policy())

    assert [candidate["id"] for candidate in selected] == [
        "high",
        "low",
        "ineligible_top_score",
    ]


def test_select_editorial_clusters_respects_max_sections():
    selected = select_editorial_clusters(
        [_candidate("a", 90), _candidate("b", 80), _candidate("c", 70)],
        _policy(max_sections=2),
    )

    assert [candidate["id"] for candidate in selected] == ["a", "b"]


def test_select_editorial_clusters_applies_topic_quota():
    policy = _policy()
    policy["section_quotas"]["industry"] = 1
    candidates = [
        _candidate("industry_top", 90, "industry"),
        _candidate("industry_second", 80, "industry"),
        _candidate("product", 70, "product"),
    ]

    selected = select_editorial_clusters(candidates, policy)

    assert [candidate["id"] for candidate in selected] == ["industry_top", "product"]


def test_select_editorial_clusters_limits_arxiv_only_to_one():
    candidates = [
        _candidate("research_a", 90, "research", tiers=["research"]),
        _candidate("research_b", 85, "research", tiers=["research"]),
        _candidate("industry", 80, "industry", tiers=["mainstream"]),
    ]

    selected = select_editorial_clusters(candidates, _policy(max_arxiv_only_sections=1))

    assert [candidate["id"] for candidate in selected] == ["research_a", "industry"]


def test_select_editorial_clusters_excludes_rejected_candidates():
    selected = select_editorial_clusters(
        [_candidate("rejected", 99, rejected=True), _candidate("accepted", 60)],
        _policy(),
    )

    assert [candidate["id"] for candidate in selected] == ["accepted"]


def test_select_editorial_clusters_summarizes_cluster_items_when_editorial_missing():
    candidates = [
        {
            "cluster": {"id": "cluster-1"},
            "items": [
                {
                    "editorial": {
                        "editorial_score": 42,
                        "topic_type": "industry",
                        "source_tier": "mainstream",
                    }
                },
                {
                    "editorial": {
                        "editorial_score": 77,
                        "topic_type": "product",
                        "source_tier": "official",
                        "eligible_for_main": True,
                    }
                },
            ],
        }
    ]

    selected = select_editorial_clusters(candidates, _policy())

    assert len(selected) == 1
    # 2 items → size bonus = (2-1) * 5 = 5; 77 + 5 = 82
    assert selected[0]["editorial"]["editorial_score"] == 82.0
    assert selected[0]["editorial"]["topic_type"] == "product"


def test_select_editorial_clusters_limits_community_sections():
    candidates = [
        _candidate("community_a", 95, tiers=["community"]),
        _candidate("community_b", 90, tiers=["community"]),
        _candidate("mainstream", 85, tiers=["mainstream"]),
    ]

    selected = select_editorial_clusters(candidates, _policy(max_community_sections=1))

    assert [candidate["id"] for candidate in selected] == ["community_a", "mainstream"]


def test_select_editorial_clusters_limits_same_source_name_without_mutating_input():
    candidates = [
        {**_candidate("source_a", 95), "source_name": "Same Source"},
        {**_candidate("source_b", 90), "source_name": "Same Source"},
        {**_candidate("other", 85), "source_name": "Other Source"},
    ]
    original_editorial = candidates[0]["editorial"].copy()

    selected = select_editorial_clusters(candidates, _policy(max_same_source_name=1))

    assert [candidate["id"] for candidate in selected] == ["source_a", "other"]
    assert candidates[0]["editorial"] == original_editorial
    assert selected[0] is not candidates[0]


def test_select_editorial_clusters_limits_same_source_id_from_cluster_items():
    candidates = [
        {
            "cluster": {"id": "cluster-a", "source_id": "shared"},
            "items": [
                {
                    "editorial": {
                        "editorial_score": 95,
                        "topic_type": "industry",
                        "source_tier": "mainstream",
                    }
                },
            ],
        },
        {
            "cluster": {"id": "cluster-b", "source_id": "shared"},
            "items": [
                {
                    "editorial": {
                        "editorial_score": 90,
                        "topic_type": "industry",
                        "source_tier": "mainstream",
                    }
                },
            ],
        },
        {
            "cluster": {"id": "cluster-c", "source_id": "distinct"},
            "items": [
                {
                    "editorial": {
                        "editorial_score": 85,
                        "topic_type": "industry",
                        "source_tier": "mainstream",
                    }
                },
            ],
        },
    ]

    selected = select_editorial_clusters(candidates, _policy(max_same_source_name=1))

    assert [candidate["cluster"]["id"] for candidate in selected] == [
        "cluster-a",
        "cluster-c",
    ]
