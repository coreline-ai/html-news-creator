from __future__ import annotations

from app.utils.source_images import (
    extract_representative_image_from_feed_entry,
    extract_representative_image_from_html,
)


def test_extract_representative_image_from_html_resolves_relative_og_image():
    html = '<html><head><meta property="og:image" content="/assets/hero.webp"></head></html>'

    image_url = extract_representative_image_from_html(
        html,
        "https://example.com/news/post",
    )

    assert image_url == "https://example.com/assets/hero.webp"


def test_extract_representative_image_from_feed_entry_uses_media_thumbnail():
    entry = {"media_thumbnail": [{"url": "https://example.com/thumb.png"}]}

    image_url = extract_representative_image_from_feed_entry(entry)

    assert image_url == "https://example.com/thumb.png"


def test_extract_representative_image_from_html_skips_logo_og_image():
    html = '<meta property="og:image" content="https://arxiv.org/static/arxiv-logo-fb.png">'

    image_url = extract_representative_image_from_html(html, "https://arxiv.org/abs/1")

    assert image_url == ""


def test_extract_representative_image_from_html_skips_reddit_static_image():
    html = """
    <meta property="og:image" content="https://www.reddit.com/static/icon.png">
    <meta property="og:image" content="https://example.com/news/hero.jpg">
    """

    image_url = extract_representative_image_from_html(html, "https://www.reddit.com/r/test")

    assert image_url == "https://example.com/news/hero.jpg"


def test_extract_representative_image_from_feed_entry_skips_reddit_static_images():
    entry = {
        "media_thumbnail": [
            {"url": "https://styles.redditmedia.com/t5_test/styles/communityIcon.png"},
            {"url": "https://example.com/content/photo.webp"},
        ],
        "links": [
            {"href": "https://www.redditstatic.com/adserver/pixel.png", "type": "image/png"},
        ],
    }

    image_url = extract_representative_image_from_feed_entry(entry)

    assert image_url == "https://example.com/content/photo.webp"
