"""Unit tests for Phase 2 verification components."""
from __future__ import annotations

from pathlib import Path
from unittest.mock import AsyncMock, patch

import pytest

from app.verification.domain_registry import DomainRegistry
from app.verification import trust_scorer as TrustScorer


# ---------------------------------------------------------------------------
# Fixture: DomainRegistry loaded from the real YAML
# ---------------------------------------------------------------------------

@pytest.fixture
def registry():
    yaml_path = Path("data/official_domains.yaml")
    return DomainRegistry(yaml_path=yaml_path)


# ---------------------------------------------------------------------------
# TC-2.1  arxiv.org classified as 'official'
# ---------------------------------------------------------------------------

def test_tc2_1_arxiv_is_official(registry):
    result = registry.classify("https://arxiv.org/abs/2401.00001")
    assert result == "official"


# ---------------------------------------------------------------------------
# TC-2.2  unknown blog classified as 'unknown'
# ---------------------------------------------------------------------------

def test_tc2_2_unknown_blog(registry):
    result = registry.classify("https://unknown-blog.io/post")
    assert result == "unknown"


# ---------------------------------------------------------------------------
# TC-2.3  openai.com classified as 'official'
# ---------------------------------------------------------------------------

def test_tc2_3_openai_is_official(registry):
    result = registry.classify("https://openai.com/blog/gpt-4")
    assert result == "official"


# ---------------------------------------------------------------------------
# TC-2.4  techcrunch.com classified as 'trusted_media'
# ---------------------------------------------------------------------------

def test_tc2_4_techcrunch_is_trusted_media(registry):
    result = registry.classify("https://techcrunch.com/article")
    assert result == "trusted_media"


# ---------------------------------------------------------------------------
# TC-2.5  official_confirmed + official_site + 3 evidence → 90-100
# ---------------------------------------------------------------------------

def test_tc2_5_official_confirmed_score_in_range():
    result = TrustScorer.score("official_confirmed", "official_site", 3)
    assert 90 <= result <= 100


# ---------------------------------------------------------------------------
# TC-2.6  unverified + unknown + 0 evidence → 0-19
# ---------------------------------------------------------------------------

def test_tc2_6_unverified_score_in_range():
    result = TrustScorer.score("unverified", "unknown", 0)
    assert 0 <= result <= 19


# ---------------------------------------------------------------------------
# TC-2.7  SourceVerifier with official URL — skips LLM, returns official_confirmed
# ---------------------------------------------------------------------------

@pytest.mark.asyncio
async def test_tc2_7_official_url_skips_llm():
    with patch("app.utils.llm_client.chat", new=AsyncMock(
        side_effect=AssertionError("LLM should not be called for official sources")
    )):
        from app.verification.verifier import SourceVerifier
        verifier = SourceVerifier()
        result = await verifier.verify(
            cluster_id="tc-2-7",
            title="OpenAI releases new model",
            summary="OpenAI announced a new model on their blog.",
            source_urls=["https://openai.com/blog"],
        )

    assert result["verification_status"] == "official_confirmed"
    assert result["trust_score"] > 0


# ---------------------------------------------------------------------------
# TC-2.8  SourceVerifier with empty source_urls → unverified
# ---------------------------------------------------------------------------

@pytest.mark.asyncio
async def test_tc2_8_empty_sources_unverified():
    from app.verification.verifier import SourceVerifier
    verifier = SourceVerifier()
    result = await verifier.verify(
        cluster_id="tc-2-8",
        title="Some unverified claim",
        summary="No sources available.",
        source_urls=[],
    )
    assert result["verification_status"] == "unverified"


# ---------------------------------------------------------------------------
# TC-2.E1  empty source_urls → trust_score == 5
# ---------------------------------------------------------------------------

@pytest.mark.asyncio
async def test_tc2_e1_empty_sources_trust_score_is_5():
    from app.verification.verifier import SourceVerifier
    verifier = SourceVerifier()
    result = await verifier.verify(
        cluster_id="tc-2-e1",
        title="Another unverified claim",
        summary="No sources.",
        source_urls=[],
    )
    assert result["trust_score"] == 5
