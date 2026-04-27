"""Unit tests for Phase 3 OCR/Vision components."""
from __future__ import annotations

import hashlib
from unittest.mock import AsyncMock, MagicMock, patch

import pytest
import httpx

from app.vision.media_downloader import MediaDownloader
from app.vision.ocr_orchestrator import OCROrchestrator
from app.vision.ocr_paddle import PaddleOCRUnavailableError
from app.vision.ocr_surya import SuryaOCRUnavailableError
from app.vision.caption_generator import CaptionGenerator

pytestmark = pytest.mark.asyncio

# ---------------------------------------------------------------------------
# Minimal valid PNG bytes (1x1)
# ---------------------------------------------------------------------------
_TINY_PNG = (
    b"\x89PNG\r\n\x1a\n"
    b"\x00\x00\x00\rIHDR"
    b"\x00\x00\x00\x01\x00\x00\x00\x01"
    b"\x08\x02\x00\x00\x00\x90wS\xde"
    b"\x00\x00\x00\x0cIDATx\x9cc\xf8\x0f\x00"
    b"\x00\x01\x01\x00\x18\xdd\x8d\xb4"
    b"\x00\x00\x00\x00IEND\xaeB`\x82"
)


def _make_mock_response(content: bytes, content_type: str, status_code: int = 200) -> MagicMock:
    """Build a mock httpx.Response."""
    mock_resp = MagicMock(spec=httpx.Response)
    mock_resp.status_code = status_code
    mock_resp.content = content
    mock_resp.headers = {"content-type": content_type}
    mock_resp.raise_for_status = MagicMock()
    return mock_resp


# ===========================================================================
# TC-3.1: download() with valid PNG → returns dict with sha256 and mime_type
# ===========================================================================
async def test_download_valid_png():
    url = "https://example.com/image.png"
    mock_resp = _make_mock_response(_TINY_PNG, "image/png")

    mock_client = AsyncMock()
    mock_client.get = AsyncMock(return_value=mock_resp)
    mock_client.__aenter__ = AsyncMock(return_value=mock_client)
    mock_client.__aexit__ = AsyncMock(return_value=False)

    with patch("httpx.AsyncClient", return_value=mock_client):
        downloader = MediaDownloader()
        result = await downloader.download(url)

    assert result is not None
    assert result["mime_type"] == "image/png"
    assert result["sha256"] == hashlib.sha256(_TINY_PNG).hexdigest()
    assert result["size_bytes"] == len(_TINY_PNG)
    assert result["url"] == url
    assert "storage_path" in result
    assert result["storage_path"].endswith(".png")


# ===========================================================================
# TC-3.2: download() when server returns HTML → returns None
# ===========================================================================
async def test_download_html_returns_none():
    url = "https://example.com/page.html"
    mock_resp = _make_mock_response(
        b"<html><body>Hello</body></html>",
        "text/html; charset=utf-8",
    )

    mock_client = AsyncMock()
    mock_client.get = AsyncMock(return_value=mock_resp)
    mock_client.__aenter__ = AsyncMock(return_value=mock_client)
    mock_client.__aexit__ = AsyncMock(return_value=False)

    with patch("httpx.AsyncClient", return_value=mock_client):
        downloader = MediaDownloader()
        result = await downloader.download(url)

    assert result is None


# ===========================================================================
# TC-3.3: download() with SSRF URL → returns None (no HTTP call made)
# ===========================================================================
async def test_download_ssrf_blocked():
    downloader = MediaDownloader()
    result = await downloader.download("http://169.254.169.254/img.png")
    assert result is None


# ===========================================================================
# TC-3.4: download() after max_images_per_run limit reached → returns None
# ===========================================================================
async def test_download_respects_max_images_per_run():
    url = "https://example.com/image.png"

    mock_client = AsyncMock()
    mock_client.__aenter__ = AsyncMock(return_value=mock_client)
    mock_client.__aexit__ = AsyncMock(return_value=False)

    with patch("httpx.AsyncClient", return_value=mock_client):
        downloader = MediaDownloader()
        from app.config import settings
        downloader._download_count = settings.max_images_per_run

        result = await downloader.download(url)

    assert result is None
    # Verify no HTTP call was made
    mock_client.get.assert_not_called()


# ===========================================================================
# TC-3.5: OCROrchestrator — both engines unavailable → returns None
# ===========================================================================
async def test_ocr_orchestrator_both_unavailable():
    orchestrator = OCROrchestrator.__new__(OCROrchestrator)
    from app.utils.logger import get_logger
    orchestrator.logger = get_logger(step="image_analyze")

    mock_paddle = MagicMock()
    mock_paddle.extract_text = AsyncMock(
        side_effect=PaddleOCRUnavailableError("paddleocr not installed")
    )

    mock_surya = MagicMock()
    mock_surya.extract_text = AsyncMock(
        side_effect=SuryaOCRUnavailableError("surya-ocr not installed")
    )

    orchestrator.paddle = mock_paddle
    orchestrator.surya = mock_surya

    result = await orchestrator.extract_text(b"fake image data")
    assert result is None


# ===========================================================================
# TC-3.6: CaptionGenerator — mock OpenAI → returns dict with caption_ko
# ===========================================================================
async def test_caption_generator_returns_dict():
    generator = CaptionGenerator.__new__(CaptionGenerator)
    from app.utils.logger import get_logger
    generator.logger = get_logger(step="image_analyze")

    expected_text = "이 이미지는 GPT-4 벤치마크 결과를 보여주는 차트입니다."

    mock_message = MagicMock()
    mock_message.content = expected_text

    mock_choice = MagicMock()
    mock_choice.message = mock_message

    mock_response = MagicMock()
    mock_response.choices = [mock_choice]

    mock_client = MagicMock()
    mock_client.chat.completions.create = AsyncMock(return_value=mock_response)
    generator.client = mock_client

    result = await generator.generate_caption(_TINY_PNG, context="AI benchmark results")

    assert isinstance(result, dict)
    assert "caption_ko" in result
    assert result["caption_ko"] == expected_text
    assert "key_information" in result
    assert "image_type" in result


# ===========================================================================
# TC-3.E1: download() when httpx raises an exception → returns None
# ===========================================================================
async def test_download_httpx_exception_returns_none():
    url = "https://example.com/broken.png"

    mock_client = AsyncMock()
    mock_client.get = AsyncMock(side_effect=httpx.ConnectError("connection refused"))
    mock_client.__aenter__ = AsyncMock(return_value=mock_client)
    mock_client.__aexit__ = AsyncMock(return_value=False)

    with patch("httpx.AsyncClient", return_value=mock_client):
        downloader = MediaDownloader()
        result = await downloader.download(url)

    assert result is None
