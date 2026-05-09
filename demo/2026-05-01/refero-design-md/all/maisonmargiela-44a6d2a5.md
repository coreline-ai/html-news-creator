# Maisonmargiela - Refero Design MD

- Source: https://styles.refero.design/style/44a6d2a5-16ef-42cd-a69c-33a7af16638d
- Original site: https://maisonmargiela.com
- Theme: `light`
- Industry: `ecommerce`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
muted runway elegance

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Greige Canvas | `#f7f7f2` | neutral | Page background or card surface |
| Coal Text | `#121212` | neutral | Primary text or dark surface |
| White Linen | `#ffffff` | neutral | Page background or card surface |
| Ash Detail | `#898989` | neutral | Border, muted text, or supporting surface |
| Ghost Gray | `#eaeae6` | neutral | Page background or card surface |
| Deep Graphite | `#000000` | neutral | Primary text or dark surface |
| Subtle Accent | `#d6d6d1` | neutral | Border, muted text, or supporting surface |

```css
:root {
  --ref-greige-canvas: #f7f7f2;
  --ref-coal-text: #121212;
  --ref-white-linen: #ffffff;
  --ref-ash-detail: #898989;
  --ref-ghost-gray: #eaeae6;
  --ref-deep-graphite: #000000;
  --ref-subtle-accent: #d6d6d1;
}
```

## Typography direction
- **Margiela Sans**: 375, 400, 475, 500, 600, 700, 10px, 11px, 12px, 13px, 14px, 15px, 16px, 1.00, 1.20, 1.40, 1.50, 1.60; substitute `Inter`.
- **Margiela Serif**: 400, 14px, 18px, 20px, 1.30, 1.40; substitute `Playfair Display`.

## Spacing / shape
- Section Gap: `64px`
- Card Padding: `16px`
- Element Gap: `4px`
- Radius: `cards: 0px, inputs: 9999px, buttons: 0px`

## Component cues
- **Announcement Banner**: Reference component style.
- **Product Card — Tabi Claw**: Reference component style.
- **Campaign CTA Block — Primavera-Verano**: Reference component style.
- **Text Only Button**: Primary interactive element for navigation and inline actions.
- **Text Underline Button**: Secondary call-to-action or link within content.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
