# Nuri - Refero Design MD

- Source: https://styles.refero.design/style/a0cb71ee-c2f2-4c37-a527-9e8ff0a0b312
- Original site: https://nuri.com
- Theme: `light`
- Industry: `fintech`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Bitcoin on lavender canvas

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Lavender Mist | `#beaaff` | brand | Action accent / signal color |
| Deep Plum | `#2c232e` | neutral | Primary text or dark surface |
| Slate Text | `#4b5563` | neutral | Border, muted text, or supporting surface |
| Phantom Gray | `#6b7280` | neutral | Border, muted text, or supporting surface |
| Powder Violet | `#e2d9ff` | brand | Action accent / signal color |
| Charcoal Icon | `#374151` | neutral | Border, muted text, or supporting surface |
| Amber Action | `#f97316` | accent | Action accent / signal color |
| Gallery White | `#ffffff` | neutral | Page background or card surface |
| Whisper White | `#f7f2ff` | neutral | Page background or card surface |
| Cloud Gray | `#f9fafb` | neutral | Page background or card surface |

```css
:root {
  --ref-lavender-mist: #beaaff;
  --ref-deep-plum: #2c232e;
  --ref-slate-text: #4b5563;
  --ref-phantom-gray: #6b7280;
  --ref-powder-violet: #e2d9ff;
  --ref-charcoal-icon: #374151;
  --ref-amber-action: #f97316;
  --ref-gallery-white: #ffffff;
}
```

## Typography direction
- **Sharp Grotesk Bold**: 900, 72px, 118px, 0.90, 1.00; substitute `Montserrat Black`.
- **Harriet Display**: 300, 400, 24px, 30px, 50px, 55px, 62px, 112px, 0.90, 0.94, 1.20, 1.33; substitute `Playfair Display`.
- **Inter**: 400, 500, 600, 12px, 14px, 15px, 16px, 17px, 20px, 24px, 28px, 32px, 0.90, 1.00, 1.20, 1.32, 1.33, 1.40, 1.43, 1.50, 1.63; substitute `Inter`.

## Spacing / shape
- Section Gap: `48px`
- Card Padding: `12px`
- Element Gap: `24px`
- Radius: `tags: 9999px, cards: 9999px, buttons: 8px, general: 9999px`

## Surface cues
- **Whisper White Canvas** `#f7f2ff`: Dominant page background, providing a soft, slightly off-white base for all content.
- **Gallery White Surface** `#ffffff`: Default background for most UI components and content blocks that need to stand out from the canvas.
- **Powder Violet Card** `#e2d9ff`: Distinctive background for card elements, using a branded color at a subtle tint.

## Component cues
- **Primary Action Button**: Call to action
- **Ghost Button**: Secondary action
- **Flag Selector Button**: Language or region selection
- **Large Hero Heading**: Brand statement
- **Subtle Card**: Content container

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
