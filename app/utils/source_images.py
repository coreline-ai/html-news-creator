from __future__ import annotations

import re
from html import unescape
from typing import Any
from urllib.parse import urljoin, urlparse

import httpx

from app.utils.url_utils import is_ssrf_blocked

_IMAGE_META_KEYS = {
    "og:image",
    "og:image:url",
    "og:image:secure_url",
    "twitter:image",
    "twitter:image:src",
    "image",
}

_IMAGE_EXTENSIONS = (".jpg", ".jpeg", ".png", ".webp", ".gif", ".avif")


def _entry_get(entry: Any, key: str, default: Any = None) -> Any:
    if hasattr(entry, "get"):
        return entry.get(key, default)
    return getattr(entry, key, default)


def _dict_get(value: Any, key: str, default: Any = None) -> Any:
    if isinstance(value, dict):
        return value.get(key, default)
    if hasattr(value, "get"):
        return value.get(key, default)
    return getattr(value, key, default)


def _is_http_url(url: str) -> bool:
    parsed = urlparse(url)
    return parsed.scheme in {"http", "https"} and bool(parsed.netloc)


def _normalize_image_url(url: str, base_url: str = "") -> str:
    if not url:
        return ""
    normalized = urljoin(base_url, unescape(url.strip()))
    return normalized if _is_http_url(normalized) else ""


def _extract_attrs(tag: str) -> dict[str, str]:
    attrs: dict[str, str] = {}
    for match in re.finditer(r"([a-zA-Z_:.-]+)\s*=\s*([\"'])(.*?)\2", tag, re.DOTALL):
        attrs[match.group(1).lower()] = match.group(3).strip()
    return attrs


_SKIP_SUBSTRINGS = (
    "front/assets", "favicon", "tracking", "analytics", "placeholder",
    "default-user", "default_user", "default-avatar", "default_avatar",
    # Recurring publisher promo/event assets that are commonly embedded in
    # article bodies but are not evidence images for the article itself.
    "strictlyvc",
)
_SKIP_TOKENS = (
    "avatar", "logo", "icon", "badge", "noborder", "button", "pixel",
    "emoji", "spinner", "spacer", "separator", "divider",
)
_SKIP_EXTENSIONS = (".svg", ".ico")
_REDDIT_STATIC_HOSTS = ("styles.redditmedia.com", "redditstatic.com")

# Journalist/author portrait patterns: these appear in article bylines and get
# mistakenly picked up as representative article images.
_AUTHOR_PORTRAIT_PATTERNS = (
    "author_profile_images",   # Chorus CMS (The Verge, Polygon, etc.)
    "profile_images",
    "/chorus/author",          # Chorus CMS author asset path
    "news/photo/member",       # AI타임스 reporter profile image path
    "/photo/member/",
    "_blurple",                # The Verge's journalist portrait naming scheme
    "/author/",
    "/authors/",
    "/headshot",               # Generic headshot path
    "/byline",                 # Byline image path
    "/reporter",
    "/journalist",
    "/contributor",
    "/writer",
    "/staff/",
    "/profile/",
    "/portrait",
    "author-photo",
    "author-image",
    "staff-photo",
    "reporter-photo",
    "journalist-photo",
    "profile-photo",
    "headshot",
)
_UNRELATED_ATTR_PATTERNS = (
    "author", "byline", "reporter", "journalist", "contributor", "writer",
    "staff", "profile", "portrait", "headshot", "avatar", "logo", "icon",
    "sponsor", "ad", "ads", "advertisement",
)
_UNRELATED_ATTR_RE = re.compile(
    r"(?:^|[^a-z0-9])("
    + "|".join(re.escape(pattern) for pattern in _UNRELATED_ATTR_PATTERNS)
    + r")(?:$|[^a-z0-9])"
)
_SKIP_TOKEN_RE = re.compile(
    r"(?:^|[^a-z0-9])("
    + "|".join(re.escape(pattern) for pattern in _SKIP_TOKENS)
    + r")(?:$|[^a-z0-9])"
)
_MIN_CONTENT_IMAGE_WIDTH = 300
_MIN_CONTENT_IMAGE_HEIGHT = 160


def _is_reddit_static_image_url(url: str) -> bool:
    parsed = urlparse(url)
    host = parsed.netloc.lower().split(":", 1)[0]
    path = parsed.path.lower()
    if host == "reddit.com" or host.endswith(".reddit.com"):
        return path.startswith("/static/") or path == "/static"
    return any(host == blocked or host.endswith(f".{blocked}") for blocked in _REDDIT_STATIC_HOSTS)


def _is_unsuitable_image_url(url: str) -> bool:
    lower = url.lower()
    if _is_reddit_static_image_url(lower):
        return True
    if any(k in lower for k in _SKIP_SUBSTRINGS):
        return True
    if _SKIP_TOKEN_RE.search(lower):
        return True
    if any(k in lower for k in _AUTHOR_PORTRAIT_PATTERNS):
        return True
    return any(lower.endswith(ext) for ext in _SKIP_EXTENSIONS)


def _numeric_attr(attrs: dict[str, str], key: str) -> int | None:
    raw = attrs.get(key, "")
    match = re.search(r"\d+", raw)
    return int(match.group(0)) if match else None


def _is_unsuitable_image_attrs(attrs: dict[str, str]) -> bool:
    """Reject author/profile/decorative images using local tag metadata.

    We cannot perform visual recognition in the collector, so the policy is
    intentionally conservative: if an image is labelled as author/byline/profile
    or is explicitly tiny, do not let it become report evidence.
    """
    blob = " ".join(
        str(attrs.get(key, "") or "").lower()
        for key in ("alt", "class", "id", "aria-label", "title", "data-testid")
    )
    if _UNRELATED_ATTR_RE.search(blob):
        return True

    width = _numeric_attr(attrs, "width")
    height = _numeric_attr(attrs, "height")
    if width is not None and width < _MIN_CONTENT_IMAGE_WIDTH:
        return True
    if height is not None and height < _MIN_CONTENT_IMAGE_HEIGHT:
        return True
    return False


def is_usable_representative_image_url(url: str) -> bool:
    return bool(url) and _is_http_url(url) and not _is_unsuitable_image_url(url)


def is_complete_main_image_url(url: str) -> bool:
    """Return whether a URL is safe enough to boost an article as image-backed.

    This is deliberately stricter than "any image exists": logos, avatars,
    journalist headshots, tracking pixels, SVG icons, Reddit UI assets, and
    other decorative URLs are all rejected by `is_usable_representative_image_url`.
    """
    return is_usable_representative_image_url(url)


def extract_content_images_from_html(
    html: str, base_url: str = "", max_images: int = 5
) -> list[str]:
    """본문 <img> 태그에서 실제 콘텐츠 이미지 URL 목록을 추출한다.

    로고·아바타·아이콘 등 UI 요소는 제거하고, 기사 본문의 다이어그램·사진 등만 반환한다.
    """
    if not html:
        return []

    seen: set[str] = set()
    results: list[str] = []

    for match in re.finditer(r"<img\b[^>]*>", html, re.IGNORECASE | re.DOTALL):
        attrs = _extract_attrs(match.group(0))
        src = (
            attrs.get("src", "")
            or attrs.get("data-src", "")
            or attrs.get("data-lazy-src", "")
            or attrs.get("data-original", "")
        )
        if not src:
            continue
        if _is_unsuitable_image_attrs(attrs):
            continue

        abs_src = _normalize_image_url(src, base_url)
        if not abs_src or abs_src in seen:
            continue

        lower = abs_src.lower()
        if _is_unsuitable_image_url(lower):
            continue

        seen.add(abs_src)
        results.append(abs_src)
        if len(results) >= max_images:
            break

    return results


def extract_representative_image_from_html(html: str, base_url: str = "") -> str:
    """Extract a representative image from HTML meta/link tags.

    Priority is source-provided metadata: og:image, twitter:image, and image_src.
    Relative URLs are resolved against the final source URL when provided.
    """
    if not html:
        return ""

    for match in re.finditer(r"<meta\b[^>]*>", html, re.IGNORECASE | re.DOTALL):
        attrs = _extract_attrs(match.group(0))
        key = attrs.get("property") or attrs.get("name") or attrs.get("itemprop") or ""
        if key.lower() in _IMAGE_META_KEYS:
            image_url = _normalize_image_url(attrs.get("content", ""), base_url)
            if is_usable_representative_image_url(image_url):
                return image_url

    for match in re.finditer(r"<link\b[^>]*>", html, re.IGNORECASE | re.DOTALL):
        attrs = _extract_attrs(match.group(0))
        rel = attrs.get("rel", "").lower()
        href = attrs.get("href", "")
        if "image_src" in rel:
            image_url = _normalize_image_url(href, base_url)
            if is_usable_representative_image_url(image_url):
                return image_url

    return ""


def extract_representative_image_from_feed_entry(entry: Any) -> str:
    """Extract an image candidate from a feedparser entry."""
    for key in ("media_content", "media_thumbnail"):
        media_items = _entry_get(entry, key, []) or []
        if isinstance(media_items, dict):
            media_items = [media_items]
        for media in media_items:
            mime_type = str(_dict_get(media, "type", "") or "").lower()
            # Skip non-image media (e.g. YouTube returns application/x-shockwave-flash)
            if mime_type and not mime_type.startswith("image/"):
                continue
            width = _dict_get(media, "width", None)
            height = _dict_get(media, "height", None)
            if width is not None or height is not None:
                attrs = {
                    "width": str(width or ""),
                    "height": str(height or ""),
                    "alt": str(_dict_get(media, "alt", "") or ""),
                    "class": str(_dict_get(media, "class", "") or ""),
                }
                if _is_unsuitable_image_attrs(attrs):
                    continue
            image_url = _normalize_image_url(
                _dict_get(media, "url", "") or _dict_get(media, "href", "")
            )
            if is_usable_representative_image_url(image_url):
                return image_url

    image = _entry_get(entry, "image", None)
    if image:
        image_url = _normalize_image_url(
            _dict_get(image, "href", "") or _dict_get(image, "url", "")
        )
        if is_usable_representative_image_url(image_url):
            return image_url

    for link in _entry_get(entry, "links", []) or []:
        href = _dict_get(link, "href", "")
        mime_type = str(_dict_get(link, "type", "") or "").lower()
        rel = str(_dict_get(link, "rel", "") or "").lower()
        if mime_type.startswith("image/") or href.lower().endswith(_IMAGE_EXTENSIONS):
            image_url = _normalize_image_url(href)
            if is_usable_representative_image_url(image_url):
                return image_url
        if rel == "enclosure" and href.lower().endswith(_IMAGE_EXTENSIONS):
            image_url = _normalize_image_url(href)
            if is_usable_representative_image_url(image_url):
                return image_url

    return ""


def fetch_representative_image_url(url: str, timeout: float = 10.0) -> str:
    """Fetch a source page and extract its representative image URL.

    This is a fallback for already-collected rows that predate image metadata.
    It should be used sparingly and only for external http(s) URLs.
    """
    if not url or not _is_http_url(url) or is_ssrf_blocked(url):
        return ""

    response = httpx.get(
        url,
        timeout=timeout,
        follow_redirects=True,
        headers={"User-Agent": "html-news-creator/1.0"},
    )
    response.raise_for_status()
    return extract_representative_image_from_html(response.text, str(response.url))
