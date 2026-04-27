from __future__ import annotations
from app.utils.llm_client import chat, extract_json
from app.utils.logger import get_logger

TITLE_SYSTEM = """당신은 AI 트렌드 뉴스 편집장입니다.
오늘의 AI 트렌드 리포트 제목을 5개 생성해주세요.

응답은 반드시 JSON으로만:
{"titles": ["제목1", "제목2", "제목3", "제목4", "제목5"]}

요구사항:
- 한국어, 30자 이내
- 구체적 모델명/회사명 포함 (가능하면)
- 클릭베이트 금지, 사실 기반"""


class TitleGenerator:
    def __init__(self):
        self.logger = get_logger(step="generate")

    async def generate_titles(self, sections_summary: str) -> list[str]:
        try:
            text = await chat([
                {"role": "system", "content": TITLE_SYSTEM},
                {"role": "user", "content": f"오늘의 주요 AI 트렌드:\n{sections_summary[:1000]}"},
            ])
            result = extract_json(text)
            titles = result.get("titles", [])
            self.logger.info("titles_generated", count=len(titles))
            return titles
        except Exception as e:
            self.logger.error("title_generation_failed", error=str(e))
            return ["오늘의 AI 트렌드 리포트"]
