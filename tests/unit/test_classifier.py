"""Unit tests for RelevanceClassifier (Phase 1-B)."""
from __future__ import annotations
import json
from unittest.mock import AsyncMock, patch
import pytest
from app.processors.classifier import RelevanceClassifier


@pytest.mark.asyncio
async def test_tc1_6_classify_success():
    payload = {"is_ai_related": True, "score": 0.9, "category": "model_release", "reason_ko": "AI 모델"}
    with patch("app.utils.llm_client.AsyncOpenAI") as mock_cls:
        mock_stream = AsyncMock()
        mock_stream.__aiter__ = lambda self: self
        mock_stream.__anext__ = AsyncMock(side_effect=[
            _chunk(json.dumps(payload)),
            StopAsyncIteration,
        ])
        mock_cls.return_value.chat.completions.create = AsyncMock(return_value=mock_stream)
        result = await RelevanceClassifier().classify("GPT-5 Released", "OpenAI released GPT-5.", "item-1")
    assert result["is_ai_related"] is True
    assert result["score"] == pytest.approx(0.9)
    assert result["category"] == "model_release"


@pytest.mark.asyncio
async def test_tc1_e3_classify_openai_error():
    with patch("app.utils.llm_client.AsyncOpenAI") as mock_cls:
        mock_cls.return_value.chat.completions.create = AsyncMock(side_effect=RuntimeError("network error"))
        result = await RelevanceClassifier().classify("Some Article", "Some content.", "item-2")
    assert result["is_ai_related"] is False
    assert result["score"] == pytest.approx(0.0)
    assert "분류 실패" in result["reason_ko"]


def _chunk(text: str):
    from unittest.mock import MagicMock
    delta = MagicMock(); delta.content = text
    choice = MagicMock(); choice.delta = delta
    chunk = MagicMock(); chunk.choices = [choice]
    return chunk
