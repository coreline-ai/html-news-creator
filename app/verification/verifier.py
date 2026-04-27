from __future__ import annotations
from app.utils.llm_client import chat, extract_json
from app.utils.logger import get_logger
from app.verification.domain_registry import DomainRegistry
from app.verification.source_classifier import classify_source_type
from app.verification.trust_scorer import score as compute_trust_score


VERIFY_SYSTEM = """당신은 AI 뉴스 공식 출처 검증 전문가입니다.
주어진 클러스터의 제목, 요약, 출처 URL 목록을 분석하여 공식 출처 검증을 수행하세요.

응답은 반드시 JSON으로만 하세요:
{
  "verification_status": "official_confirmed|github_confirmed|paper_confirmed|trusted_media_only|social_only|unverified",
  "evidence_summary": "검증 근거 요약 (한국어)",
  "confirmed_facts": ["사실로 확인된 항목 (한국어)"],
  "unverified_claims": ["미검증 주장 (한국어)"]
}"""

VERIFY_USER = """클러스터 제목: {title}
요약: {summary}
출처 URL 목록:
{sources}

위 내용의 공식 출처를 검증해주세요."""


class SourceVerifier:
    def __init__(self):
        self.domain_registry = DomainRegistry()
        self.logger = get_logger(step="verify")

    async def verify(
        self,
        cluster_id: str,
        title: str,
        summary: str,
        source_urls: list[str],
    ) -> dict:
        """
        Verify a cluster's claims against official sources.
        Returns dict with: verification_status, trust_score, evidence_summary,
                          confirmed_facts, unverified_claims
        """
        if not source_urls:
            return {
                "verification_status": "unverified",
                "trust_score": 5,
                "evidence_summary": "출처 URL 없음",
                "confirmed_facts": [],
                "unverified_claims": [title],
            }

        # Domain-level classification (no LLM needed for clear official sources)
        official_sources = [u for u in source_urls if self.domain_registry.classify(u) == "official"]
        if official_sources:
            auto_status = "official_confirmed"
        else:
            paper_sources = [u for u in source_urls if classify_source_type(u) == "paper_arxiv"]
            github_sources = [u for u in source_urls if classify_source_type(u) == "official_github"]
            if paper_sources:
                auto_status = "paper_confirmed"
            elif github_sources:
                auto_status = "github_confirmed"
            else:
                auto_status = None

        # LLM verification for ambiguous cases
        if auto_status is None:
            try:
                sources_text = "\n".join(f"- {u}" for u in source_urls[:10])
                text = await chat([
                    {"role": "system", "content": VERIFY_SYSTEM},
                    {"role": "user", "content": VERIFY_USER.format(
                        title=title,
                        summary=summary[:500],
                        sources=sources_text,
                    )},
                ])
                llm_result = extract_json(text)
                verification_status = llm_result.get("verification_status", "unverified")
                evidence_summary = llm_result.get("evidence_summary", "")
                confirmed_facts = llm_result.get("confirmed_facts", [])
                unverified_claims = llm_result.get("unverified_claims", [])
            except Exception as e:
                self.logger.error("verify_llm_failed", cluster_id=cluster_id, error=str(e))
                verification_status = "unverified"
                evidence_summary = f"LLM 검증 실패: {e}"
                confirmed_facts = []
                unverified_claims = []
        else:
            verification_status = auto_status
            evidence_summary = f"도메인 분석으로 자동 검증: {official_sources[:3]}"
            confirmed_facts = [title]
            unverified_claims = []

        # Calculate trust score
        primary_source_type = classify_source_type(source_urls[0]) if source_urls else "unknown"
        trust_score = compute_trust_score(verification_status, primary_source_type, len(source_urls))

        result = {
            "verification_status": verification_status,
            "trust_score": trust_score,
            "evidence_summary": evidence_summary,
            "confirmed_facts": confirmed_facts,
            "unverified_claims": unverified_claims,
        }
        self.logger.info("verify_done", cluster_id=cluster_id, status=verification_status, trust_score=trust_score)
        return result
