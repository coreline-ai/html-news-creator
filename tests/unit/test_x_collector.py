"""
Unit tests for Phase 7 — XCollector.

TC-7.6: XCollector.collect() with x_enabled=False → returns []
TC-7.7: XCollector.collect() with twikit not installed → returns [] (no exception)
"""
from __future__ import annotations

import sys
from datetime import datetime, timezone
from unittest.mock import patch, MagicMock

import pytest

from app.collectors.x_collector import XCollector


_DATE_FROM = datetime(2026, 4, 27, 0, 0, 0, tzinfo=timezone.utc)
_DATE_TO = datetime(2026, 4, 27, 23, 59, 59, tzinfo=timezone.utc)


def _make_x_source() -> dict:
    return {
        "name": "X/Twitter",
        "source_type": "x",
        "url": "https://x.com",
        "trust_level": "unknown",
    }


# ---------------------------------------------------------------------------
# TC-7.6: x_enabled=False → returns []
# ---------------------------------------------------------------------------

@pytest.mark.asyncio
async def test_x_collector_disabled_returns_empty_list():
    """TC-7.6: When x_enabled=False in settings, collect() returns [] without raising."""
    source = _make_x_source()
    collector = XCollector(source)

    mock_settings = MagicMock()
    mock_settings.x_enabled = False

    with patch("app.collectors.x_collector.settings", mock_settings, create=True):
        # Patch settings inside _ensure_client's import
        with patch("app.config.settings", mock_settings):
            items = await collector.collect(_DATE_FROM, _DATE_TO)

    assert items == []


# ---------------------------------------------------------------------------
# TC-7.7: twikit not installed → returns []
# ---------------------------------------------------------------------------

@pytest.mark.asyncio
async def test_x_collector_twikit_not_installed_returns_empty_list():
    """TC-7.7: When twikit is not installed, collect() returns [] without raising."""
    source = _make_x_source()
    collector = XCollector(source)

    mock_settings = MagicMock()
    mock_settings.x_enabled = True

    # Temporarily hide twikit from sys.modules so the import fails
    original_twikit = sys.modules.get("twikit", None)
    sys.modules["twikit"] = None  # type: ignore[assignment]

    try:
        with patch("app.config.settings", mock_settings):
            items = await collector.collect(_DATE_FROM, _DATE_TO)
    finally:
        # Restore original state
        if original_twikit is None:
            sys.modules.pop("twikit", None)
        else:
            sys.modules["twikit"] = original_twikit

    assert items == []
