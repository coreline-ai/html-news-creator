# Escape Coffee Company - Refero Design MD

- Source: https://styles.refero.design/style/b5532c58-620a-4d69-8861-35b2b6443956
- Original site: https://escape.cafe
- Theme: `light`
- Industry: `ecommerce`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Raw Concrete Canvas — Bold typography and rich textures anchor a tactile, achromatic experience.

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#f5f4f2` | neutral | Page background or card surface |
| Graphite Ink | `#151515` | neutral | Primary text or dark surface |
| Asphalt Black | `#000000` | neutral | Primary text or dark surface |
| Pale Stone | `#ebe9e6` | neutral | Page background or card surface |
| Fog Gray | `#929292` | neutral | Border, muted text, or supporting surface |
| Pure White | `#ffffff` | neutral | Page background or card surface |
| Outline Gray | `#8a8a8a` | neutral | Border, muted text, or supporting surface |
| Subtle Border | `#e3e3e3` | neutral | Page background or card surface |

```css
:root {
  --ref-canvas-white: #f5f4f2;
  --ref-graphite-ink: #151515;
  --ref-asphalt-black: #000000;
  --ref-pale-stone: #ebe9e6;
  --ref-fog-gray: #929292;
  --ref-pure-white: #ffffff;
  --ref-outline-gray: #8a8a8a;
  --ref-subtle-border: #e3e3e3;
}
```

## Typography direction
- **TWK Lausanne**: 200, 300, 400, 600, 700, 11px, 13px, 14px, 16px, 18px, 19px, 22px, 24px, 28px, 50px, 1.00, 1.05, 1.06, 1.20, 1.35, 1.81; substitute `Inter`.
- **Molitor**: 300, 700, 26px, 45px, 75px, 250px, 0.85, 1.00; substitute `Oswald`.
- **Garaje**: 300, 600, 700, 18px, 22px, 1.00, 1.20; substitute `Bebas Neue`.

## Spacing / shape
- Section Gap: `40px`
- Card Padding: `16px`
- Element Gap: `10px`
- Radius: `cards: 16px, badges: 10px, inputs: 7px, buttons: 7px, default: 3px, circular: 50%`

## Surface cues
- **Canvas** `#f5f4f2`: Base page background, light UI containers, and subtle organizational bands.
- **Card Surface** `#ffffff`: Elevated content blocks like product cards or form containers, providing a clean boundary.
- **Panel** `#ebe9e6`: Slightly darker background for specific sections or elements that need subtle differentiation from the main canvas.
- **Accent Surface** `#151515`: Dark backgrounds for high-contrast sections, primary buttons, or immersive content blocks where lighter text is needed.

## Component cues
- **Filled Primary Button**: Interactive element
- **Ghost Button**: Interactive element
- **Text Link Button**: Interactive element
- **Circular Ghost Icon Button**: Interactive element
- **Product Card**: Display content

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
