from __future__ import annotations
from datetime import date, datetime, timezone
from dataclasses import dataclass, field
from app.utils.logger import get_logger

DEFAULT_OUTPUT_STYLE = "newsstream"
SIGNAL_BRIEFING_OUTPUT_STYLE = "signal_briefing"


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
        output_style: str = DEFAULT_OUTPUT_STYLE,
    ) -> AssembledReport:
        """
        Assemble final report from sections.
        sections: list of section dicts with title_ko, summary_ko, importance_score, etc.
        """
        # Sort sections by importance_score descending
        sorted_sections = sorted(sections, key=lambda s: s.get("importance_score", 0), reverse=True)

        style = (
            SIGNAL_BRIEFING_OUTPUT_STYLE
            if output_style == SIGNAL_BRIEFING_OUTPUT_STYLE
            else DEFAULT_OUTPUT_STYLE
        )

        if style == SIGNAL_BRIEFING_OUTPUT_STYLE:
            summary_ko = _signal_briefing_summary(sorted_sections)
        else:
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

        enriched_stats = {**default_stats, **(stats or {})}
        if style == SIGNAL_BRIEFING_OUTPUT_STYLE:
            enriched_stats.update(_signal_briefing_stats(sorted_sections))
            enriched_stats["output_style"] = style

        report = AssembledReport(
            title=title,
            report_date=str(run_date),
            summary_ko=summary_ko,
            created_at=created_at,
            stats=enriched_stats,
            sections=sorted_sections,
            metadata={"output_style": style},
        )

        self.logger.info("report_assembled", sections=len(sorted_sections), date=str(run_date))
        return report


def _clean_text(value: object, limit: int = 180) -> str:
    text = " ".join(str(value or "").split())
    return text if len(text) <= limit else f"{text[: limit - 1]}…"


def _signal_briefing_summary(sections: list[dict]) -> str:
    if not sections:
        return "오늘 확인된 AI 뉴스 신호가 충분하지 않습니다."
    headlines = [
        _clean_text(section.get("title_ko") or section.get("title"), 80)
        for section in sections[:3]
        if section.get("title_ko") or section.get("title")
    ]
    lead = " · ".join(headlines)
    if not lead:
        lead = _clean_text(sections[0].get("summary_ko") or sections[0].get("fact_summary"), 220)
    return (
        f"오늘은 {lead} 흐름이 두드러졌습니다. "
        "아래 섹션은 사실, 커뮤니티 신호, 개발자 관점 시사점을 분리해 정리했습니다."
    )[:500]


def _signal_briefing_stats(sections: list[dict]) -> dict:
    top_keywords = _top_keywords(sections)
    main_event = _clean_text(
        " / ".join(
            section.get("title_ko") or section.get("title") or ""
            for section in sections[:2]
            if section.get("title_ko") or section.get("title")
        ),
        220,
    )
    today_temperature = _today_temperature(sections)
    action_items = _action_items(sections)
    return {
        "top_keywords": top_keywords,
        "main_event": main_event,
        "signal_axes": _signal_axes(sections),
        "today_temperature": today_temperature,
        "action_items": action_items,
    }


def _top_keywords(sections: list[dict]) -> list[str]:
    stopwords = {
        "AI",
        "ai",
        "the",
        "and",
        "with",
        "from",
        "오늘",
        "주요",
        "요약",
        "업데이트",
        "발표",
    }
    counts: dict[str, int] = {}
    for section in sections:
        values: list[object] = [
            section.get("title_ko"),
            section.get("title"),
            section.get("category"),
        ]
        tags = section.get("tags")
        if isinstance(tags, list):
            values.extend(tags)
        for value in values:
            for token in str(value or "").replace("/", " ").replace("·", " ").split():
                token = token.strip("#,.:;()[]{}'\"").strip()
                if len(token) < 2 or token in stopwords:
                    continue
                counts[token] = counts.get(token, 0) + 1
    return [
        token
        for token, _ in sorted(counts.items(), key=lambda item: (-item[1], item[0]))[:8]
    ]


def _today_temperature(sections: list[dict]) -> list[str]:
    if not sections:
        return ["수집 신호가 부족해 온도를 산정하지 못했습니다."]
    high_score = sum(1 for section in sections if float(section.get("importance_score") or 0) >= 0.75)
    social_count = sum(1 for section in sections if section.get("social_signal_summary"))
    image_count = sum(
        1
        for section in sections
        if section.get("content_image_urls") or section.get("og_image_url")
    )
    return [
        f"상위 중요도 섹션 {high_score}개가 오늘의 핵심 흐름을 형성했습니다.",
        f"커뮤니티/소셜 신호가 포함된 섹션은 {social_count}개입니다.",
        f"대표 이미지 또는 시각 자료가 있는 섹션은 {image_count}개입니다.",
    ]


def _signal_axes(sections: list[dict]) -> list[str]:
    labels = {
        "model_release": "모델/릴리스",
        "research": "연구",
        "product": "제품",
        "safety": "안전/정책",
        "infrastructure": "인프라",
        "other": "기타",
    }
    axes: list[str] = []
    for section in sections:
        category = str(section.get("category") or "other")
        label = labels.get(category, category)
        if label not in axes:
            axes.append(label)
    return axes or ["기타"]


def _action_items(sections: list[dict]) -> list[str]:
    items: list[str] = []
    for section in sections[:3]:
        title = section.get("title_ko") or section.get("title") or "상위 섹션"
        inference = section.get("inference_summary")
        if inference:
            items.append(f"{_clean_text(title, 60)} — {_clean_text(inference, 120)}")
        else:
            items.append(f"{_clean_text(title, 80)} 원문과 릴리스 노트를 확인하세요.")
    return items or ["관심 섹션의 원문 링크와 검증 상태를 먼저 확인하세요."]
