"""Unit tests for RelevanceClassifier (Phase 1-B)."""
from __future__ import annotations
import json
from unittest.mock import AsyncMock, patch
import pytest
from app.processors.classifier import RelevanceClassifier


@pytest.mark.asyncio
async def test_tc1_6_classify_success():
    payload = {"is_ai_related": True, "score": 0.9, "category": "model_release", "reason_ko": "AI 모델"}
    with patch("app.processors.classifier.chat", new=AsyncMock(return_value=json.dumps(payload))):
        result = await RelevanceClassifier().classify("GPT-5 Released", "OpenAI released GPT-5.", "item-1")
    assert result["is_ai_related"] is True
    assert result["score"] == pytest.approx(0.9)
    assert result["category"] == "model_release"


@pytest.mark.asyncio
async def test_tc1_e3_classify_openai_error():
    with patch("app.processors.classifier.chat", new=AsyncMock(side_effect=RuntimeError("network error"))):
        result = await RelevanceClassifier().classify("Some Article", "Some content.", "item-2")
    assert result["is_ai_related"] is False
    assert result["score"] == pytest.approx(0.0)
    assert "LLM 분류 실패" in result["reason_ko"]
    assert result["fallback"] is True


@pytest.mark.asyncio
async def test_classify_error_uses_keyword_fallback_for_ai_item():
    with patch("app.processors.classifier.chat", new=AsyncMock(side_effect=RuntimeError("network error"))):
        result = await RelevanceClassifier().classify(
            "OpenAI releases GPT agent API",
            "Developers can build LLM agents with new inference tooling.",
            "item-3",
        )
    assert result["is_ai_related"] is True
    assert result["score"] > 0.0
    assert result["fallback"] is True
