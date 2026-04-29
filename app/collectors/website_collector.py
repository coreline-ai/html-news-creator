from __future__ import annotations

import gzip
import re
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
from html import unescape
from urllib.parse import urljoin

import httpx

from app.collectors.base import BaseCollector, CollectedItem
from app.utils.logger import get_logger
from app.utils.source_images import extract_representative_image_from_html
from app.utils.url_utils import canonicalize_url, is_ssrf_blocked, url_hash

logger = get_logger(step="collect")

_USER_AGENT = "html-news-creator/1.0"
_DEFAULT_TIMEOUT = 20.0


def _local_name(tag: str) -> str:
    return tag.rsplit("}", 1)[-1]


def _parse_datetime(raw: str | None) -> datetime | None:
    if not raw:
        return None

    value = unescape(raw).strip()
    if not value:
        return None

    normalized = value.replace("Z", "+00:00")
    try:
        parsed = datetime.fromisoformat(normalized)
        if parsed.tzinfo is None:
            parsed = parsed.replace(tzinfo=timezone.utc)
        return parsed.astimezone(timezone.utc)
    except ValueError:
        pass

    for fmt in ("%b %d, %Y", "%B %d, %Y", "%Y-%m-%d"):
        try:
            return datetime.strptime(value, fmt).replace(tzinfo=timezone.utc)
        except ValueError:
            pass

    try:
        return parsedate_to_datetime(value).astimezone(timezone.utc)
    except Exception:
        return None


def _attrs(tag: str) -> dict[str, str]:
    result: dict[str, str] = {}
    for match in re.finditer(r"([a-zA-Z_:.-]+)\s*=\s*([\"'])(.*?)\2", tag, re.DOTALL):
        result[match.group(1).lower()] = unescape(match.group(3).strip())
    return result


def _meta_content(html: str, keys: set[str]) -> str:
    wanted = {key.lower() for key in keys}
    for match in re.finditer(r"<meta\b[^>]*>", html, re.IGNORECASE | re.DOTALL):
        attrs = _attrs(match.group(0))
        key = attrs.get("property") or attrs.get("name") or attrs.get("itemprop") or ""
        if key.lower() in wanted:
            return attrs.get("content", "")
    return ""


def _title_from_html(html: str) -> str:
    title = _meta_content(html, {"og:title", "twitter:title"})
    if title:
        return title
    match = re.search(r"<title[^>]*>(.*?)</title>", html, re.IGNORECASE | re.DOTALL)
    if match:
        return re.sub(r"\s+", " ", unescape(match.group(1))).strip()
    return ""


def _description_from_html(html: str) -> str:
    return _meta_content(html, {"og:description", "twitter:description", "description"})


def _published_from_html(html: str) -> datetime | None:
    raw = _meta_content(
        html,
        {
            "article:published_time",
            "date",
            "datepublished",
            "publishdate",
            "pubdate",
        },
    )
    parsed = _parse_datetime(raw)
    if parsed:
        return parsed

    json_ld_match = re.search(
        r'"datePublished"\s*:\s*"([^"]+)"',
        html,
        re.IGNORECASE,
    )
    parsed = _parse_datetime(json_ld_match.group(1) if json_ld_match else None)
    if parsed:
        return parsed

    time_match = re.search(r"<time\b[^>]*>", html, re.IGNORECASE | re.DOTALL)
    if time_match:
        attrs = _attrs(time_match.group(0))
        parsed = _parse_datetime(attrs.get("datetime"))
        if parsed:
            return parsed

    time_text_match = re.search(
        r"<time\b[^>]*>(.*?)</time>",
        html,
        re.IGNORECASE | re.DOTALL,
    )
    if time_text_match:
        text = re.sub(r"<[^>]+>", "", time_text_match.group(1))
        parsed = _parse_datetime(text)
        if parsed:
            return parsed

    text_content = re.sub(r"<[^>]+>", " ", html)
    date_text_match = re.search(
        r"\b("
        r"Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|"
        r"Jul(?:y)?|Aug(?:ust)?|Sep(?:tember)?|Oct(?:ober)?|Nov(?:ember)?|"
        r"Dec(?:ember)?"
        r")\s+\d{1,2},\s+\d{4}\b",
        text_content,
        re.IGNORECASE,
    )
    if date_text_match:
        return _parse_datetime(date_text_match.group(0))

    return None


class WebsiteCollector(BaseCollector):
    """Collects official website articles from sitemap XML or listing pages."""

    def __init__(self, source: dict) -> None:
        self.source = source
        self.source_id: str = source.get("name", source.get("url", ""))
        self.url: str = source.get("url", "")
        self.sitemap_url: str = source.get("sitemap_url", "")
        self.listing_url: str = source.get("listing_url", self.url)
        self.include_patterns: list[str] = source.get("include_url_patterns", [])
        self.exclude_patterns: list[str] = source.get("exclude_url_patterns", [])
        self.max_candidates: int = int(source.get("max_candidates", 40))
        self.max_items: int = int(source.get("max_items", 20))

    def _fetch_bytes(self, url: str) -> bytes:
        if not url or is_ssrf_blocked(url):
            return b""
        response = httpx.get(
            url,
            timeout=_DEFAULT_TIMEOUT,
            follow_redirects=True,
            headers={"User-Agent": _USER_AGENT},
        )
        response.raise_for_status()
        content = response.content
        if content.startswith(b"\x1f\x8b"):
            return gzip.decompress(content)
        return content

    def _fetch_text(self, url: str) -> str:
        return self._fetch_bytes(url).decode("utf-8", errors="replace")

    def _allowed_url(self, url: str) -> bool:
        if self.include_patterns and not any(pattern in url for pattern in self.include_patterns):
            return False
        return not any(pattern in url for pattern in self.exclude_patterns)

    def _candidate_from_sitemap(self, url: str, depth: int = 0) -> list[tuple[str, datetime | None]]:
        if not url or depth > 1:
            return []

        try:
            root = ET.fromstring(self._fetch_bytes(url))
        except Exception as exc:
            logger.warning("website_sitemap_fetch_failed", source=self.source_id, url=url, error=str(exc))
            return []

        candidates: list[tuple[str, datetime | None]] = []
        root_name = _local_name(root.tag)
        if root_name == "sitemapindex":
            for sitemap in root:
                if _local_name(sitemap.tag) != "sitemap":
                    continue
                loc = ""
                for child in sitemap:
                    if _local_name(child.tag) == "loc":
                        loc = child.text or ""
                        break
                candidates.extend(self._candidate_from_sitemap(loc, depth + 1))
            return candidates

        for url_node in root:
            if _local_name(url_node.tag) != "url":
                continue
            loc = ""
            lastmod = None
            for child in url_node:
                child_name = _local_name(child.tag)
                if child_name == "loc":
                    loc = child.text or ""
                elif child_name == "lastmod":
                    lastmod = _parse_datetime(child.text)
            if loc and self._allowed_url(loc):
                candidates.append((loc, lastmod))

        return candidates

    def _candidate_from_listing(self) -> list[tuple[str, datetime | None]]:
        if not self.listing_url:
            return []

        try:
            html = self._fetch_text(self.listing_url)
        except Exception as exc:
            logger.warning(
                "website_listing_fetch_failed",
                source=self.source_id,
                url=self.listing_url,
                error=str(exc),
            )
            return []

        urls: list[str] = []
        for href in re.findall(r"href\s*=\s*([\"'])(.*?)\1", html, re.IGNORECASE | re.DOTALL):
            urls.append(urljoin(self.listing_url, unescape(href[1])))
        for raw_url in re.findall(r"https?://[^\"'<>\s]+", html, re.IGNORECASE):
            urls.append(unescape(raw_url))

        candidates: list[tuple[str, datetime | None]] = []
        seen: set[str] = set()
        listing_canonical = canonicalize_url(self.listing_url)
        for raw_url in urls:
            url = raw_url.split("#", 1)[0]
            if not url or url in seen or canonicalize_url(url) == listing_canonical:
                continue
            if not self._allowed_url(url):
                continue
            seen.add(url)
            candidates.append((url, None))
            if len(candidates) >= self.max_candidates:
                break

        return candidates

    def _discover_candidates(self) -> list[tuple[str, datetime | None]]:
        candidates: list[tuple[str, datetime | None]] = []
        if self.sitemap_url:
            candidates.extend(self._candidate_from_sitemap(self.sitemap_url))
        candidates.extend(self._candidate_from_listing())

        deduped: list[tuple[str, datetime | None]] = []
        seen: set[str] = set()
        for url, published_at in candidates:
            canonical = canonicalize_url(url)
            if canonical in seen:
                continue
            seen.add(canonical)
            deduped.append((url, published_at))
            if len(deduped) >= self.max_candidates:
                break
        return deduped

    def _fetch_article_item(
        self,
        url: str,
        fallback_published_at: datetime | None,
        date_from: datetime,
        date_to: datetime,
    ) -> CollectedItem | None:
        if fallback_published_at and fallback_published_at < date_from:
            return None
        if fallback_published_at and fallback_published_at > date_to:
            return None

        html = self._fetch_text(url)
        published_at = _published_from_html(html) or fallback_published_at
        if published_at is not None and (published_at < date_from or published_at > date_to):
            return None

        title = _title_from_html(html) or url
        description = _description_from_html(html)
        image_url = extract_representative_image_from_html(html, url)
        canonical = canonicalize_url(url)

        return CollectedItem(
            source_id=self.source_id,
            source_type="website",
            title=title,
            url=url,
            canonical_url=canonical,
            canonical_url_hash=url_hash(url),
            raw_text=description or title,
            author=None,
            published_at=published_at,
            metrics_json={},
            raw_json={
                "image_url": image_url,
                "description": description,
                "discovery": "sitemap" if fallback_published_at else "listing",
            },
        )

    async def collect(self, date_from: datetime, date_to: datetime) -> list[CollectedItem]:
        candidates = self._discover_candidates()
        items: list[CollectedItem] = []

        for url, fallback_published_at in candidates:
            try:
                item = self._fetch_article_item(
                    url,
                    fallback_published_at,
                    date_from,
                    date_to,
                )
                if item:
                    items.append(item)
                if len(items) >= self.max_items:
                    break
            except Exception as exc:
                logger.warning("website_article_fetch_failed", source=self.source_id, url=url, error=str(exc))

        logger.info("website_collected", source=self.source_id, count=len(items))
        return items
