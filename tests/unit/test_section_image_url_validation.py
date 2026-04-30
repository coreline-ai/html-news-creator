"""
Unit tests for PATCH /api/sections/{id} `image_url` validation (P1-1).

The route must reject non-http(s) URLs, URLs without a host, and other
obvious junk with a 400, while accepting absolute http(s) URLs and
empty strings (treated as "no-op for image_url" so the FE can pass an
empty editing buffer alongside other field edits).
"""
from __future__ import annotations

import uuid
from unittest.mock import AsyncMock, MagicMock

import pytest
from fastapi.testclient import TestClient

from app.admin.api import app
from app.db import get_db


# ---------------------------------------------------------------------------
# DB stub — minimal, mirrors test_admin_sections.py shape but inlined to keep
# this file self-contained.
# ---------------------------------------------------------------------------


class _SectionRow:
    def __init__(self, section_id: str) -> None:
        self.id = section_id
        self.report_id = str(uuid.uuid4())
        self.section_order = 0
        self.title = "Sample"
        self.lead = None
        self.fact_summary = None
        self.social_signal_summary = None
        self.inference_summary = None
        self.caution = None
        self.image_evidence_json = []
        self.sources_json = []
        self.confidence = None
        self.importance_score = None
        self.tags_json = []


def _make_db(section: _SectionRow | None):
    def _make_result(payload):
        scalars_mock = MagicMock()
        scalars_mock.first.return_value = payload
        scalars_mock.all.return_value = [payload] if payload is not None else []
        execute_result = MagicMock()
        execute_result.scalars.return_value = scalars_mock
        return execute_result

    db = AsyncMock()
    db.execute = AsyncMock(return_value=_make_result(section))
    db.commit = AsyncMock(return_value=None)
    db.refresh = AsyncMock(return_value=None)
    return db


def _override_db(db_obj):
    async def _gen():
        yield db_obj

    app.dependency_overrides[get_db] = _gen


def _clear_override():
    app.dependency_overrides.pop(get_db, None)


client = TestClient(app)


# ---------------------------------------------------------------------------
# Rejected URLs → 400
# ---------------------------------------------------------------------------


@pytest.mark.parametrize(
    "bad_url",
    [
        "not-a-url",                   # no scheme, no host
        "ftp://example.com/x.png",     # disallowed scheme
        "javascript:alert(1)",         # XSS vector
        "file:///etc/passwd",          # local file scheme
        "://no-scheme.example.com",    # malformed
        "http://",                     # no host
        "https://",                    # no host
        "http:///path/only",           # no host
        "data:image/png;base64,iVBOR", # data URLs not allowed
    ],
)
def test_patch_section_rejects_invalid_image_url(bad_url: str) -> None:
    sec_id = str(uuid.uuid4())
    section = _SectionRow(sec_id)
    _override_db(_make_db(section))
    try:
        resp = client.patch(
            f"/api/sections/{sec_id}", json={"image_url": bad_url}
        )
        assert resp.status_code == 400, (
            f"expected 400 for image_url={bad_url!r}, "
            f"got {resp.status_code} body={resp.text}"
        )
        detail = resp.json()["detail"].lower()
        assert "invalid image_url" in detail or "image_url" in detail
    finally:
        _clear_override()


# ---------------------------------------------------------------------------
# Accepted URLs → 200
# ---------------------------------------------------------------------------


@pytest.mark.parametrize(
    "good_url",
    [
        "http://example.com/x.png",
        "https://cdn.example.com/path/to/image.jpg",
        "https://example.com:8443/img.webp",
        "https://example.com/with?query=1&other=2",
        "https://sub.example.co.kr/이미지.png",
    ],
)
def test_patch_section_accepts_valid_http_image_url(good_url: str) -> None:
    sec_id = str(uuid.uuid4())
    section = _SectionRow(sec_id)
    _override_db(_make_db(section))
    try:
        resp = client.patch(
            f"/api/sections/{sec_id}", json={"image_url": good_url}
        )
        assert resp.status_code == 200, resp.text
        body = resp.json()["section"]
        assert body["image_evidence_json"][0]["url"] == good_url
    finally:
        _clear_override()


# ---------------------------------------------------------------------------
# Empty string is accepted as a no-op (UX detail).
# ---------------------------------------------------------------------------


def test_patch_section_image_url_empty_string_is_skipped() -> None:
    """An empty image_url alongside other fields must not 400.

    The FE often sends the entire form payload; an unfilled image input
    arrives as `""` and should not block other field updates.
    """
    sec_id = str(uuid.uuid4())
    section = _SectionRow(sec_id)
    _override_db(_make_db(section))
    try:
        resp = client.patch(
            f"/api/sections/{sec_id}",
            json={"title": "New title", "image_url": ""},
        )
        assert resp.status_code == 200, resp.text
        body = resp.json()["section"]
        assert body["title"] == "New title"
    finally:
        _clear_override()
