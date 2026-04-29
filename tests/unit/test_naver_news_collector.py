from __future__ import annotations

from datetime import datetime, timezone

import httpx
import pytest

from app.collectors.naver_news_collector import NaverNewsCollector
from app.config import settings

_DATE_FROM = datetime(2026, 4, 27, 0, 0, tzinfo=timezone.utc)
_DATE_TO = datetime(2026, 4, 28, 23, 59, 59, tzinfo=timezone.utc)


def _response(url: str, payload: dict | None = None, status_code: int = 200) -> httpx.Response:
    return httpx.Response(
        status_code,
        json=payload if payload is not None else {},
        request=httpx.Request("GET", url),
    )


@pytest.mark.asyncio
async def test_naver_news_collector_skips_without_credentials(monkeypatch):
    called = False

    def fake_get(*args, **kwargs):
        nonlocal called
        called = True
        raise AssertionError("httpx.get should not be called without credentials")

    monkeypatch.setattr(settings, "naver_client_id", "")
    monkeypatch.setattr(settings, "naver_client_secret", "")
    monkeypatch.setattr("app.collectors.naver_news_collector.httpx.get", fake_get)

    collector = NaverNewsCollector({"name": "NAVER AI", "query": "AI"})
    items = await collector.collect(_DATE_FROM, _DATE_TO)

    assert items == []
    assert called is False


@pytest.mark.asyncio
async def test_naver_news_collector_collects_items(monkeypatch):
    captured: dict = {}

    def fake_get(url, **kwargs):
        captured["url"] = url
        captured["params"] = kwargs["params"]
        captured["headers"] = kwargs["headers"]
        return _response(
            url,
            {
                "items": [
                    {
                        "title": "OpenAI releases model",
                        "originallink": "https://example.com/news/openai-model?utm_source=naver",
                        "link": "https://n.news.naver.com/article/001/0000000001",
                        "description": "Model release details",
                        "pubDate": "Tue, 28 Apr 2026 10:30:00 +0900",
                    }
                ]
            },
        )

    monkeypatch.setattr("app.collectors.naver_news_collector.httpx.get", fake_get)

    collector = NaverNewsCollector(
        {
            "name": "NAVER AI",
            "query": "OpenAI",
            "max_items": 5,
            "sort": "sim",
            "client_id": "client-id",
            "client_secret": "client-secret",
        }
    )
    items = await collector.collect(_DATE_FROM, _DATE_TO)

    assert len(items) == 1
    item = items[0]
    assert item.source_id == "NAVER AI"
    assert item.source_type == "website"
    assert item.title == "OpenAI releases model"
    assert item.url == "https://example.com/news/openai-model?utm_source=naver"
    assert item.canonical_url == "https://example.com/news/openai-model"
    assert item.raw_text == "Model release details"
    assert item.published_at == datetime(2026, 4, 28, 1, 30, tzinfo=timezone.utc)
    assert item.raw_json["provider"] == "naver_news"
    assert item.raw_json["link"] == "https://n.news.naver.com/article/001/0000000001"
    assert captured["url"] == "https://openapi.naver.com/v1/search/news.json"
    assert captured["params"] == {"query": "OpenAI", "display": 5, "start": 1, "sort": "sim"}
    assert captured["headers"]["X-Naver-Client-Id"] == "client-id"
    assert captured["headers"]["X-Naver-Client-Secret"] == "client-secret"


@pytest.mark.asyncio
async def test_naver_news_collector_strips_html_from_title_and_description(monkeypatch):
    def fake_get(url, **kwargs):
        return _response(
            url,
            {
                "items": [
                    {
                        "title": "<b>OpenAI</b> &amp; NAVER",
                        "originallink": "https://example.com/news/html",
                        "link": "https://n.news.naver.com/article/001/0000000002",
                        "description": "AI &amp; <b>news</b> update",
                        "pubDate": "Tue, 28 Apr 2026 11:00:00 +0900",
                    }
                ]
            },
        )

    monkeypatch.setattr("app.collectors.naver_news_collector.httpx.get", fake_get)

    collector = NaverNewsCollector(
        {
            "keywords": ["AI"],
            "client_id": "client-id",
            "client_secret": "client-secret",
        }
    )
    items = await collector.collect(_DATE_FROM, _DATE_TO)

    assert len(items) == 1
    assert items[0].title == "OpenAI & NAVER"
    assert items[0].raw_text == "AI & news update"
    assert items[0].raw_json["title"] == "OpenAI & NAVER"
    assert items[0].raw_json["description"] == "AI & news update"


@pytest.mark.asyncio
async def test_naver_news_collector_returns_empty_on_http_failure(monkeypatch):
    def fake_get(url, **kwargs):
        return _response(url, {"errorMessage": "invalid"}, status_code=500)

    monkeypatch.setattr("app.collectors.naver_news_collector.httpx.get", fake_get)

    collector = NaverNewsCollector(
        {"query": "AI", "client_id": "client-id", "client_secret": "client-secret"}
    )
    items = await collector.collect(_DATE_FROM, _DATE_TO)

    assert items == []
