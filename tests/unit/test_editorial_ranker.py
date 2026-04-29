from __future__ import annotations

from app.editorial.policy import load_policy
from app.editorial.ranker import rank_item


def test_mainstream_boost_scores_above_unknown_source():
    item = {
        "source_id": "the-verge",
        "source_type": "rss",
        "title": "Major AI model update reaches enterprise customers",
        "url": "https://www.theverge.com/ai/model-update",
    }

    mainstream = rank_item(item, source={"source_type": "trusted_media"})
    unknown = rank_item({**item, "source_tier": "unknown"}, source={"source_type": "unknown"})

    assert mainstream["source_tier"] == "mainstream"
    assert mainstream["editorial_score"] > unknown["editorial_score"]
    assert mainstream["score_breakdown"]["mainstream_source_boost"] > 0


def test_arxiv_is_research_and_gets_obscure_research_penalty():
    result = rank_item(
        {
            "source_id": "arXiv cs.LG",
            "source_type": "arxiv",
            "title": "A benchmark study of reasoning in multimodal agents",
            "url": "https://arxiv.org/abs/2604.12345",
        }
    )

    assert result["topic_type"] == "research"
    assert result["source_tier"] == "research"
    assert result["score_breakdown"]["penalties"] <= -load_policy()["penalties"]["obscure_research_penalty"]
    assert result["eligible_for_main"] is False


def test_official_product_source_is_eligible_for_main():
    result = rank_item(
        {
            "source_id": "openai-blog",
            "source_type": "rss",
            "title": "OpenAI launches new API features for developers",
            "url": "https://openai.com/news/new-api-features/",
        },
        source={"trust_level": "official", "source_type": "official_site"},
    )

    assert result["source_tier"] == "official"
    assert result["topic_type"] == "product"
    assert result["eligible_for_main"] is True
    assert result["rejection_reason"] is None


def test_no_source_rejection():
    result = rank_item(
        {
            "title": "AI startup announces a new assistant product",
            "url": "https://example.com/news/assistant-product",
        }
    )

    assert result["rejected"] is True
    assert result["rejection_reason"] == "no_source"
    assert result["eligible_for_main"] is False


def test_github_source_is_developer_signal_not_main_headline():
    result = rank_item(
        {
            "source_id": "GitHub openai",
            "source_type": "github",
            "title": "openai/codex v1.2.3",
            "url": "https://github.com/openai/codex/releases/tag/v1.2.3",
        },
        source={"source_type": "github", "trust_level": "official", "source_tier": "developer_signal"},
    )

    assert result["source_tier"] == "developer_signal"
    assert result["eligible_for_main"] is True
