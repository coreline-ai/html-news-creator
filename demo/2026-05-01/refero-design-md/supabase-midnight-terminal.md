# Supabase - Refero Design MD

- Source: https://styles.refero.design/style/632249f1-fd78-4c77-9b34-7bae37ff3e9b
- Original site: https://supabase.com
- Theme: `dark`
- Recommended fit: **Admin operations / developer tooling**

## North star
Midnight Terminal Interface - a dark, organized, and quietly powerful workspace.

## Why this fits html-news-creator
Useful for pipeline monitor, run logs, source health, and operator review surfaces.

## Apply to
- Run progress and status systems
- Source ledger / diagnostics panels
- Compact technical cards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Abyss | `#000000` | neutral | Deepest background elements, occasional graphic fill. |
| Ebony Canvas | `#121212` | neutral | Primary page background, base surface for components. |
| Graphite Base | `#242424` | neutral | Alternative surface background, button background for secondary actions, subtle borders. |
| Steel Surface | `#2e2e2` | neutral | Card backgrounds, elevated UI elements, default input backgrounds. The subtle deviation from pure black creates visual. |
| Carbon Border | `#393939` | neutral | Input borders, dividers, subtle separators. |
| Iron Outline | `#4d4d4d` | neutral | Subtle text, icon strokes, secondary graphic elements, subtle borders. |
| Mid-Gray Text | `#898989` | neutral | Muted body text, secondary information, disabled states. |
| Silver Highlight | `#b4b4b4` | neutral | Lightest neutral text for contrast on dark backgrounds, secondary navigation items. |

```css
:root {
  --ref-midnight-abyss: #000000;
  --ref-ebony-canvas: #121212;
  --ref-graphite-base: #242424;
  --ref-steel-surface: #2e2e2;
  --ref-carbon-border: #393939;
  --ref-iron-outline: #4d4d4d;
  --ref-mid-gray-text: #898989;
}
```

## Typography direction
- Primary: **Circular**; substitute `Inter`.
- Secondary/code: **Source Code Pro**; substitute `Menlo`.

## Spacing / shape
- Section gap: ``
- Card padding: `24px`
- Element gap: ``
- Radius: `{'cards': '16px', 'inputs': '6px', 'buttons': '6px', 'pillButtons': '9999px'}`

## Agent notes
- Treat this as reference material, not a direct template copy.
- Do not apply this wholesale to templates/report_newsstream.html.j2 unless the user explicitly asks for an HTML report migration.
- Preserve the project information hierarchy: title, why it matters, source evidence, confidence, image evidence.
