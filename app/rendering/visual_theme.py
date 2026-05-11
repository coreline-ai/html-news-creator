from __future__ import annotations

DEFAULT_VISUAL_THEME = "hyperstudio_terminal_ops"
VISUAL_THEME_ALLOWLIST: frozenset[str] = frozenset(
    {
        "linear_command_center",
        "anthropic_research_journal",
        "cursor_warm_studio",
        "hyperstudio_terminal_ops",
        "hyperstudio_solid_dark",
        "mercury_twilight_console",
    }
)


def normalize_visual_theme(value: str | None) -> str:
    """Return a supported Refero visual theme, falling back on invalid/empty input."""
    theme = str(value or "").strip()
    return theme if theme in VISUAL_THEME_ALLOWLIST else DEFAULT_VISUAL_THEME
