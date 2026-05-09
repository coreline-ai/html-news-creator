# Favorit Studio - Refero Design MD

- Source: https://styles.refero.design/style/7e03ab3b-1344-43d7-a7c4-2f31395758ae
- Original site: https://favorit.studio
- Theme: `light`
- Industry: `design`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
High-contrast editorial canvas – bold, no-nonsense.

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Midnight Ink | `#000000` | neutral | Primary text or dark surface |
| Swiper Accent | `#007aff` | accent | Action accent / signal color |

```css
:root {
  --ref-canvas-white: #ffffff;
  --ref-midnight-ink: #000000;
  --ref-swiper-accent: #007aff;
}
```

## Typography direction
- **TWKLausanne**: 400, 14px, 23px, 135px, 159px, 189px, 1.00, 1.20; substitute `system-ui, sans-serif`.
- **Favorit Times**: 400, 44px, 55px, 179px, 1.00, 1.20; substitute `serif`.

## Spacing / shape
- Section Gap: `46px`
- Card Padding: `16px`
- Element Gap: `21px`
- Radius: `all: 0px`

## Component cues
- **Ghost Button (Light BG)**: Primary Call to Action, Navigation Item
- **Ghost Button (Dark BG)**: Primary Call to Action, Navigation Item
- **Main Navigation Item**: Top-level navigation links
- **Headline Display**: Hero Section Headlines, Major Section Titles
- **Body Text Block**: Paragraphs, Detailed descriptions

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
