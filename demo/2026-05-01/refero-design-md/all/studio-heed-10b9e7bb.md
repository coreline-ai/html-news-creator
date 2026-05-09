# Studio HEED - Refero Design MD

- Source: https://styles.refero.design/style/10b9e7bb-9ffb-43eb-9360-5628d8390107
- Original site: https://www.studioheed.com
- Theme: `dark`
- Industry: `design`
- Recommended fit: **Dark webapp exploration**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Gallery Grid on Obsidian

## Apply to
- Dark theme experiments
- Operator-focused widgets
- High-contrast card systems

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Obsidian | `#000000` | neutral | Primary text or dark surface |
| Ghost White | `#ffffff` | neutral | Page background or card surface |
| Pale Stone | `#c2c1bf` | neutral | Border, muted text, or supporting surface |
| Deep Violet | `#00174f` | accent | Action accent / signal color |

```css
:root {
  --ref-obsidian: #000000;
  --ref-ghost-white: #ffffff;
  --ref-pale-stone: #c2c1bf;
  --ref-deep-violet: #00174f;
}
```

## Typography direction
- **Suisse Intl**: 600, 12px, 14px, 1.40; substitute `Inter`.

## Spacing / shape
- Section Gap: `48px`
- Card Padding: `0px`
- Element Gap: `14px`
- Radius: `cards: 5px, images: 5px`

## Surface cues
- **Obsidian Canvas** `#000000`: Dominant background for the entire application, providing a dark, immersive base.
- **Pale Stone Card** `#c2c1bf`: Alternative background for project cards, offering a lighter surface for variety.
- **Deep Violet Card** `#00174f`: Accent background for project cards, used sparingly to highlight specific content sections.

## Component cues
- **Image Project Card (Dark)**: Case study thumbnail in a grid
- **Image Project Card (Light)**: Case study thumbnail in a grid
- **Image Project Card (Violet Accent)**: Case study thumbnail in a grid, highlighting a project
- **Text Link (Header/Nav)**: Primary navigation and prominent header links
- **Badge (Text Tag)**: Categorization tag for project cards

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
