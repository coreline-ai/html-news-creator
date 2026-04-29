from __future__ import annotations

import re
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
from html import unescape
from typing import Any

import httpx

from app.collectors.base import BaseCollector, CollectedItem
from app.config import settings
from app.utils.logger import get_logger
from app.utils.url_utils import canonicalize_url, url_hash

logger = get_logger(step="collect")

_NAVER_NEWS_SEARCH_URL = "https://openapi.naver.com/v1/search/news.json"
_DEFAULT_TIMEOUT = 15.0
_DEFAULT_MAX_ITEMS = 20
_MAX_DISPLAY = 100
_ALLOWED_SORTS = {"date", "sim"}
_TAG_RE = re.compile(r"<[^>]+>")


def _clean_html(value: Any) -> str:
    if value is None:
        return ""
    text = unescape(str(value))
    text = _TAG_RE.sub("", text)
    return re.sub(r"\s+", " ", text).strip()


def _parse_pub_date(value: str | None) -> datetime | None:
    if not value:
        return None
    try:
        parsed = parsedate_to_datetime(value)
    except (TypeError, ValueError):
        return None
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=timezone.utc)
    return parsed.astimezone(timezone.utc)


def _source_queries(source: dict) -> list[str]:
    query = source.get("query")
    if isinstance(query, str) and query.strip():
        return [query.strip()]

    keywords = source.get("keywords")
    if isinstance(keywords, str) and keywords.strip():
        return [keywords.strip()]
    if isinstance(keywords, (list, tuple)):
        return [str(keyword).strip() for keyword in keywords if str(keyword).strip()]
    return []


class NaverNewsCollector(BaseCollector):
    """Collects NAVER News Search API results as website CollectedItems."""

    def __init__(self, source: dict) -> None:
        self.source = source
        queries = _source_queries(source)
        self.source_id: str = source.get("name") or (queries[0] if queries else "naver_news")
        self.queries = queries
        self.max_items = int(source.get("max_items") or _DEFAULT_MAX_ITEMS)
        sort = source.get("sort", "date")
        self.sort = sort if sort in _ALLOWED_SORTS else "date"
        self.client_id = source.get("client_id") or settings.naver_client_id
        self.client_secret = source.get("client_secret") or settings.naver_client_secret

    def _fetch_results(self, query: str, display: int) -> list[dict]:
        response = httpx.get(
            _NAVER_NEWS_SEARCH_URL,
            params={"query": query, "display": display, "start": 1, "sort": self.sort},
            headers={
                "X-Naver-Client-Id": self.client_id,
                "X-Naver-Client-Secret": self.client_secret,
            },
            timeout=_DEFAULT_TIMEOUT,
        )
        response.raise_for_status()
        data = response.json()
        items = data.get("items") if isinstance(data, dict) else None
        if not isinstance(items, list):
            raise ValueError("NAVER response missing items list")
        return items

    def _item_from_result(
        self,
        result: dict,
        query: str,
        date_from: datetime,
        date_to: datetime,
    ) -> CollectedItem | None:
        raw_url = result.get("originallink") or result.get("link") or ""
        if not raw_url:
            return None

        published_at = _parse_pub_date(result.get("pubDate"))
        if published_at is not None and (published_at < date_from or published_at > date_to):
            return None

        title = _clean_html(result.get("title")) or raw_url
        description = _clean_html(result.get("description"))
        canonical = canonicalize_url(raw_url)

        return CollectedItem(
            source_id=self.source_id,
            source_type="website",
            title=title,
            url=raw_url,
            canonical_url=canonical,
            canonical_url_hash=url_hash(raw_url),
            raw_text=description or title,
            author=None,
            published_at=published_at,
            metrics_json={},
            raw_json={
                "provider": "naver_news",
                "query": query,
                "originallink": result.get("originallink"),
                "link": result.get("link"),
                "title": title,
                "description": description,
                "pubDate": result.get("pubDate"),
            },
        )

    async def collect(self, date_from: datetime, date_to: datetime) -> list[CollectedItem]:
        if not self.client_id or not self.client_secret:
            logger.warning("naver_news_credentials_missing", source=self.source_id)
            return []
        if not self.queries:
            logger.warning("naver_news_query_missing", source=self.source_id)
            return []

        items: list[CollectedItem] = []
        seen: set[str] = set()
        per_query_display = min(_MAX_DISPLAY, max(1, self.max_items))

        for query in self.queries:
            try:
                results = self._fetch_results(query, per_query_display)
            except Exception as exc:
                logger.warning(
                    "naver_news_fetch_failed",
                    source=self.source_id,
                    query=query,
                    error=str(exc),
                )
                return []

            for result in results:
                try:
                    item = self._item_from_result(result, query, date_from, date_to)
                except Exception as exc:
                    logger.warning(
                        "naver_news_item_parse_failed",
                        source=self.source_id,
                        query=query,
                        error=str(exc),
                    )
                    continue
                if item is None or item.canonical_url in seen:
                    continue
                seen.add(item.canonical_url)
                items.append(item)
                if len(items) >= self.max_items:
                    logger.info("naver_news_collected", source=self.source_id, count=len(items))
                    return items

        logger.info("naver_news_collected", source=self.source_id, count=len(items))
        return items
