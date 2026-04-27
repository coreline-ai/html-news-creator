from __future__ import annotations
from app.utils.llm_client import chat, extract_json
from app.utils.logger import get_logger

CLASSIFY_SYSTEM = """당신은 AI 트렌드 리포트 분류 전문가입니다.
주어진 텍스트가 AI/ML 관련 내용인지 분류하고 0~1 점수를 부여하세요.

응답은 반드시 JSON으로만 하세요:
{
  "is_ai_related": true/false,
  "score": 0.0~1.0,
  "category": "model_release|research_paper|product_launch|safety|infrastructure|other",
  "reason_ko": "한국어로 분류 이유 설명"
}"""


class RelevanceClassifier:
    def __init__(self):
        self.logger = get_logger(step="classify")

    async def classify(self, title: str, content: str, item_id: str = "") -> dict:
        try:
            text = await chat([
                {"role": "system", "content": CLASSIFY_SYSTEM},
                {"role": "user", "content": f"제목: {title}\n내용: {content[:1000]}\n\n위 내용을 분류해주세요."},
            ])
            result = extract_json(text)
            self.logger.info("classified", item_id=item_id, score=result.get("score"), category=result.get("category"))
            return result
        except Exception as e:
            self.logger.error("classify_failed", item_id=item_id, error=str(e))
            return {"is_ai_related": False, "score": 0.0, "category": "other", "reason_ko": f"분류 실패: {e}"}
