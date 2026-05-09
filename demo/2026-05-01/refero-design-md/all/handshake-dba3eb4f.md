# Handshake - Refero Design MD

- Source: https://styles.refero.design/style/dba3eb4f-c1c2-437f-beb2-708e9d074729
- Original site: https://joinhandshake.com
- Theme: `light`
- Industry: `ai`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Shifting gradient nebula

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Deep Space | `#000000` | neutral | Primary text or dark surface |
| Midnight Core | `#14151c` | neutral | Primary text or dark surface |
| Cosmic Gray | `#052326` | neutral | Primary text or dark surface |
| Stardust | `#ffffff` | neutral | Page background or card surface |
| Guidepost Green | `#d3fb52` | brand | Action accent / signal color |
| Muted Text | `#666666` | neutral | Border, muted text, or supporting surface |

```css
:root {
  --ref-deep-space: #000000;
  --ref-midnight-core: #14151c;
  --ref-cosmic-gray: #052326;
  --ref-stardust: #ffffff;
  --ref-guidepost-green: #d3fb52;
  --ref-muted-text: #666666;
}
```

## Typography direction
- **NoiGrotesk**: 400, 12px, 14px, 16px, 20px, 22px, 28px, 40px, 0.85, 1.10, 1.40, 1.50; substitute `Inter`.
- **NoiGrotesk**: 500, 12px, 14px, 16px, 20px, 22px, 28px, 40px, 0.85, 1.10, 1.40, 1.50; substitute `Inter`.
- **SansPlomb**: 600, 201px, 0.80; substitute `Anton`.

## Spacing / shape
- Section Gap: `24px`
- Card Padding: `16px`
- Element Gap: `16px`
- Radius: `tags: 9999px, cards: 24px, inputs: 24px, buttons: 8px, buttons-large: 12px, navigationItems: 8px`

## Component cues
- **Primary Ghost Button**: Call to action variant
- **Navigation Ghost Button**: Navigation and secondary actions
- **Primary Filled Button**: High-priority, primary action.
- **Filter Tag**: Interactive content categorization
- **Search Input**: Primary form input for search queries.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
