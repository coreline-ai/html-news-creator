"""Unit tests for Phase 5 rendering components."""
from __future__ import annotations
from pathlib import Path
import pytest
from unittest.mock import AsyncMock, patch

from app.rendering.html_sanitizer import HTMLSanitizer
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


@pytest.mark.asyncio
async def test_playwright_pdf_uses_screen_media_and_print_background(tmp_path):
    html_path = tmp_path / "report.html"
    html_path.write_text("<html><body>report</body></html>", encoding="utf-8")
    pdf_path = tmp_path / "report.pdf"
    calls: dict[str, object] = {}

    class FakePage:
        async def goto(self, url):
            calls["goto"] = url

        async def wait_for_load_state(self, state):
            calls["load_state"] = state

        async def emulate_media(self, media):
            calls["media"] = media

        async def evaluate(self, script):
            calls["evaluate"] = script

        async def pdf(self, **kwargs):
            calls["pdf"] = kwargs
            Path(kwargs["path"]).write_bytes(b"%PDF-1.4 fake")

    class FakeBrowser:
        async def new_page(self):
            return FakePage()

        async def close(self):
            calls["closed"] = True

    class FakeChromium:
        async def launch(self, headless=True):
            calls["headless"] = headless
            return FakeBrowser()

    class FakePlaywright:
        chromium = FakeChromium()

    class FakeAsyncPlaywright:
        async def __aenter__(self):
            return FakePlaywright()

        async def __aexit__(self, *_args):
            return None

    renderer = PlaywrightRenderer()
    renderer._playwright_module = lambda: FakeAsyncPlaywright()

    result = await renderer.export_pdf(str(html_path), str(pdf_path))

    assert result == pdf_path
    assert pdf_path.read_bytes().startswith(b"%PDF")
    assert calls["media"] == "screen"
    assert calls["load_state"] == "networkidle"
    assert calls["headless"] is True
    assert calls["closed"] is True
    assert "document.fonts" in str(calls["evaluate"])
    assert calls["pdf"] == {
        "path": str(pdf_path),
        "format": "A4",
        "print_background": True,
        "margin": {
            "top": "12mm",
            "right": "10mm",
            "bottom": "12mm",
            "left": "10mm",
        },
    }


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
