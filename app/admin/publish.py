"""Report publish helper — wires the admin route to NetlifyPublisher.

Behaviour:
- Always re-renders the published HTML from the **current DB state** before
  deploying so operator edits in Review (title/summary/image/disabled toggle)
  are reflected in the deployed bundle. ``disabled_section_ids`` lets the
  caller drop specific section UUIDs from the render.
- ``dry_run=True``: re-renders but skips the Netlify deploy, returning a
  synthetic preview URL.
- Otherwise requires ``settings.netlify_auth_token`` AND
  ``settings.netlify_site_id`` to push to Netlify. Missing config falls back
  to the local static result so the operator still gets a usable HTML output.
- On a successful local/static publish, marks the Report as ``published`` and
  stamps ``published_at``.
"""
from __future__ import annotations

import json
import os
from datetime import date as date_cls, datetime, timezone
from pathlib import Path
from typing import Any, Iterable, Optional

from sqlalchemy import select

from app.admin.render import render_published
from app.config import settings
from app.db import AsyncSessionLocal
from app.deployment.netlify import NetlifyPublisher
from app.deployment.static_publisher import StaticPublisher
from app.models.db_models import Report
from app.utils.logger import get_logger

logger = get_logger(step="admin")

# Append-only audit trail for every publish attempt (incl. dry runs). Lets the
# operator reconcile "did I just deploy something?" against Netlify history
# without round-tripping the dashboard. One JSON record per line. Resolved
# lazily so tests can redirect via NEWS_STUDIO_PUBLISH_HISTORY_PATH without
# polluting the operator's real ``.logs/publish_history.jsonl``.
_PROJECT_ROOT = Path(__file__).resolve().parents[2]


def _publish_history_path() -> Path:
    override = os.getenv("NEWS_STUDIO_PUBLISH_HISTORY_PATH")
    if override:
        return Path(override)
    return _PROJECT_ROOT / ".logs" / "publish_history.jsonl"


def _synthetic_url(date_kst: str) -> str:
    base_url = (settings.report_public_base_url or "http://localhost:3000").rstrip("/")
    return f"{base_url}/news/{date_kst}-trend.html"


async def _mark_report_published(run_date: date_cls) -> None:
    async with AsyncSessionLocal() as session:
        result = await session.execute(
            select(Report).where(Report.report_date == run_date)
        )
        db_report = result.scalars().first()
        if db_report is None:
            raise LookupError(f"report not found: {run_date.isoformat()}")

        now = datetime.now(timezone.utc)
        db_report.status = "published"
        db_report.published_at = now
        db_report.updated_at = now
        await session.commit()


def _update_static_index(date_kst: str) -> None:
    StaticPublisher(public_dir="public/news")._update_index(date_kst)


def _record_publish_history(entry: dict[str, Any]) -> None:
    path = _publish_history_path()
    try:
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("a", encoding="utf-8") as fh:
            fh.write(json.dumps(entry, ensure_ascii=False) + "\n")
    except Exception as exc:  # pragma: no cover — audit log must never fail the deploy
        logger.warning("publish_history_write_failed", error=str(exc))


async def publish_report(
    date_kst: str,
    *,
    dry_run: bool = False,
    publish_dir: Optional[str] = None,
    disabled_section_ids: Optional[Iterable[str]] = None,
    output_theme: Optional[str] = None,
) -> dict[str, Any]:
    """Publish a report's static bundle to Netlify.

    ``output_theme`` (``dark`` default, ``light``, ``newsroom-white``) is
    forwarded to ``render_published`` so the deployed HTML reflects the
    per-run theme the operator picked in News Studio. ``None`` falls back
    to the dark default.

    Returns a dict mirroring the route response. Raises:
      - ValueError on bad date
      - LookupError if the report row is missing
    """
    try:
        run_date = date_cls.fromisoformat(date_kst)
    except ValueError as exc:
        raise ValueError(f"invalid date_kst (expected YYYY-MM-DD): {exc}")

    disabled_list = list(disabled_section_ids or [])
    theme_value = output_theme or "dark"

    # Step 1 — re-render from DB (always, including dry_run) so that the
    # served HTML matches the current Review state.
    async with AsyncSessionLocal() as render_session:
        rendered_path = await render_published(
            date_kst,
            render_session,
            disabled_section_ids=disabled_list,
            output_theme=theme_value,
        )

    if dry_run:
        response = {
            "status": "dry_run",
            "deployed_url": _synthetic_url(date_kst),
            "report_date": date_kst,
            "dry_run": True,
            "rendered_path": str(rendered_path),
            "disabled_count": len(disabled_list),
        }
        _record_publish_history(
            {
                "ts": datetime.now(timezone.utc).isoformat(),
                "report_date": date_kst,
                "status": "dry_run",
                "deploy_url": response["deployed_url"],
                "theme": theme_value,
                "disabled_count": len(disabled_list),
                "rendered_path": str(rendered_path),
            }
        )
        return response

    auth_token = getattr(settings, "netlify_auth_token", "") or ""
    site_id = getattr(settings, "netlify_site_id", "") or ""
    deploy_url = _synthetic_url(date_kst)

    # Match the CLI pipeline behaviour: once the HTML is rendered locally,
    # publishing succeeds from the operator's perspective. Netlify is an
    # optional remote deployment layer on top of the static result.
    _update_static_index(date_kst)
    await _mark_report_published(run_date)

    if not auth_token or not site_id:
        missing = [
            name
            for name, value in (
                ("NETLIFY_AUTH_TOKEN", auth_token),
                ("NETLIFY_SITE_ID", site_id),
            )
            if not value
        ]
        response = {
            "status": "published",
            "deployed_url": deploy_url,
            "report_date": date_kst,
            "dry_run": False,
            "rendered_path": str(rendered_path),
            "disabled_count": len(disabled_list),
            "details": {
                "status": "skipped",
                "target": "local_static",
                "reason": "netlify_configuration_missing",
                "missing": missing,
            },
        }
        _record_publish_history(
            {
                "ts": datetime.now(timezone.utc).isoformat(),
                "report_date": date_kst,
                "status": response["status"],
                "deploy_url": deploy_url,
                "theme": theme_value,
                "disabled_count": len(disabled_list),
                "rendered_path": str(rendered_path),
                "details": response["details"],
            }
        )
        logger.warning(
            "publish_netlify_config_missing_local_fallback",
            date_kst=date_kst,
            missing=",".join(missing),
            deploy_url=deploy_url,
        )
        return response

    publisher = NetlifyPublisher(site_id=site_id, auth_token=auth_token)
    deploy_result = await publisher.deploy(publish_dir=publish_dir or "public")

    deploy_url = deploy_result.get("deploy_url") or deploy_url
    response = {
        "status": "published",
        "deployed_url": deploy_url,
        "report_date": date_kst,
        "dry_run": False,
        "rendered_path": str(rendered_path),
        "disabled_count": len(disabled_list),
        "details": {
            **deploy_result,
            "target": "netlify",
            "local_status": "published",
        },
    }
    _record_publish_history(
        {
            "ts": datetime.now(timezone.utc).isoformat(),
            "report_date": date_kst,
            "status": response["status"],
            "deploy_url": deploy_url,
            "theme": theme_value,
            "disabled_count": len(disabled_list),
            "rendered_path": str(rendered_path),
            "details": response["details"],
        }
    )
    logger.info(
        "publish_report_done",
        date_kst=date_kst,
        deploy_url=deploy_url,
        netlify_status=deploy_result.get("status", "unknown"),
        disabled_count=len(disabled_list),
    )
    return response
