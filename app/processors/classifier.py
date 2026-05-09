from __future__ import annotations
from app.utils.llm_client import chat, extract_json
from app.utils.logger import get_logger

_AI_KEYWORDS = (
    "ai",
    "artificial intelligence",
    "machine learning",
    "deep learning",
    "llm",
    "gpt",
    "openai",
    "anthropic",
    "claude",
    "gemini",
    "llama",
    "mistral",
    "hugging face",
    "transformer",
    "embedding",
    "inference",
    "agent",
    "rag",
    "model",
    "neural",
    "인공지능",
    "생성형",
    "머신러닝",
    "딥러닝",
    "모델",
    "추론",
    "에이전트",
)

_RESEARCH_KEYWORDS = ("arxiv", "paper", "benchmark", "논문", "연구", "평가")
_PRODUCT_KEYWORDS = ("launch", "release", "api", "preview", "출시", "공개", "업데이트")
_SAFETY_KEYWORDS = ("safety", "policy", "regulation", "보안", "안전", "규제", "정책")
_INFRA_KEYWORDS = ("gpu", "chip", "server", "cloud", "infrastructure", "데이터센터", "칩", "클라우드")

CLASSIFY_SYSTEM = """당신은 AI 트렌드 리포트 분류 전문가입니다.
주어진 텍스트가 AI/ML 관련 내용인지 분류하고 0~1 점수를 부여하세요.

응답은 반드시 JSON으로만 하세요:
{
  "is_ai_related": true/false,
  "score": 0.0~1.0,
  "category": "model_release|research_paper|product_launch|safety|infrastructure|other",
  "reason_ko": "한국어로 분류 이유 설명"
}"""


def _fallback_classification(title: str, content: str, error: Exception) -> dict:
    text = f"{title}\n{content}".lower()
    hits = [keyword for keyword in _AI_KEYWORDS if keyword in text]
    is_ai_related = bool(hits)
    score = min(0.75, 0.35 + len(hits) * 0.08) if is_ai_related else 0.0

    if any(keyword in text for keyword in _RESEARCH_KEYWORDS):
        category = "research_paper"
    elif any(keyword in text for keyword in _SAFETY_KEYWORDS):
        category = "safety"
    elif any(keyword in text for keyword in _INFRA_KEYWORDS):
        category = "infrastructure"
    elif any(keyword in text for keyword in _PRODUCT_KEYWORDS):
        category = "product_launch"
    elif any(keyword in text for keyword in ("gpt", "llm", "model", "모델")):
        category = "model_release"
    else:
        category = "other"

    reason = (
        f"LLM 분류 실패 후 키워드 폴백 적용: {', '.join(hits[:5])}"
        if hits
        else f"LLM 분류 실패 후 AI 키워드 미검출: {error}"
    )
    return {
        "is_ai_related": is_ai_related,
        "score": score,
        "category": category,
        "reason_ko": reason,
        "fallback": True,
    }


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
            result = _fallback_classification(title, content, e)
            self.logger.warning(
                "classified_with_fallback",
                item_id=item_id,
                score=result.get("score"),
                category=result.get("category"),
            )
            return result
