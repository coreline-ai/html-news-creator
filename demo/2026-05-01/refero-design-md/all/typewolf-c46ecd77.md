# Typewolf - Refero Design MD

- Source: https://styles.refero.design/style/c46ecd77-9c92-4a85-9162-c6d4afd99d95
- Original site: https://typewolf.com
- Theme: `light`
- Industry: `design`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Letterpress on aged paper. This design feels like pages from an expertly printed, well-loved typography textbook.

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Cream Canvas | `#f8f5f5` | neutral | Page background or card surface |
| Cloud White | `#ffffff` | neutral | Page background or card surface |
| Dusty Mauve | `#cfc6c7` | neutral | Border, muted text, or supporting surface |
| Inkwell Gray | `#443235` | neutral | Primary text or dark surface |
| Charcoal Text | `#2e2c2c` | neutral | Primary text or dark surface |
| Rosewood CTA | `#916a70` | brand | Action accent / signal color |

```css
:root {
  --ref-cream-canvas: #f8f5f5;
  --ref-cloud-white: #ffffff;
  --ref-dusty-mauve: #cfc6c7;
  --ref-inkwell-gray: #443235;
  --ref-charcoal-text: #2e2c2c;
  --ref-rosewood-cta: #916a70;
}
```

## Typography direction
- **DomaineText**: 400, 14px, 16px, 18px, 24px, 28px, 1.20, 1.25, 1.30, 1.40, 1.45, 1.50; substitute `Source Serif Pro`.
- **Dia**: 900, 12px, 13px, 14px, 15px, 1.20, 1.30, 2.20; substitute `Inter`.
- **DomaineDisplayNarrow**: 700, 26px, 42px, 46px, 1.20; substitute `Playfair Display`.

## Spacing / shape
- Section Gap: `64px`
- Card Padding: `12px`
- Radius: `small: 4px, default: 0px`

## Component cues
- **Content Card Grid**: Reference component style.
- **Navigation Bar**: Reference component style.
- **Promo Card — Definitive Guide**: Reference component style.
- **Primary Call to Action Button**: Interactive element
- **Secondary Button**: Interactive element

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
