# OhDada - Refero Design MD

- Source: https://styles.refero.design/style/d69af89b-cb31-426d-b9aa-c21d127b8947
- Original site: https://ohdada.de
- Theme: `light`
- Industry: `design`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Antique Papyrus Canvas

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Kinetic Brown | `#5d3a19` | brand | Action accent / signal color |
| Canvas Parchment | `#e6e0d9` | neutral | Page background or card surface |
| Stone Mist | `#b7b3be` | neutral | Border, muted text, or supporting surface |
| Ink Depth | `#000000` | neutral | Primary text or dark surface |

```css
:root {
  --ref-kinetic-brown: #5d3a19;
  --ref-canvas-parchment: #e6e0d9;
  --ref-stone-mist: #b7b3be;
  --ref-ink-depth: #000000;
}
```

## Typography direction
- **GrandSlang-Roman**: 100, 58px, 1.00; substitute `Playfair Display`.
- **neue-haas-grotesk-display**: 400, 500, 16px, 17px, 72px, 1.00, 1.18, 1.20; substitute `Inter`.
- **neue-haas-grotesk-display**: 400, 500, 16px, 17px, 72px, 1.00, 1.18, 1.20; substitute `Inter Medium`.

## Spacing / shape
- Section Gap: `115px`
- Element Gap: `10px`
- Radius: `default: 0px`

## Surface cues
- **Canvas Parchment** `#e6e0d9`: Dominant page background, providing a soft, warm base for all content.
- **Stone Mist** `#b7b3be`: Secondary background for alternating sections, providing subtle visual contrast and separation.

## Component cues
- **Hero Headline**: Large, decorative primary headline
- **Secondary Headline**: Product section or general content headline
- **Product Link Card**: Interactive list item for products
- **Body Text Block**: General descriptive text
- **Subtle Section Separator**: Visual division between content blocks

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
