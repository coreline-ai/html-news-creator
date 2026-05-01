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


async def chat(messages: list[dict], model: str | None = None) -> str:
    """Stream a chat completion and return the full text. Uses streaming to work with local proxy.

    Wrapped in ``asyncio.wait_for`` so a hung response (e.g. proxy in
    CLOSE_WAIT) cannot stall the calling pipeline indefinitely.

    Emits a structured ``llm_call`` log line per call with input/output token
    counts (tiktoken-estimated) so the operator can grep ``.logs/`` to
    reconcile spend against the proxy.
    """
    model_name = model or settings.openai_model

    async def _run() -> str:
        client = _make_client()
        stream = await client.chat.completions.create(
            model=model_name,
            messages=messages,
            stream=True,
        )
        chunks: list[str] = []
        async for chunk in stream:
            if chunk.choices and chunk.choices[0].delta.content:
                chunks.append(chunk.choices[0].delta.content)
        return "".join(chunks)

    output = await asyncio.wait_for(_run(), timeout=_LLM_TOTAL_TIMEOUT)
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
