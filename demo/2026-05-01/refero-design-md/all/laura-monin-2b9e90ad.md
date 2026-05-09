# Laura Monin - Refero Design MD

- Source: https://styles.refero.design/style/2b9e90ad-51d9-4f29-8f7e-a343dc741eab
- Original site: https://lauramonin.com
- Theme: `light`
- Industry: `design`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Gallery Grid Serenity

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Text Black | `#000000` | neutral | Primary text or dark surface |

```css
:root {
  --ref-canvas-white: #ffffff;
  --ref-text-black: #000000;
}
```

## Typography direction
- **neue-haas-grotesk-display**: 400, 12px, 14px, 18px, 22px, 1.15, 1.20; substitute `Helvetica Neue`.
- **title**: 400, 58px, 158px, 1.20; substitute `Playfair Display`.

## Spacing / shape
- Card Padding: `9px`
- Element Gap: `7px`
- Radius: `cards: 0px, images: 0px`

## Component cues
- **Navigation Link**: Top-right global navigation items.
- **Hero Title**: Main page headline / artistic statement.
- **Image Caption**: Descriptive text accompanying visual content.
- **Info/Contact Link**: Small, functional links for contact or additional information.
- **Gallery Image Card**: Primary content display for portfolio images.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
