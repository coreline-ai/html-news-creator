from __future__ import annotations

import asyncio
from datetime import date

import pytest

import scripts.run_daily as run_daily


async def _noop_preflight(*args: object, **kwargs: object) -> None:
    return None


def test_run_pipeline_raises_on_critical_step_failure(monkeypatch):
    async def _boom(*args, **kwargs):
        raise ModuleNotFoundError("No module named 'tiktoken'")

    monkeypatch.setattr(run_daily, "run_llm_preflight", _noop_preflight)
    monkeypatch.setitem(run_daily.STEP_FUNCTIONS, "classify", _boom)

    with pytest.raises(ModuleNotFoundError, match="tiktoken"):
        asyncio.run(
            run_daily.run_pipeline(
                date(2026, 5, 8),
                mode="full",
                from_step="classify",
                to_step="classify",
                dry_run=False,
            )
        )


def test_run_pipeline_continues_when_generate_produces_no_sections(monkeypatch):
    async def _empty_generate(*args, **kwargs):
        return {"sections": 0}

    monkeypatch.setattr(run_daily, "run_llm_preflight", _noop_preflight)
    monkeypatch.setitem(run_daily.STEP_FUNCTIONS, "generate", _empty_generate)

    asyncio.run(
        run_daily.run_pipeline(
            date(2026, 5, 8),
            mode="full",
            from_step="generate",
            to_step="generate",
            dry_run=False,
        )
    )


def test_run_pipeline_allows_zero_section_dry_run(monkeypatch):
    async def _empty_generate(*args, **kwargs):
        return {"sections": 0}

    monkeypatch.setattr(run_daily, "run_llm_preflight", _noop_preflight)
    monkeypatch.setitem(run_daily.STEP_FUNCTIONS, "generate", _empty_generate)

    asyncio.run(
        run_daily.run_pipeline(
            date(2026, 5, 8),
            mode="full",
            from_step="generate",
            to_step="generate",
            dry_run=True,
        )
    )
