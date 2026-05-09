# VISIONNAIRE - Refero Design MD

- Source: https://styles.refero.design/style/0ecfea58-c1f3-4671-806d-5ae0eb779f38
- Original site: https://vision-naire.com
- Theme: `light`
- Industry: `ecommerce`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Raw monochrome canvas.

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Ink | `#000000` | neutral | Primary text or dark surface |
| Paper White | `#ffffff` | neutral | Page background or card surface |
| Ghost Gray | `#888888` | neutral | Border, muted text, or supporting surface |
| Sand Dune | `#f7f5e8` | neutral | Page background or card surface |
| Sky Blue | `#daedff` | accent | Action accent / signal color |
| Bubblegum Pink | `#ff92c4` | accent | Action accent / signal color |
| Goldenrod | `#ffe36c` | accent | Action accent / signal color |

```css
:root {
  --ref-midnight-ink: #000000;
  --ref-paper-white: #ffffff;
  --ref-ghost-gray: #888888;
  --ref-sand-dune: #f7f5e8;
  --ref-sky-blue: #daedff;
  --ref-bubblegum-pink: #ff92c4;
  --ref-goldenrod: #ffe36c;
}
```

## Typography direction
- **PP Neue Montreal**: 500, 700, 8px, 10px, 11px, 12px, 14px, 15px, 18px, 21px, 24px, 30px, 33px, 45px, 1.15, 1.20, 1.30, 1.50, 2.00, 2.78; substitute `Inter`.

## Spacing / shape
- Section Gap: `30px`
- Card Padding: `20px`
- Element Gap: `4px`
- Radius: `cards: 15px, links: 50px, images: 15px, buttons: 0px`

## Component cues
- **Ghost Primary Button**: Navigational and call-to-action elements.
- **Muted Ghost Button**: Secondary and less prominent actions.
- **Product Card**: Display individual product listings in grid layouts.
- **Newsletter Signup Overlay**: Capturing user emails with a distinct pop-up.
- **Text Input Minimal**: User input fields.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
