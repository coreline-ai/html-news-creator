from __future__ import annotations

import hashlib
import re
import textwrap
from datetime import date
from html import escape
from pathlib import Path

_PALETTES = [
    ("#0f172a", "#2563eb", "#60a5fa"),
    ("#111827", "#7c3aed", "#c084fc"),
    ("#172554", "#0891b2", "#67e8f9"),
    ("#14532d", "#16a34a", "#86efac"),
    ("#431407", "#ea580c", "#fdba74"),
]


def _slug(value: str) -> str:
    cleaned = re.sub(r"[^a-zA-Z0-9_-]+", "-", value).strip("-")
    return cleaned[:80] or "section"


def _wrap(value: str, width: int, max_lines: int) -> list[str]:
    text = re.sub(r"\s+", " ", value or "").strip()
    if not text:
        return []
    lines = textwrap.wrap(text, width=width, break_long_words=False)
    return lines[:max_lines]


def create_section_fallback_svg(
    *,
    run_date: date,
    cluster_id: str,
    title: str,
    summary: str = "",
    public_root: str | Path = "public",
) -> str:
    """Create a local visual fallback for sections without source images.

    The return value is a URL relative to `public/news/*.html`.
    """
    digest = hashlib.sha256(f"{cluster_id}:{title}".encode()).hexdigest()
    bg, accent, glow = _PALETTES[int(digest[:2], 16) % len(_PALETTES)]
    safe_cluster = _slug(cluster_id)
    output_dir = Path(public_root) / "assets" / "generated" / str(run_date)
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / f"{safe_cluster}.svg"

    title_lines = _wrap(title or "AI Trend", width=24, max_lines=3)
    summary_lines = _wrap(summary, width=44, max_lines=3)

    title_svg = "\n".join(
        f'<text x="56" y="{180 + idx * 50}" class="title">{escape(line)}</text>'
        for idx, line in enumerate(title_lines)
    )
    summary_start = 180 + max(len(title_lines), 1) * 56 + 24
    summary_svg = "\n".join(
        f'<text x="56" y="{summary_start + idx * 30}" class="summary">{escape(line)}</text>'
        for idx, line in enumerate(summary_lines)
    )

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="630" viewBox="0 0 1200 630" role="img" aria-label="{escape(title)}">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="{bg}"/>
      <stop offset="55%" stop-color="{accent}"/>
      <stop offset="100%" stop-color="{glow}"/>
    </linearGradient>
    <radialGradient id="orb" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#ffffff" stop-opacity="0.60"/>
      <stop offset="100%" stop-color="#ffffff" stop-opacity="0"/>
    </radialGradient>
    <style>
      .eyebrow {{ fill: rgba(255,255,255,0.78); font: 700 28px -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; letter-spacing: 4px; }}
      .title {{ fill: white; font: 800 44px -apple-system, BlinkMacSystemFont, "Apple SD Gothic Neo", "Noto Sans KR", sans-serif; }}
      .summary {{ fill: rgba(255,255,255,0.82); font: 500 24px -apple-system, BlinkMacSystemFont, "Apple SD Gothic Neo", "Noto Sans KR", sans-serif; }}
      .badge {{ fill: rgba(255,255,255,0.18); stroke: rgba(255,255,255,0.38); }}
    </style>
  </defs>
  <rect width="1200" height="630" fill="url(#bg)"/>
  <circle cx="980" cy="120" r="250" fill="url(#orb)"/>
  <circle cx="1080" cy="520" r="320" fill="rgba(255,255,255,0.12)"/>
  <circle cx="120" cy="540" r="220" fill="rgba(15,23,42,0.20)"/>
  <rect x="56" y="60" width="310" height="54" rx="27" class="badge"/>
  <text x="82" y="97" class="eyebrow">AI TREND</text>
  {title_svg}
  {summary_svg}
  <text x="56" y="570" class="summary">Generated fallback visual · {escape(str(run_date))}</text>
</svg>
"""
    output_path.write_text(svg, encoding="utf-8")
    return f"../assets/generated/{run_date}/{output_path.name}"
