from __future__ import annotations
from abc import ABC, abstractmethod
from dataclasses import dataclass


class ExtractorUnavailableError(Exception):
    """Raised when extractor is not configured/available."""


class ExtractorError(Exception):
    """Raised when extraction fails."""


class SSRFBlockedError(Exception):
    """Raised when URL is blocked by SSRF protection."""


@dataclass
class ExtractResult:
    raw_item_id: str
    extractor: str
    status: str  # success|low_quality|failed
    title: str | None = None
    description: str | None = None
    content_markdown: str = ""
    content_text: str = ""
    quality_score: float = 0.0  # 0~1, based on content length/structure/noise
    og_image_url: str = ""           # og:image 또는 twitter:image
    content_image_urls: list = None  # 본문 내 실제 콘텐츠 이미지 목록
    error: str | None = None

    def __post_init__(self):
        if self.content_image_urls is None:
            self.content_image_urls = []


class BaseExtractor(ABC):
    @abstractmethod
    async def extract(self, url: str, raw_item_id: str = "") -> ExtractResult:
        ...
