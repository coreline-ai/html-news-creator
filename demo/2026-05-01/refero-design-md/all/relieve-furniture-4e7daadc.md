# Relieve Furniture - Refero Design MD

- Source: https://styles.refero.design/style/4e7daadc-3dc4-4211-bf25-626ea7b216e6
- Original site: https://relievefurniture.com
- Theme: `light`
- Industry: `other`
- Recommended fit: **Research brief / AI trend page**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Sustainable canvas, precise purpose

## Apply to
- Research section pages and model-release briefs
- Lab-note style cards
- AI product/research trend summaries

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas Fog | `#f6f7f7` | neutral | Page background or card surface |
| Snowdrift | `#ffffff` | neutral | Page background or card surface |
| Ash Cloud | `#e7e5e4` | neutral | Page background or card surface |
| Midnight Forest | `#0b392f` | brand | Action accent / signal color |
| Verdant Sprout | `#0cea9e` | accent | Action accent / signal color |
| Amethyst Glow | `#6f52d3` | accent | Action accent / signal color |
| Deep Plum | `#6043ba` | accent | Action accent / signal color |
| Graphite Text | `#374151` | neutral | Border, muted text, or supporting surface |
| Stone Grey | `#778a83` | neutral | Border, muted text, or supporting surface |
| Coal Black | `#000000` | neutral | Primary text or dark surface |

```css
:root {
  --ref-canvas-fog: #f6f7f7;
  --ref-snowdrift: #ffffff;
  --ref-ash-cloud: #e7e5e4;
  --ref-midnight-forest: #0b392f;
  --ref-verdant-sprout: #0cea9e;
  --ref-amethyst-glow: #6f52d3;
  --ref-deep-plum: #6043ba;
  --ref-graphite-text: #374151;
}
```

## Typography direction
- **Planar**: 200, 300, 400, 10px, 11px, 12px, 13px, 14px, 16px, 17px, 20px, 22px, 24px, 26px, 32px, 36px, 1.00, 1.15, 1.20, 1.40, 1.50, 1.60, 1.70, 2.00; substitute `system-ui, sans-serif`.

## Spacing / shape
- Section Gap: `40px`
- Card Padding: `20px`
- Element Gap: `10px`
- Radius: `cards: 8px, chips: 9999px, images: 8px, buttons: 8px`

## Surface cues
- **Snowdrift** `#ffffff`: Primary page and card backgrounds.
- **Canvas Fog** `#f6f7f7`: Secondary background for sections and subtle component fills.
- **Coal Black** `#000000`: High-contrast background for feature cards with overlaid white text.
- **Slate Blue** `#7f6de1`: Background for specific feature cards, offering a touch of color contrast.

## Component cues
- **Ghost Primary Button**: Default action button variant, outlines call-to-actions.
- **Subtle Recessed Button**: Secondary action button for internal navigation or less prominent actions.
- **Dark Filled Button**: Prominent action button for high-attention calls to action.
- **Flat Content Card**: Information display card, primarily for textual content or small images without elevation.
- **Elevated Tooltip Card**: Interactive pop-up or dialog card for focused information.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
