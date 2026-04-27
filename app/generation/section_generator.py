from __future__ import annotations
from app.utils.llm_client import chat, extract_json
from app.utils.logger import get_logger

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


class SectionGenerator:
    def __init__(self):
        self.logger = get_logger(step="generate")

    async def generate(self, cluster_id: str, items: list[dict]) -> dict:
        if not items:
            return {"title_ko": "빈 클러스터", "fact_summary": None, "social_signal_summary": None,
                    "inference_summary": None, "summary_ko": "내용 없음", "importance_score": 0.0, "category": "other"}
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
            self.logger.info("section_generated", cluster_id=cluster_id, category=result.get("category"))
            return result
        except Exception as e:
            self.logger.error("section_generation_failed", cluster_id=cluster_id, error=str(e))
            return {"title_ko": f"클러스터 {cluster_id}", "fact_summary": None, "social_signal_summary": None,
                    "inference_summary": None, "summary_ko": f"생성 실패: {e}", "importance_score": 0.0, "category": "other"}
