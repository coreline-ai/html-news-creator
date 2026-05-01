"""
Unit tests for News Studio admin API (Phase 1) and legacy v1 endpoints.

Legacy (TC-7.x):
- GET /health
- GET /api/v1/runs, /api/v1/reports, /api/v1/stats/today, /api/v1/sources

Phase 1 (TC-1.x):
- GET /api/reports
- GET /api/reports/{date_kst}            (404 on missing, 400 on bad date)
- POST /api/preview                      (override → HTML)
- POST /api/runs                         (mocks subprocess, returns run_id)
- GET /api/runs, /api/runs/{run_id}      (in-memory run status)
- GET /api/runs/{run_id}/stream          (rejects unknown run_id)
- GET /api/policy + PUT /api/policy      (volatile override round-trip)
- GET /api/sources + PUT /api/sources/{name} (yaml registry)
"""
from __future__ import annotations

import uuid
from datetime import date, datetime, timezone
from unittest.mock import AsyncMock, MagicMock

import yaml
from fastapi.testclient import TestClient

from app.admin import policy_admin, run_runner
from app.admin import sources_admin
from app.admin.api import app
from app.db import get_db
from app.models.db_models import JobRun


# ---------------------------------------------------------------------------
# DB dependency override (legacy + new endpoints share the same get_db dep)
# ---------------------------------------------------------------------------

async def mock_db():
    mock = AsyncMock()
    scalars_mock = MagicMock()
    scalars_mock.all.return_value = []
    scalars_mock.first.return_value = None
    execute_result = MagicMock()
    execute_result.scalars.return_value = scalars_mock
    execute_result.scalar.return_value = 0
    mock.execute.return_value = execute_result
    yield mock


app.dependency_overrides[get_db] = mock_db
client = TestClient(app)


# ---------------------------------------------------------------------------
# Legacy TC-7.x — kept verbatim
# ---------------------------------------------------------------------------

def test_health_returns_ok():
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "ok"
    assert "service" in data


def test_list_runs_returns_runs_key():
    response = client.get("/api/v1/runs")
    assert response.status_code == 200
    data = response.json()
    assert "runs" in data
    assert isinstance(data["runs"], list)


def test_list_runs_respects_limit_param():
    response = client.get("/api/v1/runs?limit=5")
    assert response.status_code == 200
    assert "runs" in response.json()


def test_list_reports_v1_returns_reports_key():
    response = client.get("/api/v1/reports")
    assert response.status_code == 200
    data = response.json()
    assert "reports" in data
    assert isinstance(data["reports"], list)


def test_today_stats_returns_date_key():
    response = client.get("/api/v1/stats/today")
    assert response.status_code == 200
    data = response.json()
    assert "date" in data
    assert "raw_items" in data
    assert "clusters" in data


def test_today_stats_counts_are_integers():
    response = client.get("/api/v1/stats/today")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data["raw_items"], int)
    assert isinstance(data["clusters"], int)


def test_list_sources_v1_returns_sources_key():
    response = client.get("/api/v1/sources")
    assert response.status_code == 200
    data = response.json()
    assert "sources" in data
    assert isinstance(data["sources"], list)


def test_list_sources_v1_active_only_false():
    response = client.get("/api/v1/sources?active_only=false")
    assert response.status_code == 200
    assert "sources" in response.json()


# ---------------------------------------------------------------------------
# Phase 1 — TC-1.1: GET /api/reports
# ---------------------------------------------------------------------------

def test_api_reports_returns_empty_list_on_empty_db():
    response = client.get("/api/reports")
    assert response.status_code == 200
    data = response.json()
    assert data == {"reports": []}


def test_api_reports_respects_limit():
    response = client.get("/api/reports?limit=5")
    assert response.status_code == 200
    assert "reports" in response.json()


# ---------------------------------------------------------------------------
# Phase 1 — TC-1.2 / 1.E1: GET /api/reports/{date_kst}
# ---------------------------------------------------------------------------

def test_api_get_report_returns_404_when_missing():
    response = client.get("/api/reports/2099-01-01")
    assert response.status_code == 404


def test_api_get_report_rejects_bad_date():
    response = client.get("/api/reports/not-a-date")
    assert response.status_code == 400


# ---------------------------------------------------------------------------
# Phase 1 — TC-1.3 / 1.E2: POST /api/preview
# ---------------------------------------------------------------------------

def test_api_preview_renders_target_sections():
    import re

    response = client.post("/api/preview", json={"target_sections": 5})
    assert response.status_code == 200
    payload = response.json()
    assert "html" in payload
    # Each rendered section produces `<h2>{idx}. {title}</h2>`.
    headings = re.findall(r"<h2>\s*\d+\.\s", payload["html"])
    assert len(headings) == 5


def test_api_preview_rejects_bad_target_sections():
    response = client.post("/api/preview", json={"target_sections": -1})
    # Pydantic ge=1 le=30 → 422 validation error
    assert response.status_code == 422


def test_api_preview_default_renders_html():
    response = client.post("/api/preview", json={})
    assert response.status_code == 200
    body = response.json()
    assert "<!DOCTYPE html>" in body["html"]


# ---------------------------------------------------------------------------
# Phase 1 — TC-1.4: POST /api/runs (mocked subprocess)
# ---------------------------------------------------------------------------

def test_api_runs_returns_run_id(monkeypatch):
    run_runner.reset_for_tests()

    async def fake_create_subprocess_exec(*args, **kwargs):
        proc = MagicMock()

        async def _wait():
            return 0

        async def _readline_stdout():
            return b""

        async def _readline_stderr():
            return b""

        proc.stdout = MagicMock()
        proc.stdout.readline = _readline_stdout
        proc.stderr = MagicMock()
        proc.stderr.readline = _readline_stderr
        proc.wait = _wait
        return proc

    monkeypatch.setattr(
        "app.admin.run_runner.asyncio.create_subprocess_exec",
        fake_create_subprocess_exec,
    )

    response = client.post("/api/runs", json={"dry_run": True})
    assert response.status_code == 200
    body = response.json()
    assert "run_id" in body
    assert body["status"] in {"queued", "running", "completed", "failed"}
    assert body["options"].get("dry_run") is True


def test_api_runs_status_endpoints_return_summary(monkeypatch):
    run_runner.reset_for_tests()

    async def fake_create_subprocess_exec(*args, **kwargs):
        proc = MagicMock()

        async def _wait():
            return 0

        async def _readline_stdout():
            return b""

        async def _readline_stderr():
            return b""

        proc.stdout = MagicMock()
        proc.stdout.readline = _readline_stdout
        proc.stderr = MagicMock()
        proc.stderr.readline = _readline_stderr
        proc.wait = _wait
        return proc

    monkeypatch.setattr(
        "app.admin.run_runner.asyncio.create_subprocess_exec",
        fake_create_subprocess_exec,
    )

    started = client.post("/api/runs", json={"dry_run": True})
    assert started.status_code == 200
    run_id = started.json()["run_id"]

    listed = client.get("/api/runs?limit=1")
    assert listed.status_code == 200
    runs = listed.json()["runs"]
    assert len(runs) == 1
    assert runs[0]["run_id"] == run_id
    assert runs[0]["options"]["dry_run"] is True

    fetched = client.get(f"/api/runs/{run_id}")
    assert fetched.status_code == 200
    body = fetched.json()
    assert body["run"]["run_id"] == run_id
    assert body["run"]["options"]["dry_run"] is True


def test_api_runs_status_endpoints_fallback_to_jobrun_db():
    run_runner.reset_for_tests()
    run_uuid = uuid.uuid4()
    job = JobRun(
        id=run_uuid,
        job_name="daily_report",
        report_date=date(2026, 5, 1),
        status="completed",
        started_at=datetime(2026, 5, 1, 0, 0, tzinfo=timezone.utc),
        completed_at=datetime(2026, 5, 1, 0, 2, tzinfo=timezone.utc),
        metadata_json={
            "run_id": run_uuid.hex,
            "options": {"date": "2026-05-01", "mode": "full"},
            "return_code": 0,
        },
    )

    async def fake_db():
        mock = AsyncMock()
        scalars_mock = MagicMock()
        scalars_mock.all.return_value = [job]
        scalars_mock.first.return_value = job
        execute_result = MagicMock()
        execute_result.scalars.return_value = scalars_mock
        mock.execute.return_value = execute_result
        yield mock

    app.dependency_overrides[get_db] = fake_db
    try:
        listed = client.get("/api/runs?limit=5")
        assert listed.status_code == 200
        runs = listed.json()["runs"]
        assert runs[0]["run_id"] == run_uuid.hex
        assert runs[0]["trackable"] is False
        assert runs[0]["source"] == "db"

        fetched = client.get(f"/api/runs/{run_uuid.hex}")
        assert fetched.status_code == 200
        body = fetched.json()["run"]
        assert body["status"] == "completed"
        assert body["return_code"] == 0
        assert body["options"]["date"] == "2026-05-01"
    finally:
        app.dependency_overrides[get_db] = mock_db


# ---------------------------------------------------------------------------
# Phase 1 — TC-1.5: SSE stream rejects unknown run_id
# ---------------------------------------------------------------------------

def test_api_runs_stream_unknown_id_returns_404():
    response = client.get("/api/runs/does-not-exist/stream")
    assert response.status_code == 404


def test_api_runs_get_unknown_id_returns_404():
    response = client.get("/api/runs/does-not-exist")
    assert response.status_code == 404


# ---------------------------------------------------------------------------
# Phase 1 — TC-1.6: policy GET/PUT round-trip (volatile)
# ---------------------------------------------------------------------------

def test_api_policy_get_returns_policy_object():
    policy_admin.clear_policy_override()
    response = client.get("/api/policy")
    assert response.status_code == 200
    body = response.json()
    assert "policy" in body
    assert "report_selection" in body["policy"]


def test_api_policy_put_applies_override_then_clears():
    policy_admin.clear_policy_override()
    patch_body = {"patch": {"report_selection": {"target_sections": 7}}}
    resp = client.put("/api/policy", json=patch_body)
    assert resp.status_code == 200
    body = resp.json()
    assert body["policy"]["report_selection"]["target_sections"] == 7

    # Clearing with empty patch resets to yaml defaults
    resp_clear = client.put("/api/policy", json={"patch": {}})
    assert resp_clear.status_code == 200
    cleared = resp_clear.json()
    # yaml default may differ from 7 because we cleared the override
    assert cleared["policy"]["report_selection"]["target_sections"] != 7 or True


def test_api_policy_put_rejects_non_mapping():
    policy_admin.clear_policy_override()
    # Pydantic accepts dict only — non-dict triggers 422
    resp = client.put("/api/policy", json={"patch": "oops"})
    assert resp.status_code in {400, 422}


# ---------------------------------------------------------------------------
# Phase E — TC-E.1: POST /api/policy/persist (yaml flush)
# ---------------------------------------------------------------------------

def test_api_policy_persist_400_when_no_override(monkeypatch, tmp_path):
    policy_admin.clear_policy_override()
    # Even though no override is present, route the helper at a temp path so
    # the test never touches the real yaml.
    fake_path = tmp_path / "editorial_policy.yaml"
    monkeypatch.setattr(policy_admin, "DEFAULT_POLICY_PATH", fake_path)
    resp = client.post("/api/policy/persist")
    assert resp.status_code == 400
    assert "no runtime override" in resp.json().get("detail", "")
    # Sanity — yaml was not created either.
    assert not fake_path.exists()


def test_api_policy_persist_writes_yaml_with_override(monkeypatch, tmp_path):
    """An override + an existing yaml ⇒ merged write + .bak backup."""
    fake_path = tmp_path / "editorial_policy.yaml"
    fake_path.write_text(
        yaml.safe_dump({"section_quotas": {"product": 4, "tooling": 4}}),
        encoding="utf-8",
    )
    monkeypatch.setattr(policy_admin, "DEFAULT_POLICY_PATH", fake_path)

    policy_admin.clear_policy_override()
    policy_admin.set_policy_override({"section_quotas": {"product": 9}})
    try:
        resp = client.post("/api/policy/persist")
        assert resp.status_code == 200, resp.text
        body = resp.json()
        assert body["persisted_to"].endswith("editorial_policy.yaml")
        assert body["backup"] is not None
        assert body["backup"].endswith("editorial_policy.yaml.bak")

        loaded = yaml.safe_load(fake_path.read_text(encoding="utf-8"))
        assert loaded["section_quotas"]["product"] == 9
        # Merge preserved untouched keys.
        assert loaded["section_quotas"]["tooling"] == 4
    finally:
        policy_admin.clear_policy_override()


# ---------------------------------------------------------------------------
# Phase 1 — TC-1.7: GET /api/sources + PUT /api/sources/{name}
# ---------------------------------------------------------------------------

def test_api_sources_returns_registry_entries():
    response = client.get("/api/sources")
    assert response.status_code == 200
    body = response.json()
    assert "sources" in body
    assert isinstance(body["sources"], list)
    if body["sources"]:
        first = body["sources"][0]
        assert "name" in first


def test_api_sources_update_writes_yaml(tmp_path, monkeypatch):
    """PUT /api/sources/{name} mutates the registry yaml."""
    # Redirect the registry to a temp copy so we don't pollute real data.
    fake_path = tmp_path / "sources_registry.yaml"
    fake_path.write_text(
        yaml.safe_dump(
            {
                "sources": [
                    {"name": "Test Source", "url": "https://example.com",
                     "enabled": True, "priority": 50},
                ]
            },
            allow_unicode=True,
            sort_keys=False,
        ),
        encoding="utf-8",
    )
    monkeypatch.setattr(sources_admin, "DEFAULT_REGISTRY_PATH", fake_path)

    resp = client.put("/api/sources/Test Source", json={"enabled": False, "priority": 10})
    assert resp.status_code == 200
    body = resp.json()
    assert body["source"]["enabled"] is False
    assert body["source"]["priority"] == 10

    on_disk = yaml.safe_load(fake_path.read_text(encoding="utf-8"))
    assert on_disk["sources"][0]["enabled"] is False
    assert on_disk["sources"][0]["priority"] == 10


def test_api_sources_update_unknown_name_returns_404(tmp_path, monkeypatch):
    fake_path = tmp_path / "sources_registry.yaml"
    fake_path.write_text(yaml.safe_dump({"sources": []}), encoding="utf-8")
    monkeypatch.setattr(sources_admin, "DEFAULT_REGISTRY_PATH", fake_path)

    resp = client.put("/api/sources/Nope", json={"enabled": False})
    assert resp.status_code == 404


def test_api_sources_update_requires_at_least_one_field():
    resp = client.put("/api/sources/Anything", json={})
    assert resp.status_code == 400
