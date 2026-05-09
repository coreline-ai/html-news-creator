# Daniellelevitt - Refero Design MD

- Source: https://styles.refero.design/style/1a8d2d66-bb84-4929-acbe-2685fc9ab6e7
- Original site: https://www.daniellelevitt.com
- Theme: `mixed`
- Industry: `design`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Vivid editorial canvas

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Orange Peel | `#d15022` | brand | Action accent / signal color |
| Mint Canvas | `#75dfb5` | brand | Action accent / signal color |
| Midnight Ink | `#000000` | neutral | Primary text or dark surface |
| Purple Haze | `#e676b6` | accent | Action accent / signal color |

```css
:root {
  --ref-orange-peel: #d15022;
  --ref-mint-canvas: #75dfb5;
  --ref-midnight-ink: #000000;
  --ref-purple-haze: #e676b6;
}
```

## Typography direction
- **Helvetica Now Display**: 800, 10px, 18px, 29px, 0.95, 1.00, 1.60; substitute `system-ui`.
- **Helvetica Now Display Condensed**: 800, 72px, 0.95; substitute `system-ui`.

## Spacing / shape
- Section Gap: `50px`
- Card Padding: `0px`
- Element Gap: `20px`
- Radius: `none: 0px`

## Component cues
- **Text Link**: Standard interactive link for navigation and inline references.
- **Ghost Button**: Minimalist button with text acting as the primary visual. Used for navigation and calls to action.
- **Minimal Navigation Link**: Top-level navigation items.
- **Content Card (Image)**: Displays visual content within dynamic layouts.
- **Background Block (Mint)**: Large, distinct sections of content.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
