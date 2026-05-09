# Eat Real Food - Refero Design MD

- Source: https://styles.refero.design/style/3d32f841-490d-4e5f-aba0-43c9d0c13130
- Original site: https://realfood.gov
- Theme: `light`
- Industry: `other`
- Recommended fit: **Design reference / webapp exploration**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Stark Manifesto on Creamy Canvas

## Apply to
- General webapp UI exploration
- Demo cards and catalog surfaces
- Future admin/subscriber UI references

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Ink | `#110000` | neutral | Primary text or dark surface |
| Buttermilk | `#fdfbee` | neutral | Page background or card surface |
| Paper White | `#ffffff` | neutral | Page background or card surface |
| Light Linen | `#f3f0d6` | neutral | Page background or card surface |
| Silver Mist | `#e5e5e5` | neutral | Page background or card surface |
| Ash Shadow | `#d2d0c6` | neutral | Border, muted text, or supporting surface |
| Muted Stone | `#8d7d7d` | neutral | Border, muted text, or supporting surface |
| Pale Gray | `#bebcb3` | neutral | Border, muted text, or supporting surface |
| Warning Red | `#d50000` | accent | Action accent / signal color |
| Alert Red 1 | `#920000` | accent | Action accent / signal color |

```css
:root {
  --ref-midnight-ink: #110000;
  --ref-buttermilk: #fdfbee;
  --ref-paper-white: #ffffff;
  --ref-light-linen: #f3f0d6;
  --ref-silver-mist: #e5e5e5;
  --ref-ash-shadow: #d2d0c6;
  --ref-muted-stone: #8d7d7d;
  --ref-pale-gray: #bebcb3;
}
```

## Typography direction
- **Die Grotesk D**: 700, 32px, 44px, 48px, 96px, 115px, 144px, 155px, 170px, 0.84, 0.86, 0.92, 0.95, 0.96, 1.02, 1.04; substitute `Bebas Neue`.
- **Die Grotesk A**: 400, 500, 600, 700, 11px, 12px, 14px, 16px, 33px, 0.98, 1.10, 1.18, 1.20, 1.40, 1.50; substitute `Inter`.
- **Die Grotesk B**: 500, 700, 14px, 16px, 19px, 21px, 24px, 26px, 31px, 0.92, 0.95, 0.96, 1.10, 1.18, 1.20, 1.24, 1.50; substitute `Open Sans`.

## Spacing / shape
- Section Gap: `80px`
- Card Padding: `24px`
- Element Gap: `24px`
- Radius: `cards: 16px, images: 24px, buttons: 40px, interactive: 24px, highlightCards: 12px 12px 0px 0px`

## Surface cues
- **Light Linen** `#f3f0d6`: Base page background
- **Buttermilk** `#fdfbee`: Standard content cards, primary action buttons
- **Paper White** `#ffffff`: Elevated cards, subtle background elements, navigation

## Component cues
- **Pill Button**: Primary Call to Action
- **Ghost Text Button**: Secondary Action or Navigation
- **Navigation Link**: Global Navigation Link
- **Standard Card**: Content container for articles or features
- **Elevated Card**: Prominent content container

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
