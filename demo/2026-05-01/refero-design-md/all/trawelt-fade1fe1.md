# Trawelt - Refero Design MD

- Source: https://styles.refero.design/style/fade1fe1-bbd3-4b1a-ae19-fe88f6744fe0
- Original site: https://www.trawelt.com
- Theme: `dark`
- Industry: `agency`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Midnight forest bloom: deep, dark canvases with bursts of vivid green.

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Ink Black | `#000000` | neutral | Primary text or dark surface |
| Paper White | `#ffffff` | neutral | Page background or card surface |
| Fresh Mint | `#d3ffc3` | brand | Action accent / signal color |
| Forest Green | `#2d9b4c` | brand | Action accent / signal color |
| Desert Sand | `#e7d5ba` | neutral | Border, muted text, or supporting surface |
| Pale Sage | `#e4e9dc` | neutral | Page background or card surface |
| Cloud White | `#efefe7` | neutral | Page background or card surface |

```css
:root {
  --ref-ink-black: #000000;
  --ref-paper-white: #ffffff;
  --ref-fresh-mint: #d3ffc3;
  --ref-forest-green: #2d9b4c;
  --ref-desert-sand: #e7d5ba;
  --ref-pale-sage: #e4e9dc;
  --ref-cloud-white: #efefe7;
}
```

## Typography direction
- **Labour Grotesk**: 400, 16px, 20px, 23px, 28px, 31px, 39px, 43px, 53px, 435px, 0.80, 1.00, 1.10, 1.20, 1.30, 1.50; substitute `Space Grotesk, Cabinet Grotesk`.
- **Reckless Neue**: 250, 20px, 39px, 43px, 53px, 1.10, 1.20, 1.30; substitute `Canela, Recoleta`.

## Spacing / shape
- Section Gap: `187px`
- Card Padding: `15px`
- Element Gap: `15px`
- Radius: `cards: 15.04px, buttons: 10.08px, navigation: 15.04px`

## Surface cues
- **Canvas** `#000000`: Primary page background, providing a deep, dark base.
- **Tinted Canvas** `#e4e9dc`: Alternating background sections, offering a subtle visual shift from the main canvas.
- **Navigation Surface** `#d3ffc3`: Background for active navigation elements and other light UI bands.
- **Card Surface** `#efefe7`: Background for content cards, elevated above the canvas with a soft, almost-white appearance.

## Component cues
- **Primary Call to Action Button**: Filled button
- **Ghost Icon Button**: Outlined icon button
- **Navigation Link**: Navigational item
- **Content Card**: Information display
- **Blog Post Item**: List item for blog articles

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
