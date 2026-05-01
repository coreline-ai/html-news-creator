from __future__ import annotations

import asyncio
from datetime import datetime, timezone
from typing import Any

import httpx

from app.collectors.base import BaseCollector, CollectedItem
from app.utils.http_timeouts import COLLECTOR_TIMEOUT
from app.utils.logger import get_logger
from app.utils.url_utils import canonicalize_url, url_hash

logger = get_logger(step="collect")

_HN_API_BASE = "https://hacker-news.firebaseio.com/v0"
_HN_ITEM_URL = "https://news.ycombinator.com/item?id={id}"
_USER_AGENT = "html-news-creator/1.0"


def _normalize_keywords(value: Any) -> list[str]:
    if value is None:
        return []
    if isinstance(value, str):
        return [part.strip().lower() for part in value.split(",") if part.strip()]
    if isinstance(value, (list, tuple, set)):
        return [str(part).strip().lower() for part in value if str(part).strip()]
    return []


class HackerNewsCollector(BaseCollector):
    """Collects top Hacker News stories via the public Firebase API."""

    def __init__(self, source: dict) -> None:
        self.source = source
        self.source_id: str = source.get("name", "Hacker News")
        self.keywords: list[str] = _normalize_keywords(source.get("keywords"))
        self.max_items: int = int(source.get("max_items", 20))
        self.max_candidates: int = int(source.get("max_candidates", 100))
        self.min_score: int = int(source.get("min_score", 0))
        self.concurrency: int = max(1, int(source.get("concurrency", 10)))

    def _get_json(self, url: str) -> Any | None:
        try:
            response = httpx.get(
                url,
                timeout=COLLECTOR_TIMEOUT,
                follow_redirects=True,
                headers={"User-Agent": _USER_AGENT},
            )
            response.raise_for_status()
            return response.json()
        except Exception as exc:
            logger.warning("hackernews_fetch_failed", source=self.source_id, url=url, error=str(exc))
            return None

    def _matches_keywords(self, item: dict[str, Any], url: str) -> bool:
        if not self.keywords:
            return True
        haystack = " ".join(
            str(item.get(field) or "") for field in ("title", "text")
        )
        haystack = f"{haystack} {url}".lower()
        return any(keyword in haystack for keyword in self.keywords)

    def _item_to_collected(
        self,
        item: dict[str, Any],
        date_from: datetime,
        date_to: datetime,
    ) -> CollectedItem | None:
        hn_id = item.get("id")
        if hn_id is None:
            logger.warning("hackernews_invalid_item", source=self.source_id, reason="missing_id")
            return None

        title = str(item.get("title") or "").strip()
        if not title:
            logger.warning("hackernews_invalid_item", source=self.source_id, id=hn_id, reason="missing_title")
            return None

        score = int(item.get("score") or 0)
        if score < self.min_score:
            return None

        url = str(item.get("url") or "").strip() or _HN_ITEM_URL.format(id=hn_id)
        if not self._matches_keywords(item, url):
            return None

        published_at = None
        raw_time = item.get("time")
        if raw_time is not None:
            try:
                published_at = datetime.fromtimestamp(int(raw_time), tz=timezone.utc)
            except Exception:
                logger.warning("hackernews_invalid_time", source=self.source_id, id=hn_id, time=raw_time)

        if published_at is not None and (published_at < date_from or published_at > date_to):
            return None

        canonical = canonicalize_url(url)
        return CollectedItem(
            source_id=self.source_id,
            source_type="website",
            title=title,
            url=url,
            canonical_url=canonical,
            canonical_url_hash=url_hash(url),
            raw_text=item.get("text") or title,
            author=item.get("by") or None,
            published_at=published_at,
            metrics_json={"score": score},
            raw_json={
                "hn_id": hn_id,
                "by": item.get("by"),
                "score": score,
                "time": raw_time,
                "text": item.get("text"),
                "url": item.get("url"),
            },
        )

    async def collect(self, date_from: datetime, date_to: datetime) -> list[CollectedItem]:
        top_story_ids = self._get_json(f"{_HN_API_BASE}/topstories.json")
        if not isinstance(top_story_ids, list):
            logger.warning("hackernews_invalid_topstories", source=self.source_id)
            return []

        items: list[CollectedItem] = []
        semaphore = asyncio.Semaphore(self.concurrency)

        async def _fetch_story(story_id: int) -> tuple[int, Any | None]:
            async with semaphore:
                raw_item = await asyncio.to_thread(
                    self._get_json,
                    f"{_HN_API_BASE}/item/{story_id}.json",
                )
                return story_id, raw_item

        story_results = await asyncio.gather(
            *[_fetch_story(story_id) for story_id in top_story_ids[: self.max_candidates]]
        )

        for story_id, raw_item in story_results:
            if not isinstance(raw_item, dict):
                logger.warning("hackernews_invalid_item", source=self.source_id, id=story_id)
                continue

            collected = self._item_to_collected(raw_item, date_from, date_to)
            if collected:
                items.append(collected)
            if len(items) >= self.max_items:
                break

        logger.info("hackernews_collected", source=self.source_id, count=len(items))
        return items
