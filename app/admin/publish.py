"""Report publish helper — wires the admin route to NetlifyPublisher.

Behaviour:
- `dry_run=True`: returns a synthetic preview URL without invoking Netlify.
- Otherwise requires `settings.netlify_auth_token` AND `settings.netlify_site_id`
  to be present. Missing config raises `RuntimeError` (route → 400).
- On a successful deploy, marks the Report as `published` and stamps
  `published_at`.
"""
from __future__ import annotations

from datetime import date as date_cls, datetime
from typing import Any, Optional

from sqlalchemy import select

from app.config import settings
from app.db import AsyncSessionLocal
from app.deployment.netlify import NetlifyPublisher
from app.models.db_models import Report
from app.utils.logger import get_logger

logger = get_logger(step="admin")


def _synthetic_url(date_kst: str) -> str:
    return f"https://ai-news-5min-kr.netlify.app/{date_kst}-trend.html"


async def publish_report(
    date_kst: str,
    *,
    dry_run: bool = False,
    publish_dir: Optional[str] = None,
) -> dict[str, Any]:
    """Publish a report's static bundle to Netlify.

    Returns a dict mirroring the route response. Raises:
      - ValueError on bad date
      - LookupError if the report row is missing
      - RuntimeError if Netlify config is missing on a real deploy
    """
    try:
        run_date = date_cls.fromisoformat(date_kst)
    except ValueError as exc:
        raise ValueError(f"invalid date_kst (expected YYYY-MM-DD): {exc}")

    if dry_run:
        return {
            "status": "dry_run",
            "deployed_url": _synthetic_url(date_kst),
            "report_date": date_kst,
            "dry_run": True,
        }

    auth_token = getattr(settings, "netlify_auth_token", "") or ""
    site_id = getattr(settings, "netlify_site_id", "") or ""
    if not auth_token or not site_id:
        raise RuntimeError(
            "netlify configuration missing — set NETLIFY_AUTH_TOKEN and "
            "NETLIFY_SITE_ID before publishing"
        )

    async with AsyncSessionLocal() as session:
        result = await session.execute(
            select(Report).where(Report.report_date == run_date)
        )
        db_report = result.scalars().first()
        if db_report is None:
            raise LookupError(f"report not found: {date_kst}")

        publisher = NetlifyPublisher(site_id=site_id, auth_token=auth_token)
        deploy_result = await publisher.deploy(publish_dir=publish_dir or "public")

        deploy_url = deploy_result.get("deploy_url") or _synthetic_url(date_kst)
        if deploy_result.get("status") == "success":
            db_report.status = "published"
            db_report.published_at = datetime.utcnow()
            await session.commit()
            logger.info(
                "publish_report_done",
                date_kst=date_kst,
                deploy_url=deploy_url,
            )

        return {
            "status": deploy_result.get("status", "unknown"),
            "deployed_url": deploy_url,
            "report_date": date_kst,
            "dry_run": False,
            "details": deploy_result,
        }
