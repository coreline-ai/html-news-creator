from __future__ import annotations
import json
from datetime import date
from pathlib import Path
from app.utils.logger import get_logger


class StaticPublisher:
    def __init__(self, public_dir: str = "public/news"):
        self.public_dir = Path(public_dir)
        self.logger = get_logger(step="publish")

    def publish_report(
        self,
        run_date: date,
        html_content: str,
        report_json: dict | None = None,
    ) -> dict:
        """
        Write HTML (and optional JSON) to public/news/YYYY-MM-DD-trend.html.
        Returns: {html_path, json_path}
        """
        self.public_dir.mkdir(parents=True, exist_ok=True)

        date_str = str(run_date)
        html_path = self.public_dir / f"{date_str}-trend.html"
        html_path.write_text(html_content, encoding="utf-8")
        self.logger.info("html_published", path=str(html_path), size=len(html_content))

        result = {"html_path": str(html_path)}

        if report_json is not None:
            json_path = self.public_dir / f"{date_str}-trend.json"
            json_path.write_text(json.dumps(report_json, ensure_ascii=False, indent=2), encoding="utf-8")
            self.logger.info("json_published", path=str(json_path))
            result["json_path"] = str(json_path)

        # Update index.html with latest redirect
        self._update_index(date_str)

        return result

    def _update_index(self, latest_date: str) -> None:
        """Update public/news/index.html to redirect to latest report."""
        index_path = self.public_dir / "index.html"
        index_html = f"""<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="refresh" content="0;url={latest_date}-trend.html">
  <title>AI 트렌드 리포트 — 최신호로 이동 중</title>
</head>
<body>
  <p><a href="{latest_date}-trend.html">최신 AI 트렌드 리포트로 이동</a></p>
</body>
</html>"""
        index_path.write_text(index_html, encoding="utf-8")
