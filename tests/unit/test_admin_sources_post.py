"""POST /api/sources contract tests.

Phase C / TC-5.E1 — appending a new source via the admin API. The endpoint
delegates field validation to ``app.admin.sources_admin.add_source``; here we
exercise the HTTP wrapper plus the behaviors the FE relies on:

  - 201 + ``{source: {...}}`` envelope on success
  - duplicate name → 400
  - bad source_type → 400
  - bad name pattern → 400
  - missing required field → 422 (pydantic) — sanity check, the FE blocks first
  - bad url scheme → 400
"""
from __future__ import annotations

from unittest.mock import AsyncMock, MagicMock

import yaml
from fastapi.testclient import TestClient

from app.admin import sources_admin
from app.admin.api import app
from app.db import get_db


async def _mock_db():
    mock = AsyncMock()
    scalars_mock = MagicMock()
    scalars_mock.all.return_value = []
    scalars_mock.first.return_value = None
    execute_result = MagicMock()
    execute_result.scalars.return_value = scalars_mock
    execute_result.scalar.return_value = 0
    mock.execute.return_value = execute_result
    yield mock


app.dependency_overrides[get_db] = _mock_db
client = TestClient(app)


def _empty_registry(tmp_path):
    fake_path = tmp_path / "sources_registry.yaml"
    fake_path.write_text(
        yaml.safe_dump({"sources": []}, allow_unicode=True, sort_keys=False),
        encoding="utf-8",
    )
    return fake_path


def test_post_sources_creates_entry_and_returns_envelope(tmp_path, monkeypatch):
    fake_path = _empty_registry(tmp_path)
    monkeypatch.setattr(sources_admin, "DEFAULT_REGISTRY_PATH", fake_path)

    response = client.post(
        "/api/sources",
        json={
            "name": "Acme AI Blog",
            "source_type": "rss",
            "url": "https://example.com/feed.xml",
            "source_tier": "official",
            "priority": 75,
        },
    )
    assert response.status_code == 201, response.text
    body = response.json()
    assert "source" in body
    src = body["source"]
    assert src["name"] == "Acme AI Blog"
    assert src["source_type"] == "rss"
    assert src["url"] == "https://example.com/feed.xml"
    assert src["source_tier"] == "official"
    assert src["priority"] == 75
    # Defaults applied by add_source.
    assert src["enabled"] is True
    assert src["max_items"] == 20

    on_disk = yaml.safe_load(fake_path.read_text(encoding="utf-8"))
    names = [s["name"] for s in on_disk["sources"]]
    assert "Acme AI Blog" in names


def test_post_sources_rejects_duplicate_name(tmp_path, monkeypatch):
    fake_path = tmp_path / "sources_registry.yaml"
    fake_path.write_text(
        yaml.safe_dump(
            {
                "sources": [
                    {
                        "name": "Existing",
                        "source_type": "rss",
                        "url": "https://example.com/a",
                    }
                ]
            },
            allow_unicode=True,
            sort_keys=False,
        ),
        encoding="utf-8",
    )
    monkeypatch.setattr(sources_admin, "DEFAULT_REGISTRY_PATH", fake_path)

    response = client.post(
        "/api/sources",
        json={
            "name": "Existing",
            "source_type": "rss",
            "url": "https://example.com/b",
        },
    )
    assert response.status_code == 400
    assert "already exists" in response.json()["detail"]


def test_post_sources_rejects_unknown_source_type(tmp_path, monkeypatch):
    monkeypatch.setattr(sources_admin, "DEFAULT_REGISTRY_PATH", _empty_registry(tmp_path))

    response = client.post(
        "/api/sources",
        json={
            "name": "Test",
            "source_type": "xkcd",  # not in SOURCE_TYPES
            "url": "https://example.com/feed",
        },
    )
    assert response.status_code == 400
    assert "source_type" in response.json()["detail"]


def test_post_sources_rejects_bad_name_pattern(tmp_path, monkeypatch):
    monkeypatch.setattr(sources_admin, "DEFAULT_REGISTRY_PATH", _empty_registry(tmp_path))

    response = client.post(
        "/api/sources",
        json={
            "name": "1bad",  # must start with a letter
            "source_type": "rss",
            "url": "https://example.com/feed",
        },
    )
    assert response.status_code == 400
    assert "name" in response.json()["detail"]


def test_post_sources_rejects_bad_source_tier(tmp_path, monkeypatch):
    monkeypatch.setattr(sources_admin, "DEFAULT_REGISTRY_PATH", _empty_registry(tmp_path))

    response = client.post(
        "/api/sources",
        json={
            "name": "Test",
            "source_type": "rss",
            "url": "https://example.com/feed",
            "source_tier": "vip",
        },
    )
    assert response.status_code == 400
    assert "source_tier" in response.json()["detail"]


def test_post_sources_missing_required_field_is_422():
    # Pydantic catches missing ``name`` before it reaches add_source.
    response = client.post("/api/sources", json={"source_type": "rss"})
    assert response.status_code == 422


def test_post_sources_rejects_bad_url_scheme(tmp_path, monkeypatch):
    monkeypatch.setattr(sources_admin, "DEFAULT_REGISTRY_PATH", _empty_registry(tmp_path))

    response = client.post(
        "/api/sources",
        json={
            "name": "Test",
            "source_type": "rss",
            "url": "ftp://example.com/feed",
        },
    )
    assert response.status_code == 400
    assert "url" in response.json()["detail"]


def test_post_sources_supports_url_omitted_for_arxiv(tmp_path, monkeypatch):
    """arxiv entries identify themselves by ``category`` rather than ``url``."""
    monkeypatch.setattr(sources_admin, "DEFAULT_REGISTRY_PATH", _empty_registry(tmp_path))

    response = client.post(
        "/api/sources",
        json={
            "name": "ArxivCat",
            "source_type": "arxiv",
            "category": "cs.AI",
        },
    )
    assert response.status_code == 201, response.text
    assert response.json()["source"]["category"] == "cs.AI"
