from __future__ import annotations
import asyncio
import json
import os
import re
import httpx
from openai import AsyncOpenAI
from app.config import settings

# Hard upper bound per chat() call. The OpenAI SDK uses httpx under the hood;
# pass a structured Timeout so connect / read / write each get explicit caps.
# A single hung socket (e.g. CLOSE_WAIT against the local proxy) used to keep
# run_daily.py blocked indefinitely on stream iteration. 60s read is plenty
# for a streaming completion; 10s connect catches dead proxies.
_LLM_CONNECT_TIMEOUT = float(os.getenv("OPENAI_CONNECT_TIMEOUT", "10"))
_LLM_READ_TIMEOUT = float(os.getenv("OPENAI_READ_TIMEOUT", "60"))
_LLM_TOTAL_TIMEOUT = float(os.getenv("OPENAI_TOTAL_TIMEOUT", "120"))


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


async def chat(messages: list[dict], model: str | None = None) -> str:
    """Stream a chat completion and return the full text. Uses streaming to work with local proxy.

    Wrapped in ``asyncio.wait_for`` so a hung response (e.g. proxy in
    CLOSE_WAIT) cannot stall the calling pipeline indefinitely.
    """
    async def _run() -> str:
        client = _make_client()
        stream = await client.chat.completions.create(
            model=model or settings.openai_model,
            messages=messages,
            stream=True,
        )
        chunks: list[str] = []
        async for chunk in stream:
            if chunk.choices and chunk.choices[0].delta.content:
                chunks.append(chunk.choices[0].delta.content)
        return "".join(chunks)

    return await asyncio.wait_for(_run(), timeout=_LLM_TOTAL_TIMEOUT)


def extract_json(text: str) -> dict:
    """Extract first JSON object from text (handles markdown code fences)."""
    cleaned = re.sub(r"```(?:json)?\s*", "", text).strip().rstrip("`")
    match = re.search(r"\{.*\}", cleaned, re.DOTALL)
    if match:
        return json.loads(match.group())
    return json.loads(cleaned)
