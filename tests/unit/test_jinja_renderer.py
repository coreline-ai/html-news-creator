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


# TC-1.7: XSS prevention
def test_xss_prevention():
    renderer = make_renderer()
    report = make_report(title="<script>alert(1)</script>")
    html = renderer.render_report(report, sections=[])
    assert "<script>" not in html
    assert "&lt;script&gt;" in html


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
