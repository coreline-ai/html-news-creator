from __future__ import annotations

from datetime import datetime, timezone

import httpx
import pytest

from app.collectors.base import CollectedItem
from app.collectors.hackernews_collector import HackerNewsCollector

_DATE_FROM = datetime(2026, 4, 27, 0, 0, 0, tzinfo=timezone.utc)
_DATE_TO = datetime(2026, 4, 27, 23, 59, 59, tzinfo=timezone.utc)
_HN_TIME = int(datetime(2026, 4, 27, 12, 0, 0, tzinfo=timezone.utc).timestamp())


class FakeResponse:
    def __init__(self, payload, status_code: int = 200) -> None:
        self.payload = payload
        self.status_code = status_code

    def raise_for_status(self) -> None:
        if self.status_code >= 400:
            request = httpx.Request("GET", "https://example.com")
            response = httpx.Response(self.status_code, request=request)
            raise httpx.HTTPStatusError("error", request=request, response=response)

    def json(self):
        return self.payload


def _source(**overrides) -> dict:
    source = {"name": "Hacker News", "keywords": [], "max_items": 10, "max_candidates": 10}
    source.update(overrides)
    return source


def _story(story_id: int, **overrides) -> dict:
    story = {
        "id": story_id,
        "title": f"AI story {story_id}",
        "url": f"https://example.com/story/{story_id}",
        "by": "pg",
        "score": 123,
        "time": _HN_TIME,
        "text": "A useful AI discussion",
    }
    story.update(overrides)
    return story


def _fake_get_factory(payloads: dict[str, object]):
    def fake_get(url: str, **_kwargs):
        payload = payloads[url]
        if isinstance(payload, Exception):
            raise payload
        if isinstance(payload, tuple):
            return FakeResponse(payload[0], status_code=payload[1])
        return FakeResponse(payload)

    return fake_get


@pytest.mark.asyncio
async def test_hackernews_collector_collects_top_stories(monkeypatch):
    monkeypatch.setattr(
        "app.collectors.hackernews_collector.httpx.get",
        _fake_get_factory(
            {
                "https://hacker-news.firebaseio.com/v0/topstories.json": [1, 2],
                "https://hacker-news.firebaseio.com/v0/item/1.json": _story(1),
                "https://hacker-news.firebaseio.com/v0/item/2.json": _story(2, url=""),
            }
        ),
    )

    items = await HackerNewsCollector(_source()).collect(_DATE_FROM, _DATE_TO)

    assert len(items) == 2
    assert all(isinstance(item, CollectedItem) for item in items)
    assert all(item.source_type == "website" for item in items)
    assert items[0].title == "AI story 1"
    assert items[0].author == "pg"
    assert items[0].metrics_json["score"] == 123
    assert items[0].published_at == datetime(2026, 4, 27, 12, 0, 0, tzinfo=timezone.utc)
    assert items[1].url == "https://news.ycombinator.com/item?id=2"


@pytest.mark.asyncio
async def test_hackernews_collector_filters_by_keywords(monkeypatch):
    monkeypatch.setattr(
        "app.collectors.hackernews_collector.httpx.get",
        _fake_get_factory(
            {
                "https://hacker-news.firebaseio.com/v0/topstories.json": [1, 2, 3],
                "https://hacker-news.firebaseio.com/v0/item/1.json": _story(1, title="SQLite performance tips"),
                "https://hacker-news.firebaseio.com/v0/item/2.json": _story(2, text="Postgres query planner notes"),
                "https://hacker-news.firebaseio.com/v0/item/3.json": _story(3, url="https://example.com/python"),
            }
        ),
    )

    items = await HackerNewsCollector(_source(keywords=["postgres", "python"])).collect(_DATE_FROM, _DATE_TO)

    assert [item.title for item in items] == ["AI story 2", "AI story 3"]


@pytest.mark.asyncio
async def test_hackernews_collector_filters_by_min_score(monkeypatch):
    monkeypatch.setattr(
        "app.collectors.hackernews_collector.httpx.get",
        _fake_get_factory(
            {
                "https://hacker-news.firebaseio.com/v0/topstories.json": [1, 2],
                "https://hacker-news.firebaseio.com/v0/item/1.json": _story(1, score=49),
                "https://hacker-news.firebaseio.com/v0/item/2.json": _story(2, score=50),
            }
        ),
    )

    items = await HackerNewsCollector(_source(min_score=50)).collect(_DATE_FROM, _DATE_TO)

    assert [item.raw_json["hn_id"] for item in items] == [2]


@pytest.mark.asyncio
async def test_hackernews_collector_returns_empty_list_on_http_failure(monkeypatch):
    monkeypatch.setattr(
        "app.collectors.hackernews_collector.httpx.get",
        _fake_get_factory(
            {
                "https://hacker-news.firebaseio.com/v0/topstories.json": httpx.TimeoutException("timeout"),
            }
        ),
    )

    items = await HackerNewsCollector(_source()).collect(_DATE_FROM, _DATE_TO)

    assert items == []
