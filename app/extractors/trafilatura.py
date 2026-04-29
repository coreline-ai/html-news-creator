from __future__ import annotations

import asyncio

from app.config import settings
from app.extractors.base import (
    BaseExtractor,
    ExtractResult,
    ExtractorError,
    ExtractorUnavailableError,
)
from app.utils.logger import get_logger
from app.utils.source_images import (
    extract_representative_image_from_html,
    extract_content_images_from_html,
)


def _calc_quality(content: str) -> float:
    return min(1.0, len(content) / 2000)


class TrafilaturaExtractor(BaseExtractor):
    def __init__(self) -> None:
        self._enabled = settings.trafilatura_enabled
        self.logger = get_logger(step="extract")

    def _extract_sync(self, url: str) -> ExtractResult:
        try:
            import httpx
            import trafilatura
        except ImportError as exc:
            raise ExtractorUnavailableError(f"Required package not installed: {exc}") from exc

        response = httpx.get(url, timeout=30, follow_redirects=True)
        response.raise_for_status()
        html = response.text

        content_text: str = trafilatura.extract(
            html, include_comments=False, output_format="txt"
        ) or ""
        content_markdown: str = trafilatura.extract(
            html, include_comments=False, output_format="markdown"
        ) or ""

        base_url = str(response.url)
        og_image_url = extract_representative_image_from_html(html, base_url)
        content_image_urls = extract_content_images_from_html(html, base_url, max_images=5)

        quality = _calc_quality(content_text or content_markdown)
        status = "success" if quality > 0.0 else "low_quality"

        return ExtractResult(
            raw_item_id="",  # filled in by caller
            extractor="trafilatura",
            status=status,
            content_text=content_text,
            content_markdown=content_markdown,
            quality_score=quality,
            og_image_url=og_image_url,
            content_image_urls=content_image_urls,
        )

    async def extract(self, url: str, raw_item_id: str = "") -> ExtractResult:
        if not self._enabled:
            raise ExtractorUnavailableError("Trafilatura is disabled in configuration")

        try:
            result = await asyncio.to_thread(self._extract_sync, url)
            result.raw_item_id = raw_item_id
            return result
        except (ExtractorUnavailableError, ExtractorError):
            raise
        except Exception as exc:
            raise ExtractorError(f"Trafilatura extraction failed: {exc}") from exc
