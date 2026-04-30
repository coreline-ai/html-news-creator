from __future__ import annotations
import httpx
from app.config import settings
from app.utils.logger import get_logger


class Notifier:
    def __init__(self):
        self.logger = get_logger(step="notify")

    async def notify_slack(self, message: str, webhook_url: str = "") -> bool:
        """Send Slack notification via webhook. Returns True on success."""
        url = webhook_url or getattr(settings, "slack_webhook_url", "")
        if not url:
            self.logger.info("slack_skipped", reason="no_webhook_url")
            return False

        try:
            async with httpx.AsyncClient(timeout=10.0) as client:
                resp = await client.post(url, json={"text": message})
                resp.raise_for_status()
                self.logger.info("slack_sent", status=resp.status_code)
                return True
        except Exception as e:
            self.logger.error("slack_failed", error=str(e))
            return False

    async def notify_report_ready(self, run_date: str, report_url: str, stats: dict) -> None:
        """Send standard report-ready notification."""
        total = stats.get("total_sources", 0)
        ai_relevant = stats.get("ai_relevant", 0)
        clusters = stats.get("clusters", 0)

        message = (
            f"✅ AI 트렌드 리포트 발행 완료 ({run_date})\n"
            f"📊 수집: {total}건 | AI 관련: {ai_relevant}건 | 주제: {clusters}개\n"
            f"🔗 {report_url}"
        )
        await self.notify_slack(message)
