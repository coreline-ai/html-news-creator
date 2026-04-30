from __future__ import annotations

from app.extractors.base import (
    BaseExtractor,
    ExtractResult,
    ExtractorError,
    ExtractorUnavailableError,
    SSRFBlockedError,
)
from app.extractors.firecrawl import FirecrawlExtractor
from app.extractors.crawl4ai import Crawl4AIExtractor
from app.extractors.trafilatura import TrafilaturaExtractor
from app.utils.url_utils import is_ssrf_blocked
from app.utils.logger import get_logger


class ExtractorOrchestrator:
    def __init__(self):
        self.extractors: list[BaseExtractor] = [
            FirecrawlExtractor(),
            Crawl4AIExtractor(),
            TrafilaturaExtractor(),
        ]
        self.logger = get_logger(step="extract")

    async def extract(self, url: str, raw_item_id: str = "") -> ExtractResult:
        # 1. SSRF check
        if is_ssrf_blocked(url):
            raise SSRFBlockedError(f"SSRF blocked: {url}")

        # 2. Try each extractor in order (fallback chain)
        last_error = None
        for extractor in self.extractors:
            try:
                result = await extractor.extract(url, raw_item_id)
                if result.status == "success" and result.quality_score > 0.1:
                    self.logger.info("extract_success", extractor=result.extractor, url=url)
                    return result
            except ExtractorUnavailableError:
                continue  # skip, try next
            except ExtractorError as e:
                last_error = str(e)
                self.logger.warning(
                    "extractor_failed",
                    extractor=type(extractor).__name__,
                    url=url,
                    error=str(e),
                )
                continue

        # 3. All extractors failed — add to manual queue (Redis lpush)
        # For now, just log and return failed result
        self.logger.error("all_extractors_failed", url=url, last_error=last_error)
        return ExtractResult(
            raw_item_id=raw_item_id,
            extractor="none",
            status="failed",
            error=last_error or "all extractors failed",
        )
