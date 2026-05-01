"""Health + read-only contract checks against the live ASGI app.

Anything that mutates state lives in the other integration files; this one
just confirms the four "always-on" endpoints respond with the documented
shape. The yaml-backed fixtures (sources registry, editorial policy) are
read straight off disk so any drift between the docs and the actual files
shows up here.
"""
from __future__ import annotations

import pytest

# All tests in this module talk to the FastAPI app through the in-memory
# ASGI transport set up by conftest.async_client.
pytestmark = pytest.mark.asyncio


# ---------------------------------------------------------------------------
# /health — legacy + smoke
# ---------------------------------------------------------------------------

async def test_health_endpoint_returns_status_ok(async_client):
    resp = await async_client.get("/health")
    assert resp.status_code == 200
    body = resp.json()
    assert body["status"] == "ok"


# ---------------------------------------------------------------------------
# /api/reports — empty DB still returns the documented {"reports": [...]} shape
# ---------------------------------------------------------------------------

async def test_api_reports_returns_reports_list_shape(async_client):
    resp = await async_client.get("/api/reports")
    assert resp.status_code == 200
    body = resp.json()
    assert "reports" in body and isinstance(body["reports"], list)


# ---------------------------------------------------------------------------
# /api/sources — yaml-backed registry, ≥37 entries (current production count)
# ---------------------------------------------------------------------------

async def test_api_sources_returns_full_registry(async_client):
    resp = await async_client.get("/api/sources")
    assert resp.status_code == 200
    body = resp.json()
    sources = body["sources"]
    assert isinstance(sources, list)
    # The yaml currently ships 37 entries; the assertion is a floor so adding
    # more sources doesn't break the suite.
    assert len(sources) >= 37, f"expected ≥37 registry entries, got {len(sources)}"
    # Every entry must at least carry a name — that's the unique key the FE
    # uses to address PUT /api/sources/{name}.
    for entry in sources:
        assert "name" in entry and entry["name"]


# ---------------------------------------------------------------------------
# /api/policy — yaml + override merge exposes all 5 documented sections
# ---------------------------------------------------------------------------

async def test_api_policy_returns_documented_sections(async_client):
    """The 5 keys called out in dev-plan/AGENTS.md must be present.

    The yaml ships extra keys (``quality_gates``, ``main_headline``,
    ``source_aliases``) — those are not asserted to keep the test scoped to
    the public contract.
    """
    resp = await async_client.get("/api/policy")
    assert resp.status_code == 200
    policy = resp.json()["policy"]
    assert isinstance(policy, dict)
    expected = {
        "source_tiers",
        "scoring_weights",
        "penalties",
        "section_quotas",
        "report_selection",
    }
    missing = expected - set(policy.keys())
    assert not missing, f"missing policy sections: {missing}"
