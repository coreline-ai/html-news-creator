#!/usr/bin/env python3
"""Design-token lint for the operator webapp.

Scans `ui/src/` (excluding shadcn primitives) for raw color, radius, and
shadow values that should instead reference tokens declared in
`docs/design/tokens.css`. The forbidden-pattern set comes from
`docs/design/06-automation-spec.md` section 4.

Usage:
    python scripts/lint_design_tokens.py                # default scope
    python scripts/lint_design_tokens.py path [path...] # custom scope

Exit code is the number of violations; 0 means clean.
"""

from __future__ import annotations

import re
import sys
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

DEFAULT_TARGETS = [ROOT / "ui" / "src"]

EXCLUDE_DIRS = {
    "node_modules",
    "dist",
    ".vite",
    "playwright-report",
    "test-results",
}

EXCLUDE_PATH_PARTS = (
    ("components", "ui"),  # shadcn primitives keep their own canonical values
)

INCLUDE_SUFFIXES = (".ts", ".tsx", ".css")


@dataclass(frozen=True)
class Rule:
    name: str
    pattern: re.Pattern[str]
    message: str


RULES: tuple[Rule, ...] = (
    Rule(
        "raw-hex",
        re.compile(r"#[0-9a-fA-F]{3,8}\b"),
        "raw hex color — use a semantic token (var(--foreground) etc.)",
    ),
    Rule(
        "rgb",
        re.compile(r"\brgba?\([^)]+\)"),
        "raw rgb()/rgba() — use a semantic token",
    ),
    Rule(
        "hsl",
        re.compile(r"\bhsla?\([^)]+\)"),
        "raw hsl()/hsla() — use a semantic token",
    ),
    Rule(
        "oklch-direct",
        # oklch(...) that is NOT immediately preceded by `var(--…)` reference
        re.compile(r"\boklch\([^)]+\)"),
        "direct oklch() — wrap in var(--token) instead",
    ),
    Rule(
        "raw-radius",
        re.compile(r"border-radius:\s*(?!0|var\(|inherit|unset)\d"),
        "raw border-radius value — use var(--radius-sm/md/lg)",
    ),
    Rule(
        "raw-shadow",
        re.compile(r"box-shadow:\s*(?!none|var\(|inherit|unset)"),
        "raw box-shadow — use var(--shadow-xs/sm/md)",
    ),
)


def iter_files(targets: list[Path]) -> list[Path]:
    files: list[Path] = []
    for target in targets:
        if target.is_file() and target.suffix in INCLUDE_SUFFIXES:
            files.append(target)
            continue
        if not target.is_dir():
            continue
        for path in target.rglob("*"):
            if not path.is_file() or path.suffix not in INCLUDE_SUFFIXES:
                continue
            if any(part in EXCLUDE_DIRS for part in path.parts):
                continue
            if any(
                all(seg in path.parts for seg in tup)
                for tup in EXCLUDE_PATH_PARTS
            ):
                continue
            files.append(path)
    return sorted(files)


COMMENT_PREFIXES = ("//", "*")


def is_comment_line(stripped: str) -> bool:
    return stripped.startswith(COMMENT_PREFIXES)


def lint_file(path: Path) -> list[tuple[int, str, str, str]]:
    """Return (line_no, rule_name, snippet, message) tuples."""
    violations: list[tuple[int, str, str, str]] = []
    text = path.read_text(encoding="utf-8", errors="replace")
    in_block_comment = False
    for line_no, raw in enumerate(text.splitlines(), start=1):
        stripped = raw.strip()
        # Skip simple comment forms — devs often paste hex codes in design notes.
        if "/*" in stripped and "*/" not in stripped:
            in_block_comment = True
            continue
        if in_block_comment:
            if "*/" in stripped:
                in_block_comment = False
            continue
        if is_comment_line(stripped):
            continue
        for rule in RULES:
            for match in rule.pattern.finditer(raw):
                # oklch-direct allowlist: ignore matches that appear inside
                # `var(...)` or are commented out.
                if rule.name == "oklch-direct":
                    span_before = raw[: match.start()].rstrip()
                    if span_before.endswith("var(") or "var(" in span_before[-40:]:
                        # crude allowlist: any var() within the recent context
                        # means the oklch is part of a variable declaration. We
                        # still flag declarations *outside* tokens.css though.
                        if "tokens.css" not in str(path):
                            pass
                violations.append(
                    (line_no, rule.name, raw.strip()[:120], rule.message)
                )
    return violations


def main(argv: list[str]) -> int:
    targets: list[Path] = (
        [Path(p).resolve() for p in argv[1:]] if len(argv) > 1 else DEFAULT_TARGETS
    )
    files = iter_files(targets)
    if not files:
        print(f"no files matched in {[str(t) for t in targets]}")
        return 0

    total = 0
    rule_counts: dict[str, int] = {}
    for path in files:
        for line_no, rule_name, snippet, msg in lint_file(path):
            rel = path.relative_to(ROOT) if ROOT in path.parents else path
            print(f"{rel}:{line_no}: [{rule_name}] {msg}")
            print(f"    {snippet}")
            total += 1
            rule_counts[rule_name] = rule_counts.get(rule_name, 0) + 1

    if total == 0:
        print(f"clean — {len(files)} files scanned")
        return 0

    print()
    print(f"{total} violation(s) across {len(files)} files")
    for name, count in sorted(rule_counts.items()):
        print(f"  {name}: {count}")
    return min(total, 125)  # cap exit code so shells don't truncate


if __name__ == "__main__":
    sys.exit(main(sys.argv))
