from __future__ import annotations
from pathlib import Path
from datetime import datetime
import jinja2
from app.utils.logger import get_logger


class JinjaRenderer:
    def __init__(self, templates_dir: str = "templates"):
        self.env = jinja2.Environment(
            loader=jinja2.FileSystemLoader(templates_dir),
            autoescape=True,  # XSS prevention — REQUIRED
            undefined=jinja2.Undefined,
        )
        self.logger = get_logger(step="render")

    def render_report(self, report: object, sections: list) -> str:
        """Render daily report HTML. report and sections can be dicts or ORM objects."""
        tmpl = self.env.get_template("report_newsstream.html.j2")
        html = tmpl.render(report=report, sections=sections)
        self.logger.info("render_complete", sections=len(sections))
        return html

    def render_to_file(self, report: object, sections: list, output_path: str) -> Path:
        """Render and write to file. Creates parent dirs if needed."""
        html = self.render_report(report, sections)
        path = Path(output_path)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(html, encoding="utf-8")
        self.logger.info("render_saved", path=str(path), size_bytes=len(html.encode()))
        return path
