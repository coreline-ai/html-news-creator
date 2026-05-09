# MAKR - Refero Design MD

- Source: https://styles.refero.design/style/f2bf6db7-37b6-4394-be97-6bbb2c45c268
- Original site: https://makr.com
- Theme: `light`
- Industry: `ecommerce`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Workshop-crafted monochrome utility.

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Ink | `#1c1717` | neutral | Primary text or dark surface |
| Canvas | `#ffffff` | neutral | Page background or card surface |
| Fog | `#f0f0f0` | neutral | Page background or card surface |
| Stone | `#a9aea9` | neutral | Border, muted text, or supporting surface |

```css
:root {
  --ref-ink: #1c1717;
  --ref-canvas: #ffffff;
  --ref-fog: #f0f0f0;
  --ref-stone: #a9aea9;
}
```

## Typography direction
- **Sohne Web**: 400, 11px, 12px, 13px, 14px, 16px, 18px, 20px, 32px, 1.15, 1.35, 1.40, 1.45, 1.80; substitute `Inter`.
- **CircularXXMonoWeb**: 400, 13px, 20px, 1.15; substitute `Space Mono`.

## Spacing / shape
- Section Gap: `90px`
- Card Padding: `12px`
- Element Gap: `5px`
- Radius: `all: 0px`

## Component cues
- **Primary Filled Button**: Call to action.
- **Text Input**: Form text entry.
- **Product Tag Badge**: Informational labels for products or promotions.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
