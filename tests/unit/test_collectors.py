"""
Unit tests for Phase 1-A collectors.

TC-1.1  RSSCollector returns 10 CollectedItems when feedparser returns 10 entries.
TC-1.2  RSSCollector detects duplicate URLs via canonical_url_hash.
TC-1.3  ArxivCollector returns 1 item when arxiv.Client.results returns 1 result.
TC-1.E1 RSSCollector returns empty list (no exception) when feedparser always raises.
"""
from __future__ import annotations

import time
from datetime import datetime, timezone
from types import SimpleNamespace
from unittest.mock import MagicMock, patch

import pytest

from app.collectors.rss_collector import RSSCollector
from app.collectors.arxiv_collector import ArxivCollector
from app.collectors.base import CollectedItem

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

_TODAY = datetime(2026, 4, 27, tzinfo=timezone.utc)
_DATE_FROM = datetime(2026, 4, 27, 0, 0, 0, tzinfo=timezone.utc)
_DATE_TO = datetime(2026, 4, 27, 23, 59, 59, tzinfo=timezone.utc)

# time.struct_time for 2026-04-27 12:00 UTC, built via calendar so it is
# unambiguously UTC (calendar.timegm is the inverse of time.gmtime).
import calendar as _cal
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
