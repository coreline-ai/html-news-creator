from __future__ import annotations
from pathlib import Path
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

    def render_report(
        self,
        report: object,
        sections: list,
        output_theme: str = "dark",
    ) -> str:
        """Render daily report HTML. report and sections can be dicts or ORM objects.

        `output_theme` is forwarded to the Jinja context so the template can
        flip the initial `data-theme` / class on `<html>`. Defaults to "dark"
        to match the operator-facing News Studio default; callers (admin
        publish path, run script) pass through whatever the run options say.
        """
        tmpl = self.env.get_template("report_newsstream.html.j2")
        html = tmpl.render(
            report=report,
            sections=sections,
            output_theme=output_theme,
        )
        self.logger.info(
            "render_complete", sections=len(sections), output_theme=output_theme
        )
        return html

    def render_to_file(
        self,
        report: object,
        sections: list,
        output_path: str,
        output_theme: str = "dark",
    ) -> Path:
        """Render and write to file. Creates parent dirs if needed."""
        html = self.render_report(report, sections, output_theme=output_theme)
        path = Path(output_path)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(html, encoding="utf-8")
        self.logger.info("render_saved", path=str(path), size_bytes=len(html.encode()))
        return path
