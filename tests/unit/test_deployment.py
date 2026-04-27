"""Unit tests for Phase 6 deployment components.

TC-6.1  StaticPublisher.publish_report() — HTML file written at expected path
TC-6.2  StaticPublisher.publish_report() with report_json — JSON file also created
TC-6.3  StaticPublisher.publish_report() — index.html updated with redirect to latest date
TC-6.4  Notifier.notify_slack() — empty webhook_url → returns False (no network call)
TC-6.5  Notifier.notify_slack() — mock httpx 200 → returns True
TC-6.6  NetlifyPublisher.deploy() — netlify CLI not installed → returns {"status": "skipped"}
"""
from __future__ import annotations

from datetime import date
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from app.deployment.static_publisher import StaticPublisher
from app.deployment.netlify import NetlifyPublisher
from app.utils.notifier import Notifier


# ---------------------------------------------------------------------------
# TC-6.1  HTML file written at expected path
# ---------------------------------------------------------------------------

def test_publish_report_html_file_exists(tmp_path):
    """TC-6.1: publish_report writes HTML to YYYY-MM-DD-trend.html."""
    publisher = StaticPublisher(public_dir=str(tmp_path / "news"))
    run_date = date(2026, 4, 27)
    html_content = "<html><body>Test</body></html>"

    result = publisher.publish_report(run_date=run_date, html_content=html_content)

    expected_path = tmp_path / "news" / "2026-04-27-trend.html"
    assert expected_path.exists(), "HTML file should exist at expected path"
    assert expected_path.read_text(encoding="utf-8") == html_content
    assert result["html_path"] == str(expected_path)


# ---------------------------------------------------------------------------
# TC-6.2  JSON file created when report_json is provided
# ---------------------------------------------------------------------------

def test_publish_report_json_file_created(tmp_path):
    """TC-6.2: publish_report also writes JSON when report_json is given."""
    publisher = StaticPublisher(public_dir=str(tmp_path / "news"))
    run_date = date(2026, 4, 27)
    html_content = "<html><body>Test</body></html>"
    report_json = {"title": "AI Trend", "items": [1, 2, 3]}

    result = publisher.publish_report(
        run_date=run_date, html_content=html_content, report_json=report_json
    )

    expected_json_path = tmp_path / "news" / "2026-04-27-trend.json"
    assert expected_json_path.exists(), "JSON file should exist"
    assert "json_path" in result
    assert result["json_path"] == str(expected_json_path)

    import json
    written = json.loads(expected_json_path.read_text(encoding="utf-8"))
    assert written == report_json


# ---------------------------------------------------------------------------
# TC-6.3  index.html updated with redirect to latest date
# ---------------------------------------------------------------------------

def test_publish_report_updates_index_html(tmp_path):
    """TC-6.3: publish_report updates index.html with a redirect to the latest date."""
    publisher = StaticPublisher(public_dir=str(tmp_path / "news"))
    run_date = date(2026, 4, 27)
    html_content = "<html><body>Test</body></html>"

    publisher.publish_report(run_date=run_date, html_content=html_content)

    index_path = tmp_path / "news" / "index.html"
    assert index_path.exists(), "index.html should be created"
    index_content = index_path.read_text(encoding="utf-8")
    assert "2026-04-27-trend.html" in index_content, "index.html should reference the latest report"
    assert 'http-equiv="refresh"' in index_content, "index.html should contain a meta refresh redirect"


# ---------------------------------------------------------------------------
# TC-6.4  notify_slack with empty webhook_url → returns False without network call
# ---------------------------------------------------------------------------

@pytest.mark.asyncio
async def test_notify_slack_empty_webhook_returns_false():
    """TC-6.4: notify_slack returns False when no webhook URL is configured."""
    notifier = Notifier()

    # Patch settings to ensure no url leaks through
    with patch("app.utils.notifier.settings") as mock_settings:
        mock_settings.slack_webhook_url = ""
        result = await notifier.notify_slack(message="hello", webhook_url="")

    assert result is False


# ---------------------------------------------------------------------------
# TC-6.5  notify_slack — mock httpx returns 200 → returns True
# ---------------------------------------------------------------------------

@pytest.mark.asyncio
async def test_notify_slack_success_returns_true():
    """TC-6.5: notify_slack returns True when the HTTP POST succeeds."""
    notifier = Notifier()

    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.raise_for_status = MagicMock()

    mock_client = AsyncMock()
    mock_client.post = AsyncMock(return_value=mock_response)
    mock_client.__aenter__ = AsyncMock(return_value=mock_client)
    mock_client.__aexit__ = AsyncMock(return_value=False)

    with patch("app.utils.notifier.httpx.AsyncClient", return_value=mock_client):
        result = await notifier.notify_slack(
            message="Report ready!", webhook_url="https://hooks.slack.com/test"
        )

    assert result is True
    mock_client.post.assert_awaited_once()


# ---------------------------------------------------------------------------
# TC-6.6  NetlifyPublisher.deploy() — CLI not installed → {"status": "skipped"}
# ---------------------------------------------------------------------------

@pytest.mark.asyncio
async def test_netlify_deploy_cli_not_found():
    """TC-6.6: deploy returns status=skipped when netlify CLI is not installed."""
    publisher = NetlifyPublisher(site_id="test-site", auth_token="test-token")

    with patch("app.deployment.netlify.asyncio.to_thread", side_effect=FileNotFoundError):
        result = await publisher.deploy(publish_dir="public")

    assert result["status"] == "skipped"
    assert "error" in result
