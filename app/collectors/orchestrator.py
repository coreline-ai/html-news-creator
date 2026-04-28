from __future__ import annotations
import asyncio
import yaml
from datetime import date, datetime, timezone
from pathlib import Path

from app.collectors.base import BaseCollector, CollectResult, CollectedItem
from app.collectors.rss_collector import RSSCollector
from app.collectors.github_collector import GitHubCollector
from app.collectors.arxiv_collector import ArxivCollector
from app.utils.logger import get_logger

REGISTRY_PATH = Path("data/sources_registry.yaml")


class CollectorOrchestrator:
    def __init__(self, registry_path: Path = REGISTRY_PATH):
        self.registry_path = registry_path
        self.logger = get_logger(step="collect")

    def _load_registry(self) -> list[dict]:
        with open(self.registry_path) as f:
            return yaml.safe_load(f)["sources"]

    def _make_collector(self, source: dict) -> BaseCollector | None:
        t = source.get("source_type")
        if t == "rss":
            return RSSCollector(source)
        elif t == "github":
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

        date_from = datetime(run_date.year, run_date.month, run_date.day, 0, 0, 0, tzinfo=timezone.utc)
        date_to = datetime(run_date.year, run_date.month, run_date.day, 23, 59, 59, tzinfo=timezone.utc)

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

        date_from = datetime(run_date.year, run_date.month, run_date.day, 0, 0, 0, tzinfo=timezone.utc)
        date_to = datetime(run_date.year, run_date.month, run_date.day, 23, 59, 59, tzinfo=timezone.utc)

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
