# Monte - Refero Design MD

- Source: https://styles.refero.design/style/fb6ac216-c11a-47c3-88e8-0423541da69c
- Original site: https://montecafe.com.au
- Theme: `light`
- Industry: `other`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Warm Terracotta Cafe

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Terracotta | `#b84b30` | brand | Action accent / signal color |
| Espresso Shot | `#5f1d1a` | accent | Action accent / signal color |
| Cream Canvas | `#f8f4e9` | neutral | Page background or card surface |
| Silver Border | `#e5e7eb` | neutral | Page background or card surface |
| Carbon Text | `#000000` | neutral | Primary text or dark surface |
| Pure Frost | `#ffffff` | neutral | Page background or card surface |
| Stone Gray | `#666666` | neutral | Border, muted text, or supporting surface |
| Medium Gray | `#999999` | neutral | Border, muted text, or supporting surface |
| Dark Overlay | `#3e3d3a` | neutral | Primary text or dark surface |

```css
:root {
  --ref-terracotta: #b84b30;
  --ref-espresso-shot: #5f1d1a;
  --ref-cream-canvas: #f8f4e9;
  --ref-silver-border: #e5e7eb;
  --ref-carbon-text: #000000;
  --ref-pure-frost: #ffffff;
  --ref-stone-gray: #666666;
  --ref-medium-gray: #999999;
}
```

## Typography direction
- **Riposte**: 400, 600, 10px, 11px, 12px, 13px, 14px, 15px, 16px, 17px, 20px, 23px, 24px, 36px, 0.90, 1.00, 1.10, 1.20, 1.25, 1.35, 1.40; substitute `Georgia, serif`.
- **Apercu Mono**: 400, 12px, 15px, 16px, 1.33, 1.35; substitute `monospace`.

## Spacing / shape
- Section Gap: `48px`
- Card Padding: `24px`
- Element Gap: `5px`
- Radius: `cards: 14px, inputs: 9999px, buttons: 0px`

## Surface cues
- **Cream Canvas** `#f8f4e9`: Base page background
- **Terracotta Surface** `#b84b30`: Primary brand surface for hero sections, footer, and feature cards
- **Dark Overlay Surface** `#3e3d3a`: Specific badge backgrounds, providing contrast for white text

## Component cues
- **Ghost Header Button**: Navigation and secondary actions.
- **Outlined Call to Action Button**: Primary interactive element.
- **Terracotta Feature Card**: Highlights features or product categories.
- **Transparent Image Overlay Card**: Used for subtle visual effects over images.
- **Rounded Input Field**: User data entry.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
