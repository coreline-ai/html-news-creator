# Patrick Miller - Refero Design MD

- Source: https://styles.refero.design/style/bb63a015-b018-4bd9-be66-0973ac6be753
- Original site: https://patrickmiller.se
- Theme: `mixed`
- Industry: `design`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Editorial photography portfolio.

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Ink | `#000000` | neutral | Primary text or dark surface |
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Pewter Mist | `#a4b1b3` | neutral | Border, muted text, or supporting surface |
| Steel Green | `#4c564b` | neutral | Action accent / signal color |
| Ocean Blue | `#004b82` | brand | Action accent / signal color |
| Warm Peach | `#fd9b65` | accent | Action accent / signal color |
| Rosewood Red | `#6f2c30` | accent | Action accent / signal color |
| Alabaster Creme | `#f8f5d1` | accent | Action accent / signal color |
| Blush Sand | `#e9d1c7` | accent | Action accent / signal color |
| Sage Green | `#9ac8ae` | accent | Action accent / signal color |

```css
:root {
  --ref-midnight-ink: #000000;
  --ref-canvas-white: #ffffff;
  --ref-pewter-mist: #a4b1b3;
  --ref-steel-green: #4c564b;
  --ref-ocean-blue: #004b82;
  --ref-warm-peach: #fd9b65;
  --ref-rosewood-red: #6f2c30;
  --ref-alabaster-creme: #f8f5d1;
}
```

## Typography direction
- **MlrStandard**: 400, 500, 16px, 32px, 331px, 0.80, 0.90, 1.20, 1.30; substitute `Arial`.
- **-apple-system**: 200, 32px, 1.20; substitute `Inter`.

## Spacing / shape
- Section Gap: `48px`
- Card Padding: `72px`
- Element Gap: `16px`
- Radius: `all: 0px`

## Component cues
- **Ghost Text Link**: Navigation and informational links.
- **Navigation Arrow Button**: Pagination and content progression.
- **Primary Action Button**: Main call-to-action for print editions.
- **Title Block**: Large, artistic page titles.
- **Overlay Contact Link**: Fixed position utility link.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
