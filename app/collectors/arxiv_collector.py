from __future__ import annotations

from datetime import datetime, timezone

import arxiv

from app.collectors.base import BaseCollector, CollectedItem
from app.utils.logger import get_logger
from app.utils.url_utils import canonicalize_url, url_hash

logger = get_logger(step="collect")

_MAX_RESULTS = 100


class ArxivCollector(BaseCollector):
    """Collects recent papers from an arXiv category."""

    def __init__(self, source: dict) -> None:
        self.source = source
        self.category: str = source["category"]
        self.source_id: str = source.get("name", self.category)
        self.max_items: int = int(source.get("max_items", _MAX_RESULTS))
        self.max_candidates: int = int(source.get("max_candidates", _MAX_RESULTS))

    async def collect(self, date_from: datetime, date_to: datetime) -> list[CollectedItem]:
        try:
            search = arxiv.Search(
                query=f"cat:{self.category}",
                max_results=self.max_candidates,
                sort_by=arxiv.SortCriterion.SubmittedDate,
            )

            items: list[CollectedItem] = []
            client = arxiv.Client()

            for result in client.results(search):
                published_at: datetime | None = None
                if result.published:
                    published_at = result.published
                    # Ensure timezone-aware
                    if published_at.tzinfo is None:
                        published_at = published_at.replace(tzinfo=timezone.utc)
                    else:
                        published_at = published_at.astimezone(timezone.utc)

                # Filter by date window
                if published_at is not None and published_at < date_from:
                    # Results are sorted newest-first; once we go past date_from we can stop.
                    break

                if published_at is not None and published_at > date_to:
                    continue

                raw_url = result.entry_id  # e.g. https://arxiv.org/abs/2401.12345
                canonical = canonicalize_url(raw_url)
                canon_hash = url_hash(raw_url)

                authors = ", ".join(a.name for a in result.authors) if result.authors else None

                item = CollectedItem(
                    source_id=self.source_id,
                    source_type="arxiv",
                    title=result.title.strip(),
                    url=raw_url,
                    canonical_url=canonical,
                    canonical_url_hash=canon_hash,
                    raw_text=result.summary,
                    author=authors,
                    published_at=published_at,
                    metrics_json={},
                    raw_json={
                        "arxiv_id": result.get_short_id(),
                        "categories": result.categories,
                        "pdf_url": result.pdf_url,
                        "doi": result.doi,
                    },
                )
                items.append(item)
                if len(items) >= self.max_items:
                    break

            logger.info("arxiv_collected", source=self.source_id, count=len(items))
            return items

        except Exception as exc:
            logger.error("arxiv_collect_failed", source=self.source_id, error=str(exc))
            return []
