#!/usr/bin/env python3
"""Build docs/design/tokens.css from docs/design/tokens.json.

Single source of truth: tokens.json. Running this script regenerates
tokens.css so the two files cannot drift.

Usage:
    python3 scripts/build_tokens.py            # write tokens.css
    python3 scripts/build_tokens.py --check    # exit 1 if regen would change tokens.css

Idempotent — running twice produces byte-identical output.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
JSON_PATH = ROOT / "docs" / "design" / "tokens.json"
CSS_PATH = ROOT / "docs" / "design" / "tokens.css"

# --- key mappings ----------------------------------------------------------

# semantic color keys: snake_case → kebab-case CSS var
def kebab(name: str) -> str:
    return name.replace("_", "-")


# sidebar JSON key → CSS variable suffix
SIDEBAR_KEY_MAP = {
    "bg": "sidebar",
    "fg": "sidebar-foreground",
    "primary": "sidebar-primary",
    "primary_fg": "sidebar-primary-foreground",
    "accent": "sidebar-accent",
    "accent_fg": "sidebar-accent-foreground",
    "border": "sidebar-border",
    "ring": "sidebar-ring",
}


# --- emit helpers ----------------------------------------------------------

def emit_var(name: str, value: str) -> str:
    return f"  --{name}: {value};"


def emit_color_block(label: str, color_root: dict) -> list[str]:
    """Emit semantic + sidebar + chart + status for one mode (light/dark)."""
    lines: list[str] = []

    # Semantic surfaces / actions / etc.
    sem = color_root["semantic"][label]
    for key, item in sem.items():
        lines.append(emit_var(kebab(key), item["$value"]))

    lines.append("")
    lines.append(f"  /* sidebar ({label}) */")
    side = color_root["sidebar"][label]
    for key, item in side.items():
        lines.append(emit_var(SIDEBAR_KEY_MAP[key], item["$value"]))

    lines.append("")
    lines.append(f"  /* chart palette ({label}) */")
    chart = color_root["chart"][label]
    for key, item in chart.items():
        lines.append(emit_var(f"chart-{key}", item["$value"]))

    lines.append("")
    lines.append(f"  /* status ({label}) */")
    status = color_root["status"][label]
    for key, item in status.items():
        lines.append(emit_var(f"status-{key}", item["$value"]))

    return lines


def emit_root_extras(tokens: dict) -> list[str]:
    """Emit non-color tokens (radius, shadow, spacing, typography, motion, z, layout)."""
    out: list[str] = []

    out.append("")
    out.append("  /* radius */")
    out.append("  --radius: 0;")
    for key, item in tokens["radius"].items():
        if key.startswith("$"):
            continue
        out.append(emit_var(f"radius-{key}", item["$value"]))

    out.append("")
    out.append("  /* shadow */")
    for key, item in tokens["shadow"].items():
        if key.startswith("$"):
            continue
        out.append(emit_var(f"shadow-{key}", item["$value"]))

    out.append("")
    out.append("  /* spacing */")
    for key, item in tokens["spacing"].items():
        if key.startswith("$"):
            continue
        out.append(emit_var(f"space-{key}", item["$value"]))

    typo = tokens["typography"]
    out.append("")
    out.append("  /* typography — families */")
    for key, item in typo["family"].items():
        if key.startswith("$"):
            continue
        val = item["$value"]
        # Resolve {typography.family.display} reference for body
        if isinstance(val, str) and val.startswith("{") and val.endswith("}"):
            ref = val.strip("{}").split(".")
            cursor: object = tokens
            for seg in ref:
                cursor = cursor[seg]  # type: ignore[index]
            val = cursor["$value"]  # type: ignore[index]
        out.append(emit_var(f"font-{key}", val))

    out.append("")
    out.append("  /* typography — sizes */")
    for key, item in typo["size"].items():
        if key.startswith("$"):
            continue
        out.append(emit_var(f"text-{key}", item["$value"]))

    out.append("")
    out.append("  /* typography — weights */")
    for key, item in typo["weight"].items():
        out.append(emit_var(f"weight-{key}", str(item["$value"])))

    out.append("")
    out.append("  /* typography — leading */")
    for key, item in typo["leading"].items():
        out.append(emit_var(f"leading-{key}", str(item["$value"])))

    out.append("")
    out.append("  /* typography — tracking */")
    for key, item in typo["tracking"].items():
        out.append(emit_var(f"tracking-{key}", str(item["$value"])))

    motion = tokens["motion"]
    out.append("")
    out.append("  /* motion — duration */")
    for key, item in motion["duration"].items():
        if key.startswith("$"):
            continue
        out.append(emit_var(f"duration-{key}", item["$value"]))

    out.append("")
    out.append("  /* motion — ease */")
    for key, item in motion["ease"].items():
        if key.startswith("$"):
            continue
        v = item["$value"]
        bezier = f"cubic-bezier({v[0]}, {v[1]}, {v[2]}, {v[3]})"
        out.append(emit_var(f"ease-{key}", bezier))

    out.append("")
    out.append("  /* z-index */")
    for key, item in tokens["z_index"].items():
        out.append(emit_var(f"z-{kebab(key)}", str(item["$value"])))

    out.append("")
    out.append("  /* layout */")
    for key, item in tokens["layout"].items():
        if key.startswith("$"):
            continue
        out.append(emit_var(kebab(key), item["$value"]))

    return out


# --- @theme inline block (Tailwind v4 mapping) -----------------------------

THEME_INLINE = """\
@theme inline {
  --color-background: var(--background);
  --color-foreground: var(--foreground);
  --color-card: var(--card);
  --color-card-foreground: var(--card-foreground);
  --color-popover: var(--popover);
  --color-popover-foreground: var(--popover-foreground);
  --color-primary: var(--primary);
  --color-primary-foreground: var(--primary-foreground);
  --color-secondary: var(--secondary);
  --color-secondary-foreground: var(--secondary-foreground);
  --color-muted: var(--muted);
  --color-muted-foreground: var(--muted-foreground);
  --color-accent: var(--accent);
  --color-accent-foreground: var(--accent-foreground);
  --color-destructive: var(--destructive);
  --color-destructive-foreground: var(--destructive-foreground);
  --color-border: var(--border);
  --color-input: var(--input);
  --color-ring: var(--ring);
  --color-chart-1: var(--chart-1);
  --color-chart-2: var(--chart-2);
  --color-chart-3: var(--chart-3);
  --color-chart-4: var(--chart-4);
  --color-chart-5: var(--chart-5);
  --color-sidebar: var(--sidebar);
  --color-sidebar-foreground: var(--sidebar-foreground);
  --color-sidebar-primary: var(--sidebar-primary);
  --color-sidebar-primary-foreground: var(--sidebar-primary-foreground);
  --color-sidebar-accent: var(--sidebar-accent);
  --color-sidebar-accent-foreground: var(--sidebar-accent-foreground);
  --color-sidebar-border: var(--sidebar-border);
  --color-sidebar-ring: var(--sidebar-ring);

  --radius-sm: 0.375rem;
  --radius-md: 0.5rem;
  --radius-lg: 0px;
  --radius-xl: 0px;
}\
"""

# --- base resets (kept inline; mirrors what humans wrote previously) -------

BASE_RESETS = """\
*,
*::before,
*::after {
  box-sizing: border-box;
  border-color: var(--border);
}

html {
  height: 100%;
  -webkit-tap-highlight-color: color-mix(in oklab, var(--foreground) 20%, transparent);
}

body {
  margin: 0;
  background: var(--background);
  color: var(--foreground);
  font-family: var(--font-body);
  font-size: var(--text-base);
  line-height: var(--leading-relaxed);
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-rendering: optimizeLegibility;
}

h1, h2, h3 {
  text-wrap: balance;
}

p {
  text-wrap: pretty;
}

@media (pointer: coarse) {
  button,
  [role="button"],
  input,
  select,
  textarea,
  [data-slot="select-trigger"] {
    min-height: 44px;
  }
}

.dark *::-webkit-scrollbar {
  width: 8px;
  height: 8px;
}
.dark *::-webkit-scrollbar-track {
  background: oklch(0.205 0 0);
}
.dark *::-webkit-scrollbar-thumb {
  background: oklch(0.4 0 0);
  border-radius: 4px;
}
.dark *::-webkit-scrollbar-thumb:hover {
  background: oklch(0.5 0 0);
}\
"""


# --- main builder ----------------------------------------------------------

HEADER = """\
/* =========================================================================
 * html-news-creator — Design Tokens
 *
 * AUTO-GENERATED by scripts/build_tokens.py from docs/design/tokens.json.
 * DO NOT EDIT THIS FILE BY HAND. Edit tokens.json and run `make build-tokens`.
 *
 * Source: docs/design/02-tokens.md
 * Basis: shadcn/ui new-york style (OKLCH monochrome) + DESIGN.md
 * ========================================================================= */
"""


def build_css(tokens: dict) -> str:
    parts: list[str] = [HEADER, "", THEME_INLINE, ""]

    # :root (light)
    parts.append(":root {")
    parts.append("  color-scheme: light;")
    parts.append("")
    parts.append("  /* semantic surfaces / actions / feedback */")
    parts.extend(emit_color_block("light", tokens["color"]))
    parts.extend(emit_root_extras(tokens))
    parts.append("}")
    parts.append("")

    # .dark — only color overrides (non-color tokens inherit from :root)
    parts.append(".dark {")
    parts.append("  color-scheme: dark;")
    parts.append("")
    parts.append("  /* semantic surfaces / actions / feedback */")
    parts.extend(emit_color_block("dark", tokens["color"]))
    parts.append("}")
    parts.append("")

    # @media auto-dark mirror
    parts.append("@media (prefers-color-scheme: dark) {")
    parts.append("  :root:not(.light) {")
    parts.append("    color-scheme: dark;")
    sem = tokens["color"]["semantic"]["dark"]
    parts.append("")
    for key, item in sem.items():
        parts.append(f"    --{kebab(key)}: {item['$value']};")
    parts.append("  }")
    parts.append("}")
    parts.append("")

    parts.append(BASE_RESETS)
    parts.append("")  # trailing newline

    return "\n".join(parts)


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description="Build tokens.css from tokens.json")
    parser.add_argument(
        "--check",
        action="store_true",
        help="Exit 1 if regen would change tokens.css (no write).",
    )
    args = parser.parse_args(argv[1:])

    if not JSON_PATH.is_file():
        print(f"missing input: {JSON_PATH}", file=sys.stderr)
        return 2

    tokens = json.loads(JSON_PATH.read_text(encoding="utf-8"))
    new_css = build_css(tokens)

    if args.check:
        existing = CSS_PATH.read_text(encoding="utf-8") if CSS_PATH.is_file() else ""
        if existing == new_css:
            print(f"clean — {CSS_PATH.relative_to(ROOT)} matches {JSON_PATH.relative_to(ROOT)}")
            return 0
        print(
            f"drift — {CSS_PATH.relative_to(ROOT)} differs from build output. "
            "Run `make build-tokens`.",
            file=sys.stderr,
        )
        return 1

    CSS_PATH.write_text(new_css, encoding="utf-8")
    line_count = new_css.count("\n") + 1
    print(f"wrote {CSS_PATH.relative_to(ROOT)} ({line_count} lines)")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
