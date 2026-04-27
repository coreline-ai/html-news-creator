from __future__ import annotations
from datetime import datetime
from app.collectors.base import BaseCollector, CollectedItem
from app.utils.url_utils import canonicalize_url, url_hash
from app.utils.logger import get_logger


class XCollectorUnavailableError(Exception):
    pass


class XCollector(BaseCollector):
    """
    X/Twitter collector using twikit library.
    Only active when x_enabled=True in settings.
    """

    SEARCH_QUERIES = [
        "AI model release lang:en",
        "LLM announcement lang:en",
        "artificial intelligence breakthrough lang:en",
        "machine learning paper lang:en",
        "OpenAI OR Anthropic OR Google DeepMind announcement lang:en",
    ]

    def __init__(self, source: dict):
        self.source = source
        self.logger = get_logger(step="collect")
        self._client = None

    async def _ensure_client(self):
        from app.config import settings
        if not settings.x_enabled:
            raise XCollectorUnavailableError("X/Twitter collection disabled (x_enabled=False)")
        try:
            import twikit
            # Note: twikit requires cookie-based auth or developer account
            # This is a stub — full auth setup requires X developer credentials
            self._client = twikit
        except ImportError:
            raise XCollectorUnavailableError("twikit not installed")

    async def collect(self, date_from: datetime, date_to: datetime) -> list[CollectedItem]:
        try:
            await self._ensure_client()
        except XCollectorUnavailableError as e:
            self.logger.info("x_collector_skipped", reason=str(e))
            return []

        items: list[CollectedItem] = []
        # Stub implementation — full twikit integration requires API auth
        # Real implementation would:
        # 1. client.search_tweet(query, "Latest") for each SEARCH_QUERIES entry
        # 2. Filter by date_from/date_to
        # 3. Filter by min engagement (retweet_count + like_count >= 100)
        # 4. Convert to CollectedItem with source_type="x"
        self.logger.info("x_collect_stub", note="Full impl requires twikit auth setup")
        return items
