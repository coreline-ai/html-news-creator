from __future__ import annotations

from app.utils.source_images import (
    extract_content_images_from_html,
    extract_representative_image_from_feed_entry,
    extract_representative_image_from_html,
    is_complete_main_image_url,
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


def test_extract_representative_image_from_html_skips_author_portrait_url():
    html = """
    <meta property="og:image" content="https://cdn.example.com/author_profile_images/reporter.jpg">
    <meta property="og:image" content="https://cdn.example.com/news/main-hero.jpg">
    """

    image_url = extract_representative_image_from_html(html, "https://example.com/news")

    assert image_url == "https://cdn.example.com/news/main-hero.jpg"


def test_extract_content_images_skips_byline_and_tiny_images():
    html = """
    <article>
      <img src="/authors/jane.jpg" class="byline author" width="120" height="120">
      <img src="/pixel.jpg" width="1" height="1">
      <img src="/images/main-ai-chip.jpg" class="article-image" width="1200" height="675">
    </article>
    """

    images = extract_content_images_from_html(html, "https://example.com/story")

    assert images == ["https://example.com/images/main-ai-chip.jpg"]


def test_complete_main_image_rejects_reporter_headshot():
    assert is_complete_main_image_url("https://example.com/news/hero.webp") is True
    assert is_complete_main_image_url("https://example.com/headshot/reporter.jpg") is False
    assert (
        is_complete_main_image_url(
            "https://cdn.aitimes.com/news/photo/member/cpark_20220210101322.png"
        )
        is False
    )
    assert (
        is_complete_main_image_url(
            "https://cdn.aitimes.com/image/newsroom/default-user.png"
        )
        is False
    )


def test_complete_main_image_rejects_recurring_promo_asset():
    assert (
        is_complete_main_image_url(
            "https://techcrunch.com/wp-content/uploads/2026/03/"
            "StrictlyVC-San-Francisco-2026-no-date.png"
        )
        is False
    )


def test_ai_chip_images_are_not_rejected_by_icon_substring():
    html = """
    <article>
      <img src="/images/nvidia-silicon-chip-hero.jpg"
           alt="NVIDIA silicon chip for AI inference"
           width="1200"
           height="675">
    </article>
    """

    images = extract_content_images_from_html(html, "https://example.com/story")

    assert images == ["https://example.com/images/nvidia-silicon-chip-hero.jpg"]
    assert (
        is_complete_main_image_url(
            "https://cdn.example.com/images/nvidia-silicon-chip-hero.jpg"
        )
        is True
    )
