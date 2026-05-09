# IKEA - Refero Design MD

- Source: https://styles.refero.design/style/e7b37c82-239c-48d5-b293-79a2bfa235cc
- Original site: https://www.ikea.com
- Theme: `light`
- Industry: `ecommerce`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Scandinavian sunshine on white birch

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Ikea Yellow | `#ffdb00` | brand | Action accent / signal color |
| Core Black | `#111111` | neutral | Primary text or dark surface |
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Deep Sea Blue | `#0159a3` | accent | Action accent / signal color |
| Off-White | `#fffefb` | neutral | Page background or card surface |
| Text Black | `#000000` | neutral | Primary text or dark surface |
| Mid Grey | `#818181` | neutral | Border, muted text, or supporting surface |
| Light Grey | `#dadada` | neutral | Page background or card surface |
| Soft Peach | `#ffa6da` | accent | Action accent / signal color |

```css
:root {
  --ref-ikea-yellow: #ffdb00;
  --ref-core-black: #111111;
  --ref-canvas-white: #ffffff;
  --ref-deep-sea-blue: #0159a3;
  --ref-off-white: #fffefb;
  --ref-text-black: #000000;
  --ref-mid-grey: #818181;
  --ref-light-grey: #dadada;
}
```

## Typography direction
- **Noto IKEA**: 400, 700, 13px, 14px, 16px, 20px, 36px, 51px, 1.00, 1.08, 1.20, 1.40, 1.57, 1.62; substitute `Inter`.

## Spacing / shape
- Section Gap: `80px`
- Card Padding: `16px`
- Element Gap: `24px`
- Page Max Width: `1440px`
- Radius: `all: 8px`

## Component cues
- **Primary Action Button**: Main call-to-action button, drawing immediate attention.
- **Dark Icon Button**: Small, functional buttons for video controls or navigation, offering a clear visual cue.
- **Light Icon Button**: Small, functional buttons for controls like video pause, against lighter backgrounds.
- **Ghost Header Button**: Secondary call-to-action or functional button within headers, unobtrusive.
- **Content Card - Yellow**: Highlighting key information or promotional content.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
