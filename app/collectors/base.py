from __future__ import annotations
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class CollectedItem:
    source_id: str
    source_type: str  # rss|github|arxiv|x
    title: str
    url: str
    canonical_url: str
    canonical_url_hash: str
    raw_text: str | None = None
    author: str | None = None
    published_at: datetime | None = None
    metrics_json: dict = field(default_factory=dict)
    raw_json: dict = field(default_factory=dict)


@dataclass
class CollectResult:
    total: int = 0
    inserted: int = 0
    skipped: int = 0
    failed: int = 0


class BaseCollector(ABC):
    @abstractmethod
    async def collect(self, date_from: datetime, date_to: datetime) -> list[CollectedItem]:
        ...
