from __future__ import annotations
import json
from openai import AsyncOpenAI
from app.config import settings
from app.utils.logger import get_logger
from app.rendering.html_sanitizer import HTMLSanitizer


LAYOUT_PLANNER_SYSTEM = """당신은 AI 뉴스 리포트 HTML 레이아웃 전문가입니다.
주어진 리포트 데이터로 완전한 HTML 페이지를 생성하세요.

요구사항:
- 완전한 <!DOCTYPE html> HTML5 문서
- 반응형 CSS (모바일/데스크톱)
- 한국어 콘텐츠
- 접근성 (aria 속성, semantic HTML)
- 인라인 CSS만 사용 (외부 파일 없음)
- <script> 태그 사용 금지 (정적 HTML만)
- fact/social_signal/inference 섹션 구분 표시
- 검증 배지 (공식 확인 = 초록, 미검증 = 노랑)"""


class GenerativeHTMLRenderer:
    def __init__(self):
        self.client = AsyncOpenAI(api_key=settings.openai_api_key, base_url=settings.openai_base_url)
        self.sanitizer = HTMLSanitizer()
        self.logger = get_logger(step="render")

    async def render(self, report: dict, sections: list[dict]) -> str:
        """
        Generate HTML using LLM. The output is sanitized before return.
        Falls back to empty string on failure.
        """
        report_json = json.dumps({
            "title": report.get("title", "AI 트렌드 리포트"),
            "report_date": report.get("report_date", ""),
            "summary_ko": report.get("summary_ko", ""),
            "stats": report.get("stats", {}),
            "sections": [
                {
                    "title": s.get("title_ko", s.get("title", "")),
                    "summary_ko": s.get("summary_ko", ""),
                    "fact_summary": s.get("fact_summary"),
                    "social_signal_summary": s.get("social_signal_summary"),
                    "inference_summary": s.get("inference_summary"),
                    "verification_status": s.get("verification_status", "unverified"),
                    "importance_score": s.get("importance_score", 0.0),
                }
                for s in sections[:8]  # limit to 8 sections for token budget
            ],
        }, ensure_ascii=False)

        try:
            response = await self.client.chat.completions.create(
                model=settings.openai_model,
                messages=[
                    {"role": "system", "content": LAYOUT_PLANNER_SYSTEM},
                    {"role": "user", "content": f"다음 데이터로 HTML 리포트를 생성하세요:\n\n{report_json}"},
                ],
                max_tokens=4000,
                temperature=0.2,
            )
            raw_html = response.choices[0].message.content
            # Extract HTML if wrapped in code blocks
            if "```html" in raw_html:
                raw_html = raw_html.split("```html")[1].split("```")[0].strip()
            elif "```" in raw_html:
                raw_html = raw_html.split("```")[1].split("```")[0].strip()

            # Sanitize LLM output
            # For full-page HTML, we skip bleach (which strips <html>/<head>) and
            # instead just remove script/iframe tags
            import re
            sanitized = re.sub(r"<script[^>]*>.*?</script>", "", raw_html, flags=re.DOTALL | re.IGNORECASE)
            sanitized = re.sub(r"<iframe[^>]*>.*?</iframe>", "", sanitized, flags=re.DOTALL | re.IGNORECASE)

            self.logger.info("generative_html_done", length=len(sanitized))
            return sanitized
        except Exception as e:
            self.logger.error("generative_html_failed", error=str(e))
            return ""
