# Roberta's Pizza - Refero Design MD

- Source: https://styles.refero.design/style/3e497155-bd96-4134-a4a5-855bd885a25c
- Original site: https://www.robertaspizza.com
- Theme: `light`
- Industry: `other`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Vivid Red & Industrial Grit – a raw, energetic palette with no-nonsense type for an unpretentious, bold brand.

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Pizza Red | `#ed2023` | brand | Action accent / signal color |
| Ink Black | `#2b2f36` | neutral | Primary text or dark surface |
| Crisp White | `#ffffff` | neutral | Page background or card surface |
| Pitch Black | `#000000` | neutral | Primary text or dark surface |
| Hover Gray | `#bfbfbf` | neutral | Border, muted text, or supporting surface |

```css
:root {
  --ref-pizza-red: #ed2023;
  --ref-ink-black: #2b2f36;
  --ref-crisp-white: #ffffff;
  --ref-pitch-black: #000000;
  --ref-hover-gray: #bfbfbf;
}
```

## Typography direction
- **Borensa**: 400, 14px, 22px, 26px, 80px, 120px, 0.88, 1.25, 1.36, 1.38, 2.14; substitute `Brush Script MT`.
- **Offset TM**: 400, 20px, 22px, 24px, 34px, 54px, 80px, 1.00, 1.11, 1.25, 1.30, 1.36, 1.43, 1.50; substitute `Inter`.

## Spacing / shape
- Section Gap: `40px`
- Card Padding: `20px`
- Element Gap: `16px`
- Radius: `tags: 16000px, buttons: 7.2px, circular: 100%, callToAction: 7.2px`

## Surface cues
- **Crisp White Canvas** `#ffffff`: Dominant page background and primary content surface, supporting high-contrast text.
- **Ink Black Surface** `#2b2f36`: Used for dark sections and button backgrounds, providing a contrasting backdrop for white text.
- **Pizza Red Accent** `#ed2023`: High-impact sections and primary calls to action, drawing immediate attention.

## Component cues
- **Primary Action Button**: Critical call to action
- **Secondary Outline Button**: Alternative or less prominent actions
- **Dark Inverse Button**: Actions on light backgrounds that require strong visual weight
- **Input Field**: Data entry
- **Small Circular Button**: Icon-only actions or minimal interactive elements

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
