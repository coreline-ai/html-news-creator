"""Unit tests for JinjaRenderer (Phase 1-C)."""
from __future__ import annotations
import os
import pytest
import jinja2
from app.rendering.jinja_renderer import JinjaRenderer

# Resolve templates directory relative to this test file
TEMPLATES_DIR = os.path.join(os.path.dirname(__file__), "../../templates")


def make_renderer() -> JinjaRenderer:
    return JinjaRenderer(templates_dir=TEMPLATES_DIR)


def make_report(**overrides) -> dict:
    base = {
        "title": "AI 트렌드 리포트",
        "report_date": "2026-04-27",
        "summary_ko": "오늘의 요약입니다.",
        "created_at": "2026-04-27 09:00",
        "stats": {
            "total_sources": 0,
            "ai_relevant": 0,
            "clusters": 0,
            "verified": 0,
        },
    }
    base.update(overrides)
    return base


# TC-1.7: XSS prevention — user-supplied summary_ko must be HTML-escaped.
# The template contains legitimate inline <script> blocks, so we check that
# injected content is escaped, not that the page has zero script tags.
def test_xss_prevention():
    renderer = make_renderer()
    report = make_report(summary_ko="<script>alert(1)</script>")
    html = renderer.render_report(report, sections=[])
    assert "&lt;script&gt;alert(1)&lt;/script&gt;" in html


# TC-1.8: Stats appear in footer
def test_stats_in_footer():
    renderer = make_renderer()
    report = make_report(stats={
        "total_sources": 42,
        "ai_relevant": 10,
        "clusters": 3,
        "verified": 5,
    })
    html = renderer.render_report(report, sections=[])
    assert "42" in html


# TC-1.9: Empty sections renders without error and shows empty-state message
def test_empty_sections():
    renderer = make_renderer()
    report = make_report()
    html = renderer.render_report(report, sections=[])
    assert "오늘 수집된" in html


# TC-1.E1: Missing template file raises TemplateNotFound
def test_missing_template_raises():
    renderer = make_renderer()
    with pytest.raises(jinja2.TemplateNotFound):
        renderer.env.get_template("nonexistent_template.html.j2")


def test_youtube_section_renders_play_overlay():
    renderer = make_renderer()
    section = {
        "title": "영상 뉴스",
        "summary_ko": "요약",
        "content_image_urls": ["https://i.ytimg.com/vi/abc123/hqdefault.jpg"],
        "og_image_url": "",
        "sources_json": [
            {
                "name": "YouTube",
                "url": "https://www.youtube.com/watch?v=abc123",
                "video_id": "abc123",
            }
        ],
    }

    html = renderer.render_report(make_report(), sections=[section])

    # Template uses .yt-play class (CSS ::after triangle) for the play button.
    assert 'class="yt-play"' in html


def test_regular_image_section_does_not_render_play_overlay():
    renderer = make_renderer()
    section = {
        "title": "일반 뉴스",
        "summary_ko": "요약",
        "content_image_urls": ["https://example.com/news/photo.jpg"],
        "og_image_url": "",
        "sources_json": [
            {"name": "Example", "url": "https://example.com/news/story"},
        ],
    }

    html = renderer.render_report(make_report(), sections=[section])

    assert "youtube-play-overlay" not in html


def test_newsroom_white_theme_is_available_without_replacing_existing_themes():
    renderer = make_renderer()
    html = renderer.render_report(make_report(), sections=[])

    assert '[data-theme="dark"]' in html
    assert '[data-theme="newsroom-white"]' in html
    assert "ico-newsroom" in html
    assert "var themes = ['light', 'dark', 'newsroom-white'];" in html
    assert "뉴스룸 화이트로 전환" in html
    assert "기본 라이트 모드로 전환" in html
