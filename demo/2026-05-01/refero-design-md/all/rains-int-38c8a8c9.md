# Rains INT - Refero Design MD

- Source: https://styles.refero.design/style/38c8a8c9-4d2e-462a-bff0-80c9d9619ef2
- Original site: https://www.rains.com
- Theme: `light`
- Industry: `ecommerce`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Monochromatic Canvas, Bold Interruption

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas Fog | `#efefef` | neutral | Page background or card surface |
| Midnight Ink | `#10100f` | neutral | Primary text or dark surface |
| Pure Arctic | `#ffffff` | neutral | Page background or card surface |
| Deep Graphite | `#26292a` | neutral | Primary text or dark surface |
| Bright Solar | `#fffb85` | brand | Action accent / signal color |
| Subtle Gray | `#b3b3b2` | neutral | Border, muted text, or supporting surface |
| Dark Button | `#40403f` | neutral | Border, muted text, or supporting surface |

```css
:root {
  --ref-canvas-fog: #efefef;
  --ref-midnight-ink: #10100f;
  --ref-pure-arctic: #ffffff;
  --ref-deep-graphite: #26292a;
  --ref-bright-solar: #fffb85;
  --ref-subtle-gray: #b3b3b2;
  --ref-dark-button: #40403f;
}
```

## Typography direction
- **EuropaGroNr2SB**: 400, 12px, 14px, 1.20; substitute `Open Sans`.
- **EuropaGroNr2SH**: 400, 600, 700, 14px, 16px, 20px, 32px, 40px, 48px, 232px, 245px, 0.90, 1.00, 1.02, 1.20; substitute `Open Sans`.

## Spacing / shape
- Section Gap: `40px`
- Card Padding: `16px`
- Element Gap: `16px`
- Radius: `other: 9999px, buttons: 9999px`

## Component cues
- **Filled Primary Button**: Primary calls to action, prominent interactive elements.
- **Ghost Secondary Button**: Secondary actions that need to de-emphasize visual weight.
- **Bare Navigation Link**: Top-level navigation items and in-text links.
- **Transparent Dark Button**: Alternative dark button with transparent background for subtle interaction.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
