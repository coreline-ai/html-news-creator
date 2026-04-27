"""Unit tests for the extractor layer (Phase 1-B)."""
from __future__ import annotations

from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from app.extractors.base import ExtractResult, ExtractorError, ExtractorUnavailableError, SSRFBlockedError
from app.extractors.orchestrator import ExtractorOrchestrator


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _success_result(extractor: str, quality: float = 0.5) -> ExtractResult:
    return ExtractResult(
        raw_item_id="item-1",
        extractor=extractor,
        status="success",
        content_markdown="x" * int(quality * 2000),
        quality_score=quality,
    )


def _make_orchestrator(
    firecrawl_side_effect=None,
    crawl4ai_side_effect=None,
    trafilatura_side_effect=None,
    crawl4ai_result: ExtractResult | None = None,
) -> ExtractorOrchestrator:
    """Return an ExtractorOrchestrator whose extractors are replaced with mocks."""
    orchestrator = ExtractorOrchestrator.__new__(ExtractorOrchestrator)

    from app.utils.logger import get_logger
    orchestrator.logger = get_logger(step="extract")

    mock_firecrawl = MagicMock()
    if firecrawl_side_effect is not None:
        mock_firecrawl.extract = AsyncMock(side_effect=firecrawl_side_effect)
    else:
        mock_firecrawl.extract = AsyncMock(return_value=_success_result("firecrawl"))

    mock_crawl4ai = MagicMock()
    if crawl4ai_side_effect is not None:
        mock_crawl4ai.extract = AsyncMock(side_effect=crawl4ai_side_effect)
    elif crawl4ai_result is not None:
        mock_crawl4ai.extract = AsyncMock(return_value=crawl4ai_result)
    else:
        mock_crawl4ai.extract = AsyncMock(return_value=_success_result("crawl4ai"))

    mock_trafilatura = MagicMock()
    if trafilatura_side_effect is not None:
        mock_trafilatura.extract = AsyncMock(side_effect=trafilatura_side_effect)
    else:
        mock_trafilatura.extract = AsyncMock(return_value=_success_result("trafilatura"))

    orchestrator.extractors = [mock_firecrawl, mock_crawl4ai, mock_trafilatura]
    return orchestrator


# ---------------------------------------------------------------------------
# TC-1.4  Fallback: FirecrawlExtractor raises ExtractorError → Crawl4AI succeeds
# ---------------------------------------------------------------------------

@pytest.mark.asyncio
async def test_tc1_4_fallback_to_crawl4ai():
    """When Firecrawl raises ExtractorError, orchestrator falls back to Crawl4AI."""
    crawl4ai_result = _success_result("crawl4ai", quality=0.6)
    orchestrator = _make_orchestrator(
        firecrawl_side_effect=ExtractorError("firecrawl boom"),
        crawl4ai_result=crawl4ai_result,
    )

    result = await orchestrator.extract("https://example.com/article", "item-1")

    assert result.extractor == "crawl4ai"
    assert result.status == "success"
    assert result.quality_score > 0.1


# ---------------------------------------------------------------------------
# TC-1.5  All extractors raise ExtractorError → returns status="failed"
# ---------------------------------------------------------------------------

@pytest.mark.asyncio
async def test_tc1_5_all_extractors_fail():
    """When all extractors raise ExtractorError, orchestrator returns a failed ExtractResult."""
    orchestrator = _make_orchestrator(
        firecrawl_side_effect=ExtractorError("firecrawl failed"),
        crawl4ai_side_effect=ExtractorError("crawl4ai failed"),
        trafilatura_side_effect=ExtractorError("trafilatura failed"),
    )

    result = await orchestrator.extract("https://example.com/article", "item-2")

    assert result.status == "failed"
    assert result.extractor == "none"
    assert result.error is not None


# ---------------------------------------------------------------------------
# TC-1.E1  SSRF-blocked URL raises SSRFBlockedError
# ---------------------------------------------------------------------------

@pytest.mark.asyncio
async def test_tc1_e1_ssrf_blocked():
    """Requests to SSRF-protected addresses raise SSRFBlockedError before any extractor runs."""
    orchestrator = ExtractorOrchestrator.__new__(ExtractorOrchestrator)
    from app.utils.logger import get_logger
    orchestrator.logger = get_logger(step="extract")
    # No extractors should be called; set an empty list to be safe
    orchestrator.extractors = []

    with pytest.raises(SSRFBlockedError):
        await orchestrator.extract("http://169.254.169.254/latest", "item-ssrf")


# ---------------------------------------------------------------------------
# TC-1.E2  FirecrawlExtractor with empty API key raises ExtractorUnavailableError
# ---------------------------------------------------------------------------

@pytest.mark.asyncio
async def test_tc1_e2_firecrawl_no_api_key():
    """FirecrawlExtractor.extract() raises ExtractorUnavailableError when API key is empty."""
    from app.extractors.firecrawl import FirecrawlExtractor

    with patch("app.extractors.firecrawl.settings") as mock_settings:
        mock_settings.firecrawl_api_key = ""
        extractor = FirecrawlExtractor()

    with pytest.raises(ExtractorUnavailableError):
        await extractor.extract("https://example.com/article", "item-3")
