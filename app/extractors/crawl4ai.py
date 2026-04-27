from __future__ import annotations

from app.config import settings
from app.extractors.base import (
    BaseExtractor,
    ExtractResult,
    ExtractorError,
    ExtractorUnavailableError,
)
from app.utils.logger import get_logger


def _calc_quality(content: str) -> float:
    return min(1.0, len(content) / 2000)


class Crawl4AIExtractor(BaseExtractor):
    def __init__(self) -> None:
        self._enabled = settings.crawl4ai_enabled
        self.logger = get_logger(step="extract")

    async def extract(self, url: str, raw_item_id: str = "") -> ExtractResult:
        if not self._enabled:
            raise ExtractorUnavailableError("Crawl4AI is disabled in configuration")

        try:
            from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig, CacheMode
        except ImportError as exc:
            raise ExtractorUnavailableError(f"crawl4ai is not installed: {exc}") from exc

        try:
            browser_config = BrowserConfig(headless=True)
            run_config = CrawlerRunConfig(cache_mode=CacheMode.BYPASS)

            async with AsyncWebCrawler(config=browser_config) as crawler:
                result = await crawler.arun(url=url, config=run_config)

            if not result.success:
                raise ExtractorError(f"Crawl4AI failed for {url}: {result.error_message}")

            # Prefer fit_markdown, fall back to plain markdown
            content_markdown: str = ""
            if result.markdown:
                if hasattr(result.markdown, "fit_markdown") and result.markdown.fit_markdown:
                    content_markdown = result.markdown.fit_markdown
                elif hasattr(result.markdown, "__str__"):
                    content_markdown = str(result.markdown)

            # Also try direct string attribute
            if not content_markdown and hasattr(result, "fit_markdown") and result.fit_markdown:
                content_markdown = result.fit_markdown

            quality = _calc_quality(content_markdown)
            status = "success" if quality > 0.0 else "low_quality"

            return ExtractResult(
                raw_item_id=raw_item_id,
                extractor="crawl4ai",
                status=status,
                content_markdown=content_markdown,
                quality_score=quality,
            )
        except (ExtractorUnavailableError, ExtractorError):
            raise
        except Exception as exc:
            raise ExtractorError(f"Crawl4AI extraction failed: {exc}") from exc
