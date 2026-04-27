"""Unit tests for RelevanceClassifier (Phase 1-B)."""
from __future__ import annotations

import json
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from app.processors.classifier import RelevanceClassifier


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _make_openai_response(payload: dict) -> MagicMock:
    """Build a fake OpenAI ChatCompletion response object."""
    message = MagicMock()
    message.content = json.dumps(payload)

    choice = MagicMock()
    choice.message = message

    response = MagicMock()
    response.choices = [choice]
    return response


# ---------------------------------------------------------------------------
# TC-1.6  Successful classification returns correct fields
# ---------------------------------------------------------------------------

@pytest.mark.asyncio
async def test_tc1_6_classify_success():
    """OpenAI returns a valid JSON payload → classifier propagates is_ai_related and score."""
    payload = {
        "is_ai_related": True,
        "score": 0.9,
        "category": "model_release",
        "reason_ko": "AI 모델",
    }

    with patch("app.processors.classifier.AsyncOpenAI") as mock_openai_cls:
        mock_client = MagicMock()
        mock_client.chat.completions.create = AsyncMock(
            return_value=_make_openai_response(payload)
        )
        mock_openai_cls.return_value = mock_client

        classifier = RelevanceClassifier()
        result = await classifier.classify(
            title="GPT-5 Released",
            content="OpenAI released GPT-5 today with major improvements.",
            item_id="item-tc16",
        )

    assert result["is_ai_related"] is True
    assert result["score"] == pytest.approx(0.9)
    assert result["category"] == "model_release"
    assert "reason_ko" in result


# ---------------------------------------------------------------------------
# TC-1.E3  OpenAI raises exception → returns safe fallback dict
# ---------------------------------------------------------------------------

@pytest.mark.asyncio
async def test_tc1_e3_classify_openai_error():
    """When OpenAI raises an exception, classifier returns a safe fallback with score=0.0."""
    with patch("app.processors.classifier.AsyncOpenAI") as mock_openai_cls:
        mock_client = MagicMock()
        mock_client.chat.completions.create = AsyncMock(
            side_effect=RuntimeError("network error")
        )
        mock_openai_cls.return_value = mock_client

        classifier = RelevanceClassifier()
        result = await classifier.classify(
            title="Some Article",
            content="Some content here.",
            item_id="item-tc1e3",
        )

    assert result["is_ai_related"] is False
    assert result["score"] == pytest.approx(0.0)
    assert result["category"] == "other"
    assert "분류 실패" in result["reason_ko"]
