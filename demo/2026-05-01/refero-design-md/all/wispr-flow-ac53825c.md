# Wispr Flow - Refero Design MD

- Source: https://styles.refero.design/style/ac53825c-1e06-4ae0-8489-cace5c5e0339
- Original site: https://wisprflow.ai
- Theme: `light`
- Industry: `productivity`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Warm parchment sophistication

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Parchment | `#ffffeb` | neutral | Page background or card surface |
| Ink | `#1a1a1a` | neutral | Primary text or dark surface |
| Forest Canopy | `#034f46` | brand | Action accent / signal color |
| Pale Lavender | `#f0d7ff` | accent | Action accent / signal color |
| Stone | `#e4e4d0` | neutral | Page background or card surface |
| Charcoal Text | `#222222` | neutral | Primary text or dark surface |
| Muted Ash | `#8a8a80` | neutral | Border, muted text, or supporting surface |
| White | `#ffffff` | neutral | Page background or card surface |
| Sunburst | `#ffa946` | accent | Action accent / signal color |

```css
:root {
  --ref-parchment: #ffffeb;
  --ref-ink: #1a1a1a;
  --ref-forest-canopy: #034f46;
  --ref-pale-lavender: #f0d7ff;
  --ref-stone: #e4e4d0;
  --ref-charcoal-text: #222222;
  --ref-muted-ash: #8a8a80;
  --ref-white: #ffffff;
}
```

## Typography direction
- **Figtree**: 400, 500, 600, 700, 14px, 16px, 20px, 22px, 24px, 32px, 0.95, 1.00, 1.30; substitute `system-ui`.
- **EB Garamond**: 400, 32px, 48px, 64px, 120px, 0.85, 0.95, 1.10, 1.30; substitute `serif`.
- **Apple Color Emoji**: 400, 72px, 1.3.

## Spacing / shape
- Section Gap: `64px`
- Card Padding: `32px`
- Element Gap: `8px`
- Radius: `cards: 32px, badges: 992px, global: 1600px, images: 40px, inputs: 14px, buttons: 12px`

## Surface cues
- **Parchment Canvas** `#ffffeb`: Base page background and default light content surfaces.
- **Ink Content Block** `#1a1a1a`: Prominent dark content sections, hero backgrounds, and featured card surfaces.
- **Forest Canopy Feature Block** `#034f46`: Distinct, attention-grabbing sections and branded cards.

## Component cues
- **Primary Action Button**: Interactive element
- **Outline Ghost Button**: Interactive element
- **Branded Action Button**: Interactive element
- **Soft Card**: Content container
- **Dark Content Card**: Content container

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
