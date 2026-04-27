from __future__ import annotations

from app.config import settings
from app.extractors.base import (
    BaseExtractor,
    ExtractResult,
    ExtractorError,
    ExtractorUnavailableError,
)
from app.utils.logger import get_logger


def _calc_quality(content_markdown: str) -> float:
    return min(1.0, len(content_markdown) / 2000)


class FirecrawlExtractor(BaseExtractor):
    def __init__(self) -> None:
        self._api_key = settings.firecrawl_api_key
        self.logger = get_logger(step="extract")

    async def extract(self, url: str, raw_item_id: str = "") -> ExtractResult:
        if not self._api_key:
            raise ExtractorUnavailableError("Firecrawl API key is not configured")

        try:
            from firecrawl import FirecrawlApp

            app = FirecrawlApp(api_key=self._api_key)
            response = app.scrape_url(url, formats=["markdown"])

            # firecrawl-py returns a ScrapeResponse object; access attributes directly
            content_markdown: str = ""
            title: str | None = None

            if hasattr(response, "markdown") and response.markdown:
                content_markdown = response.markdown or ""
            if hasattr(response, "metadata") and response.metadata:
                title = response.metadata.get("title")

            quality = _calc_quality(content_markdown)
            status = "success" if quality > 0.0 else "low_quality"

            return ExtractResult(
                raw_item_id=raw_item_id,
                extractor="firecrawl",
                status=status,
                title=title,
                content_markdown=content_markdown,
                quality_score=quality,
            )
        except (ExtractorUnavailableError, ImportError):
            raise
        except Exception as exc:
            raise ExtractorError(f"Firecrawl extraction failed: {exc}") from exc
