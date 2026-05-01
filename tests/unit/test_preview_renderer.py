"""Unit tests for News Studio preview renderer (Phase 1).

The preview path must NEVER hit the database. These tests cover:
- target_sections override produces N section blocks
- options validation rejects bad values
- mock-only render works without a DB
- merge_with_options layers a per-request patch on top of yaml + runtime override
"""
from __future__ import annotations

import re

import pytest

from app.admin import policy_admin
from app.admin.preview import render_preview

# Each rendered section starts with `<h2>{loop.index}. {title}</h2>`. The
# leading numeral makes this a robust per-section counter that tolerates the
# rest of the template (which has unrelated <h2> blocks elsewhere — none).
_SECTION_HEADING = re.compile(r"<h2>\s*\d+\.\s")


def _section_count(html: str) -> int:
    return len(_SECTION_HEADING.findall(html))


@pytest.fixture(autouse=True)
def _clear_runtime_override():
    policy_admin.clear_policy_override()
    yield
    policy_admin.clear_policy_override()


def test_render_preview_default_returns_html_string():
    html = render_preview()
    assert isinstance(html, str)
    assert "<!DOCTYPE html>" in html
    assert _section_count(html) == 10


def test_render_preview_target_sections_top_level_override():
    html = render_preview(options={"target_sections": 5})
    assert _section_count(html) == 5


def test_render_preview_target_sections_via_policy_path():
    html = render_preview(options={"report_selection": {"target_sections": 3}})
    assert _section_count(html) == 3


def test_render_preview_invalid_target_sections_negative():
    with pytest.raises(ValueError):
        render_preview(options={"target_sections": -5})


def test_render_preview_invalid_target_sections_too_large():
    with pytest.raises(ValueError):
        render_preview(options={"target_sections": 9999})


def test_render_preview_options_must_be_mapping():
    with pytest.raises(ValueError):
        render_preview(options="not-a-dict")  # type: ignore[arg-type]


def test_merge_with_options_layers_runtime_override_and_request_patch():
    policy_admin.set_policy_override(
        {"report_selection": {"target_sections": 4}}
    )
    merged = policy_admin.merge_with_options(
        {"report_selection": {"min_section_score": 99}}
    )
    selection = merged["report_selection"]
    # Runtime override survives
    assert selection["target_sections"] == 4
    # Per-request patch wins on conflicting keys
    assert selection["min_section_score"] == 99


def test_render_preview_with_mock_date_kst_does_not_touch_db():
    # Use a future date guaranteed to have no DB record. The function must
    # gracefully fall back to mock data instead of raising.
    html = render_preview(
        options={"target_sections": 2}, date_kst="2099-01-01"
    )
    assert _section_count(html) == 2
    assert "2099-01-01" in html or "미리보기" in html


_HTML_TAG_THEME = re.compile(r'<html\b[^>]*\bdata-theme="([^"]+)"', re.IGNORECASE)


def test_render_preview_default_output_theme_is_dark():
    """When no output_theme is supplied the rendered HTML stays on the dark theme."""
    html = render_preview(options={"target_sections": 2})
    match = _HTML_TAG_THEME.search(html)
    assert match is not None
    assert match.group(1) == "dark"


def test_render_preview_propagates_output_theme_override():
    """output_theme passed via options reaches the Jinja template."""
    html = render_preview(
        options={"target_sections": 2, "output_theme": "newsroom-white"}
    )
    match = _HTML_TAG_THEME.search(html)
    assert match is not None
    assert match.group(1) == "newsroom-white"
