# Authkit - Refero Design MD

- Source: https://styles.refero.design/style/e80231a2-e4d6-406a-a2c9-2e6109679690
- Original site: https://authkit.com
- Theme: `dark`
- Recommended fit: **Admin operations / developer tooling**

## North star
Midnight Command Center. Imagine a high-tech dashboard glowing softly in a dark room, with frosted glass elements reflecting subtle light.

## Why this fits html-news-creator
Useful for pipeline monitor, run logs, source health, and operator review surfaces.

## Apply to
- Run progress and status systems
- Source ledger / diagnostics panels
- Compact technical cards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Abyss | `#05060f` | neutral | Page backgrounds, elevated card backgrounds, deep shadows. |
| Ghost White | `#ffffff` | neutral | Primary text for headings and high-contrast elements, icon fills. |
| Storm Gray | `#2f343` | neutral | Subtle shadows, secondary background for interactive states. |
| Comet | `#d8ecf8` | brand | Primary body text, prominent links, and headings; provides high readability against dark backgrounds. |
| Arctic Mist | `#d1e4fa` | brand | Secondary body text, icon outlines, button text; a cool, muted off-white for softer emphasis. |
| Celestial Light | `#b6d9fc` | brand | Focus states for interactive elements, subtle highlights. |
| Azure Glow | `#c7d3ea` | neutral | Less prominent body text, disabled states, and subtle borders; a desaturated blue-gray that recedes gracefully. |
| Slate Dew | `#3f4959` | neutral | Outline for informational badges and subtle accents. |

```css
:root {
  --ref-midnight-abyss: #05060f;
  --ref-ghost-white: #ffffff;
  --ref-storm-gray: #2f343;
  --ref-comet: #d8ecf8;
  --ref-arctic-mist: #d1e4fa;
  --ref-celestial-light: #b6d9fc;
  --ref-azure-glow: #c7d3ea;
}
```

## Typography direction
- Primary: **Untitled Sans**; substitute `Inter`.
- Secondary/code: **aeonikPro**; substitute `Space Grotesk`.

## Spacing / shape
- Section gap: `48px`
- Card padding: `24px`
- Element gap: `8px`
- Radius: `{'pill': '999px', 'cards': '12-16px', 'badges': '6px', 'inputs': '2-4px', 'buttons': '999px'}`

## Agent notes
- Treat this as reference material, not a direct template copy.
- Do not apply this wholesale to templates/report_newsstream.html.j2 unless the user explicitly asks for an HTML report migration.
- Preserve the project information hierarchy: title, why it matters, source evidence, confidence, image evidence.
