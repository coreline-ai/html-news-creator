from __future__ import annotations
from app.utils.llm_client import chat, extract_json
from app.utils.logger import get_logger

_FALLBACK_SUMMARY_MAX = 260
DEFAULT_OUTPUT_STYLE = "newsstream"
SIGNAL_BRIEFING_OUTPUT_STYLE = "signal_briefing"

SECTION_SYSTEM_NEWSSTREAM = """당신은 AI 트렌드 리포트 작성 전문가입니다.
주어진 기사/논문 클러스터의 내용을 분석하여 한국어 섹션 요약을 작성하세요.

응답은 반드시 JSON으로만:
{
  "title_ko": "섹션 제목 (15자 이내)",
  "fact_summary": "공식 확인된 사실 요약 (없으면 null)",
  "social_signal_summary": "소셜/커뮤니티 신호 요약 (없으면 null)",
  "inference_summary": "추론/분석 내용 (없으면 null)",
  "summary_ko": "전체 요약 2-3문장",
  "importance_score": 0.0~1.0,
  "category": "model_release|research|product|safety|infrastructure|other"
}"""

SECTION_SYSTEM_SIGNAL_BRIEFING = """당신은 개발자를 위한 AI 시그널 브리핑 편집자입니다.
주어진 기사/논문/커뮤니티 클러스터를 하나의 흐름으로 묶어 한국어 브리핑 섹션을 작성하세요.

형식 원칙:
- 제목은 35~55자 내외로, 사건의 흐름과 의미가 드러나게 작성
- 여러 소식이 섞인 클러스터는 key_updates에 2~4개 핵심 업데이트로 분해
- 이미지가 있으면 독자가 확인할 디테일을 image_detail_hint에 한 문장으로 제안
- 과장 없이 사실 / 소셜 신호 / 추론을 분리

응답은 반드시 JSON으로만:
{
  "title_ko": "브리핑 섹션 제목",
  "fact_summary": "확인된 사실 요약",
  "social_signal_summary": "소셜/커뮤니티 신호 요약 (없으면 null)",
  "inference_summary": "개발자/운영자 관점 시사점 (없으면 null)",
  "summary_ko": "전체 요약 2-3문장",
  "key_updates": ["주요 소식 1", "주요 소식 2"],
  "image_detail_hint": "이미지에서 확인할 디테일 (없으면 null)",
  "tags": ["tooling", "model"],
  "importance_score": 0.0~1.0,
  "category": "model_release|research|product|safety|infrastructure|other"
}"""


def _truncate(value: str, limit: int) -> str:
    text = " ".join(str(value or "").split())
    return text if len(text) <= limit else f"{text[: limit - 1]}…"


def _normalize_output_style(value: str | None) -> str:
    return (
        SIGNAL_BRIEFING_OUTPUT_STYLE
        if value == SIGNAL_BRIEFING_OUTPUT_STYLE
        else DEFAULT_OUTPUT_STYLE
    )


def _fallback_key_updates(items: list[dict]) -> list[str]:
    updates = [
        _truncate(item.get("title") or item.get("url") or "", 120)
        for item in items[:4]
        if item.get("title") or item.get("url")
    ]
    return [update for update in updates if update]


def _fallback_section(
    cluster_id: str,
    items: list[dict],
    error: Exception | None = None,
    output_style: str = DEFAULT_OUTPUT_STYLE,
) -> dict:
    first = items[0] if items else {}
    title = _truncate(first.get("title") or "AI 트렌드 요약", 24)
    source_name = first.get("source_name") or first.get("url") or "수집 출처"
    content = first.get("content_text") or first.get("raw_text") or ""
    summary = _truncate(
        content
        or "LLM 섹션 생성에 실패해 수집된 제목과 출처를 기반으로 폴백 섹션을 생성했습니다.",
        _FALLBACK_SUMMARY_MAX,
    )
    reason = f"LLM 생성 실패: {error}" if error else "내용 없음"
    return {
        "title_ko": title,
        "fact_summary": f"{source_name} 기준으로 확인된 항목입니다. {summary}",
        "social_signal_summary": None,
        "inference_summary": reason,
        "summary_ko": summary,
        "importance_score": 0.15,
        "category": "other",
        "fallback": True,
        "cluster_id": cluster_id,
    }
    if _normalize_output_style(output_style) == SIGNAL_BRIEFING_OUTPUT_STYLE:
        fallback["key_updates"] = _fallback_key_updates(items) or [summary]
        fallback["image_detail_hint"] = None
        fallback["tags"] = ["fallback"]
    return fallback


class SectionGenerator:
    def __init__(self, output_style: str = DEFAULT_OUTPUT_STYLE):
        self.output_style = _normalize_output_style(output_style)
        self.logger = get_logger(step="generate")

    async def generate(self, cluster_id: str, items: list[dict]) -> dict:
        if not items:
            return _fallback_section(
                cluster_id,
                [],
                None,
                output_style=self.output_style,
            )
        items_text = "\n\n".join(
            f"[{i+1}] 제목: {item.get('title','')}\n출처: {item.get('url','')}\n내용: {item.get('content_text','')[:500]}"
            for i, item in enumerate(items[:5])
        )
        section_system = (
            SECTION_SYSTEM_SIGNAL_BRIEFING
            if self.output_style == SIGNAL_BRIEFING_OUTPUT_STYLE
            else SECTION_SYSTEM_NEWSSTREAM
        )
        try:
            text = await chat([
                {"role": "system", "content": section_system},
                {"role": "user", "content": f"클러스터 기사 목록:\n{items_text}\n\n위 내용으로 리포트 섹션을 작성해주세요."},
            ])
            result = extract_json(text)
            result.setdefault("title_ko", _truncate(items[0].get("title", "AI 트렌드"), 24))
            result.setdefault("summary_ko", result.get("fact_summary") or "수집된 자료 기반 요약입니다.")
            result.setdefault("fact_summary", result.get("summary_ko"))
            result.setdefault("social_signal_summary", None)
            result.setdefault("inference_summary", None)
            result.setdefault("importance_score", 0.1)
            result.setdefault("category", "other")
            if self.output_style == SIGNAL_BRIEFING_OUTPUT_STYLE:
                key_updates = result.get("key_updates")
                if not isinstance(key_updates, list):
                    key_updates = _fallback_key_updates(items)
                result["key_updates"] = [
                    _truncate(update, 180)
                    for update in key_updates[:4]
                    if str(update or "").strip()
                ]
                result.setdefault("image_detail_hint", None)
                tags = result.get("tags")
                if not isinstance(tags, list):
                    tags = []
                result["tags"] = [
                    _truncate(tag, 28)
                    for tag in tags[:8]
                    if str(tag or "").strip()
                ]
            self.logger.info(
                "section_generated",
                cluster_id=cluster_id,
                category=result.get("category"),
                output_style=self.output_style,
            )
            return result
        except Exception as e:
            self.logger.error("section_generation_failed", cluster_id=cluster_id, error=str(e))
            return _fallback_section(
                cluster_id,
                items,
                e,
                output_style=self.output_style,
            )
