# Coda - Refero Design MD

- Source: https://styles.refero.design/style/0f0d4cb7-5109-4e81-8c8d-f6bd0441b27c
- Original site: https://coda.io
- Theme: `light`
- Industry: `productivity`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Crisp canvas, structured workspace.

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Ink | `#212121` | neutral | Primary text or dark surface |
| White Canvas | `#ffffff` | neutral | Page background or card surface |
| Amber Glow | `#fff6ec` | neutral | Page background or card surface |
| Soft Gray | `#e0e0e0` | neutral | Page background or card surface |
| Slate Text | `#666666` | neutral | Border, muted text, or supporting surface |
| Ash Text | `#8e8e8e` | neutral | Border, muted text, or supporting surface |
| Obsidian | `#000000` | neutral | Primary text or dark surface |
| Warm Gray Text | `#444444` | neutral | Border, muted text, or supporting surface |
| Sunset Orange | `#ee5a29` | accent | Action accent / signal color |

```css
:root {
  --ref-midnight-ink: #212121;
  --ref-white-canvas: #ffffff;
  --ref-amber-glow: #fff6ec;
  --ref-soft-gray: #e0e0e0;
  --ref-slate-text: #666666;
  --ref-ash-text: #8e8e8e;
  --ref-obsidian: #000000;
  --ref-warm-gray-text: #444444;
}
```

## Typography direction
- **Calibre-R**: 700, 38px, 52px, 72px, 1.00, 1.10; substitute `Montserrat`.
- **Inter**: 400, 600, 700, 10px, 14px, 16px, 20px, 22px, 1.20, 1.38, 1.43, 1.50, 1.55; substitute `Inter`.
- **Tiempos-Headline**: 300, 38px, 1.37; substitute `Playfair Display`.

## Spacing / shape
- Section Gap: `113px`
- Card Padding: `16px`
- Element Gap: `8px`
- Radius: `cards: 8px, icons: 44px, buttons: 8px, smallElements: 4px`

## Surface cues
- **White Canvas** `#ffffff`: Primary page background and default surface for content.
- **Amber Glow Section** `#fff6ec`: Accent background for hero sections or footers, providing visual warmth and distinction.
- **Elevated Card** `#ffffff`: Interactive elements or content groupings that subtly stand out from the canvas with a light shadow.

## Component cues
- **Primary Filled Button**: Primary call to action.
- **Ghost Button**: Secondary action or navigation.
- **Tertiary White Button**: Less prominent actions on contrasting backgrounds.
- **Compact Ghost Button**: Smaller, less emphatic actions, often within product UI.
- **Feature Card**: Content container for showcasing features or information.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
