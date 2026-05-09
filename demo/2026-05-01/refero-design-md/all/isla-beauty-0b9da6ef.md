# Isla Beauty - Refero Design MD

- Source: https://styles.refero.design/style/0b9da6ef-bec5-4073-90af-66c67e72f2a4
- Original site: https://isla-beauty.com
- Theme: `light`
- Industry: `ecommerce`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Clinical purity on a canvas.

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Isla Red | `#e4263d` | brand | Action accent / signal color |
| Pure Black | `#000000` | neutral | Primary text or dark surface |
| Ink Grey | `#1a1a1a` | neutral | Primary text or dark surface |
| Cream Canvas | `#f8f6f3` | neutral | Page background or card surface |
| White Surface | `#ffffff` | neutral | Page background or card surface |
| Deep Grey | `#2e2e2e` | neutral | Primary text or dark surface |
| Warm Grey Border | `#e4dfd9` | neutral | Page background or card surface |
| Muted Text Grey | `#6f6f6f` | neutral | Border, muted text, or supporting surface |
| Stone Grey | `#8a8580` | neutral | Border, muted text, or supporting surface |
| Minimal Border Grey | `#212121` | neutral | Primary text or dark surface |

```css
:root {
  --ref-isla-red: #e4263d;
  --ref-pure-black: #000000;
  --ref-ink-grey: #1a1a1a;
  --ref-cream-canvas: #f8f6f3;
  --ref-white-surface: #ffffff;
  --ref-deep-grey: #2e2e2e;
  --ref-warm-grey-border: #e4dfd9;
  --ref-muted-text-grey: #6f6f6f;
}
```

## Typography direction
- **Soehne Buch**: 400, 12px, 13px, 15px, 16px, 1.00, 1.20, 1.40; substitute `Inter`.
- **Nimbus Sans**: 400, 500, 700, 10px, 11px, 13px, 14px, 15px, 16px, 17px, 30px, 36px, 54px, 68px, 1.00, 1.05, 1.10, 1.20, 1.55; substitute `Roboto`.
- **Soehne Kraftig**: 400, 500, 11px, 12px, 14px, 60px, 0.98, 1.00, 1.20, 1.40; substitute `Inter`.

## Spacing / shape
- Section Gap: `50px`
- Card Padding: `15px`
- Element Gap: `10px`
- Radius: `cards: 3px, pills: 999px, badges: 3px, inputs: 3px, buttons: 3px`

## Surface cues
- **Cream Canvas** `#f8f6f3`: Base page background and soft foundational surfaces.
- **White Surface** `#ffffff`: Elevated cards, component backgrounds, and areas requiring higher contrast.
- **Soft Peach** `#f5e7df`: Informational accent surfaces, such as subtle badge backgrounds.

## Component cues
- **Primary Action Button**: Primary Call to Action
- **Ghost Button**: Secondary Action, Navigation
- **Subtle Link Button**: Tertiary Action, Inline Navigation
- **Product Card**: Display individual products or features.
- **Cream Information Card**: Informational panels or content blocks.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
