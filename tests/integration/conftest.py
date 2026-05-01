"""Shared fixtures for News Studio integration tests.

These tests exercise the FastAPI app through an in-memory ASGI transport
(``httpx.AsyncClient`` + ``ASGITransport``), so they validate the actual
HTTP/SSE contract without needing a live uvicorn process. The DB layer is
replaced with an ``AsyncMock`` (mirroring ``tests/unit/test_admin_api.py``)
so we don't need Postgres — the integration value here is the *FastAPI
wiring* (routing, validation, SSE framing, dependency injection), not the
ORM round-trip.

External services (LLM proxy, Netlify, asyncio subprocesses) are mocked at
the module boundary by individual tests. No tests in this directory should
ever attempt a real network call.

A module-level ``pytestmark`` of ``integration`` is auto-applied by the
``pytest_collection_modifyitems`` hook below so callers can opt in/out via
``pytest -m integration`` / ``-m "not integration"``.
"""
from __future__ import annotations

from typing import AsyncIterator
from unittest.mock import AsyncMock, MagicMock

import pytest
import pytest_asyncio
from httpx import ASGITransport, AsyncClient

from app.admin.api import app
from app.db import get_db


def pytest_collection_modifyitems(config, items):
    """Auto-apply the ``integration`` marker to every test in this folder.

    Keeps individual test files free of boilerplate while still allowing the
    ``pytest -m "not integration"`` filter used by ``.github/workflows/ci.yml``
    to skip them in the unit suite.
    """
    for item in items:
        if "tests/integration/" in str(item.fspath).replace("\\", "/"):
            item.add_marker(pytest.mark.integration)


# ---------------------------------------------------------------------------
# DB dependency override — keep us off Postgres.
# ---------------------------------------------------------------------------

def _empty_db_factory():
    """Return an async generator that yields a fresh AsyncMock session.

    The mock answers ``execute()`` with an empty result set so plain GETs
    return ``[]``/``{}`` without raising. Tests that need richer DB state
    install their own override on top of this default.
    """
    async def _gen():
        mock = AsyncMock()
        scalars_mock = MagicMock()
        scalars_mock.all.return_value = []
        scalars_mock.first.return_value = None
        execute_result = MagicMock()
        execute_result.scalars.return_value = scalars_mock
        execute_result.scalar.return_value = 0
        mock.execute.return_value = execute_result
        yield mock

    return _gen


@pytest.fixture(autouse=True)
def _install_default_db_override():
    """Reset the ``get_db`` override around every test.

    Tests that need report rows can install their own override via
    ``app.dependency_overrides[get_db] = ...`` — this fixture restores the
    empty default after they finish so subsequent tests start clean.
    """
    app.dependency_overrides[get_db] = _empty_db_factory()
    try:
        yield
    finally:
        app.dependency_overrides.pop(get_db, None)


# ---------------------------------------------------------------------------
# httpx AsyncClient bound to the ASGI app (no socket, no port, no uvicorn).
# ---------------------------------------------------------------------------

@pytest_asyncio.fixture
async def async_client() -> AsyncIterator[AsyncClient]:
    """Yield an ``httpx.AsyncClient`` that drives the FastAPI app in-process."""
    transport = ASGITransport(app=app)
    async with AsyncClient(
        transport=transport, base_url="http://testserver"
    ) as client:
        yield client


__all__ = ["async_client"]
