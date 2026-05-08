# Ramp - Refero Design MD

- Source: https://styles.refero.design/style/b38702a0-75ab-474c-9106-00b624535825
- Original site: https://ramp.com
- Theme: `dark`
- Recommended fit: **Admin operations / developer tooling**

## North star
Deep Ocean Command Center - a stark, high-contrast control panel set against an endless dark expanse.

## Why this fits html-news-creator
Useful for pipeline monitor, run logs, source health, and operator review surfaces.

## Apply to
- Run progress and status systems
- Source ledger / diagnostics panels
- Compact technical cards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Deep Space Black | `#0c0a08` | neutral | Primary page background, base surface for components - establishes the dark theme depth. |
| Pure White | `#ffffff` | neutral | Primary text color, crucial for high contrast readability against dark backgrounds, interactive element text. |
| Ash Gray | `#1a1919` | neutral | Secondary surface background, used for lifted cards or subtle section breaks against the primary background. |
| Charcoal Black | `#000000` | neutral | Illustrative elements, icons, and occasionally deeper backgrounds for visual breaks. |
| Ivory White | `#f4f2f0` | neutral | Alternate background for specific white-themed cards or content sections, offering high contrast to deep blacks. |
| Slate Gray | `#999ba3` | neutral | Subtle text, inactive states, faint borders, and muted icons. |
| Iron Gray | `#4d505d` | neutral | Input field borders, secondary structural elements. |
| Midnight Ink | `#010412` | neutral | Subtle shadow color, creating depth on dark surfaces without being stark. |

```css
:root {
  --ref-deep-space-black: #0c0a08;
  --ref-pure-white: #ffffff;
  --ref-ash-gray: #1a1919;
  --ref-charcoal-black: #000000;
  --ref-ivory-white: #f4f2f0;
  --ref-slate-gray: #999ba3;
  --ref-iron-gray: #4d505d;
}
```

## Typography direction
- Primary: **lausanne**; substitute `system-ui, sans-serif`.
- Secondary/code: **Arial**; substitute `sans-serif`.

## Spacing / shape
- Section gap: `24px`
- Card padding: `24px`
- Element gap: `8px`
- Radius: `{'nav': '4px', 'cards': '12px', 'input': '10px', 'buttons': '4px', 'default': '12px'}`

## Agent notes
- Treat this as reference material, not a direct template copy.
- Do not apply this wholesale to templates/report_newsstream.html.j2 unless the user explicitly asks for an HTML report migration.
- Preserve the project information hierarchy: title, why it matters, source evidence, confidence, image evidence.
