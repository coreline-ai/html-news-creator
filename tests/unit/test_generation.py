"""Unit tests for Phase 4 generation components."""
from __future__ import annotations

import json
from datetime import date
from unittest.mock import AsyncMock, MagicMock

import pytest

from app.generation.embeddings import EmbeddingClient
from app.generation.clusterer import HDBSCANClusterer, ClusterResult
from app.generation.section_generator import SectionGenerator
from app.generation.report_assembler import ReportAssembler
from app.generation.title_generator import TitleGenerator


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _make_embedding_response(vectors: list[list[float]]) -> MagicMock:
    """Build a fake OpenAI embeddings response."""
    items = []
    for vec in vectors:
        item = MagicMock()
        item.embedding = vec
        items.append(item)
    response = MagicMock()
    response.data = items
    return response


def _make_chat_response(payload: dict) -> MagicMock:
    """Build a fake OpenAI ChatCompletion response."""
    message = MagicMock()
    message.content = json.dumps(payload)
    choice = MagicMock()
    choice.message = message
    response = MagicMock()
    response.choices = [choice]
    return response


# ---------------------------------------------------------------------------
# TC-4.1  embed_batch returns correct shape for 2 texts
# ---------------------------------------------------------------------------

@pytest.mark.asyncio
async def test_tc4_1_embed_batch_two_texts():
    """Mock OpenAI to return 1536-dim vectors for 2 texts → list of 2 vectors each length 1536."""
    vectors = [[0.0] * 1536, [1.0] * 1536]
    fake_response = _make_embedding_response(vectors)

    client = EmbeddingClient()
    client.client = MagicMock()
    client.client.embeddings = MagicMock()
    client.client.embeddings.create = AsyncMock(return_value=fake_response)

    result = await client.embed_batch(["hello", "world"])

    assert len(result) == 2
    assert len(result[0]) == 1536
    assert len(result[1]) == 1536
    client.client.embeddings.create.assert_called_once()


# ---------------------------------------------------------------------------
# TC-4.2  embed_batch([]) returns [] without API call
# ---------------------------------------------------------------------------

@pytest.mark.asyncio
async def test_tc4_2_embed_batch_empty():
    """embed_batch([]) → returns [] with no API call."""
    client = EmbeddingClient()
    client.client = MagicMock()
    client.client.embeddings = MagicMock()
    client.client.embeddings.create = AsyncMock()

    result = await client.embed_batch([])

    assert result == []
    client.client.embeddings.create.assert_not_called()


# ---------------------------------------------------------------------------
# TC-4.3  HDBSCANClusterer.cluster([]) → n_clusters=0
# ---------------------------------------------------------------------------

def test_tc4_3_cluster_empty():
    """cluster([]) → ClusterResult with n_clusters=0 and empty labels."""
    clusterer = HDBSCANClusterer()
    result = clusterer.cluster([])

    assert isinstance(result, ClusterResult)
    assert result.n_clusters == 0
    assert result.labels == []
    assert result.noise_count == 0
    assert result.cluster_sizes == {}


# ---------------------------------------------------------------------------
# TC-4.4  HDBSCANClusterer.cluster with 2 embeddings → labels length 2
# ---------------------------------------------------------------------------

def test_tc4_4_cluster_two_embeddings():
    """cluster with 2 1536-dim embeddings → labels list of length 2."""
    vec1 = [1.0] + [0.0] * 1535
    vec2 = [0.0] * 1535 + [1.0]
    clusterer = HDBSCANClusterer(min_cluster_size=2)

    result = clusterer.cluster([vec1, vec2])

    assert isinstance(result, ClusterResult)
    assert len(result.labels) == 2


# ---------------------------------------------------------------------------
# TC-4.5  SectionGenerator.generate() with mocked OpenAI
# ---------------------------------------------------------------------------

@pytest.mark.asyncio
async def test_tc4_5_section_generator_success():
    """Mock OpenAI → SectionGenerator.generate() returns dict with title_ko and summary_ko."""
    payload = {
        "title_ko": "GPT-5 출시",
        "fact_summary": "OpenAI가 GPT-5를 발표했다.",
        "social_signal_summary": None,
        "inference_summary": None,
        "summary_ko": "OpenAI가 GPT-5를 공식 출시했다. 성능이 크게 향상되었다.",
        "importance_score": 0.9,
        "category": "model_release",
    }
    import json
    from unittest.mock import patch as mock_patch, AsyncMock

    items = [{"title": "GPT-5 Released", "content_text": "OpenAI released GPT-5.", "url": "https://example.com"}]
    with mock_patch("app.generation.section_generator.chat", new=AsyncMock(return_value=json.dumps(payload))):
        result = await SectionGenerator().generate("cluster-1", items)

    assert "title_ko" in result
    assert "summary_ko" in result
    assert result["title_ko"] == "GPT-5 출시"
    assert result["importance_score"] == 0.9


# ---------------------------------------------------------------------------
# TC-4.6  SectionGenerator.generate([]) → importance_score=0.0, no API call
# ---------------------------------------------------------------------------

@pytest.mark.asyncio
async def test_tc4_6_section_generator_empty_items():
    """SectionGenerator.generate([]) → dict with importance_score=0.0, no API call."""
    result = await SectionGenerator().generate("cluster-empty", [])

    assert result["importance_score"] == 0.0
    assert "title_ko" in result
    assert "summary_ko" in result


# ---------------------------------------------------------------------------
# TC-4.7  ReportAssembler.assemble() — 3 sections sorted by importance_score
# ---------------------------------------------------------------------------

def test_tc4_7_report_assembler_sorts_sections():
    """assemble() with 3 sections → sorted by importance_score desc, stats.clusters=3."""
    assembler = ReportAssembler()
    sections = [
        {"title_ko": "섹션A", "summary_ko": "A 요약", "importance_score": 0.5, "category": "other"},
        {"title_ko": "섹션B", "summary_ko": "B 요약", "importance_score": 0.9, "category": "model_release"},
        {"title_ko": "섹션C", "summary_ko": "C 요약", "importance_score": 0.3, "category": "research"},
    ]

    report = assembler.assemble(
        run_date=date(2026, 4, 27),
        title="오늘의 AI 트렌드",
        sections=sections,
    )

    assert report.stats["clusters"] == 3
    # Must be sorted descending by importance_score
    scores = [s["importance_score"] for s in report.sections]
    assert scores == sorted(scores, reverse=True)
    assert report.sections[0]["title_ko"] == "섹션B"
    assert report.report_date == "2026-04-27"
    assert report.title == "오늘의 AI 트렌드"


# ---------------------------------------------------------------------------
# TC-4.8  TitleGenerator.generate_titles() with mocked OpenAI
# ---------------------------------------------------------------------------

@pytest.mark.asyncio
async def test_tc4_8_title_generator_success():
    """Mock OpenAI → TitleGenerator.generate_titles() returns list of str."""
    payload = {
        "titles": [
            "GPT-5 공개, AI 시대 새 장",
            "구글 Gemini 2.0 업데이트",
            "오픈소스 LLM 급성장",
            "AI 규제 논의 가속화",
            "메타 Llama 4 출시 임박",
        ]
    }
    import json
    from unittest.mock import patch as mock_patch, AsyncMock

    with mock_patch("app.generation.title_generator.chat", new=AsyncMock(return_value=json.dumps(payload))):
        titles = await TitleGenerator().generate_titles("GPT-5 출시. 구글 Gemini 업데이트.")

    assert isinstance(titles, list)
    assert len(titles) == 5
    assert all(isinstance(t, str) for t in titles)
