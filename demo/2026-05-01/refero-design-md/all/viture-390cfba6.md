# VITURE - Refero Design MD

- Source: https://styles.refero.design/style/390cfba6-8c2f-4273-8c9e-750d470b6e2e
- Original site: https://www.viture.com
- Theme: `light`
- Industry: `ecommerce`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
High-contrast tech canvas

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight | `#0c0c0c` | neutral | Primary text or dark surface |
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Ash Gray | `#7e7e7f` | neutral | Border, muted text, or supporting surface |
| Ink Black | `#000000` | neutral | Primary text or dark surface |
| Silver Mist | `#949597` | neutral | Border, muted text, or supporting surface |
| Light Frost | `#f7f7f8` | neutral | Page background or card surface |
| Pale Clay | `#eff0f3` | neutral | Page background or card surface |
| Storm Gray | `#5b5c5d` | neutral | Border, muted text, or supporting surface |
| Muted Clay | `#abacae` | neutral | Border, muted text, or supporting surface |
| Blaze Orange | `#ff5f34` | brand | Action accent / signal color |

```css
:root {
  --ref-midnight: #0c0c0c;
  --ref-canvas-white: #ffffff;
  --ref-ash-gray: #7e7e7f;
  --ref-ink-black: #000000;
  --ref-silver-mist: #949597;
  --ref-light-frost: #f7f7f8;
  --ref-pale-clay: #eff0f3;
  --ref-storm-gray: #5b5c5d;
}
```

## Typography direction
- **FontSeasonSans**: 400, 500, 600, 700, 800, 12px, 14px, 16px, 20px, 23px, 28px, 32px, 60px, 72px, 105px, 340px, 1.00, 1.20, 1.25, 1.33, 1.35, 1.38, 1.40, 1.43, 1.50, 1.63; substitute `Inter`.

## Spacing / shape
- Section Gap: `48px`
- Card Padding: `44px`
- Element Gap: `4px`
- Radius: `cards: 28px, pills: 9999px, images: 28px, inputs: 16px, buttons: 9999px, largeFeatures: 120px`

## Surface cues
- **Canvas White** `#ffffff`: Primary page background
- **Light Frost** `#f7f7f8`: Elevated card backgrounds, input fields
- **Pale Clay** `#eff0f3`: Alternative card backgrounds, subtle UI elements
- **Silver Mist** `#949597`: Alternative background panels for sections within content
- **Ink Black** `#000000`: Deepest backgrounds, especially for footers or full-bleed dark sections

## Component cues
- **Primary Filled Button**: High-emphasis action
- **Ghost Border Button**: Secondary action on dark backgrounds
- **Text Button**: Minimalistic interactive element
- **Feature Card**: Content container with subtle elevation
- **Input Field**: Standard form input

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
