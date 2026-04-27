from __future__ import annotations
import json

from openai import AsyncOpenAI

from app.config import settings
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

CLASSIFY_USER = """제목: {title}
내용 (처음 1000자): {content}

위 내용을 분류해주세요."""


class RelevanceClassifier:
    def __init__(self):
        self.client = AsyncOpenAI(api_key=settings.openai_api_key, base_url=settings.openai_base_url)
        self.logger = get_logger(step="classify")

    async def classify(self, title: str, content: str, item_id: str = "") -> dict:
        """
        Returns dict: {is_ai_related, score, category, reason_ko}
        score >= 0.80: report candidate
        score 0.50~0.79: supplementary candidate
        score < 0.50: exclude
        """
        try:
            response = await self.client.chat.completions.create(
                model=settings.openai_model,
                messages=[
                    {"role": "system", "content": CLASSIFY_SYSTEM},
                    {
                        "role": "user",
                        "content": CLASSIFY_USER.format(
                            title=title,
                            content=content[:1000],
                        ),
                    },
                ],
                response_format={"type": "json_object"},
                max_tokens=300,
                temperature=0,
            )
            result = json.loads(response.choices[0].message.content)
            self.logger.info(
                "classified",
                item_id=item_id,
                score=result.get("score"),
                category=result.get("category"),
            )
            return result
        except Exception as e:
            self.logger.error("classify_failed", item_id=item_id, error=str(e))
            return {
                "is_ai_related": False,
                "score": 0.0,
                "category": "other",
                "reason_ko": f"분류 실패: {e}",
            }
