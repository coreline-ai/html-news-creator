# Podcorn - Refero Design MD

- Source: https://styles.refero.design/style/8d4b0738-c302-45c6-98c9-b3cd36e04613
- Original site: https://podcorn.com
- Theme: `light`
- Industry: `media`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Soft-edged digital canvas

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas Pink | `#fff4f2` | neutral | Action accent / signal color |
| True White | `#ffffff` | neutral | Page background or card surface |
| Inkwell Indigo | `#090335` | brand | Action accent / signal color |
| Deep Ocean | `#132645` | brand | Action accent / signal color |
| Coral Sunset | `#ffb0a1` | accent | Action accent / signal color |
| Firebrick Red | `#fc736c` | accent | Action accent / signal color |
| Ash Gray | `#434352` | neutral | Border, muted text, or supporting surface |
| Stone Grey | `#8993a2` | neutral | Border, muted text, or supporting surface |
| Outline Gray | `#d8d8d8` | neutral | Border, muted text, or supporting surface |
| Charcoal Black | `#000000` | neutral | Primary text or dark surface |

```css
:root {
  --ref-canvas-pink: #fff4f2;
  --ref-true-white: #ffffff;
  --ref-inkwell-indigo: #090335;
  --ref-deep-ocean: #132645;
  --ref-coral-sunset: #ffb0a1;
  --ref-firebrick-red: #fc736c;
  --ref-ash-gray: #434352;
  --ref-stone-grey: #8993a2;
}
```

## Typography direction
- **Gilroy**: 400, 500, 600, 700, 14px, 15px, 16px, 18px, 20px, 22px, 25px, 1.00, 1.13, 1.20, 1.57, 1.58, 1.67, 1.70, 1.88; substitute `Inter`.
- **Georgia**: 400, 700, 21px, 27px, 40px, 1.44; substitute `Lora`.

## Spacing / shape
- Section Gap: `75px`
- Card Padding: `55px`
- Element Gap: `20px`
- Page Max Width: `1105px`
- Radius: `cards: 0px, modal: 8px, buttons: 0px`

## Surface cues
- **Canvas Pink** `#fff4f2`: Primary page background, creating a soft, warm base.
- **True White** `#ffffff`: Component backgrounds like cards and modals, subtly lighter than the canvas.

## Component cues
- **Filled Primary Button**: Primary action button
- **Outlined Secondary Button**: Secondary action button, ghost style
- **Navigation Button**: Navigational link within the header
- **Navigation Link**: Standard navigation text link
- **Content Card**: Container for content sections

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
