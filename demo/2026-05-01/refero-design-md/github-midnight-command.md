# GitHub - Refero Design MD

- Source: https://styles.refero.design/style/c3ceca5c-d329-4559-b947-016172941ba2
- Original site: https://github.com
- Theme: `dark`
- Recommended fit: **Admin operations / developer tooling**

## North star
Midnight command center, subtly glowing

## Why this fits html-news-creator
Useful for pipeline monitor, run logs, source health, and operator review surfaces.

## Apply to
- Run progress and status systems
- Source ledger / diagnostics panels
- Compact technical cards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Deep Space | `#0d1117` | neutral | Primary page background, base for most dark surfaces |
| Midnight Ink | `#000000` | neutral | Elevated surfaces, code blocks, modal backgrounds, and deeply shadowed areas |
| Code Canvas | `#151a22` | neutral | Secondary background for sections, code editor areas, and subtle surface differentiation |
| Subtle Gray | `#21262d` | neutral | Borders between sections, divider lines, and very soft visual separation |
| Ash Gray | `#283041` | neutral | Faint background for inactive states or subtle borders, hinting at elevation |
| Ghost White | `#ffffff` | neutral | Primary text, prominent icons, and active navigation elements. Also used as a white background for some translucent ele. |
| Faded Silver | `#f0f6fc` | neutral | Secondary text, subheadings, and muted UI elements that require slightly less prominence than primary text |
| UI Gray | `#9198a1` | neutral | Placeholder text, secondary icons, and less prominent text labels |

```css
:root {
  --ref-deep-space: #0d1117;
  --ref-midnight-ink: #000000;
  --ref-code-canvas: #151a22;
  --ref-subtle-gray: #21262d;
  --ref-ash-gray: #283041;
  --ref-ghost-white: #ffffff;
  --ref-faded-silver: #f0f6fc;
}
```

## Typography direction
- Primary: **Mona Sans**; substitute `Inter`.
- Secondary/code: **Mona Sans VF**; substitute `Inter`.

## Spacing / shape
- Section gap: `24px`
- Card padding: `8px`
- Element gap: `16px`
- Radius: `{'pill': '60px', 'cards': '24px', 'input': '8px', 'buttons': '6px', 'default': '6px'}`

## Agent notes
- Treat this as reference material, not a direct template copy.
- Do not apply this wholesale to templates/report_newsstream.html.j2 unless the user explicitly asks for an HTML report migration.
- Preserve the project information hierarchy: title, why it matters, source evidence, confidence, image evidence.
