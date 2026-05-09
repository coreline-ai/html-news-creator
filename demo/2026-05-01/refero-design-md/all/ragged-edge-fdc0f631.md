# Ragged Edge - Refero Design MD

- Source: https://styles.refero.design/style/fdc0f631-442c-466d-ab79-e1fff2bfdb7d
- Original site: https://raggededge.com
- Theme: `light`
- Industry: `agency`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Kinetic typographic canvases

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Ink | `#181f1f` | neutral | Primary text or dark surface |
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Fog Gray | `#d1d2d2` | neutral | Border, muted text, or supporting surface |
| Muted Slate | `#a3a5a5` | neutral | Border, muted text, or supporting surface |
| Graphite | `#000000` | neutral | Primary text or dark surface |
| Pristine Mist | `#eaf7f3` | neutral | Page background or card surface |
| Lagoon Violet | `#516fea` | accent | Action accent / signal color |
| Deep Mocha | `#1f3233` | neutral | Primary text or dark surface |
| Motion Blur Gradient | `#ffc240` | brand | Action accent / signal color |
| Alert Red | `#f56565` | accent | Action accent / signal color |

```css
:root {
  --ref-midnight-ink: #181f1f;
  --ref-canvas-white: #ffffff;
  --ref-fog-gray: #d1d2d2;
  --ref-muted-slate: #a3a5a5;
  --ref-graphite: #000000;
  --ref-pristine-mist: #eaf7f3;
  --ref-lagoon-violet: #516fea;
  --ref-deep-mocha: #1f3233;
}
```

## Typography direction
- **Grit-Regular**: 400, 500, 14px, 16px, 20px, 30px, 56px, 1.00, 1.20, 1.25, 1.43, 1.50, 2.60; substitute `Inter`.
- **ABCDiatypeExpanded-Bold**: 400, 10px, 12px, 16px, 20px, 40px, 78px, 82px, 1.10, 1.15, 1.20, 2.00; substitute `Bebas Neue`.

## Spacing / shape
- Section Gap: `180px`
- Card Padding: `16px`
- Element Gap: `16px`
- Radius: `cards: 40px, inputs: 54px, buttons: 64px, navigationItems: 64px`

## Surface cues
- **Pristine Mist Canvas** `#eaf7f3`: Primary page background for a fresh, clean base.
- **Canvas White Content** `#ffffff`: Default background for most content blocks and cards atop the canvas.
- **Deep Mocha Section** `#1f3233`: Distinct, darker background for contrasting content sections.
- **Midnight Ink Elevated** `#181f1f`: Darkest background for high-contrast elements, filled buttons, or specific feature areas.
- **Graphite Overlay** `#000000`: Used for hero background if not gradient, or as a very dark, impactful surface.

## Component cues
- **Ghost Navigation Item**: Subtle interactive navigation links
- **Filled Primary Button**: High-priority call to action button
- **Outlined Accent Button**: Secondary call to action button with brand accent
- **Soft Input Field**: User input text field
- **Nav Button**: Top navigation menu item

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
