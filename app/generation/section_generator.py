from __future__ import annotations
from app.utils.llm_client import chat, extract_json
from app.utils.logger import get_logger

_FALLBACK_SUMMARY_MAX = 260

SECTION_SYSTEM = """당신은 AI 트렌드 리포트 작성 전문가입니다.
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


def _truncate(value: str, limit: int) -> str:
    text = " ".join(str(value or "").split())
    return text if len(text) <= limit else f"{text[: limit - 1]}…"


def _fallback_section(cluster_id: str, items: list[dict], error: Exception | None = None) -> dict:
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


class SectionGenerator:
    def __init__(self):
        self.logger = get_logger(step="generate")

    async def generate(self, cluster_id: str, items: list[dict]) -> dict:
        if not items:
            return _fallback_section(cluster_id, [], None)
        items_text = "\n\n".join(
            f"[{i+1}] 제목: {item.get('title','')}\n출처: {item.get('url','')}\n내용: {item.get('content_text','')[:500]}"
            for i, item in enumerate(items[:5])
        )
        try:
            text = await chat([
                {"role": "system", "content": SECTION_SYSTEM},
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
            self.logger.info("section_generated", cluster_id=cluster_id, category=result.get("category"))
            return result
        except Exception as e:
            self.logger.error("section_generation_failed", cluster_id=cluster_id, error=str(e))
            return _fallback_section(cluster_id, items, e)
