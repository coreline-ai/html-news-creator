#!/usr/bin/env python3
from __future__ import annotations

import argparse
import datetime as dt
import html
import json
import math
import re
import sys
import time
import unicodedata
from dataclasses import dataclass
from pathlib import Path
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen

BASE_URL = "https://styles.refero.design"
DEFAULT_OUT_DIR = Path("demo/2026-05-01/refero-design-md")
DEFAULT_LIBRARY_HTML = Path("demo/2026-05-01/refero-design-library.html")
USER_AGENT = "html-news-creator refero-design-catalog/1.0 (public reference only; polite local catalog)"
SORTS = ("trending", "popular", "newest")
UUID_RE = re.compile(r"styles\.refero\.design/style/([0-9a-fA-F-]{36})")
HEX_RE = re.compile(r"^#[0-9a-fA-F]{6}$")
MAX_COLORS_IN_MD = 10
MAX_COLORS_IN_CATALOG = 6
MAX_COMPONENTS_IN_MD = 5
MAX_SURFACES_IN_MD = 5
MAX_TEXT = 220


@dataclass(frozen=True)
class CrawlStats:
    discovered: int
    existing_ids: int
    skipped_existing: int
    generated_docs: int
    detail_failures: int
    catalog_entries: int


class ReferoError(RuntimeError):
    pass


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Create a local Refero design style catalog from public style metadata.",
    )
    parser.add_argument("--out-dir", type=Path, default=DEFAULT_OUT_DIR)
    parser.add_argument("--library-html", type=Path, default=DEFAULT_LIBRARY_HTML)
    parser.add_argument("--base-url", default=BASE_URL)
    parser.add_argument("--sorts", default=",".join(SORTS), help="Comma-separated list: trending,popular,newest")
    parser.add_argument("--max-pages", type=int, default=250, help="Safety cap per list mode")
    parser.add_argument("--sleep-sec", type=float, default=0.18, help="Delay after public API requests")
    parser.add_argument("--retries", type=int, default=3)
    parser.add_argument("--timeout-sec", type=float, default=25.0)
    parser.add_argument("--refresh-existing", action="store_true", help="Regenerate docs even when an ID already has a local MD")
    parser.add_argument("--no-cache", action="store_true", help="Do not use the local detail JSON cache")
    parser.add_argument("--dry-run", action="store_true")
    return parser.parse_args(argv)


def eprint(message: str) -> None:
    print(message, file=sys.stderr, flush=True)


def fetch_json(
    url: str,
    *,
    retries: int,
    timeout_sec: float,
    sleep_sec: float,
    cache_path: Path | None = None,
) -> dict[str, Any]:
    if cache_path and cache_path.exists():
        with cache_path.open("r", encoding="utf-8") as fp:
            return json.load(fp)

    last_error: Exception | None = None
    for attempt in range(1, retries + 1):
        try:
            req = Request(
                url,
                headers={
                    "Accept": "application/json",
                    "User-Agent": USER_AGENT,
                },
            )
            with urlopen(req, timeout=timeout_sec) as response:
                payload = json.load(response)
            if sleep_sec > 0:
                time.sleep(sleep_sec)
            if cache_path:
                cache_path.parent.mkdir(parents=True, exist_ok=True)
                tmp = cache_path.with_suffix(cache_path.suffix + ".tmp")
                with tmp.open("w", encoding="utf-8") as fp:
                    json.dump(payload, fp, ensure_ascii=False, indent=2)
                    fp.write("\n")
                tmp.replace(cache_path)
            if not isinstance(payload, dict):
                raise ReferoError(f"Unexpected JSON payload for {url}: {type(payload).__name__}")
            return payload
        except HTTPError as exc:
            last_error = exc
            if exc.code not in {408, 425, 429, 500, 502, 503, 504}:
                break
        except (TimeoutError, URLError, json.JSONDecodeError) as exc:
            last_error = exc
        wait = min(12.0, (1.7 ** attempt) + 0.25)
        eprint(f"[retry {attempt}/{retries}] {url} failed: {last_error}; sleeping {wait:.1f}s")
        time.sleep(wait)
    raise ReferoError(f"Failed to fetch {url}: {last_error}")


def list_url(base_url: str, sort: str, page: int | None = None, cursor: str | None = None) -> str:
    params: dict[str, str] = {"sort": sort}
    if cursor:
        params["cursor"] = cursor
    elif page is not None:
        params["page"] = str(page)
    return f"{base_url.rstrip('/')}/api/styles?{urlencode(params)}"


def detail_url(base_url: str, style_id: str) -> str:
    return f"{base_url.rstrip('/')}/api/styles/{style_id}"


def style_page_url(base_url: str, style_id: str) -> str:
    return f"{base_url.rstrip('/')}/style/{style_id}"


def discover_styles(args: argparse.Namespace) -> dict[str, dict[str, Any]]:
    discovered: dict[str, dict[str, Any]] = {}
    sorts = [s.strip() for s in args.sorts.split(",") if s.strip()]
    for sort in sorts:
        if sort == "newest":
            cursor: str | None = None
            seen_cursors: set[str] = set()
            for page_no in range(1, args.max_pages + 1):
                url = list_url(args.base_url, sort, cursor=cursor)
                payload = fetch_json(
                    url,
                    retries=args.retries,
                    timeout_sec=args.timeout_sec,
                    sleep_sec=args.sleep_sec,
                )
                styles = payload.get("styles") or []
                if not isinstance(styles, list) or not styles:
                    eprint(f"[discover] {sort} cursor page {page_no}: empty; stop")
                    break
                added = merge_summaries(discovered, styles, sort)
                eprint(f"[discover] {sort} cursor page {page_no}: {len(styles)} items, +{added} new")
                next_cursor = payload.get("nextCursor")
                if not next_cursor or not isinstance(next_cursor, str):
                    break
                if next_cursor in seen_cursors:
                    eprint(f"[discover] {sort}: repeated cursor; stop")
                    break
                seen_cursors.add(next_cursor)
                cursor = next_cursor
            continue

        for page in range(1, args.max_pages + 1):
            url = list_url(args.base_url, sort, page=page)
            payload = fetch_json(
                url,
                retries=args.retries,
                timeout_sec=args.timeout_sec,
                sleep_sec=args.sleep_sec,
            )
            styles = payload.get("styles") or []
            if not isinstance(styles, list) or not styles:
                eprint(f"[discover] {sort} page {page}: empty; stop")
                break
            added = merge_summaries(discovered, styles, sort)
            eprint(f"[discover] {sort} page {page}: {len(styles)} items, +{added} new")
    return discovered


def merge_summaries(discovered: dict[str, dict[str, Any]], styles: list[Any], sort: str) -> int:
    added = 0
    for raw in styles:
        if not isinstance(raw, dict):
            continue
        style_id = str(raw.get("id") or "").strip()
        if not style_id:
            continue
        if style_id not in discovered:
            copy = dict(raw)
            copy["firstSeenSort"] = sort
            copy["seenSorts"] = [sort]
            discovered[style_id] = copy
            added += 1
        else:
            seen = discovered[style_id].setdefault("seenSorts", [])
            if sort not in seen:
                seen.append(sort)
    return added


def extract_existing_paths(out_dir: Path) -> dict[str, Path]:
    paths: dict[str, Path] = {}
    if not out_dir.exists():
        return paths
    for md_path in out_dir.rglob("*.md"):
        if md_path.name.startswith("_catalog"):
            continue
        try:
            text = md_path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            text = md_path.read_text(errors="ignore")
        for style_id in UUID_RE.findall(text):
            paths.setdefault(style_id.lower(), md_path)
    return paths


def normalize_entry(
    style_id: str,
    summary: dict[str, Any],
    detail: dict[str, Any] | None,
    base_url: str,
) -> dict[str, Any]:
    style = (detail or {}).get("style") if isinstance(detail, dict) else None
    if not isinstance(style, dict):
        style = {}
    design = ((style.get("fullResult") or {}).get("designSystem") or {}) if isinstance(style.get("fullResult"), dict) else {}
    if not isinstance(design, dict):
        design = {}

    name = text_value(design.get("siteName") or style.get("siteName") or summary.get("siteName") or "Untitled")
    colors = normalize_colors(design.get("colors") or summary.get("colors") or [])
    typography = normalize_typography(design.get("typography") or [])
    fonts = normalize_fonts(summary.get("fonts"), typography)
    theme = text_value(design.get("theme") or style.get("colorScheme") or summary.get("colorScheme") or "unknown").lower()
    if theme not in {"light", "dark", "mixed", "both"}:
        theme = "mixed" if "dark" in theme and "light" in theme else (theme or "unknown")
    industry = text_value(design.get("industry") or style.get("industry") or summary.get("industry") or "")
    north_star = clean_sentence(design.get("northStar") or summary.get("northStar") or "")
    description = clean_sentence(design.get("description") or summary.get("description") or "")
    spacing = design.get("spacing") if isinstance(design.get("spacing"), dict) else {}
    components = normalize_named_blocks(design.get("components") or [], ("name", "role", "description"))
    surfaces = normalize_named_blocks(design.get("surfaces") or [], ("name", "hex", "purpose"))

    return {
        "id": style_id,
        "name": name,
        "slug": slugify(name) or f"style-{style_id[:8]}",
        "siteUrl": text_value(style.get("url") or summary.get("url") or ""),
        "referoUrl": style_page_url(base_url, style_id),
        "theme": theme,
        "industry": industry,
        "northStar": north_star,
        "description": description,
        "fit": infer_fit(name, theme, industry, north_star, description, colors, fonts),
        "colors": colors,
        "fonts": fonts,
        "typography": typography,
        "spacing": spacing,
        "components": components,
        "surfaces": surfaces,
        "createdAt": text_value(style.get("createdAt") or summary.get("createdAt") or ""),
        "firstSeenSort": text_value(summary.get("firstSeenSort") or ""),
        "seenSorts": summary.get("seenSorts") if isinstance(summary.get("seenSorts"), list) else [],
        "thumbnailUrl": text_value(style.get("thumbnailUrl") or summary.get("thumbnailUrl") or ""),
        "hasDetail": bool(detail),
    }


def text_value(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, str):
        return " ".join(value.strip().split())
    return " ".join(str(value).strip().split())


def clean_sentence(value: Any, limit: int = MAX_TEXT) -> str:
    text = text_value(value)
    text = text.replace("`", "'")
    if len(text) <= limit:
        return text
    cut = text[: limit - 1].rsplit(" ", 1)[0]
    return f"{cut}…"


def normalize_colors(raw: Any) -> list[dict[str, str]]:
    colors: list[dict[str, str]] = []
    if not isinstance(raw, list):
        return colors
    for item in raw:
        if not isinstance(item, dict):
            continue
        hex_value = text_value(item.get("hex"))
        if not HEX_RE.match(hex_value):
            continue
        colors.append(
            {
                "name": text_value(item.get("name") or "Color"),
                "hex": hex_value.lower(),
                "group": text_value(item.get("group") or ""),
                "role": clean_sentence(item.get("role") or "", 140),
            }
        )
    return colors


def normalize_typography(raw: Any) -> list[dict[str, str]]:
    typography: list[dict[str, str]] = []
    if not isinstance(raw, list):
        return typography
    for item in raw:
        if not isinstance(item, dict):
            continue
        family = text_value(item.get("family"))
        if not family:
            continue
        typography.append(
            {
                "family": family,
                "role": clean_sentence(item.get("role") or "", 130),
                "sizes": text_value(item.get("sizes") or ""),
                "weight": text_value(item.get("weight") or ""),
                "lineHeight": text_value(item.get("lineHeight") or ""),
                "substitute": text_value(item.get("substitute") or ""),
            }
        )
    return typography


def normalize_fonts(summary_fonts: Any, typography: list[dict[str, str]]) -> list[str]:
    fonts: list[str] = []
    if isinstance(summary_fonts, list):
        for font in summary_fonts:
            add_unique(fonts, text_value(font))
    for item in typography:
        add_unique(fonts, item.get("family", ""))
        substitute = item.get("substitute", "")
        if substitute:
            add_unique(fonts, substitute.split(",", 1)[0])
    return fonts[:8]


def add_unique(values: list[str], value: str) -> None:
    value = text_value(value)
    if value and value not in values:
        values.append(value)


def normalize_named_blocks(raw: Any, keys: tuple[str, ...]) -> list[dict[str, str]]:
    blocks: list[dict[str, str]] = []
    if not isinstance(raw, list):
        return blocks
    for item in raw:
        if not isinstance(item, dict):
            continue
        block = {key: clean_sentence(item.get(key) or "", 150) for key in keys}
        if any(block.values()):
            blocks.append(block)
    return blocks


def slugify(value: str) -> str:
    normalized = unicodedata.normalize("NFKD", value)
    ascii_value = normalized.encode("ascii", "ignore").decode("ascii")
    ascii_value = re.sub(r"[^a-zA-Z0-9]+", "-", ascii_value).strip("-").lower()
    return re.sub(r"-{2,}", "-", ascii_value)[:72]


def infer_fit(
    name: str,
    theme: str,
    industry: str,
    north_star: str,
    description: str,
    colors: list[dict[str, str]],
    fonts: list[str],
) -> str:
    haystack = " ".join(
        [
            name,
            theme,
            industry,
            north_star,
            description,
            " ".join(fonts),
            " ".join(c.get("name", "") for c in colors),
            " ".join(c.get("group", "") for c in colors),
        ]
    ).lower()
    if any(token in haystack for token in ["terminal", "command", "developer", "code", "github", "linear", "cursor", "supabase", "vercel", "render"]):
        return "Admin console / run monitor / developer tooling"
    if any(token in haystack for token in ["journal", "editorial", "serif", "news", "magazine", "essay", "public", "financial journal"]):
        return "Editorial report / executive brief"
    if any(token in haystack for token in ["data", "analytics", "ledger", "chart", "finance", "trading", "dashboard", "table"]):
        return "Source ledger / evidence dashboard"
    if any(token in haystack for token in ["gradient", "neon", "vivid", "playful", "creator", "marketing", "ecommerce", "product", "color"]):
        return "Visual board / colorful report variant"
    if any(token in haystack for token in ["ai", "research", "lab", "model", "agent"]):
        return "Research brief / AI trend page"
    if theme == "dark":
        return "Dark webapp exploration"
    return "Design reference / webapp exploration"


def color_luminance(hex_value: str) -> float:
    value = hex_value.lstrip("#")
    if len(value) != 6:
        return 0.5
    r, g, b = (int(value[i : i + 2], 16) / 255 for i in (0, 2, 4))
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def suggested_color_role(color: dict[str, str]) -> str:
    group = color.get("group", "").lower()
    name = color.get("name", "").lower()
    lum = color_luminance(color.get("hex", ""))
    if group in {"brand", "accent", "semantic"} or any(k in name for k in ["blue", "violet", "orange", "green", "red", "yellow", "pink"]):
        return "Action accent / signal color"
    if lum < 0.25:
        return "Primary text or dark surface"
    if lum > 0.85:
        return "Page background or card surface"
    return "Border, muted text, or supporting surface"


def css_var_name(color_name: str) -> str:
    return f"--ref-{slugify(color_name) or 'color'}"


def markdown_escape(value: str) -> str:
    return text_value(value).replace("|", "\\|")


def html_escape(value: Any) -> str:
    return html.escape(text_value(value), quote=True)


def unique_md_path(out_dir: Path, entry: dict[str, Any], taken_paths: set[Path]) -> Path:
    docs_dir = out_dir / "all"
    docs_dir.mkdir(parents=True, exist_ok=True)
    base = slugify(entry["name"]) or f"style-{entry['id'][:8]}"
    candidate = docs_dir / f"{base}-{entry['id'][:8]}.md"
    suffix = 2
    while candidate in taken_paths or candidate.exists():
        candidate = docs_dir / f"{base}-{entry['id'][:8]}-{suffix}.md"
        suffix += 1
    taken_paths.add(candidate)
    return candidate


def render_style_md(entry: dict[str, Any]) -> str:
    name = entry["name"]
    lines: list[str] = []
    lines.append(f"# {name} - Refero Design MD")
    lines.append("")
    lines.append(f"- Source: {entry['referoUrl']}")
    if entry.get("siteUrl"):
        lines.append(f"- Original site: {entry['siteUrl']}")
    lines.append(f"- Theme: `{entry.get('theme') or 'unknown'}`")
    if entry.get("industry"):
        lines.append(f"- Industry: `{entry['industry']}`")
    lines.append(f"- Recommended fit: **{entry['fit']}**")
    lines.append("- Status: generated local summary; existing curated IDs are not overwritten")
    lines.append("")
    lines.append("## Why this fits html-news-creator")
    note = entry.get("northStar") or entry.get("description") or "Use this as a compact design reference for future demo variants and admin webapp explorations."
    lines.append(note)
    lines.append("")
    lines.append("## Apply to")
    for item in apply_to_items(entry["fit"], entry.get("theme", "")):
        lines.append(f"- {item}")
    lines.append("")
    lines.append("## Core tokens to borrow")
    lines.append("")
    colors = entry.get("colors", [])[:MAX_COLORS_IN_MD]
    if colors:
        lines.append("| Name | Hex | Group | Suggested role |")
        lines.append("|---|---:|---|---|")
        for color in colors:
            lines.append(
                "| {name} | `{hex}` | {group} | {role} |".format(
                    name=markdown_escape(color.get("name", "Color")),
                    hex=color.get("hex", ""),
                    group=markdown_escape(color.get("group") or "token"),
                    role=markdown_escape(suggested_color_role(color)),
                )
            )
        lines.append("")
        lines.append("```css")
        lines.append(":root {")
        for color in colors[:8]:
            lines.append(f"  {css_var_name(color.get('name', 'color'))}: {color.get('hex', '')};")
        lines.append("}")
        lines.append("```")
    else:
        lines.append("No palette tokens were available in the public style metadata.")
    lines.append("")
    lines.append("## Typography direction")
    typography = entry.get("typography", [])
    fonts = entry.get("fonts", [])
    if typography:
        for item in typography[:3]:
            label = item.get("family", "Type")
            detail = ", ".join(x for x in [item.get("weight"), item.get("sizes"), item.get("lineHeight")] if x)
            substitute = f"; substitute `{item['substitute']}`" if item.get("substitute") else ""
            lines.append(f"- **{label}**: {detail or 'use as primary family'}{substitute}.")
    elif fonts:
        lines.append(f"- Primary: **{fonts[0]}**; substitute `Inter, system-ui` when unavailable.")
        if len(fonts) > 1:
            lines.append(f"- Supporting families: {', '.join(f'**{font}**' for font in fonts[1:4])}.")
    else:
        lines.append("- Use the project default stack: Pretendard / Inter / system-ui.")
    lines.append("")
    lines.append("## Spacing / shape")
    spacing = entry.get("spacing") if isinstance(entry.get("spacing"), dict) else {}
    if spacing:
        for key in ["sectionGap", "cardPadding", "elementGap", "pageMaxWidth"]:
            if spacing.get(key):
                lines.append(f"- {labelize(key)}: `{text_value(spacing[key])}`")
        radius = spacing.get("radius")
        if isinstance(radius, dict) and radius:
            formatted = ", ".join(f"{k}: {v}" for k, v in list(radius.items())[:8])
            lines.append(f"- Radius: `{formatted}`")
    else:
        lines.append("- Keep section rhythm explicit; use the palette and typography above as the primary cues.")
    lines.append("")
    surfaces = entry.get("surfaces", [])[:MAX_SURFACES_IN_MD]
    if surfaces:
        lines.append("## Surface cues")
        for surface in surfaces:
            name = surface.get("name") or "Surface"
            hex_value = f" `{surface['hex']}`" if surface.get("hex") else ""
            purpose = surface.get("purpose") or "Use as a local surface layer."
            lines.append(f"- **{name}**{hex_value}: {purpose}")
        lines.append("")
    components = entry.get("components", [])[:MAX_COMPONENTS_IN_MD]
    if components:
        lines.append("## Component cues")
        for component in components:
            name = component.get("name") or "Component"
            role = component.get("role") or component.get("description") or "Reference component style."
            lines.append(f"- **{name}**: {role}")
        lines.append("")
    lines.append("## Agent notes")
    lines.append("- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.")
    lines.append("- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.")
    lines.append("- This document links back to the Refero source page instead of mirroring media assets.")
    lines.append("")
    return "\n".join(lines)


def apply_to_items(fit: str, theme: str) -> list[str]:
    if "Admin console" in fit:
        return ["Admin run monitor and review states", "Compact evidence cards and source inspection panels", "Dark-mode operational dashboards"]
    if "Editorial" in fit:
        return ["Long-form AI report reading experience", "Executive brief layouts and narrative summaries", "Article cards with strong typography hierarchy"]
    if "Source ledger" in fit:
        return ["Source ledger, ranking, and verification screens", "Cluster evidence dashboards", "Dense data tables with clear hierarchy"]
    if "Visual board" in fit:
        return ["Colorful demo variants and visual-board layouts", "Hero cards and image-led sections", "Marketing-style preview pages for generated reports"]
    if "Research" in fit:
        return ["Research section pages and model-release briefs", "Lab-note style cards", "AI product/research trend summaries"]
    if theme == "dark":
        return ["Dark theme experiments", "Operator-focused widgets", "High-contrast card systems"]
    return ["General webapp UI exploration", "Demo cards and catalog surfaces", "Future admin/subscriber UI references"]


def labelize(value: str) -> str:
    return re.sub(r"(?<!^)([A-Z])", r" \1", value).replace("_", " ").title()


def write_text(path: Path, text: str, dry_run: bool) -> None:
    if dry_run:
        eprint(f"[dry-run] would write {path}")
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def build_catalog_entries(
    discovered: dict[str, dict[str, Any]],
    existing_paths: dict[str, Path],
    generated_entries: dict[str, dict[str, Any]],
    generated_paths: dict[str, Path],
    out_dir: Path,
    base_url: str,
) -> list[dict[str, Any]]:
    entries: list[dict[str, Any]] = []
    for style_id, summary in discovered.items():
        entry = dict(generated_entries.get(style_id) or normalize_entry(style_id, summary, None, base_url))
        path = generated_paths.get(style_id) or existing_paths.get(style_id.lower())
        if path:
            entry["localMd"] = str(path.relative_to(out_dir.parent))
            entry["documentStatus"] = "generated" if style_id in generated_paths else "curated-or-existing"
        else:
            entry["localMd"] = ""
            entry["documentStatus"] = "missing-detail"
        entry["colors"] = entry.get("colors", [])[:MAX_COLORS_IN_CATALOG]
        entries.append(entry)
    entries.sort(key=lambda item: (item.get("documentStatus") != "generated", item.get("name", "").lower(), item.get("id", "")))
    return entries


def render_catalog_md(entries: list[dict[str, Any]], stats: CrawlStats, generated_at: str) -> str:
    lines = [
        "# Refero Design Catalog - All Local References",
        "",
        f"- Generated at: `{generated_at}`",
        f"- Discovered public styles: **{stats.discovered}**",
        f"- Existing local style IDs skipped: **{stats.skipped_existing}** / {stats.existing_ids}",
        f"- Newly generated Markdown docs: **{stats.generated_docs}**",
        f"- Detail fetch failures: **{stats.detail_failures}**",
        "- Scope: concise local summaries, token references, and links back to Refero source pages; media assets are not downloaded.",
        "",
        "## Local library files",
        "",
        "- HTML library: [`../refero-design-library.html`](../refero-design-library.html)",
        "- JSON catalog: [`_catalog_all.json`](_catalog_all.json)",
        "- Previous curated shortlist: [`_catalog.md`](_catalog.md)",
        "",
        "## Entries",
        "",
        "| Name | Theme | Industry | Fit | Local MD | Source | Colors |",
        "|---|---|---|---|---|---|---|",
    ]
    for entry in entries:
        local_md = entry.get("localMd") or ""
        local_link = f"[`{Path(local_md).name}`]({Path(local_md).relative_to('refero-design-md') if local_md.startswith('refero-design-md/') else local_md})" if local_md else "-"
        source_link = f"[Refero]({entry.get('referoUrl', '')})"
        colors = " ".join(color.get("hex", "") for color in entry.get("colors", [])[:4])
        lines.append(
            "| {name} | `{theme}` | {industry} | {fit} | {local} | {source} | {colors} |".format(
                name=markdown_escape(entry.get("name", "Untitled")),
                theme=markdown_escape(entry.get("theme", "unknown")),
                industry=markdown_escape(entry.get("industry", "-") or "-"),
                fit=markdown_escape(entry.get("fit", "-")),
                local=local_link,
                source=source_link,
                colors=markdown_escape(colors),
            )
        )
    lines.append("")
    return "\n".join(lines)


def render_catalog_json(entries: list[dict[str, Any]], stats: CrawlStats, generated_at: str, base_url: str) -> str:
    payload = {
        "generatedAt": generated_at,
        "source": base_url.rstrip("/"),
        "scope": "public Refero style metadata converted into concise local design references",
        "stats": {
            "discovered": stats.discovered,
            "existingIds": stats.existing_ids,
            "skippedExisting": stats.skipped_existing,
            "generatedDocs": stats.generated_docs,
            "detailFailures": stats.detail_failures,
            "catalogEntries": stats.catalog_entries,
        },
        "entries": [catalog_entry_json(entry) for entry in entries],
    }
    return json.dumps(payload, ensure_ascii=False, indent=2) + "\n"


def catalog_entry_json(entry: dict[str, Any]) -> dict[str, Any]:
    return {
        "id": entry.get("id"),
        "name": entry.get("name"),
        "theme": entry.get("theme"),
        "industry": entry.get("industry"),
        "fit": entry.get("fit"),
        "siteUrl": entry.get("siteUrl"),
        "referoUrl": entry.get("referoUrl"),
        "localMd": entry.get("localMd"),
        "documentStatus": entry.get("documentStatus"),
        "firstSeenSort": entry.get("firstSeenSort"),
        "seenSorts": entry.get("seenSorts"),
        "createdAt": entry.get("createdAt"),
        "northStar": entry.get("northStar"),
        "colors": entry.get("colors", [])[:MAX_COLORS_IN_CATALOG],
        "fonts": entry.get("fonts", [])[:6],
    }


def render_library_html(entries: list[dict[str, Any]], stats: CrawlStats, generated_at: str) -> str:
    theme_counts = count_by(entries, "theme")
    status_counts = count_by(entries, "documentStatus")
    industry_options = sorted({entry.get("industry", "") for entry in entries if entry.get("industry")})[:200]
    cards = "\n".join(render_style_card(entry) for entry in entries)
    industry_option_html = "\n".join(
        f'<option value="{html_escape(value)}">{html_escape(value)}</option>' for value in industry_options
    )
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Refero Design Library · html-news-creator</title>
<link rel="icon" href="data:,">
<style>
:root {{
  --ink:#17130f; --muted:#665f57; --paper:#f7f1e6; --card:#fffaf1; --line:rgba(23,19,15,.14);
  --dark:#111214; --blue:#406cff; --violet:#8f5cff; --green:#1fbf84; --orange:#ff8a3d;
}}
*{{box-sizing:border-box}} html{{scroll-behavior:smooth}} body{{margin:0;font-family:Pretendard,Inter,-apple-system,BlinkMacSystemFont,system-ui,sans-serif;color:var(--ink);background:radial-gradient(circle at 7% -10%,rgba(64,108,255,.22),transparent 32%),radial-gradient(circle at 95% 5%,rgba(255,138,61,.22),transparent 30%),linear-gradient(180deg,#f9f3e9 0%,#efe5d6 100%);-webkit-font-smoothing:antialiased}}
a{{color:inherit;text-decoration:none}} .nav{{position:sticky;top:0;z-index:20;display:flex;justify-content:space-between;align-items:center;gap:16px;padding:14px 22px;background:rgba(249,243,233,.82);border-bottom:1px solid var(--line);backdrop-filter:blur(18px)}}
.nav strong{{font-size:13px;letter-spacing:.02em}} .nav .links{{display:flex;gap:8px;flex-wrap:wrap}} .nav a{{border:1px solid var(--line);border-radius:999px;padding:8px 10px;font-size:12px;font-weight:800;background:rgba(255,255,255,.42)}}
.wrap{{max-width:1440px;margin:0 auto;padding:54px 24px 96px}} .hero{{display:grid;grid-template-columns:1.05fr .95fr;gap:28px;align-items:end;margin-bottom:28px}} .kicker{{font-size:12px;text-transform:uppercase;letter-spacing:.14em;font-weight:950;color:#6a5b48}}
h1{{font-size:clamp(48px,8vw,112px);line-height:.86;letter-spacing:-.085em;margin:8px 0 0;max-width:980px}} .hero p{{font-size:17px;line-height:1.68;color:var(--muted);margin:0;max-width:720px}} .hero-card{{border:1px solid var(--line);border-radius:34px;padding:22px;background:rgba(255,250,241,.74);box-shadow:0 24px 80px rgba(49,35,18,.12)}}
.stats{{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:10px;margin-top:18px}} .stat{{border:1px solid var(--line);border-radius:22px;padding:16px;background:#fff}} .stat b{{display:block;font-size:28px;letter-spacing:-.05em}} .stat span{{font-size:10px;text-transform:uppercase;letter-spacing:.12em;color:var(--muted);font-weight:900}}
.filters{{position:sticky;top:59px;z-index:15;display:grid;grid-template-columns:2fr repeat(3,1fr);gap:10px;padding:12px;margin:24px 0 18px;background:rgba(249,243,233,.9);border:1px solid var(--line);border-radius:24px;backdrop-filter:blur(18px)}} input,select{{width:100%;border:1px solid var(--line);border-radius:16px;padding:12px 13px;font:inherit;font-size:14px;background:#fff;color:var(--ink)}}
.summary{{display:flex;gap:10px;flex-wrap:wrap;margin:0 0 18px}} .pill{{display:inline-flex;gap:6px;align-items:center;border:1px solid var(--line);border-radius:999px;padding:8px 10px;background:rgba(255,255,255,.58);font-size:12px;font-weight:850;color:#564b40}}
.grid{{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:14px}} .style-card{{min-height:312px;position:relative;overflow:hidden;border:1px solid var(--line);border-radius:28px;padding:18px;display:flex;flex-direction:column;justify-content:space-between;background:var(--bg,#fff);box-shadow:0 18px 56px rgba(49,35,18,.10)}} .style-card:before{{content:"";position:absolute;inset:0 0 auto 0;height:9px;background:var(--strip,linear-gradient(90deg,#111,#777))}} .style-card:after{{content:"";position:absolute;right:-58px;top:-58px;width:150px;height:150px;border-radius:999px;background:var(--strip,linear-gradient(90deg,#111,#777));filter:blur(22px);opacity:.22}} .style-card>*{{position:relative;z-index:1}}
.style-card.dark{{background:#111214;color:#f8f3eb;border-color:rgba(255,255,255,.12)}} .style-card.mixed{{background:linear-gradient(135deg,#121316 0%,#262a36 48%,#fffaf1 49%,#fff 100%);color:#fff}} .style-card.mixed .note{{background:rgba(0,0,0,.44);border-radius:14px;padding:8px}}
.topline{{display:flex;justify-content:space-between;gap:12px;align-items:center;font-size:10px;letter-spacing:.08em;text-transform:uppercase;font-weight:950;opacity:.72}} h2{{font-size:27px;line-height:.96;letter-spacing:-.06em;margin:16px 0 0}} .fit{{display:inline-flex;margin-top:10px;border:1px solid currentColor;border-radius:999px;padding:6px 9px;font-size:11px;font-weight:900;opacity:.7}} .note{{font-size:13px;line-height:1.48;color:inherit;opacity:.72;margin:12px 0 0;display:-webkit-box;-webkit-line-clamp:4;-webkit-box-orient:vertical;overflow:hidden}}
.swatches{{display:flex;gap:6px;flex-wrap:wrap;margin-top:14px}} .swatches span{{width:26px;height:26px;border-radius:999px;border:1px solid rgba(128,128,128,.35);box-shadow:inset 0 0 0 1px rgba(255,255,255,.16)}} .fonts{{font-size:11px;opacity:.68;margin-top:10px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}}
.actions{{display:flex;gap:8px;flex-wrap:wrap;margin-top:16px}} .actions a{{border-radius:999px;padding:9px 11px;font-size:12px;font-weight:900;border:1px solid currentColor}} .actions a.primary{{background:var(--ink);color:#fff;border-color:var(--ink)}} .dark .actions a.primary,.mixed .actions a.primary{{background:#fff;color:#111;border-color:#fff}}
.empty{{display:none;border:1px dashed var(--line);border-radius:24px;padding:24px;background:rgba(255,255,255,.52);color:var(--muted);font-weight:800}} body.no-results .empty{{display:block}} body.no-results .grid{{display:none}}
.footer{{margin-top:30px;color:var(--muted);font-size:13px;line-height:1.6}}
@media(max-width:1180px){{.grid{{grid-template-columns:repeat(3,1fr)}}.hero{{grid-template-columns:1fr}}}}
@media(max-width:860px){{.grid{{grid-template-columns:repeat(2,1fr)}}.filters{{grid-template-columns:1fr 1fr}}.stats{{grid-template-columns:repeat(2,1fr)}}.nav{{align-items:flex-start;flex-direction:column}}}}
@media(max-width:560px){{.grid{{grid-template-columns:1fr}}.filters{{position:relative;top:auto;grid-template-columns:1fr}}h1{{font-size:52px}}}}
</style>
</head>
<body>
<nav class="nav"><strong>Refero Design Library · html-news-creator</strong><div class="links"><a href="index.html">Demo index</a><a href="refero-design-md/_catalog_all.md">Catalog MD</a><a href="refero-design-md/_catalog_all.json">Catalog JSON</a><a href="https://styles.refero.design/">Refero source</a></div></nav>
<main class="wrap">
  <section class="hero">
    <div>
      <div class="kicker">Public style references · local MD library</div>
      <h1>Design systems, indexed for report UI experiments.</h1>
    </div>
    <div class="hero-card">
      <p>Concise local references generated from public Refero style metadata. Existing curated Markdown files are preserved; missing styles get new local MD documents under <code>refero-design-md/all/</code>.</p>
      <div class="stats">
        <div class="stat"><b>{stats.discovered}</b><span>Discovered</span></div>
        <div class="stat"><b>{stats.generated_docs}</b><span>New MD</span></div>
        <div class="stat"><b>{stats.skipped_existing}</b><span>Skipped IDs</span></div>
        <div class="stat"><b>{stats.detail_failures}</b><span>Failures</span></div>
      </div>
    </div>
  </section>
  <section class="filters" aria-label="Library filters">
    <input id="q" type="search" placeholder="Search name, fit, industry, colors, fonts...">
    <select id="theme"><option value="">All themes</option><option value="light">Light</option><option value="dark">Dark</option><option value="mixed">Mixed</option><option value="both">Both</option><option value="unknown">Unknown</option></select>
    <select id="industry"><option value="">All industries</option>{industry_option_html}</select>
    <select id="status"><option value="">All docs</option><option value="generated">Generated</option><option value="curated-or-existing">Curated / existing</option><option value="missing-detail">Missing detail</option></select>
  </section>
  <div class="summary">
    <span class="pill" id="visibleCount">{len(entries)} visible</span>
    <span class="pill">Light {theme_counts.get('light', 0)}</span>
    <span class="pill">Dark {theme_counts.get('dark', 0)}</span>
    <span class="pill">Mixed {theme_counts.get('mixed', 0) + theme_counts.get('both', 0)}</span>
    <span class="pill">Generated {status_counts.get('generated', 0)}</span>
    <span class="pill">Built {html_escape(generated_at)}</span>
  </div>
  <p class="empty">No matching style references. Clear filters to show the full library.</p>
  <section class="grid" id="cards">
{cards}
  </section>
  <p class="footer">This page intentionally references source URLs and local Markdown summaries only. It does not download or mirror Refero media assets.</p>
</main>
<script>
const cards = [...document.querySelectorAll('.style-card')];
const q = document.querySelector('#q');
const theme = document.querySelector('#theme');
const industry = document.querySelector('#industry');
const status = document.querySelector('#status');
const visibleCount = document.querySelector('#visibleCount');
function applyFilters() {{
  const query = q.value.trim().toLowerCase();
  const wantedTheme = theme.value;
  const wantedIndustry = industry.value;
  const wantedStatus = status.value;
  let visible = 0;
  for (const card of cards) {{
    const text = card.dataset.search || '';
    const ok = (!query || text.includes(query)) && (!wantedTheme || card.dataset.theme === wantedTheme) && (!wantedIndustry || card.dataset.industry === wantedIndustry) && (!wantedStatus || card.dataset.status === wantedStatus);
    card.hidden = !ok;
    if (ok) visible += 1;
  }}
  visibleCount.textContent = `${{visible}} visible`;
  document.body.classList.toggle('no-results', visible === 0);
}}
[q, theme, industry, status].forEach(el => el.addEventListener('input', applyFilters));
applyFilters();
</script>
</body>
</html>
"""


def count_by(entries: list[dict[str, Any]], key: str) -> dict[str, int]:
    counts: dict[str, int] = {}
    for entry in entries:
        value = text_value(entry.get(key) or "unknown")
        counts[value] = counts.get(value, 0) + 1
    return counts


def render_style_card(entry: dict[str, Any]) -> str:
    theme = entry.get("theme") or "unknown"
    card_class = "dark" if theme == "dark" else ("mixed" if theme in {"mixed", "both"} else "light")
    colors = entry.get("colors", [])[:MAX_COLORS_IN_CATALOG]
    strip = gradient(colors)
    swatches = "".join(
        f'<span style="background:{html_escape(color.get("hex", ""))}" title="{html_escape(color.get("name", "Color"))} {html_escape(color.get("hex", ""))}"></span>'
        for color in colors
    )
    fonts = ", ".join(entry.get("fonts", [])[:4])
    note = entry.get("northStar") or entry.get("description") or "Compact design reference for local UI exploration."
    local_md = entry.get("localMd") or ""
    md_href = html_escape(local_md) if local_md else "#"
    md_label = "Open MD" if local_md else "No local MD"
    source = html_escape(entry.get("referoUrl") or "#")
    site_url = entry.get("siteUrl") or ""
    site_link = f'<a href="{html_escape(site_url)}">Site</a>' if site_url else ""
    search_text = " ".join(
        [
            entry.get("name", ""),
            theme,
            entry.get("industry", ""),
            entry.get("fit", ""),
            note,
            fonts,
            " ".join(c.get("name", "") + " " + c.get("hex", "") for c in colors),
        ]
    ).lower()
    return f"""    <article class="style-card {card_class}" style="--strip:{html_escape(strip)}" data-theme="{html_escape(theme)}" data-industry="{html_escape(entry.get('industry') or '')}" data-status="{html_escape(entry.get('documentStatus') or '')}" data-search="{html_escape(search_text)}">
      <div>
        <div class="topline"><span>{html_escape(entry.get('documentStatus') or 'style')}</span><span>{html_escape(theme)}</span></div>
        <h2>{html_escape(entry.get('name') or 'Untitled')}</h2>
        <span class="fit">{html_escape(entry.get('fit') or 'Design reference')}</span>
        <p class="note">{html_escape(note)}</p>
        <div class="swatches" aria-label="color tokens">{swatches}</div>
        <div class="fonts">{html_escape(fonts or 'Typography metadata unavailable')}</div>
      </div>
      <div class="actions"><a class="primary" href="{md_href}">{md_label}</a><a href="{source}">Refero</a>{site_link}</div>
    </article>"""


def gradient(colors: list[dict[str, str]]) -> str:
    hexes = [color.get("hex", "") for color in colors if HEX_RE.match(color.get("hex", ""))]
    if not hexes:
        return "linear-gradient(90deg,#17130f,#75675a)"
    if len(hexes) == 1:
        return f"linear-gradient(90deg,{hexes[0]},{hexes[0]})"
    if len(hexes) == 2:
        return f"linear-gradient(90deg,{hexes[0]},{hexes[1]})"
    return "linear-gradient(135deg," + ",".join(hexes[:5]) + ")"


def update_index_link(index_path: Path, dry_run: bool) -> bool:
    if not index_path.exists():
        return False
    text = index_path.read_text(encoding="utf-8")
    if 'href="refero-design-library.html"' in text:
        return False
    marker = '<a href="#refero-design-md">Refero MD</a>'
    replacement = marker + '<a href="refero-design-library.html">Refero Library</a>'
    if marker not in text:
        return False
    write_text(index_path, text.replace(marker, replacement, 1), dry_run)
    return True


def generate(args: argparse.Namespace) -> CrawlStats:
    out_dir = args.out_dir
    out_dir.mkdir(parents=True, exist_ok=True)
    all_dir = out_dir / "all"
    all_dir.mkdir(parents=True, exist_ok=True)

    existing_paths = extract_existing_paths(out_dir)
    eprint(f"[existing] found {len(existing_paths)} existing style IDs under {out_dir}")

    discovered = discover_styles(args)
    eprint(f"[discover] total unique style IDs: {len(discovered)}")

    cache_dir = None if args.no_cache else out_dir / ".cache"
    taken_paths = set(out_dir.rglob("*.md"))
    generated_entries: dict[str, dict[str, Any]] = {}
    generated_paths: dict[str, Path] = {}
    detail_failures = 0
    skipped_existing = 0

    for index, (style_id, summary) in enumerate(discovered.items(), start=1):
        if style_id.lower() in existing_paths and not args.refresh_existing:
            skipped_existing += 1
            continue
        cache_path = cache_dir / f"{style_id}.json" if cache_dir else None
        try:
            detail = fetch_json(
                detail_url(args.base_url, style_id),
                retries=args.retries,
                timeout_sec=args.timeout_sec,
                sleep_sec=args.sleep_sec,
                cache_path=cache_path,
            )
        except ReferoError as exc:
            detail_failures += 1
            eprint(f"[detail] failed {style_id}: {exc}")
            continue
        entry = normalize_entry(style_id, summary, detail, args.base_url)
        md_path = unique_md_path(out_dir, entry, taken_paths)
        write_text(md_path, render_style_md(entry), args.dry_run)
        generated_entries[style_id] = entry
        generated_paths[style_id] = md_path
        if len(generated_entries) % 50 == 0:
            eprint(f"[generate] {len(generated_entries)} Markdown docs written ({index}/{len(discovered)} scanned)")

    refreshed_paths = extract_existing_paths(out_dir)
    refreshed_paths.update({style_id.lower(): path for style_id, path in generated_paths.items()})
    catalog_entries = build_catalog_entries(discovered, refreshed_paths, generated_entries, generated_paths, out_dir, args.base_url)
    generated_at = dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat()
    stats = CrawlStats(
        discovered=len(discovered),
        existing_ids=len(existing_paths),
        skipped_existing=skipped_existing,
        generated_docs=len(generated_entries),
        detail_failures=detail_failures,
        catalog_entries=len(catalog_entries),
    )
    write_text(out_dir / "_catalog_all.md", render_catalog_md(catalog_entries, stats, generated_at), args.dry_run)
    write_text(out_dir / "_catalog_all.json", render_catalog_json(catalog_entries, stats, generated_at, args.base_url), args.dry_run)
    write_text(args.library_html, render_library_html(catalog_entries, stats, generated_at), args.dry_run)
    update_index_link(args.library_html.parent / "index.html", args.dry_run)
    eprint(
        f"[done] discovered={stats.discovered} skipped_existing={stats.skipped_existing} "
        f"generated={stats.generated_docs} detail_failures={stats.detail_failures} catalog_entries={stats.catalog_entries}"
    )
    return stats


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    try:
        generate(args)
    except KeyboardInterrupt:
        eprint("Interrupted")
        return 130
    except ReferoError as exc:
        eprint(f"ERROR: {exc}")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
