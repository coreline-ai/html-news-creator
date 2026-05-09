# Holiday 100 - Refero Design MD

- Source: https://styles.refero.design/style/48fa5bef-d910-40e1-b9b0-c0fcad055c6f
- Original site: https://shopping.google.com/m/bestthings
- Theme: `dark`
- Industry: `ecommerce`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Midnight product showcase

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Ink | `#202124` | neutral | Primary text or dark surface |
| Ash Gray | `#e8e8e8` | neutral | Page background or card surface |
| Pale Gray | `#e8f0fe` | neutral | Page background or card surface |
| Steel Gray | `#9e9e9e` | neutral | Border, muted text, or supporting surface |
| Charcoal Surface | `#333438` | neutral | Primary text or dark surface |
| Sky Link | `#99c3ff` | accent | Action accent / signal color |
| Grape Glow | `#c58af9` | accent | Action accent / signal color |
| Crimson Alert | `#980b0b` | accent | Action accent / signal color |
| Cerulean Insight | `#113979` | accent | Action accent / signal color |
| Mint Whisper | `#a8dab5` | accent | Action accent / signal color |

```css
:root {
  --ref-midnight-ink: #202124;
  --ref-ash-gray: #e8e8e8;
  --ref-pale-gray: #e8f0fe;
  --ref-steel-gray: #9e9e9e;
  --ref-charcoal-surface: #333438;
  --ref-sky-link: #99c3ff;
  --ref-grape-glow: #c58af9;
  --ref-crimson-alert: #980b0b;
}
```

## Typography direction
- **Crimson Pro**: 200, 400, 48px, 80px, 220px, 0.91, 1.00; substitute `serif`.
- **Google Sans**: 200, 400, 500, 14px, 16px, 24px, 30px, 1.00, 1.14, 1.20, 1.25, 1.43, 1.50, 1.71; substitute `system-ui`.
- **Arial**: 400, 700, 14px, 1.20, 1.43; substitute `system-ui`.

## Spacing / shape
- Section Gap: `36px`
- Card Padding: `24px`
- Element Gap: `6px`
- Radius: `pill: 9999px, cards: 20px, links: 2px, buttons: 20px, default: 20px`

## Surface cues
- **Midnight Ink** `#202124`: Base page background and default product card surface
- **Charcoal Surface** `#333438`: Elevated card background for subtle layering

## Component cues
- **Pill Button**: Primary Call to Action
- **Ghost Link**: Secondary Action / Navigation
- **Product Card**: Information Display / Product Listing
- **Accent Product Card**: Highlight / Themed Product Listing

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
