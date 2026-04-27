from __future__ import annotations
import re
try:
    import bleach
    _BLEACH_AVAILABLE = True
except ImportError:
    _BLEACH_AVAILABLE = False
from app.utils.logger import get_logger


ALLOWED_TAGS = [
    "a", "abbr", "b", "blockquote", "br", "caption", "cite", "code",
    "col", "colgroup", "dd", "del", "details", "dl", "dt", "em",
    "figure", "figcaption", "h1", "h2", "h3", "h4", "h5", "h6",
    "hr", "i", "img", "ins", "kbd", "li", "mark", "ol", "p", "pre",
    "q", "s", "section", "small", "span", "strong", "sub", "summary",
    "sup", "table", "tbody", "td", "th", "thead", "time", "tr", "u", "ul",
    "article", "header", "footer", "nav", "main", "div",
]

ALLOWED_ATTRIBUTES = {
    "*": ["class", "id", "style"],
    "a": ["href", "title", "rel", "target"],
    "img": ["src", "alt", "title", "width", "height", "loading"],
    "time": ["datetime"],
    "td": ["colspan", "rowspan"],
    "th": ["colspan", "rowspan", "scope"],
    "col": ["span"],
    "colgroup": ["span"],
}

BLOCKED_CSS_PATTERNS = [
    re.compile(r"expression\s*\(", re.IGNORECASE),
    re.compile(r"javascript\s*:", re.IGNORECASE),
    re.compile(r"vbscript\s*:", re.IGNORECASE),
    re.compile(r"data\s*:", re.IGNORECASE),
    re.compile(r"@import", re.IGNORECASE),
    re.compile(r"behavior\s*:", re.IGNORECASE),
]


def _clean_style(tag: str, name: str, value: str) -> str | bool:
    """Filter style attribute values for XSS."""
    if name == "style":
        for pattern in BLOCKED_CSS_PATTERNS:
            if pattern.search(value):
                return False
    if name in ("href", "src"):
        v = value.strip().lower()
        if any(v.startswith(p) for p in ["javascript:", "vbscript:", "data:"]):
            return False
    return value


class HTMLSanitizer:
    def __init__(self):
        self.logger = get_logger(step="render")

    def sanitize(self, html: str) -> str:
        """Sanitize HTML using bleach. Falls back to basic tag stripping if bleach not available."""
        if not html:
            return ""

        if _BLEACH_AVAILABLE:
            cleaned = bleach.clean(
                html,
                tags=ALLOWED_TAGS,
                attributes=_clean_style,
                strip=True,
                strip_comments=True,
            )
        else:
            # Simple fallback: strip all tags
            cleaned = re.sub(r"<[^>]+>", "", html)

        return cleaned

    def sanitize_url(self, url: str) -> str:
        """Block dangerous URL schemes."""
        if not url:
            return ""
        stripped = url.strip().lower()
        if any(stripped.startswith(s) for s in ["javascript:", "vbscript:", "data:"]):
            return "#"
        return url
