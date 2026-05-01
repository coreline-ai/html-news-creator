"""Unit tests — admin re-render image-evidence filtering.

Phase F bundle Y guarantees that section image evidence stored in the DB is
re-validated through ``app.utils.source_images.is_usable_representative_image_url``
before reaching the Jinja template. Operators (or the upstream collector)
occasionally accept journalist headshots, Reddit UI assets, or decorative
SVGs as "image evidence". These would otherwise leak into the published
HTML even though they are demonstrably unsuitable.

We test the filter at the boundary the renderer actually uses
(``_section_to_render_dict``) — patching the predicate so the cases stay
deterministic regardless of how the URL-classifier evolves.
"""
from __future__ import annotations

from unittest.mock import MagicMock, patch

import pytest

from app.admin.render import _section_to_render_dict


class _FakeSection:
    """Minimal stand-in mirroring the columns ``_section_to_render_dict`` reads."""

    def __init__(self, image_evidence: list[dict] | None) -> None:
        self.id = "stub"
        self.section_order = 0
        self.title = "T"
        self.lead = None
        self.fact_summary = "fact"
        self.social_signal_summary = None
        self.inference_summary = None
        self.caution = None
        self.image_evidence_json = image_evidence
        self.sources_json = []
        self.confidence = None
        self.importance_score = 1.0
        self.tags_json = []


# ---------------------------------------------------------------------------
# Cases
# ---------------------------------------------------------------------------

def test_render_image_filter_keeps_usable_content_url():
    """A single content image that passes the filter is preserved verbatim."""
    section = _FakeSection(
        [{"url": "https://cdn.example/photo.jpg", "source": "content"}]
    )
    fake_filter = MagicMock(return_value=True)
    with patch("app.admin.render.is_usable_representative_image_url", fake_filter):
        out = _section_to_render_dict(section)

    assert out["content_image_urls"] == ["https://cdn.example/photo.jpg"]
    fake_filter.assert_called_with("https://cdn.example/photo.jpg")


def test_render_image_filter_drops_unusable_content_url():
    """A single content image rejected by the filter is removed."""
    section = _FakeSection(
        [{"url": "https://reddit.com/static/icon.svg", "source": "content"}]
    )
    fake_filter = MagicMock(return_value=False)
    with patch("app.admin.render.is_usable_representative_image_url", fake_filter):
        out = _section_to_render_dict(section)

    assert out["content_image_urls"] == []
    # No og fallback either — the filter rejected everything.
    assert out["og_image_url"] == ""


def test_render_image_filter_handles_empty_evidence_list():
    """No image evidence at all → empty content list and empty fallback."""
    section = _FakeSection([])
    fake_filter = MagicMock(return_value=True)
    with patch("app.admin.render.is_usable_representative_image_url", fake_filter):
        out = _section_to_render_dict(section)

    assert out["content_image_urls"] == []
    assert out["og_image_url"] == ""
    fake_filter.assert_not_called()


def test_render_image_filter_partial_pass_keeps_only_usable():
    """A mixed list: only the URLs the filter approves survive."""
    section = _FakeSection(
        [
            {"url": "https://cdn.example/good.jpg", "source": "content"},
            {"url": "https://reddit.com/static/bad.svg", "source": "content"},
            {"url": "https://cdn.example/also-good.png", "source": "content"},
        ]
    )

    def _fake(url: str) -> bool:
        return "good" in url

    with patch(
        "app.admin.render.is_usable_representative_image_url",
        side_effect=_fake,
    ):
        out = _section_to_render_dict(section)

    assert out["content_image_urls"] == [
        "https://cdn.example/good.jpg",
        "https://cdn.example/also-good.png",
    ]


def test_render_image_filter_fallback_picks_first_usable_non_content():
    """When content images all fail but an og-style fallback is usable,
    ``og_image_url`` is populated from that entry — and only if it passes the
    filter. If both content and og candidates fail, both fields stay empty
    (the template's existing SVG fallback handles it downstream)."""
    section = _FakeSection(
        [
            {"url": "https://reddit.com/static/icon.svg", "source": "content"},
            {"url": "https://cdn.example/og-bad.svg", "source": "og"},
            {"url": "https://cdn.example/og-good.jpg", "source": "og"},
        ]
    )

    def _fake(url: str) -> bool:
        return url.endswith(".jpg")

    with patch(
        "app.admin.render.is_usable_representative_image_url",
        side_effect=_fake,
    ):
        out = _section_to_render_dict(section)

    # No content image passed.
    assert out["content_image_urls"] == []
    # Fallback chose the first usable non-content URL.
    assert out["og_image_url"] == "https://cdn.example/og-good.jpg"


# ---------------------------------------------------------------------------
# Defensive: filter rejects everything → fully empty (template will SVG-fallback)
# ---------------------------------------------------------------------------

def test_render_image_filter_all_rejected_yields_empty_fields():
    section = _FakeSection(
        [
            {"url": "x", "source": "content"},
            {"url": "y", "source": "og"},
        ]
    )
    with patch(
        "app.admin.render.is_usable_representative_image_url",
        return_value=False,
    ):
        out = _section_to_render_dict(section)

    assert out["content_image_urls"] == []
    assert out["og_image_url"] == ""
