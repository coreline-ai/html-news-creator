# mishmash® - Refero Design MD

- Source: https://styles.refero.design/style/ebac84e6-b22c-4d21-845f-9165158af844
- Original site: https://mishmash.pt
- Theme: `light`
- Industry: `ecommerce`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Stationery storefront on paper

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Ink | `#171717` | neutral | Primary text or dark surface |
| Cloud Canvas | `#ffffff` | neutral | Page background or card surface |
| Fog Gray | `#f2f2f2` | neutral | Page background or card surface |
| Whisper White | `#e3e3e3` | neutral | Page background or card surface |
| Ash Gray | `#858585` | neutral | Border, muted text, or supporting surface |
| Slate Gray | `#919191` | neutral | Border, muted text, or supporting surface |
| Silver Mist | `#a1a1a1` | neutral | Border, muted text, or supporting surface |
| Parchment Yellow | `#f4debb` | accent | Action accent / signal color |
| Sunset Gold | `#f9cb86` | accent | Action accent / signal color |

```css
:root {
  --ref-midnight-ink: #171717;
  --ref-cloud-canvas: #ffffff;
  --ref-fog-gray: #f2f2f2;
  --ref-whisper-white: #e3e3e3;
  --ref-ash-gray: #858585;
  --ref-slate-gray: #919191;
  --ref-silver-mist: #a1a1a1;
  --ref-parchment-yellow: #f4debb;
}
```

## Typography direction
- **Circular**: 400, 500, 600, 10px, 14px, 16px, 18px, 20px, 30px, 38px, 46px, 1.04, 1.12, 1.20; substitute `system-ui`.

## Spacing / shape
- Section Gap: `48px`
- Card Padding: `24px`
- Element Gap: `16px`
- Page Max Width: `1536px`
- Radius: `cards: 16px, forms: 4px, badges: 99999px, buttons: 12px`

## Surface cues
- **Cloud Canvas** `#ffffff`: Base page background and primary card surfaces.
- **Fog Gray** `#f2f2f2`: Secondary background areas, navigation bar, and subtle section differentiation.
- **Whisper White** `#e3e3e3`: Subtler background for selected cards or specific UI elements.
- **Parchment Yellow** `#f4debb`: Accent background for promotional cards or highlighted content.

## Component cues
- **Primary Filled Button**: Call to action.
- **Ghost Button**: Secondary action or navigation.
- **Outlined Button**: Tertiary action.
- **Product Card**: Displays product information in a grid.
- **Promotional Card**: Highlights special offers or collections.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
