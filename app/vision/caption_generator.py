from __future__ import annotations
import base64
from app.utils.llm_client import chat
from app.utils.logger import get_logger


class CaptionGenerator:
    SYSTEM_PROMPT = """당신은 AI 기술 이미지 분석 전문가입니다.
주어진 이미지를 분석하고 한국어로 설명해주세요.
이미지에서 중요한 정보(모델 성능 지표, 아키텍처 다이어그램, 벤치마크 결과 등)를 추출해주세요.

응답 형식:
- caption_ko: 이미지 내용 한국어 설명 (1-2문장)
- key_information: 이미지에서 추출한 핵심 정보 목록
- image_type: chart|diagram|screenshot|photo|other"""

    def __init__(self):
        self.logger = get_logger(step="image_analyze")

    async def generate_caption(self, image_data: bytes, context: str = "") -> dict:
        """
        Generate a caption for an image using OpenAI Vision.
        Returns: {caption_ko, key_information, image_type}
        """
        try:
            b64_image = base64.b64encode(image_data).decode()

            messages = [
                {"role": "system", "content": self.SYSTEM_PROMPT},
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": f"기사 맥락: {context[:200]}" if context else "다음 이미지를 분석해주세요."},
                        {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{b64_image}"}},
                    ],
                },
            ]

            content = await chat(messages)
            self.logger.info("caption_generated", length=len(content))

            # Parse response (simple text parsing, not JSON mode since vision doesn't support it)
            return {
                "caption_ko": content,
                "key_information": [],
                "image_type": "other",
                "raw_response": content,
            }
        except Exception as e:
            self.logger.error("caption_failed", error=str(e))
            return {
                "caption_ko": "",
                "key_information": [],
                "image_type": "other",
                "error": str(e),
            }
