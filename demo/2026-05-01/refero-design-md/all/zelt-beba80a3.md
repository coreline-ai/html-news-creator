# Zelt - Refero Design MD

- Source: https://styles.refero.design/style/beba80a3-8f10-48fd-9e6c-a3436112f45b
- Original site: https://zelt.app
- Theme: `light`
- Industry: `saas`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Warm beige canvas with yellow accents

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Graphite | `#121718` | neutral | Primary text or dark surface |
| Canvas Cloud | `#ffffff` | neutral | Page background or card surface |
| Warm Mist | `#f6f3ef` | neutral | Page background or card surface |
| Soft Stone | `#e4e0dd` | neutral | Page background or card surface |
| Deep Charcoal | `#2f2f2f` | neutral | Primary text or dark surface |
| Utility Gray | `#444444` | neutral | Border, muted text, or supporting surface |
| Amber Glow | `#ffcd6d` | accent | Action accent / signal color |
| Soft Amber | `#ffe2aa` | accent | Action accent / signal color |

```css
:root {
  --ref-midnight-graphite: #121718;
  --ref-canvas-cloud: #ffffff;
  --ref-warm-mist: #f6f3ef;
  --ref-soft-stone: #e4e0dd;
  --ref-deep-charcoal: #2f2f2f;
  --ref-utility-gray: #444444;
  --ref-amber-glow: #ffcd6d;
  --ref-soft-amber: #ffe2aa;
}
```

## Typography direction
- **sans-serif**: 300, 400, 500, 700, 8px, 12px, 13px, 14px, 15px, 16px, 17px, 18px, 23px, 24px, 29px, 32px, 43px, 58px, 76px, 86px, 101px, 0.95, 1.00, 1.02, 1.15, 1.16, 1.20, 1.24, 1.35, 1.40, 1.60, 2.63; substitute `system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol'`.

## Spacing / shape
- Section Gap: `43px`
- Element Gap: `14px`
- Radius: `misc: 4px, tags: 8px, cards: 12px, buttons: 12px`

## Surface cues
- **Soft Stone** `#e4e0dd`: Primary page background, base canvas
- **Warm Mist** `#f6f3ef`: Secondary background, subtle distinction for content blocks
- **Canvas Cloud** `#ffffff`: Card backgrounds, main content area fills
- **Deep Charcoal** `#2f2f2f`: Accented card backgrounds, footer

## Component cues
- **Primary Action Button**: Filled button for main calls to action
- **Ghost Button**: Outlined button for secondary actions or links
- **Soft Card**: Container for content sections with subtle elevation
- **Alternate Card (Warm Mist)**: Subtle background card for specific content types
- **Alternate Card (Deep Charcoal)**: Darker card for emphasized sections

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
