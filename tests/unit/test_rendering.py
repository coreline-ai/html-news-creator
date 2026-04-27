"""Unit tests for Phase 5 rendering components."""
from __future__ import annotations
import pytest
import unittest.mock as mock
from unittest.mock import AsyncMock, patch

from app.rendering.html_sanitizer import HTMLSanitizer, _BLEACH_AVAILABLE
from app.rendering.playwright_renderer import PlaywrightRenderer, PlaywrightUnavailableError


# ---------------------------------------------------------------------------
# TC-5.1: <script> tag is stripped, safe <p> is kept
#
# bleach.clean(strip=True) removes the <script>...</script> tags themselves
# but retains inner text as inert plain text — the executable element is gone.
# The fallback (no bleach) uses re.sub which also strips the tag+content.
# Either way, the <script> element must not be present.
# ---------------------------------------------------------------------------
def test_sanitize_script_stripped():
    sanitizer = HTMLSanitizer()
    result = sanitizer.sanitize("<script>alert(1)</script><p>Hello</p>")
    # The opening/closing script tags must be gone (no executable element)
    assert "<script>" not in result
    assert "</script>" not in result
    # The safe paragraph content must survive
    assert "Hello" in result


# ---------------------------------------------------------------------------
# TC-5.2: javascript: href is blocked
# ---------------------------------------------------------------------------
def test_sanitize_javascript_href_blocked():
    sanitizer = HTMLSanitizer()
    result = sanitizer.sanitize('<a href="javascript:alert(1)">click</a>')
    # The dangerous href must not appear in the output
    assert "javascript:" not in result.lower()
    # The link text or element may still be present in some form, but the
    # dangerous attribute value must be gone


# ---------------------------------------------------------------------------
# TC-5.3: data: src on img is blocked
# ---------------------------------------------------------------------------
def test_sanitize_data_src_blocked():
    sanitizer = HTMLSanitizer()
    result = sanitizer.sanitize('<img src="data:image/png;base64,abc">')
    # The data: src must be removed or neutralized
    assert "data:image/png" not in result


# ---------------------------------------------------------------------------
# TC-5.4: Empty string input returns empty string
# ---------------------------------------------------------------------------
def test_sanitize_empty_string():
    sanitizer = HTMLSanitizer()
    assert sanitizer.sanitize("") == ""


# ---------------------------------------------------------------------------
# TC-5.5: sanitize_url blocks javascript: scheme
# ---------------------------------------------------------------------------
def test_sanitize_url_javascript_blocked():
    sanitizer = HTMLSanitizer()
    assert sanitizer.sanitize_url("javascript:alert(1)") == "#"


# ---------------------------------------------------------------------------
# TC-5.6: sanitize_url passes safe https URL unchanged
# ---------------------------------------------------------------------------
def test_sanitize_url_safe_passthrough():
    sanitizer = HTMLSanitizer()
    assert sanitizer.sanitize_url("https://openai.com") == "https://openai.com"


# ---------------------------------------------------------------------------
# TC-5.7: PlaywrightRenderer raises PlaywrightUnavailableError when
#         playwright is not installed (we simulate by patching the module)
# ---------------------------------------------------------------------------
def test_playwright_unavailable_raises(monkeypatch):
    # Simulate playwright not being importable
    renderer = PlaywrightRenderer()
    renderer._playwright_module = None  # force "not installed" state

    with pytest.raises(PlaywrightUnavailableError):
        import asyncio
        asyncio.run(renderer.screenshot("dummy.html", "dummy.png"))


# ---------------------------------------------------------------------------
# TC-5.8: GenerativeHTMLRenderer.render() with mocked OpenAI — returns a
#         string and strips any <script> tags from the LLM output
# ---------------------------------------------------------------------------
@pytest.mark.asyncio
async def test_generative_html_render_mocked():
    from app.rendering.generative_html import GenerativeHTMLRenderer

    fake_html = (
        "<!DOCTYPE html><html><body>"
        "<script>evil()</script>"
        "<h1>AI 트렌드 리포트</h1>"
        "</body></html>"
    )

    renderer = GenerativeHTMLRenderer()

    with patch("app.rendering.generative_html.chat", new=AsyncMock(return_value=fake_html)):
        result = await renderer.render(
            report={"title": "Test", "report_date": "2026-04-27"},
            sections=[],
        )

    # Must return a non-empty string
    assert isinstance(result, str)
    assert len(result) > 0
    # script tags must be stripped
    assert "<script>" not in result
    assert "evil()" not in result
    # safe content must still be present
    assert "AI 트렌드 리포트" in result
