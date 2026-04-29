from __future__ import annotations

from datetime import datetime, timezone

import httpx
import pytest

from app.collectors.website_collector import WebsiteCollector


def _response(url: str, text: str, status_code: int = 200) -> httpx.Response:
    return httpx.Response(
        status_code,
        text=text,
        request=httpx.Request("GET", url),
    )


@pytest.mark.asyncio
async def test_website_collector_collects_from_sitemap(monkeypatch):
    sitemap_url = "https://www.anthropic.com/sitemap.xml"
    article_url = "https://www.anthropic.com/news/example-ai-news"
    image_url = "https://www.anthropic.com/image.png"

    sitemap_xml = f"""<?xml version="1.0" encoding="UTF-8"?>
    <urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
      <url>
        <loc>{article_url}</loc>
        <lastmod>2026-04-28T02:00:00Z</lastmod>
      </url>
    </urlset>
    """
    article_html = f"""
    <html><head>
      <meta property="og:title" content="Anthropic AI News"/>
      <meta property="og:description" content="Official update"/>
      <meta property="og:image" content="{image_url}"/>
      <meta property="article:published_time" content="2026-04-28T02:00:00Z"/>
    </head></html>
    """

    def fake_get(url, **kwargs):
        if url == sitemap_url:
            return _response(url, sitemap_xml)
        if url == article_url:
            return _response(url, article_html)
        raise AssertionError(f"unexpected url: {url}")

    monkeypatch.setattr("app.collectors.website_collector.httpx.get", fake_get)

    collector = WebsiteCollector(
        {
            "name": "Anthropic News",
            "source_type": "website",
            "url": "https://www.anthropic.com/news",
            "sitemap_url": sitemap_url,
            "include_url_patterns": ["https://www.anthropic.com/news/"],
        }
    )
    items = await collector.collect(
        datetime(2026, 4, 27, 15, tzinfo=timezone.utc),
        datetime(2026, 4, 28, 14, 59, 59, tzinfo=timezone.utc),
    )

    assert len(items) == 1
    assert items[0].source_type == "website"
    assert items[0].title == "Anthropic AI News"
    assert items[0].raw_json["image_url"] == image_url


@pytest.mark.asyncio
async def test_website_collector_collects_from_listing(monkeypatch):
    listing_url = "https://ai.meta.com/blog/"
    article_url = "https://ai.meta.com/blog/example-meta-ai/"

    listing_html = f'<html><body><a href="{article_url}">Example</a></body></html>'
    article_html = """
    <html><head>
      <meta name="og:title" content="Meta AI Blog Post"/>
      <meta name="description" content="Meta official blog update"/>
      <meta property="og:image" content="/hero.jpg"/>
      <meta property="article:published_time" content="2026-04-08T00:00:00Z"/>
    </head></html>
    """

    def fake_get(url, **kwargs):
        if url == listing_url:
            return _response(url, listing_html)
        if url == article_url:
            return _response(url, article_html)
        raise AssertionError(f"unexpected url: {url}")

    monkeypatch.setattr("app.collectors.website_collector.httpx.get", fake_get)

    collector = WebsiteCollector(
        {
            "name": "Meta AI Blog",
            "source_type": "website",
            "url": listing_url,
            "listing_url": listing_url,
            "include_url_patterns": ["https://ai.meta.com/blog/"],
        }
    )
    items = await collector.collect(
        datetime(2026, 4, 8, 0, tzinfo=timezone.utc),
        datetime(2026, 4, 8, 23, 59, 59, tzinfo=timezone.utc),
    )

    assert len(items) == 1
    assert items[0].title == "Meta AI Blog Post"
    assert items[0].raw_json["image_url"] == "https://ai.meta.com/hero.jpg"
