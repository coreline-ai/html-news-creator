# Literal - Refero Design MD

- Source: https://styles.refero.design/style/7e698bf6-6b31-40ed-a89a-40f4c37ade38
- Original site: https://literal.club
- Theme: `light`
- Industry: `media`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Literary white canvas

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Forest Green | `#278458` | brand | Action accent / signal color |
| Inkwell | `#444340` | neutral | Border, muted text, or supporting surface |
| Book Page White | `#ffffff` | neutral | Page background or card surface |
| Shelf Gray | `#f8f8f8` | neutral | Page background or card surface |
| Parchment Gray | `#9a988b` | neutral | Border, muted text, or supporting surface |
| Divider Gray | `#eeeeee` | neutral | Page background or card surface |
| Pitch Black | `#000000` | neutral | Primary text or dark surface |

```css
:root {
  --ref-forest-green: #278458;
  --ref-inkwell: #444340;
  --ref-book-page-white: #ffffff;
  --ref-shelf-gray: #f8f8f8;
  --ref-parchment-gray: #9a988b;
  --ref-divider-gray: #eeeeee;
  --ref-pitch-black: #000000;
}
```

## Typography direction
- **Inter**: 400, 500, 700, 14px, 15px, 16px, 22px, 40px, 1.35, 1.40, 1.43, 1.45, 1.50; substitute `system-ui`.
- **Libre Baskerville**: 500, 28px, 1.35; substitute `Georgia`.

## Spacing / shape
- Section Gap: `133px`
- Card Padding: `20px`
- Element Gap: `20px`
- Radius: `cards: 8px, buttons: 5px, default: 4px`

## Surface cues
- **Book Page White** `#ffffff`: Primary page background, base for content.
- **Shelf Gray** `#f8f8f8`: Secondary background for distinct content sections or panels.

## Component cues
- **Primary Action Button**: Filled button indicating a main action.
- **Compact Action Button**: Smaller, filled button for secondary calls to action.
- **Outline Ghost Button**: Subtle button with a transparent background.
- **Feature Card**: Card with white background for displaying features or content blocks.
- **Subtle Highlight Card**: Card with a light gray background for differentiating content blocks.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
