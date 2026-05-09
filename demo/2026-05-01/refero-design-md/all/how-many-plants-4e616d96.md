# How Many Plants - Refero Design MD

- Source: https://styles.refero.design/style/4e616d96-14ea-43d6-9662-0ad3fa19ef7c
- Original site: https://howmanyplants.com
- Theme: `light`
- Industry: `design`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Artisanal plant journal

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas Cream | `#f9f5f1` | neutral | Page background or card surface |
| Inkwell Black | `#222222` | neutral | Primary text or dark surface |
| Sprout Green | `#bfb33b` | brand | Action accent / signal color |

```css
:root {
  --ref-canvas-cream: #f9f5f1;
  --ref-inkwell-black: #222222;
  --ref-sprout-green: #bfb33b;
}
```

## Typography direction
- **Chromatica**: 400, 500, 14px, 16px, 20px, 24px, 36px, 0.89, 1.33, 1.43, 1.60, 2.00; substitute `Playfair Display`.
- **Hellenictypewriter**: 400, 500, 16px, 20px, 28px, 36px, 1.14, 1.25, 1.33, 1.60; substitute `Roboto Mono`.

## Spacing / shape
- Section Gap: `32px`
- Card Padding: `48px`
- Element Gap: `16px`
- Page Max Width: `1376px`
- Radius: `cards: 0px, inputs: 0px, buttons: 0px, default: 0px`

## Surface cues
- **Canvas Cream** `#f9f5f1`: Base page background and primary card surfaces
- **Sprout Green Accent** `#bfb33b`: Decorative background elements like illustrative shelves, adding a layer of visual interest and brand accent

## Component cues
- **Primary Ghost Button**: Main call-to-action button for a planted, vintage feel
- **Navigation Link**: Site navigation and sub-navigation
- **Search Input**: Site-wide search functionality
- **Text Outline Button**: Secondary action or category filter
- **Illustrative Shelf**: Decorative background element with layered content

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
