from __future__ import annotations

from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from app.utils.llm_client import chat


class _EmptyAsyncStream:
    def __aiter__(self):
        return self

    async def __anext__(self):
        raise StopAsyncIteration


@pytest.mark.asyncio
async def test_chat_retries_non_stream_when_stream_is_empty():
    response = MagicMock()
    message = MagicMock()
    message.content = '{"ok": true}'
    choice = MagicMock()
    choice.message = message
    response.choices = [choice]

    with (
        patch(
            "app.utils.llm_client._stream_chat_completions_raw",
            AsyncMock(return_value=""),
        ) as stream_create,
        patch("app.utils.llm_client.AsyncOpenAI") as mock_cls,
    ):
        create = AsyncMock(return_value=response)
        mock_cls.return_value.chat.completions.create = create

        result = await chat([{"role": "user", "content": "ping"}], model="test-model")

    assert result == '{"ok": true}'
    assert stream_create.await_count == 1
    assert create.await_count == 1
    assert create.await_args.kwargs["stream"] is False


@pytest.mark.asyncio
async def test_chat_uses_raw_stream_when_available():
    with (
        patch(
            "app.utils.llm_client._stream_chat_completions_raw",
            AsyncMock(return_value='{"ok": true}'),
        ) as stream_create,
        patch("app.utils.llm_client.AsyncOpenAI") as mock_cls,
    ):
        result = await chat([{"role": "user", "content": "ping"}], model="test-model")

    assert result == '{"ok": true}'
    assert stream_create.await_count == 1
    mock_cls.return_value.chat.completions.create.assert_not_called()


@pytest.mark.asyncio
async def test_chat_can_skip_streaming_with_env(monkeypatch):
    monkeypatch.setenv("OPENAI_CHAT_STREAM", "false")
    response = MagicMock()
    message = MagicMock()
    message.content = '{"ok": true}'
    choice = MagicMock()
    choice.message = message
    response.choices = [choice]

    with patch("app.utils.llm_client.AsyncOpenAI") as mock_cls:
        create = AsyncMock(return_value=response)
        mock_cls.return_value.chat.completions.create = create

        result = await chat([{"role": "user", "content": "ping"}], model="test-model")

    assert result == '{"ok": true}'
    assert create.await_count == 1
    assert create.await_args.kwargs["stream"] is False


@pytest.mark.asyncio
async def test_chat_raises_when_output_is_empty(monkeypatch):
    monkeypatch.setenv("OPENAI_CHAT_STREAM", "false")
    response = MagicMock()
    message = MagicMock()
    message.content = ""
    choice = MagicMock()
    choice.message = message
    response.choices = [choice]

    with patch("app.utils.llm_client.AsyncOpenAI") as mock_cls:
        mock_cls.return_value.chat.completions.create = AsyncMock(return_value=response)

        with pytest.raises(RuntimeError, match="LLM returned empty output"):
            await chat([{"role": "user", "content": "ping"}], model="test-model")
