from __future__ import annotations
import re
from urllib.parse import urlparse


GITHUB_PATTERN = re.compile(r"github\.com/([^/]+)(?:/([^/]+))?")
ARXIV_PATTERN = re.compile(r"arxiv\.org/(?:abs|pdf)/(\d{4}\.\d+)")
HUGGINGFACE_PATTERN = re.compile(r"huggingface\.co/([^/]+)")


def classify_source_type(url: str) -> str:
    """
    Returns one of:
    official_site | official_docs | official_github | official_huggingface |
    paper_arxiv | trusted_media | community | unknown
    """
    url_lower = url.lower()
    parsed = urlparse(url_lower)
    domain = parsed.netloc.lstrip("www.")

    if ARXIV_PATTERN.search(url):
        return "paper_arxiv"

    if "github.com" in domain:
        return "official_github"

    if "huggingface.co" in domain:
        return "official_huggingface"

    official_domains = [
        "openai.com", "anthropic.com", "deepmind.google", "ai.meta.com",
        "ai.google", "research.google", "labs.google", "mistral.ai",
        "cohere.com", "stability.ai", "x.ai", "inflection.ai"
    ]
    if any(domain == d or domain.endswith("." + d) for d in official_domains):
        if "docs" in parsed.path or "documentation" in parsed.path:
            return "official_docs"
        return "official_site"

    trusted_media = ["techcrunch.com", "venturebeat.com", "theverge.com", "wired.com", "arstechnica.com"]
    if any(domain == d or domain.endswith("." + d) for d in trusted_media):
        return "trusted_media"

    community = ["reddit.com", "news.ycombinator.com", "twitter.com", "x.com"]
    if any(domain == d or domain.endswith("." + d) for d in community):
        return "community"

    return "unknown"
