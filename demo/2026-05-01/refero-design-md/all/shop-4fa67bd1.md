# Shop - Refero Design MD

- Source: https://styles.refero.design/style/4fa67bd1-f01d-454a-b522-4a0359ff9815
- Original site: https://shop.app
- Theme: `light`
- Industry: `ecommerce`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Digital boutique showcase

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas | `#ffffff` | neutral | Page background or card surface |
| Ink Black | `#000000` | neutral | Primary text or dark surface |
| Subtle Gray | `#ebebeb` | neutral | Page background or card surface |
| Muted Text | `#707070` | neutral | Border, muted text, or supporting surface |
| Soft Gray | `#c9cbcc` | neutral | Border, muted text, or supporting surface |
| Placeholder Text | `#7b7b7b` | neutral | Border, muted text, or supporting surface |
| Shop Violet | `#5433eb` | brand | Action accent / signal color |
| Violet Shadow | `#c0b5f3` | accent | Action accent / signal color |

```css
:root {
  --ref-canvas: #ffffff;
  --ref-ink-black: #000000;
  --ref-subtle-gray: #ebebeb;
  --ref-muted-text: #707070;
  --ref-soft-gray: #c9cbcc;
  --ref-placeholder-text: #7b7b7b;
  --ref-shop-violet: #5433eb;
  --ref-violet-shadow: #c0b5f3;
}
```

## Typography direction
- **GTStandard-MRegular**: 400, 9px, 11px, 12px, 14px, 16px, 1.29, 1.33, 1.38; substitute `Inter`.
- **GTStandard-MMedium**: 400, 11px, 12px, 1.33; substitute `Inter`.
- **Shopify Sans**: 400, 700, 10px, 14px, 1.20, 1.57, 1.71; substitute `Poppins`.

## Spacing / shape
- Section Gap: `40px`
- Card Padding: `16px`
- Element Gap: `8px`
- Radius: `cards: 11.4046px, large: 28px, other: 8px, inputs: 1e+07px, buttons: 22.8092px, display: 32px`

## Surface cues
- **Canvas Background** `#ffffff`: Primary page background layer, forms the foundational white space.

## Component cues
- **Ghost Button**: Secondary action or navigational link.
- **Rounded White Button**: General utility button, often found in modals or forms.
- **Pill Button**: Prominent action or filter button.
- **Flat Square Button**: Icon-only button or small inline action.
- **Product Card**: Displays individual product items.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
