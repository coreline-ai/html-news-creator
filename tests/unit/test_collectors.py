"""
Unit tests for Phase 1-A collectors.

TC-1.1  RSSCollector returns 10 CollectedItems when feedparser returns 10 entries.
TC-1.2  RSSCollector detects duplicate URLs via canonical_url_hash.
TC-1.3  ArxivCollector returns 1 item when arxiv.Client.results returns 1 result.
TC-1.E1 RSSCollector returns empty list (no exception) when feedparser always raises.
"""
from __future__ import annotations

import calendar as _cal
import time
from datetime import date, datetime, timezone
from types import SimpleNamespace
from unittest.mock import MagicMock, patch

import httpx
import pytest

from app.collectors.rss_collector import RSSCollector
from app.collectors.arxiv_collector import ArxivCollector
from app.collectors.base import CollectedItem
from app.collectors.github_collector import GitHubCollector
from app.collectors.hackernews_collector import HackerNewsCollector
from app.collectors.naver_news_collector import NaverNewsCollector
from app.collectors.orchestrator import CollectorOrchestrator

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

_TODAY = datetime(2026, 4, 27, tzinfo=timezone.utc)
_DATE_FROM = datetime(2026, 4, 27, 0, 0, 0, tzinfo=timezone.utc)
_DATE_TO = datetime(2026, 4, 27, 23, 59, 59, tzinfo=timezone.utc)

# time.struct_time for 2026-04-27 12:00 UTC, built via calendar so it is
# unambiguously UTC (calendar.timegm is the inverse of time.gmtime).
_PUBLISHED_UTC_TS = _cal.timegm((2026, 4, 27, 12, 0, 0, 0, 0, 0))
_PUBLISHED_STRUCT = time.gmtime(_PUBLISHED_UTC_TS)


def _make_rss_source(url: str = "https://example.com/feed.xml") -> dict:
    return {"name": "Test Feed", "source_type": "rss", "url": url, "trust_level": "official"}


def _make_feed_entry(url: str, title: str = "Test Title") -> dict:
    """Return a minimal feedparser-style entry dict."""
    return {
        "link": url,
        "title": title,
        "published_parsed": _PUBLISHED_STRUCT,
        "summary": "Entry summary text",
        "author": "Test Author",
        "id": url,
        "tags": [],
    }


def _make_fake_feed(entries: list[dict]) -> MagicMock:
    feed = MagicMock()
    feed.get = lambda key, default=None: entries if key == "entries" else default
    feed.__getitem__ = lambda self, key: entries if key == "entries" else [][0]
    return feed


# ---------------------------------------------------------------------------
# TC-1.1: RSS returns 10 items
# ---------------------------------------------------------------------------

@pytest.mark.asyncio
async def test_rss_collector_returns_ten_items():
    """TC-1.1: feedparser returns 10 entries → RSSCollector.collect returns 10 CollectedItems."""
    entries = [_make_feed_entry(f"https://example.com/post/{i}") for i in range(10)]

    fake_feed = MagicMock()
    fake_feed.get = lambda key, default=None: entries if key == "entries" else default

    source = _make_rss_source()
    collector = RSSCollector(source)

    with patch("app.collectors.rss_collector.feedparser.parse", return_value=fake_feed):
        items = await collector.collect(_DATE_FROM, _DATE_TO)

    assert len(items) == 10
    assert all(isinstance(item, CollectedItem) for item in items)
    assert all(item.source_type == "rss" for item in items)


# ---------------------------------------------------------------------------
# TC-1.2: Duplicate URL detected via canonical_url_hash
# ---------------------------------------------------------------------------

@pytest.mark.asyncio
async def test_rss_collector_duplicate_hash():
    """TC-1.2: Two entries with the same URL produce the same canonical_url_hash."""
    url = "https://example.com/post/1?utm_source=twitter"
    entries = [
        _make_feed_entry(url, title="First"),
        _make_feed_entry(url, title="Second (duplicate)"),
    ]

    fake_feed = MagicMock()
    fake_feed.get = lambda key, default=None: entries if key == "entries" else default

    source = _make_rss_source()
    collector = RSSCollector(source)

    with patch("app.collectors.rss_collector.feedparser.parse", return_value=fake_feed):
        items = await collector.collect(_DATE_FROM, _DATE_TO)

    assert len(items) == 2
    # Both items must share the same canonical_url_hash (UTM params stripped)
    assert items[0].canonical_url_hash == items[1].canonical_url_hash
    # And their canonical_url should be the same (stripped of UTM params)
    assert items[0].canonical_url == items[1].canonical_url


@pytest.mark.asyncio
async def test_rss_collector_preserves_feed_image_url():
    """RSS media image candidates must survive into raw_json for report cards."""
    image_url = "https://example.com/images/hero.jpg"
    entry = _make_feed_entry("https://example.com/post/with-image")
    entry["media_thumbnail"] = [{"url": image_url}]

    fake_feed = MagicMock()
    fake_feed.get = lambda key, default=None: [entry] if key == "entries" else default

    source = _make_rss_source()
    collector = RSSCollector(source)

    with patch("app.collectors.rss_collector.feedparser.parse", return_value=fake_feed):
        items = await collector.collect(_DATE_FROM, _DATE_TO)

    assert len(items) == 1
    assert items[0].raw_json["image_url"] == image_url


@pytest.mark.asyncio
async def test_rss_collector_preserves_youtube_video_id():
    """YouTube RSS video id should survive into raw_json for rendering hints."""
    entry = _make_feed_entry("https://www.youtube.com/watch?v=abc123", "YouTube demo")
    entry["yt_videoid"] = "abc123"

    fake_feed = MagicMock()
    fake_feed.get = lambda key, default=None: [entry] if key == "entries" else default

    collector = RSSCollector(_make_rss_source("https://www.youtube.com/feeds/videos.xml"))

    with patch("app.collectors.rss_collector.feedparser.parse", return_value=fake_feed):
        items = await collector.collect(_DATE_FROM, _DATE_TO)

    assert len(items) == 1
    assert items[0].raw_json["video_id"] == "abc123"


@pytest.mark.asyncio
async def test_rss_collector_falls_back_to_httpx_bytes_when_url_parse_has_no_entries():
    """Some valid feeds parse only after fetching bytes with a normal UA."""
    entry = _make_feed_entry("https://example.com/fallback-feed")

    bozo_feed = MagicMock()
    bozo_feed.get = lambda key, default=None: {
        "bozo": True,
        "entries": [],
        "bozo_exception": ValueError("syntax error"),
    }.get(key, default)

    parsed_feed = MagicMock()
    parsed_feed.get = lambda key, default=None: [entry] if key == "entries" else default

    def fake_httpx_get(url, **_kwargs):
        return httpx.Response(
            200,
            content=b"<?xml version='1.0'?><rss><channel></channel></rss>",
            request=httpx.Request("GET", url),
        )

    source = _make_rss_source("https://example.com/feed-needs-httpx.xml")
    collector = RSSCollector(source)

    with patch(
        "app.collectors.rss_collector.feedparser.parse",
        side_effect=[bozo_feed, parsed_feed],
    ), patch("app.collectors.rss_collector.httpx.get", side_effect=fake_httpx_get):
        items = await collector.collect(_DATE_FROM, _DATE_TO)

    assert [item.url for item in items] == ["https://example.com/fallback-feed"]


@pytest.mark.asyncio
async def test_rss_collector_uses_source_timeout_for_httpx_byte_fallback():
    """source.timeout should be used when feedparser URL parsing needs httpx byte fallback."""
    entry = _make_feed_entry("https://example.com/timeout-feed")

    bozo_feed = MagicMock()
    bozo_feed.get = lambda key, default=None: {
        "bozo": True,
        "entries": [],
        "bozo_exception": ValueError("syntax error"),
    }.get(key, default)

    parsed_feed = MagicMock()
    parsed_feed.get = lambda key, default=None: [entry] if key == "entries" else default

    seen_timeouts = []

    def fake_httpx_get(url, **kwargs):
        seen_timeouts.append(kwargs.get("timeout"))
        return httpx.Response(
            200,
            content=b"<?xml version='1.0'?><rss><channel></channel></rss>",
            request=httpx.Request("GET", url),
        )

    source = {**_make_rss_source("https://example.com/feed.xml"), "timeout": 7}
    collector = RSSCollector(source)

    with patch(
        "app.collectors.rss_collector.feedparser.parse",
        side_effect=[bozo_feed, parsed_feed],
    ), patch("app.collectors.rss_collector.httpx.get", side_effect=fake_httpx_get):
        items = await collector.collect(_DATE_FROM, _DATE_TO)

    assert [item.url for item in items] == ["https://example.com/timeout-feed"]
    # The httpx.get fallback now wraps the per-source timeout in an
    # ``httpx.Timeout`` so connect/read are bounded — preventing the 5/1
    # indefinite-read hang sample. The overall budget still tracks the
    # configured ``timeout: 7``.
    assert len(seen_timeouts) == 1
    forwarded = seen_timeouts[0]
    assert isinstance(forwarded, httpx.Timeout)
    assert forwarded.read == 7.0
    assert forwarded.connect is not None and forwarded.connect <= 7.0


@pytest.mark.asyncio
async def test_rss_collector_tries_fallback_url_when_primary_fetch_fails():
    """fallback_url should be collected when the primary feed cannot be fetched."""
    entry = _make_feed_entry("https://example.com/from-fallback")
    fallback_feed = MagicMock()
    fallback_feed.get = lambda key, default=None: [entry] if key == "entries" else default

    source = {
        **_make_rss_source("https://example.com/primary.xml"),
        "fallback_url": "https://example.com/fallback.xml",
    }
    collector = RSSCollector(source)
    collector._fetch_feed_for_url = MagicMock(side_effect=[RuntimeError("down"), fallback_feed])

    items = await collector.collect(_DATE_FROM, _DATE_TO)

    assert [item.url for item in items] == ["https://example.com/from-fallback"]
    assert collector._fetch_feed_for_url.call_args_list[0].args == ("https://example.com/primary.xml",)
    assert collector._fetch_feed_for_url.call_args_list[1].args == ("https://example.com/fallback.xml",)


@pytest.mark.asyncio
async def test_rss_collector_returns_empty_when_primary_and_fallback_fail():
    """If both primary and fallback feeds fail, collect should keep returning []."""
    source = {
        **_make_rss_source("https://example.com/primary.xml"),
        "fallback_url": "https://example.com/fallback.xml",
    }
    collector = RSSCollector(source)
    collector._fetch_feed_for_url = MagicMock(side_effect=[RuntimeError("down"), RuntimeError("also down")])

    items = await collector.collect(_DATE_FROM, _DATE_TO)

    assert items == []


@pytest.mark.asyncio
async def test_rss_collector_ai_filter_keeps_only_ai_related_entries():
    """ai_filter should filter by default AI keywords plus source keywords."""
    ai_entry = _make_feed_entry("https://example.com/openai-release", "OpenAI releases new model")
    custom_keyword_entry = _make_feed_entry("https://example.com/robotics-update", "Automation update")
    custom_keyword_entry["content"] = [{"value": "New robotics benchmark results were published."}]
    non_ai_entry = _make_feed_entry("https://example.com/garden-update", "Gardening tips")
    non_ai_entry["summary"] = "Spring planting guide for vegetables."

    fake_feed = MagicMock()
    fake_feed.get = lambda key, default=None: [
        ai_entry,
        custom_keyword_entry,
        non_ai_entry,
    ] if key == "entries" else default

    source = {**_make_rss_source(), "ai_filter": True, "keywords": ["robotics"]}
    collector = RSSCollector(source)

    with patch("app.collectors.rss_collector.feedparser.parse", return_value=fake_feed):
        items = await collector.collect(_DATE_FROM, _DATE_TO)

    assert [item.url for item in items] == [
        "https://example.com/openai-release",
        "https://example.com/robotics-update",
    ]


def test_collector_orchestrator_date_window_uses_configured_timezone(monkeypatch):
    """2026-04-28 KST should query 2026-04-27 15:00 UTC onward."""
    from app.config import settings

    monkeypatch.setattr(settings, "timezone", "Asia/Seoul")

    date_from, date_to = CollectorOrchestrator()._date_window_utc(date(2026, 4, 28))

    from app.pipeline.date_window import _SLACK_HOURS_AFTER, _SLACK_HOURS_BEFORE

    # KST midnight = 15:00 UTC; window starts SLACK_HOURS_BEFORE hours earlier
    assert date_from == datetime(2026, 4, 27, 15 - _SLACK_HOURS_BEFORE, 0, 0, tzinfo=timezone.utc)
    assert date_to == datetime(
        2026, 4, 28, 14 + _SLACK_HOURS_AFTER, 59, 59, 999999, tzinfo=timezone.utc
    )


def test_collector_orchestrator_uses_github_anonymous_fallback(monkeypatch):
    """GitHub source should not be skipped when anonymous fallback is enabled."""
    from app.config import settings

    monkeypatch.setattr(settings, "github_token", "")
    monkeypatch.setattr(settings, "github_allow_unauthenticated", True)

    collector = CollectorOrchestrator()._make_collector(
        {"name": "GitHub openai", "source_type": "github", "org": "openai"}
    )

    assert isinstance(collector, GitHubCollector)


def test_collector_orchestrator_can_disable_github_anonymous_fallback(monkeypatch):
    from app.config import settings

    monkeypatch.setattr(settings, "github_token", "")
    monkeypatch.setattr(settings, "github_allow_unauthenticated", False)

    collector = CollectorOrchestrator()._make_collector(
        {"name": "GitHub openai", "source_type": "github", "org": "openai"}
    )

    assert collector is None


def test_collector_orchestrator_routes_hackernews_collector_type():
    """Special collectors use collector_type while keeping DB-safe source_type."""
    collector = CollectorOrchestrator()._make_collector(
        {
            "name": "Hacker News AI",
            "source_type": "website",
            "collector_type": "hackernews",
            "keywords": ["ai"],
        }
    )

    assert isinstance(collector, HackerNewsCollector)


def test_collector_orchestrator_routes_naver_news_collector_type():
    """NAVER Search API source must not require a new source_type enum value."""
    collector = CollectorOrchestrator()._make_collector(
        {
            "name": "NAVER AI News",
            "source_type": "website",
            "collector_type": "naver_news",
            "query": "AI",
        }
    )

    assert isinstance(collector, NaverNewsCollector)


# ---------------------------------------------------------------------------
# TC-1.3: ArxivCollector returns 1 item
# ---------------------------------------------------------------------------

@pytest.mark.asyncio
async def test_arxiv_collector_returns_one_item():
    """TC-1.3: arxiv.Client.results returns 1 result → ArxivCollector.collect returns 1 item."""

    class FakeAuthor:
        name = "Alice Researcher"

    fake_result = SimpleNamespace(
        entry_id="https://arxiv.org/abs/2604.12345",
        title="A Groundbreaking AI Paper",
        summary="This paper introduces a new approach to ...",
        published=datetime(2026, 4, 27, 10, 0, 0, tzinfo=timezone.utc),
        authors=[FakeAuthor()],
        categories=["cs.AI"],
        pdf_url="https://arxiv.org/pdf/2604.12345",
        doi=None,
        get_short_id=lambda: "2604.12345",
    )

    source = {
        "name": "arXiv cs.AI",
        "source_type": "arxiv",
        "category": "cs.AI",
        "trust_level": "official",
    }
    collector = ArxivCollector(source)

    with patch("app.collectors.arxiv_collector.arxiv.Client") as MockClient:
        mock_client_instance = MagicMock()
        mock_client_instance.results.return_value = iter([fake_result])
        MockClient.return_value = mock_client_instance

        items = await collector.collect(_DATE_FROM, _DATE_TO)

    assert len(items) == 1
    item = items[0]
    assert isinstance(item, CollectedItem)
    assert item.source_type == "arxiv"
    assert item.title == "A Groundbreaking AI Paper"
    assert item.raw_text == "This paper introduces a new approach to ..."
    assert item.author == "Alice Researcher"


# ---------------------------------------------------------------------------
# TC-1.E1: RSSCollector swallows exception after 3 retries
# ---------------------------------------------------------------------------

@pytest.mark.asyncio
async def test_rss_collector_exception_returns_empty_list():
    """TC-1.E1: feedparser raises an exception every time → collect returns [] (no re-raise)."""
    source = _make_rss_source()
    collector = RSSCollector(source)

    call_count = 0

    def always_raise(*args, **kwargs):
        nonlocal call_count
        call_count += 1
        raise ConnectionError("Network error")

    # Patch feedparser.parse to always raise, and override tenacity retry to
    # exhaust immediately (wait=0, attempts=3).
    with patch("app.collectors.rss_collector.feedparser.parse", side_effect=always_raise):
        # Re-bind tenacity retry with zero wait so the test doesn't sleep 10 s.
        from tenacity import retry, stop_after_attempt, wait_fixed

        @retry(wait=wait_fixed(0), stop=stop_after_attempt(3), reraise=False)
        def patched_fetch(self_inner):
            return always_raise()

        original_fetch = RSSCollector._fetch_feed
        RSSCollector._fetch_feed = patched_fetch
        try:
            items = await collector.collect(_DATE_FROM, _DATE_TO)
        finally:
            RSSCollector._fetch_feed = original_fetch

    assert items == []
    assert call_count == 3  # called exactly 3 times (1 attempt + 2 retries)
