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

    with patch("app.utils.llm_client.AsyncOpenAI") as mock_cls:
        create = AsyncMock(side_effect=[_EmptyAsyncStream(), response])
        mock_cls.return_value.chat.completions.create = create

        result = await chat([{"role": "user", "content": "ping"}], model="test-model")

    assert result == '{"ok": true}'
    assert create.await_count == 2
    assert create.await_args_list[0].kwargs["stream"] is True
    assert create.await_args_list[1].kwargs["stream"] is False
