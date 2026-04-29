from __future__ import annotations
import asyncio
import yaml
from datetime import date, datetime
from pathlib import Path

from app.collectors.base import BaseCollector, CollectResult, CollectedItem
from app.collectors.arxiv_collector import ArxivCollector
from app.collectors.github_collector import GitHubCollector
from app.collectors.hackernews_collector import HackerNewsCollector
from app.collectors.naver_news_collector import NaverNewsCollector
from app.collectors.rss_collector import RSSCollector
from app.collectors.website_collector import WebsiteCollector
from app.utils.logger import get_logger

REGISTRY_PATH = Path("data/sources_registry.yaml")


class CollectorOrchestrator:
    def __init__(self, registry_path: Path = REGISTRY_PATH):
        self.registry_path = registry_path
        self.logger = get_logger(step="collect")

    def _load_registry(self) -> list[dict]:
        with open(self.registry_path) as f:
            return yaml.safe_load(f)["sources"]

    def _date_window_utc(self, run_date: date) -> tuple[datetime, datetime]:
        """Return the configured local-day window converted to UTC.

        Reports are dated in the configured product timezone (default
        Asia/Seoul), while most source APIs expose UTC timestamps. This prevents
        KST morning news from being lost when the UTC calendar day differs.
        """
        from app.pipeline.date_window import local_day_window_utc

        return local_day_window_utc(run_date)

    def _make_collector(self, source: dict) -> BaseCollector | None:
        from app.config import settings

        t = source.get("source_type")
        collector_type = source.get("collector_type") or t

        # `source_type` is persisted to DB and must stay within the existing
        # enum. `collector_type` lets registry entries route to special
        # collectors while remaining enum-safe, e.g. source_type=website.
        if collector_type == "hackernews":
            return HackerNewsCollector(source)
        if collector_type == "naver_news":
            return NaverNewsCollector(source)

        if t == "rss":
            return RSSCollector(source)
        elif t == "website":
            return WebsiteCollector(source)
        elif t == "github":
            if not settings.github_token:
                if not settings.github_allow_unauthenticated:
                    self.logger.info("github_source_skipped", source=source.get("name"), reason="no_token")
                    return None
                self.logger.info(
                    "github_anonymous_fallback",
                    source=source.get("name"),
                    reason="no_token",
                )
            return GitHubCollector(source)
        elif t == "arxiv":
            return ArxivCollector(source)
        return None

    async def collect_items(
        self,
        run_date: date,
        source_types: list[str] | None = None,
    ) -> list[CollectedItem]:
        sources = self._load_registry()
        if source_types:
            sources = [s for s in sources if s.get("source_type") in source_types]

        date_from, date_to = self._date_window_utc(run_date)

        collectors = [c for s in sources if (c := self._make_collector(s)) is not None]

        async def _collect_one(collector: BaseCollector) -> list[CollectedItem]:
            try:
                return await collector.collect(date_from, date_to)
            except Exception as e:
                self.logger.error("collector_failed", error=str(e))
                return []

        results = await asyncio.gather(*[_collect_one(c) for c in collectors])
        return [item for batch in results for item in batch]

    async def run(
        self,
        run_date: date,
        source_types: list[str] | None = None,
        dry_run: bool = False,
    ) -> CollectResult:
        sources = self._load_registry()
        if source_types:
            sources = [s for s in sources if s.get("source_type") in source_types]

        date_from, date_to = self._date_window_utc(run_date)

        collectors = [c for s in sources if (c := self._make_collector(s)) is not None]

        async def _collect_one(collector: BaseCollector) -> list[CollectedItem]:
            try:
                return await collector.collect(date_from, date_to)
            except Exception as e:
                self.logger.error("collector_failed", error=str(e))
                return []

        results = await asyncio.gather(*[_collect_one(c) for c in collectors])
        all_items: list[CollectedItem] = [item for batch in results for item in batch]

        result = CollectResult(total=len(all_items))
        if not dry_run:
            # In a real implementation, upsert to DB here
            result.inserted = len(all_items)
        else:
            self.logger.info("dry_run_collect", total=len(all_items))

        return result
