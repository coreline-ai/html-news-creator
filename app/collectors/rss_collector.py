from __future__ import annotations

import calendar
import re
import socket
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
from typing import Any
from urllib.parse import parse_qs, urlparse

import feedparser
import httpx
from tenacity import retry, stop_after_attempt, wait_fixed

from app.collectors.base import BaseCollector, CollectedItem
from app.utils.http_timeouts import COLLECTOR_TIMEOUT
from app.utils.logger import get_logger
from app.utils.source_images import extract_representative_image_from_feed_entry
from app.utils.url_utils import canonicalize_url, url_hash

logger = get_logger(step="collect")

_FEED_TIMEOUT = 30  # seconds
_USER_AGENT = "html-news-creator/1.0"
_DEFAULT_AI_KEYWORDS = (
    "ai",
    "artificial intelligence",
    "machine learning",
    "deep learning",
    "generative ai",
    "genai",
    "llm",
    "large language model",
    "openai",
    "anthropic",
    "deepmind",
    "neural",
    "transformer",
    "agent",
)


def _normalize_keywords(value: Any) -> list[str]:
    if value is None:
        return []
    if isinstance(value, str):
        return [part.strip().lower() for part in value.split(",") if part.strip()]
    if isinstance(value, (list, tuple, set)):
        return [str(part).strip().lower() for part in value if str(part).strip()]
    return []


def _normalize_timeout(value: Any) -> float:
    try:
        timeout = float(value)
    except (TypeError, ValueError):
        return float(_FEED_TIMEOUT)
    return timeout if timeout > 0 else float(_FEED_TIMEOUT)


def _entry_text(entry: dict, field: str) -> str:
    val = entry.get(field)
    if isinstance(val, list):
        return " ".join(str(part.get("value", "")) for part in val if isinstance(part, dict))
    if isinstance(val, str):
        return val
    return ""


def _entry_tags(entry: dict) -> list[str]:
    return [
        str(t.get("term"))
        for t in entry.get("tags", [])
        if isinstance(t, dict) and t.get("term")
    ]


def _entry_video_id(entry: dict, url: str) -> str:
    """Return a YouTube video id from feedparser fields or the entry URL."""
    for key in ("yt_videoid", "yt_video_id", "video_id"):
        value = entry.get(key)
        if value:
            return str(value)

    entry_id = str(entry.get("id") or "")
    if entry_id.startswith("yt:video:"):
        return entry_id.rsplit(":", 1)[-1]

    parsed = urlparse(url)
    host = parsed.netloc.lower()
    if "youtube.com" in host:
        return parse_qs(parsed.query).get("v", [""])[0]
    if "youtu.be" in host:
        return parsed.path.strip("/").split("/", 1)[0]
    return ""


def _keyword_matches(haystack: str, keyword: str) -> bool:
    if keyword.isalnum():
        return re.search(rf"\b{re.escape(keyword)}\b", haystack) is not None
    return keyword in haystack


def _parse_feed_url(url: str, timeout: float) -> feedparser.FeedParserDict:
    previous_timeout = socket.getdefaulttimeout()
    try:
        socket.setdefaulttimeout(timeout)
        return feedparser.parse(
            url,
            request_headers={"Connection": "close", "User-Agent": _USER_AGENT},
        )
    finally:
        socket.setdefaulttimeout(previous_timeout)


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
        self.fallback_url: str | None = source.get("fallback_url") or None
        self.max_items: int | None = source.get("max_items")
        self.timeout: float = _normalize_timeout(source.get("timeout", _FEED_TIMEOUT))
        self.ai_filter: bool = bool(source.get("ai_filter"))
        self.ai_keywords: list[str] = list(_DEFAULT_AI_KEYWORDS) + _normalize_keywords(
            source.get("keywords")
        )

    @retry(wait=wait_fixed(5), stop=stop_after_attempt(3), reraise=False)
    def _fetch_feed_for_url(self, url: str) -> feedparser.FeedParserDict:
        feed = _parse_feed_url(url, self.timeout)
        if feed.get("bozo") and not feed.get("entries"):
            # Some feeds serve bytes that feedparser's URL opener fails to
            # decode, while the same content parses cleanly when fetched with a
            # normal HTTP client. Keep this narrow fallback so malformed or
            # truly unavailable feeds still fail after retries.
            response = httpx.get(
                url,
                timeout=httpx.Timeout(
                    self.timeout,
                    connect=min(self.timeout, COLLECTOR_TIMEOUT.connect or self.timeout),
                ),
                follow_redirects=True,
                headers={"User-Agent": _USER_AGENT},
            )
            response.raise_for_status()
            feed = feedparser.parse(response.content)
        if feed.get("bozo") and not feed.get("entries"):
            raise ValueError(f"Bozo feed with no entries: {feed.get('bozo_exception')}")
        return feed

    def _fetch_feed(self) -> feedparser.FeedParserDict:
        try:
            return self._fetch_feed_for_url(self.url)
        except Exception as primary_exc:
            if not self.fallback_url:
                raise
            logger.warning(
                "rss_primary_fetch_failed_trying_fallback",
                source=self.source_id,
                url=self.url,
                fallback_url=self.fallback_url,
                error=str(primary_exc),
            )
            return self._fetch_feed_for_url(self.fallback_url)

    def _matches_ai_filter(self, entry: dict, url: str) -> bool:
        if not self.ai_filter:
            return True
        haystack = " ".join(
            [
                str(entry.get("title") or ""),
                _entry_text(entry, "summary"),
                _entry_text(entry, "content"),
                url,
                " ".join(_entry_tags(entry)),
            ]
        ).lower()
        return any(_keyword_matches(haystack, keyword) for keyword in self.ai_keywords)

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

                if not self._matches_ai_filter(entry, raw_url):
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
                image_url = extract_representative_image_from_feed_entry(entry)

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
                        "tags": _entry_tags(entry),
                        "image_url": image_url,
                        "video_id": _entry_video_id(entry, raw_url),
                    },
                )
                items.append(item)
                if self.max_items and len(items) >= self.max_items:
                    break

            except Exception as exc:
                logger.warning("rss_entry_parse_failed", source=self.source_id, error=str(exc))

        logger.info("rss_collected", source=self.source_id, count=len(items))
        return items
