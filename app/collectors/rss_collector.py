from __future__ import annotations

import calendar
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime

import feedparser
from tenacity import retry, stop_after_attempt, wait_fixed

from app.collectors.base import BaseCollector, CollectedItem
from app.utils.logger import get_logger
from app.utils.url_utils import canonicalize_url, url_hash

logger = get_logger(step="collect")

_FEED_TIMEOUT = 30  # seconds


def _parse_entry_datetime(entry: dict) -> datetime | None:
    """Try to parse a published/updated timestamp from a feedparser entry."""
    # feedparser provides published_parsed / updated_parsed as time.struct_time (UTC)
    for attr in ("published_parsed", "updated_parsed"):
        parsed = entry.get(attr)
        if parsed is not None:
            try:
                ts = calendar.timegm(parsed)
                return datetime.fromtimestamp(ts, tz=timezone.utc)
            except Exception:
                pass

    # Fallback: parse the raw string
    for attr in ("published", "updated"):
        raw = entry.get(attr)
        if raw:
            try:
                return parsedate_to_datetime(raw).astimezone(timezone.utc)
            except Exception:
                pass

    return None


class RSSCollector(BaseCollector):
    """Collects items from an RSS/Atom feed."""

    def __init__(self, source: dict) -> None:
        self.source = source
        self.source_id: str = source.get("name", source.get("url", ""))
        self.url: str = source["url"]

    @retry(wait=wait_fixed(5), stop=stop_after_attempt(3), reraise=False)
    def _fetch_feed(self) -> feedparser.FeedParserDict:
        feed = feedparser.parse(self.url, request_headers={"Connection": "close"})
        if feed.get("bozo") and not feed.get("entries"):
            raise ValueError(f"Bozo feed with no entries: {feed.get('bozo_exception')}")
        return feed

    async def collect(self, date_from: datetime, date_to: datetime) -> list[CollectedItem]:
        try:
            feed = self._fetch_feed()
        except Exception as exc:
            logger.error("rss_fetch_failed", source=self.source_id, error=str(exc))
            return []

        items: list[CollectedItem] = []
        for entry in feed.get("entries", []):
            try:
                raw_url: str = entry.get("link") or entry.get("id") or ""
                if not raw_url:
                    continue

                title: str = entry.get("title", "").strip()
                published_at = _parse_entry_datetime(entry)

                # Date filtering — only include entries within the window when we
                # can determine a publication date.
                if published_at is not None:
                    if published_at < date_from or published_at > date_to:
                        continue

                canonical = canonicalize_url(raw_url)
                canon_hash = url_hash(raw_url)

                # Extract plain text / summary
                raw_text: str | None = None
                for field in ("summary", "content"):
                    val = entry.get(field)
                    if isinstance(val, list) and val:
                        raw_text = val[0].get("value", "")
                        break
                    elif isinstance(val, str) and val:
                        raw_text = val
                        break

                author: str | None = entry.get("author") or None

                item = CollectedItem(
                    source_id=self.source_id,
                    source_type="rss",
                    title=title,
                    url=raw_url,
                    canonical_url=canonical,
                    canonical_url_hash=canon_hash,
                    raw_text=raw_text,
                    author=author,
                    published_at=published_at,
                    raw_json={
                        "id": entry.get("id"),
                        "tags": [t.get("term") for t in entry.get("tags", [])],
                    },
                )
                items.append(item)

            except Exception as exc:
                logger.warning("rss_entry_parse_failed", source=self.source_id, error=str(exc))

        logger.info("rss_collected", source=self.source_id, count=len(items))
        return items
