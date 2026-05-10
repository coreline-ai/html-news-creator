from __future__ import annotations
from pathlib import Path
import jinja2
from app.utils.logger import get_logger

DEFAULT_OUTPUT_STYLE = "newsstream"
OUTPUT_STYLE_TEMPLATES = {
    "newsstream": "report_newsstream.html.j2",
    "signal_briefing": "report_signal_briefing.html.j2",
}


def normalize_output_style(value: str | None) -> str:
    style = str(value or DEFAULT_OUTPUT_STYLE)
    return style if style in OUTPUT_STYLE_TEMPLATES else DEFAULT_OUTPUT_STYLE


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
        output_style: str = DEFAULT_OUTPUT_STYLE,
    ) -> str:
        """Render daily report HTML. report and sections can be dicts or ORM objects.

        `output_theme` is forwarded to the Jinja context so the template can
        flip the initial `data-theme` / class on `<html>`. Defaults to "dark"
        to match the operator-facing News Studio default; callers (admin
        publish path, run script) pass through whatever the run options say.
        """
        requested_style = str(output_style or DEFAULT_OUTPUT_STYLE)
        style = normalize_output_style(output_style)
        if style != requested_style:
            self.logger.warning(
                "invalid_output_style_fallback",
                output_style=requested_style,
                fallback=style,
            )
        tmpl = self.env.get_template(OUTPUT_STYLE_TEMPLATES[style])
        html = tmpl.render(
            report=report,
            sections=sections,
            output_theme=output_theme,
            output_style=style,
        )
        self.logger.info(
            "render_complete",
            sections=len(sections),
            output_theme=output_theme,
            output_style=style,
        )
        return html

    def render_to_file(
        self,
        report: object,
        sections: list,
        output_path: str,
        output_theme: str = "dark",
        output_style: str = DEFAULT_OUTPUT_STYLE,
    ) -> Path:
        """Render and write to file. Creates parent dirs if needed."""
        html = self.render_report(
            report,
            sections,
            output_theme=output_theme,
            output_style=output_style,
        )
        path = Path(output_path)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(html, encoding="utf-8")
        self.logger.info("render_saved", path=str(path), size_bytes=len(html.encode()))
        return path
