# Home - Refero Design MD

- Source: https://styles.refero.design/style/604af0f7-b4c3-4921-93af-9da03df81493
- Original site: https://www.swoosh.nike
- Theme: `dark`
- Industry: `other`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Gaming console dark mode

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Ink | `#111111` | neutral | Primary text or dark surface |
| Ghost | `#ffffff` | neutral | Page background or card surface |
| Parchment | `#e5e5e5` | neutral | Page background or card surface |
| Slate | `#39393b` | neutral | Primary text or dark surface |
| Carbon | `#28282a` | neutral | Primary text or dark surface |
| Stone | `#707072` | neutral | Border, muted text, or supporting surface |
| Deep Space | `#1f1f21` | neutral | Primary text or dark surface |
| Electron Green | `#b7ff2c` | accent | Action accent / signal color |

```css
:root {
  --ref-midnight-ink: #111111;
  --ref-ghost: #ffffff;
  --ref-parchment: #e5e5e5;
  --ref-slate: #39393b;
  --ref-carbon: #28282a;
  --ref-stone: #707072;
  --ref-deep-space: #1f1f21;
  --ref-electron-green: #b7ff2c;
}
```

## Typography direction
- **Roobert**: 400, 500, 700, 14px, 16px, 20px, 24px, 64px, 110px, 0.85, 1.00, 1.20, 1.40, 1.50; substitute `system-ui`.
- **ui-sans-serif**: 400, 500, 700, 14px, 16px, 1.20, 1.50; substitute `system-ui`.

## Spacing / shape
- Section Gap: `24px`
- Card Padding: `20px`
- Element Gap: `16px`
- Radius: `cards: 6px, buttons: 6px, default: 6px, navElements: 6px`

## Component cues
- **Primary Action Button**: Call to action button
- **Ghost Navigation Button**: Navigation and secondary action buttons
- **Dark Filled Button**: Tertiary action button or navigation element
- **Light Content Card**: Information display card on dark background
- **Dark Content Card**: Information display card on dark background

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
