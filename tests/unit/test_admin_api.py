"""
Unit tests for Phase 7 — Admin API.

TC-7.1: GET /health → 200, {"status": "ok"}
TC-7.2: GET /api/v1/runs → 200, returns {"runs": [...]}
TC-7.3: GET /api/v1/reports → 200, returns {"reports": [...]}
TC-7.4: GET /api/v1/stats/today → 200, returns dict with "date" key
TC-7.5: GET /api/v1/sources → 200, returns {"sources": [...]}
"""
from __future__ import annotations

from unittest.mock import AsyncMock, MagicMock

import pytest
from fastapi.testclient import TestClient

from app.admin.api import app
from app.db import get_db


# ---------------------------------------------------------------------------
# DB dependency override
# ---------------------------------------------------------------------------

async def mock_db():
    mock = AsyncMock()
    # scalars().all() returns an empty list for list endpoints
    scalars_mock = MagicMock()
    scalars_mock.all.return_value = []
    execute_result = MagicMock()
    execute_result.scalars.return_value = scalars_mock
    # scalar() returns 0 for count queries
    execute_result.scalar.return_value = 0
    mock.execute.return_value = execute_result
    yield mock


app.dependency_overrides[get_db] = mock_db

client = TestClient(app)


# ---------------------------------------------------------------------------
# TC-7.1: GET /health
# ---------------------------------------------------------------------------

def test_health_returns_ok():
    """TC-7.1: GET /health returns 200 with status ok."""
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "ok"
    assert "service" in data


# ---------------------------------------------------------------------------
# TC-7.2: GET /api/v1/runs
# ---------------------------------------------------------------------------

def test_list_runs_returns_runs_key():
    """TC-7.2: GET /api/v1/runs returns 200 with runs list."""
    response = client.get("/api/v1/runs")
    assert response.status_code == 200
    data = response.json()
    assert "runs" in data
    assert isinstance(data["runs"], list)


def test_list_runs_respects_limit_param():
    """TC-7.2: limit query param is accepted without error."""
    response = client.get("/api/v1/runs?limit=5")
    assert response.status_code == 200
    assert "runs" in response.json()


# ---------------------------------------------------------------------------
# TC-7.3: GET /api/v1/reports
# ---------------------------------------------------------------------------

def test_list_reports_returns_reports_key():
    """TC-7.3: GET /api/v1/reports returns 200 with reports list."""
    response = client.get("/api/v1/reports")
    assert response.status_code == 200
    data = response.json()
    assert "reports" in data
    assert isinstance(data["reports"], list)


# ---------------------------------------------------------------------------
# TC-7.4: GET /api/v1/stats/today
# ---------------------------------------------------------------------------

def test_today_stats_returns_date_key():
    """TC-7.4: GET /api/v1/stats/today returns 200 with date key."""
    response = client.get("/api/v1/stats/today")
    assert response.status_code == 200
    data = response.json()
    assert "date" in data
    assert "raw_items" in data
    assert "clusters" in data


def test_today_stats_counts_are_integers():
    """TC-7.4: raw_items and clusters are integers."""
    response = client.get("/api/v1/stats/today")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data["raw_items"], int)
    assert isinstance(data["clusters"], int)


# ---------------------------------------------------------------------------
# TC-7.5: GET /api/v1/sources
# ---------------------------------------------------------------------------

def test_list_sources_returns_sources_key():
    """TC-7.5: GET /api/v1/sources returns 200 with sources list."""
    response = client.get("/api/v1/sources")
    assert response.status_code == 200
    data = response.json()
    assert "sources" in data
    assert isinstance(data["sources"], list)


def test_list_sources_active_only_false():
    """TC-7.5: active_only=false query param is accepted without error."""
    response = client.get("/api/v1/sources?active_only=false")
    assert response.status_code == 200
    assert "sources" in response.json()
