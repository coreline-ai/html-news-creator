from __future__ import annotations
from datetime import date, datetime, timezone
from dataclasses import dataclass, field
from app.utils.logger import get_logger


@dataclass
class AssembledReport:
    title: str
    report_date: str
    summary_ko: str
    created_at: str
    stats: dict = field(default_factory=dict)
    sections: list[dict] = field(default_factory=list)
    metadata: dict = field(default_factory=dict)

    def to_dict(self) -> dict:
        return {
            "title": self.title,
            "report_date": self.report_date,
            "summary_ko": self.summary_ko,
            "created_at": self.created_at,
            "stats": self.stats,
            "sections": self.sections,
            "metadata": self.metadata,
        }


class ReportAssembler:
    def __init__(self):
        self.logger = get_logger(step="generate")

    def assemble(
        self,
        run_date: date,
        title: str,
        sections: list[dict],
        stats: dict | None = None,
    ) -> AssembledReport:
        """
        Assemble final report from sections.
        sections: list of section dicts with title_ko, summary_ko, importance_score, etc.
        """
        # Sort sections by importance_score descending
        sorted_sections = sorted(sections, key=lambda s: s.get("importance_score", 0), reverse=True)

        # Build overall summary from top sections
        top_summaries = [s.get("summary_ko", "") for s in sorted_sections[:3]]
        summary_ko = " ".join(filter(None, top_summaries))[:500]

        created_at = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M")

        default_stats = {
            "total_sources": 0,
            "ai_relevant": 0,
            "clusters": len(sections),
            "verified": sum(1 for s in sections if s.get("verification_status") == "official_confirmed"),
        }

        report = AssembledReport(
            title=title,
            report_date=str(run_date),
            summary_ko=summary_ko,
            created_at=created_at,
            stats={**default_stats, **(stats or {})},
            sections=sorted_sections,
        )

        self.logger.info("report_assembled", sections=len(sorted_sections), date=str(run_date))
        return report
