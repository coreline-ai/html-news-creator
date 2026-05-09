# Subset - Refero Design MD

- Source: https://styles.refero.design/style/a4dcee26-dd31-415a-ac99-64299959e7f1
- Original site: https://knickey.com
- Theme: `light`
- Industry: `ecommerce`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Organic Canvas, Understated Authority

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Oatmeal Canvas | `#f5f4ee` | neutral | Page background or card surface |
| Ink | `#241f20` | neutral | Primary text or dark surface |
| Pure White | `#ffffff` | neutral | Page background or card surface |
| Cool Stone | `#808080` | neutral | Border, muted text, or supporting surface |
| Rich Earth | `#000000` | neutral | Primary text or dark surface |
| Deep Forest | `#233735` | brand | Action accent / signal color |
| Mineral Blue | `#6487ba` | brand | Action accent / signal color |
| Spring Bud | `#8bbd78` | accent | Action accent / signal color |
| Sunset Orange | `#ff965b` | accent | Action accent / signal color |
| Misty Rose | `#edcdc2` | accent | Action accent / signal color |

```css
:root {
  --ref-oatmeal-canvas: #f5f4ee;
  --ref-ink: #241f20;
  --ref-pure-white: #ffffff;
  --ref-cool-stone: #808080;
  --ref-rich-earth: #000000;
  --ref-deep-forest: #233735;
  --ref-mineral-blue: #6487ba;
  --ref-spring-bud: #8bbd78;
}
```

## Typography direction
- **FoundersGrotesk**: 400, 500, 700, 13px, 14px, 15px, 16px, 17px, 18px, 20px, 24px, 0.90, 1.00, 1.10, 1.20, 1.40, 1.43, 1.46, 1.50, 1.53, 1.60, 1.63; substitute `Inter`.
- **TTRamillas_Light**: 400, 18px, 20px, 24px, 32px, 40px, 42px, 1.00, 1.20, 1.24, 1.29, 1.38, 1.40, 1.53; substitute `Playfair Display`.
- **GTStandard-M**: 400, 17px, 1.50; substitute `Roboto Mono`.

## Spacing / shape
- Section Gap: `64px`
- Card Padding: `16px`
- Element Gap: `8px`
- Radius: `cards: 0px, badges: 0px, inputs: 0px, buttons: 0px, circularElements: 50%`

## Surface cues
- **Oatmeal Canvas** `#f5f4ee`: Base page background and default card surface.
- **Pure White** `#ffffff`: Elevated card backgrounds, input fields, and certain contrasting UI elements.

## Component cues
- **Primary Action Button**: Filled button for main calls to action.
- **Secondary Action Button**: Filled button for alternative calls to action.
- **Ghost Button**: Outlined button for less prominent actions.
- **Informative Badge**: Small, distinct label for status or newness.
- **Product Card**: Container for product listings.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
