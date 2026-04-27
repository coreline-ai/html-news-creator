from __future__ import annotations
import json
import re
from openai import AsyncOpenAI
from app.config import settings


def _make_client() -> AsyncOpenAI:
    return AsyncOpenAI(
        api_key=settings.openai_api_key,
        base_url=settings.openai_base_url,
    )


async def chat(messages: list[dict], model: str | None = None) -> str:
    """Stream a chat completion and return the full text. Uses streaming to work with local proxy."""
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


def extract_json(text: str) -> dict:
    """Extract first JSON object from text (handles markdown code fences)."""
    cleaned = re.sub(r"```(?:json)?\s*", "", text).strip().rstrip("`")
    match = re.search(r"\{.*\}", cleaned, re.DOTALL)
    if match:
        return json.loads(match.group())
    return json.loads(cleaned)
