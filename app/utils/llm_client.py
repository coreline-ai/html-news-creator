from __future__ import annotations
import asyncio
import json
import os
import re
import httpx
import tiktoken
from openai import AsyncOpenAI
from app.config import settings
from app.utils.logger import get_logger

# Hard upper bound per chat() call. The OpenAI SDK uses httpx under the hood;
# pass a structured Timeout so connect / read / write each get explicit caps.
# A single hung socket (e.g. CLOSE_WAIT against the local proxy) used to keep
# run_daily.py blocked indefinitely on stream iteration. 60s read is plenty
# for a streaming completion; 10s connect catches dead proxies.
_LLM_CONNECT_TIMEOUT = float(os.getenv("OPENAI_CONNECT_TIMEOUT", "10"))
_LLM_READ_TIMEOUT = float(os.getenv("OPENAI_READ_TIMEOUT", "60"))
_LLM_TOTAL_TIMEOUT = float(os.getenv("OPENAI_TOTAL_TIMEOUT", "120"))
_FALSE_VALUES = {"0", "false", "no", "off"}

_logger = get_logger(step="llm")


def _make_client() -> AsyncOpenAI:
    return AsyncOpenAI(
        api_key=settings.openai_api_key,
        base_url=settings.openai_base_url,
        timeout=httpx.Timeout(
            timeout=_LLM_TOTAL_TIMEOUT,
            connect=_LLM_CONNECT_TIMEOUT,
            read=_LLM_READ_TIMEOUT,
            write=_LLM_READ_TIMEOUT,
        ),
        max_retries=1,
    )


def _encoding_for(model: str) -> tiktoken.Encoding:
    # Local proxy models (gpt-5.5, …) aren't in tiktoken's registry. cl100k_base
    # is the right approximation for OpenAI-compatible chat completions and
    # matches gpt-3.5/4 tokenization within a few percent.
    try:
        return tiktoken.encoding_for_model(model)
    except KeyError:
        return tiktoken.get_encoding("cl100k_base")


def _message_content_to_text(content: object) -> str:
    if isinstance(content, str):
        return content
    if isinstance(content, list):
        parts: list[str] = []
        for item in content:
            if isinstance(item, dict):
                parts.append(str(item.get("text") or item.get("content") or ""))
            else:
                parts.append(str(getattr(item, "text", "") or getattr(item, "content", "")))
        return "".join(parts)
    return "" if content is None else str(content)


def _use_stream_first() -> bool:
    """Return whether chat completions should try streaming before non-stream."""
    return os.getenv("OPENAI_CHAT_STREAM", "true").strip().lower() not in _FALSE_VALUES


def _llm_disabled() -> bool:
    return os.getenv("NEWS_LLM_DISABLED", "").strip().lower() not in {"", *_FALSE_VALUES}


async def _stream_chat_completions_raw(
    messages: list[dict],
    model_name: str,
) -> str:
    """Collect OpenAI-compatible SSE deltas without relying on SDK parsing.

    The local proxy emits `event: message` SSE frames for `/chat/completions`.
    Some OpenAI SDK versions iterate those frames but surface no delta text for
    the Codex/GPT route, while the raw `data:` payload contains valid
    `choices[].delta.content`. Parsing the SSE ourselves keeps gpt-5.5 usable
    while remaining compatible with standard OpenAI `data: ...` streams.
    """
    url = f"{str(settings.openai_base_url).rstrip('/')}/chat/completions"
    chunks: list[str] = []
    async with httpx.AsyncClient(
        timeout=httpx.Timeout(
            timeout=_LLM_TOTAL_TIMEOUT,
            connect=_LLM_CONNECT_TIMEOUT,
            read=_LLM_READ_TIMEOUT,
            write=_LLM_READ_TIMEOUT,
        )
    ) as client:
        async with client.stream(
            "POST",
            url,
            headers={
                "Authorization": f"Bearer {settings.openai_api_key}",
                "Content-Type": "application/json",
            },
            json={
                "model": model_name,
                "messages": messages,
                "stream": True,
            },
        ) as response:
            response.raise_for_status()
            async for line in response.aiter_lines():
                if not line.startswith("data:"):
                    continue
                data = line.removeprefix("data:").strip()
                if not data or data == "[DONE]":
                    continue
                try:
                    payload = json.loads(data)
                except json.JSONDecodeError:
                    continue
                choices = payload.get("choices")
                if isinstance(choices, list) and choices:
                    choice = choices[0] if isinstance(choices[0], dict) else {}
                    delta = choice.get("delta")
                    if isinstance(delta, dict) and isinstance(delta.get("content"), str):
                        chunks.append(delta["content"])
                        continue
                    message = choice.get("message")
                    if isinstance(message, dict) and isinstance(message.get("content"), str):
                        chunks.append(message["content"])
                        continue
                if (
                    payload.get("type") == "response.output_text.delta"
                    and isinstance(payload.get("delta"), str)
                ):
                    chunks.append(payload["delta"])
    return "".join(chunks)


async def chat(messages: list[dict], model: str | None = None) -> str:
    """Stream a chat completion and return the full text. Uses streaming to work with local proxy.

    Wrapped in ``asyncio.wait_for`` so a hung response (e.g. proxy in
    CLOSE_WAIT) cannot stall the calling pipeline indefinitely.

    Emits a structured ``llm_call`` log line per call with input/output token
    counts (tiktoken-estimated) so the operator can grep ``.logs/`` to
    reconcile spend against the proxy.
    """
    model_name = model or settings.openai_model
    if _llm_disabled():
        raise RuntimeError("LLM disabled by preflight; using local fallback")

    async def _run_stream() -> str:
        return await _stream_chat_completions_raw(messages, model_name)

    async def _run_non_stream() -> str:
        client = _make_client()
        response = await client.chat.completions.create(
            model=model_name,
            messages=messages,
            stream=False,
        )
        if not response.choices:
            return ""
        return _message_content_to_text(response.choices[0].message.content)

    if _use_stream_first():
        output = await asyncio.wait_for(_run_stream(), timeout=_LLM_TOTAL_TIMEOUT)
        if not output.strip():
            _logger.warning("llm_stream_empty_retrying_non_stream", model=model_name)
            output = await asyncio.wait_for(_run_non_stream(), timeout=_LLM_TOTAL_TIMEOUT)
    else:
        output = await asyncio.wait_for(_run_non_stream(), timeout=_LLM_TOTAL_TIMEOUT)
    if not output.strip():
        raise RuntimeError(f"LLM returned empty output for model {model_name}")
    try:
        enc = _encoding_for(model_name)
        input_tokens = sum(
            len(enc.encode(str(m.get("content", "")))) for m in messages
        )
        output_tokens = len(enc.encode(output))
        _logger.info(
            "llm_call",
            model=model_name,
            input_tokens=input_tokens,
            output_tokens=output_tokens,
            total_tokens=input_tokens + output_tokens,
        )
    except Exception as exc:  # pragma: no cover — telemetry must never fail a run
        _logger.warning("llm_token_count_failed", model=model_name, error=str(exc))
    return output


def extract_json(text: str) -> dict:
    """Extract first JSON object from text (handles markdown code fences)."""
    cleaned = re.sub(r"```(?:json)?\s*", "", text).strip().rstrip("`")
    match = re.search(r"\{.*\}", cleaned, re.DOTALL)
    if match:
        return json.loads(match.group())
    return json.loads(cleaned)
