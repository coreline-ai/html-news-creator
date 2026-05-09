# Afterglo - Refero Design MD

- Source: https://styles.refero.design/style/b13069df-7475-4b51-a734-621e3da75f8b
- Original site: https://myafterglo.com
- Theme: `light`
- Industry: `ecommerce`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Warm Minimalism

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#f3f2ec` | neutral | Page background or card surface |
| Deep Charcoal | `#131313` | neutral | Primary text or dark surface |
| Pure Black | `#000000` | neutral | Primary text or dark surface |
| Platinum Gray | `#e3e4df` | neutral | Page background or card surface |
| Faded Stone | `#cbc9bd` | neutral | Border, muted text, or supporting surface |
| Snow White | `#ffffff` | neutral | Page background or card surface |
| Terra Cotta | `#f68e6d` | accent | Action accent / signal color |
| Sky Mist | `#7faad2` | semantic | Action accent / signal color |

```css
:root {
  --ref-canvas-white: #f3f2ec;
  --ref-deep-charcoal: #131313;
  --ref-pure-black: #000000;
  --ref-platinum-gray: #e3e4df;
  --ref-faded-stone: #cbc9bd;
  --ref-snow-white: #ffffff;
  --ref-terra-cotta: #f68e6d;
  --ref-sky-mist: #7faad2;
}
```

## Typography direction
- **Aeonik**: 400, 500, 13px, 15px, 22px, 33px, 50px, 132px, 0.80, 0.90, 1.00, 1.10, 1.20, 1.30; substitute `Inter`.
- **Cardinal Fruit**: 400, 500, 33px, 42px, 54px, 187px, 1.00, 1.10; substitute `Playfair Display`.

## Spacing / shape
- Section Gap: `25px`
- Card Padding: `29px`
- Element Gap: `4px`
- Radius: `default: 5px`

## Surface cues
- **Canvas White** `#f3f2ec`: Base page background and general content area.
- **Default Card** `#f3f2ec`: Standard raised content containers, visually identical to the canvas but conceptually a distinct layer.
- **Faded Stone** `#cbc9bd`: Subtle background shifts for alternate sections, providing gentle visual rhythm.

## Component cues
- **Primary Filled Button**: Call to action button
- **Ghost Button**: Secondary action or navigation
- **Default Card**: Content container
- **Badge (Out of Stock)**: Informational label
- **Badge (Team Fav)**: Highlight label

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
