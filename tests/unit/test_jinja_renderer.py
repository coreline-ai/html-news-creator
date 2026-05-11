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


def test_signal_briefing_output_style_uses_briefing_template():
    renderer = make_renderer()
    html = renderer.render_report(
        make_report(
            stats={
                "total_sources": 3,
                "ai_relevant": 3,
                "clusters": 1,
                "verified": 1,
                "top_keywords": ["Claude", "tooling"],
                "main_event": "개발자 도구 신호 확대",
                "today_temperature": ["개발자 도구 섹션이 강했습니다."],
                "action_items": ["원문 릴리스 노트를 확인하세요."],
            }
        ),
        sections=[
            {
                "title": "Claude Code와 개발자 도구 신호가 확대",
                "fact_summary": "공식 릴리스와 커뮤니티 반응이 함께 관찰됐습니다.",
                "importance_score": 0.8,
                "key_updates": ["CLI 사용 사례 증가", "커뮤니티 논의 확산"],
                "tags": ["tooling"],
                "sources_json": [],
            }
        ],
        output_style="signal_briefing",
    )

    assert "<!DOCTYPE html>" in html
    assert "Signal Briefing" in html
    assert "Hyperstudio Terminal Ops" in html
    assert "font-size: 2.2em;" in html
    assert "h1 { font-size: 1.7em; }" in html
    assert ".metric span { color: var(--muted); font-size: 12px;" in html
    assert "핵심 기류" in html
    assert "후속 체크포인트" in html


def test_signal_briefing_supports_hyperstudio_white_theme_toggle():
    renderer = make_renderer()
    html = renderer.render_report(
        make_report(),
        sections=[],
        output_style="signal_briefing",
        output_theme="newsroom-white",
    )

    assert 'data-theme="newsroom-white"' in html
    assert "visual_theme=hyperstudio-terminal-ops" in html
    assert '[data-theme="dark"]' in html
    assert '[data-theme="newsroom-white"]' in html
    assert "ico-newsroom" in html
    assert "var themes = ['light', 'dark', 'newsroom-white'];" in html
    assert "뉴스룸 화이트로 전환" in html
    assert "기본 라이트 모드로 전환" in html


def test_signal_briefing_defaults_to_hyperstudio_visual_theme():
    renderer = make_renderer()
    html = renderer.render_report(
        make_report(),
        sections=[],
        output_style="signal_briefing",
    )

    assert 'data-visual-theme="hyperstudio_terminal_ops"' in html
    assert "visual_theme=hyperstudio-terminal-ops" in html
    assert "visual_theme_id=hyperstudio_terminal_ops" in html


def test_signal_briefing_visual_theme_presets_render_data_attribute():
    renderer = make_renderer()
    template = renderer.env.get_template("report_signal_briefing.html.j2")
    visual_themes = [
        "linear_command_center",
        "anthropic_research_journal",
        "cursor_warm_studio",
        "hyperstudio_terminal_ops",
        "mercury_twilight_console",
    ]

    for visual_theme in visual_themes:
        html = template.render(
            report=make_report(),
            sections=[],
            output_theme="dark",
            output_style="signal_briefing",
            visual_theme=visual_theme,
        )

        assert f'data-visual-theme="{visual_theme}"' in html
        assert f"visual_theme_id={visual_theme}" in html


def test_signal_briefing_visual_theme_presets_define_distinct_tokens():
    renderer = make_renderer()
    html = renderer.render_report(
        make_report(),
        sections=[],
        output_style="signal_briefing",
    )

    assert '[data-visual-theme="linear_command_center"]' in html
    assert '[data-visual-theme="anthropic_research_journal"]' in html
    assert '[data-visual-theme="cursor_warm_studio"]' in html
    assert '[data-visual-theme="hyperstudio_terminal_ops"]' in html
    assert '[data-visual-theme="mercury_twilight_console"]' in html
    assert "--visual-grid-size: 28px;" in html
    assert "--font-heading: Georgia, 'Times New Roman', serif;" in html
    assert "--radius: 18px;" in html
    assert "--visual-image-filter: saturate(.7) contrast(1.15) brightness(.72) hue-rotate(8deg);" in html
