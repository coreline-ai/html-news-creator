#!/usr/bin/env python3
"""Export a generated report HTML file to PDF with Playwright.

Examples:
    python scripts/export_pdf.py --date 2026-05-01
    python scripts/export_pdf.py --html public/news/2026-05-01-trend.html
"""
from __future__ import annotations

import argparse
import asyncio
import sys
from datetime import date as date_cls
from pathlib import Path

# Allow ``python scripts/export_pdf.py`` without requiring PYTHONPATH=.
PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from app.rendering.playwright_renderer import (  # noqa: E402
    PlaywrightRenderer,
    PlaywrightUnavailableError,
)


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Export public/news/YYYY-MM-DD-trend.html to PDF.",
    )
    parser.add_argument(
        "--date",
        default=None,
        help="Report date YYYY-MM-DD. Defaults to today when --html is omitted.",
    )
    parser.add_argument(
        "--html",
        default=None,
        help="Input HTML path. Overrides --date-derived input path.",
    )
    parser.add_argument(
        "--output",
        default=None,
        help="Output PDF path. Defaults next to the HTML file.",
    )
    parser.add_argument("--format", default="A4", help="PDF paper format.")
    parser.add_argument(
        "--media",
        choices=["screen", "print"],
        default="screen",
        help="CSS media emulation. screen preserves the published theme.",
    )
    parser.add_argument(
        "--no-print-background",
        action="store_true",
        help="Disable CSS background printing.",
    )
    return parser.parse_args()


async def _main() -> int:
    args = _parse_args()
    run_date = args.date or date_cls.today().isoformat()
    if args.date:
        date_cls.fromisoformat(args.date)

    html_path = Path(args.html) if args.html else Path("public/news") / f"{run_date}-trend.html"
    output_path = (
        Path(args.output)
        if args.output
        else html_path.with_suffix(".pdf")
    )

    if not html_path.is_file():
        print(f"HTML not found: {html_path}", file=sys.stderr)
        return 2

    renderer = PlaywrightRenderer()
    try:
        pdf_path = await renderer.export_pdf(
            str(html_path),
            str(output_path),
            format=args.format,
            media=args.media,
            print_background=not args.no_print_background,
        )
    except PlaywrightUnavailableError as exc:
        print(
            f"{exc}. Install browser runtime with: python -m playwright install chromium",
            file=sys.stderr,
        )
        return 3

    print(pdf_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(asyncio.run(_main()))
