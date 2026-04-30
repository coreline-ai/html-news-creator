from __future__ import annotations

from types import SimpleNamespace

from app.extractors.base import ExtractResult
from scripts.run_daily import (
    _extract_result_metadata,
    _fallback_extract_result_from_raw_item,
    _is_access_blocked_error,
)


def test_fallback_extract_result_uses_rss_summary_text():
    raw_item = SimpleNamespace(
        id="item-1",
        source_type="rss",
        title="OpenAI official update",
        raw_text="Official RSS summary captured during collection.",
    )

    result = _fallback_extract_result_from_raw_item(
        raw_item,
        error="403 Forbidden: Cloudflare challenge",
    )

    assert result is not None
    assert result.extractor == "rss_summary_fallback"
    assert result.status == "low_quality"
    assert result.title == "OpenAI official update"
    assert result.content_text == raw_item.raw_text
    assert result.content_markdown == raw_item.raw_text
    assert result.quality_score > 0
    assert result.error == "403 Forbidden: Cloudflare challenge"


def test_fallback_extract_result_skips_empty_raw_text():
    raw_item = SimpleNamespace(
        id="item-2",
        source_type="rss",
        title="Empty item",
        raw_text="   ",
    )

    assert _fallback_extract_result_from_raw_item(raw_item, error="403") is None


def test_extract_result_metadata_marks_fallback_and_error():
    result = ExtractResult(
        raw_item_id="item-3",
        extractor="rss_summary_fallback",
        status="low_quality",
        content_text="summary",
        content_markdown="summary",
        quality_score=0.1,
        og_image_url="https://example.com/hero.jpg",
        content_image_urls=["https://example.com/body.jpg"],
        error="403 Forbidden",
    )

    metadata = _extract_result_metadata(result)

    assert metadata == {
        "og_image_url": "https://example.com/hero.jpg",
        "content_image_urls": ["https://example.com/body.jpg"],
        "extract_error": "403 Forbidden",
        "fallback": True,
        "fallback_source": "raw_item.raw_text",
    }


def test_access_blocked_error_detects_cloudflare_403():
    assert _is_access_blocked_error("403 Forbidden: Cloudflare challenge") is True
    assert _is_access_blocked_error("Enable JavaScript and cookies to continue") is True
    assert _is_access_blocked_error("temporary parse failure") is False
    assert _is_access_blocked_error(None) is False
