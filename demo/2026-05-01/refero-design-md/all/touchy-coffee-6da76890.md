# Touchy Coffee - Refero Design MD

- Source: https://styles.refero.design/style/6da76890-6e04-452a-834d-ff019e232c2b
- Original site: https://touchycoffee.com
- Theme: `light`
- Industry: `ecommerce`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
whimsical indie zine

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Burnt Sienna | `#9f4920` | brand | Action accent / signal color |
| Forest Green | `#5b9133` | brand | Action accent / signal color |
| Periwinkle Mist | `#a697c6` | accent | Action accent / signal color |
| Graphite | `#000000` | neutral | Primary text or dark surface |
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Muted Sage | `#788c8c` | neutral | Border, muted text, or supporting surface |

```css
:root {
  --ref-burnt-sienna: #9f4920;
  --ref-forest-green: #5b9133;
  --ref-periwinkle-mist: #a697c6;
  --ref-graphite: #000000;
  --ref-canvas-white: #ffffff;
  --ref-muted-sage: #788c8c;
}
```

## Typography direction
- **Apercu Mono**: 400, 20px, 24px, 50px, 1.20, 1.50; substitute `Space Mono`.
- **Apercu Mono Bold**: 700, 20px, 1.20; substitute `Space Mono Bold`.

## Spacing / shape
- Section Gap: `80px`
- Card Padding: `10px`
- Element Gap: `20px`
- Radius: `cards: 20px, other: 100px, buttons: 100px`

## Component cues
- **Ghost Header Button**: Navigation and utility actions
- **Filled Primary Button**: Key interactions and calls to action
- **Filled Forest Green Button**: Secondary calls to action or context-specific actions
- **Product Card**: Displaying individual product items
- **Promotional Modal**: Temporary messages or offers

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
