# Evernote - Refero Design MD

- Source: https://styles.refero.design/style/0c0b6140-2b6c-44f8-8bba-4ecfcadba420
- Original site: https://evernote.com
- Theme: `light`
- Industry: `productivity`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Calm workspace, grounded neutrals

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas | `#f9f6f2` | neutral | Page background or card surface |
| Surface Off-White | `#f4eee5` | neutral | Page background or card surface |
| Pure White | `#ffffff` | neutral | Page background or card surface |
| Vivid Evernote Green | `#94e130` | brand | Action accent / signal color |
| Midnight Graphite | `#141414` | neutral | Primary text or dark surface |
| Deep Black | `#000000` | neutral | Primary text or dark surface |
| Carbon Gray | `#262626` | neutral | Primary text or dark surface |
| Medium Gray | `#4e4d4c` | neutral | Border, muted text, or supporting surface |
| Muted Silver | `#a1a1a1` | neutral | Border, muted text, or supporting surface |
| Light Gray Stroke | `#e7e7e7` | neutral | Page background or card surface |

```css
:root {
  --ref-canvas: #f9f6f2;
  --ref-surface-off-white: #f4eee5;
  --ref-pure-white: #ffffff;
  --ref-vivid-evernote-green: #94e130;
  --ref-midnight-graphite: #141414;
  --ref-deep-black: #000000;
  --ref-carbon-gray: #262626;
  --ref-medium-gray: #4e4d4c;
}
```

## Typography direction
- **Figtree**: 300, 400, 500, 600, 8px, 12px, 13px, 14px, 16px, 18px, 20px, 24px, 40px, 50px, 72px, 1.00, 1.10, 1.20, 1.30, 1.40, 1.50, 1.60; substitute `Inter`.
- **Inter**: 400, 600, 16px, 20px, 1.30, 1.50; substitute `system-ui`.

## Spacing / shape
- Section Gap: `32px`
- Card Padding: `32px`
- Element Gap: `8px`
- Page Max Width: `1320px`
- Radius: `cards: 10px, buttons: 5px, circular: 52px, largeCards: 16px`

## Surface cues
- **Canvas** `#f9f6f2`: Base page background
- **Surface Off-White** `#f4eee5`: Secondary background for sections and larger content blocks
- **Pure White** `#ffffff`: Component backgrounds, cards, and elevated UI elements

## Component cues
- **Primary Filled Button**: Call to action
- **Secondary Filled Button**: Secondary call to action
- **Ghost Text Button**: Tertiary action or navigation link
- **Primary Feature Card**: Content container
- **Secondary Content Card**: Informational container

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
