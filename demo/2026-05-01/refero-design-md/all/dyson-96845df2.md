# Dyson - Refero Design MD

- Source: https://styles.refero.design/style/96845df2-7ddb-420a-814e-c339f95a6554
- Original site: https://dyson.com
- Theme: `light`
- Industry: `other`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
engineered precision, clean displays

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Dyson Ink | `#333333` | neutral | Primary text or dark surface |
| Ghost Gray | `#999999` | neutral | Border, muted text, or supporting surface |
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Deep Graphite | `#000000` | neutral | Primary text or dark surface |
| Aluminum | `#919191` | neutral | Border, muted text, or supporting surface |
| Medium Gray | `#555555` | neutral | Border, muted text, or supporting surface |
| Light Silver | `#ebebeb` | neutral | Page background or card surface |
| Warm Paper | `#fff8e6` | neutral | Page background or card surface |
| Steel Gray | `#dadada` | neutral | Page background or card surface |
| Success Green | `#79b928` | brand | Action accent / signal color |

```css
:root {
  --ref-dyson-ink: #333333;
  --ref-ghost-gray: #999999;
  --ref-canvas-white: #ffffff;
  --ref-deep-graphite: #000000;
  --ref-aluminum: #919191;
  --ref-medium-gray: #555555;
  --ref-light-silver: #ebebeb;
  --ref-warm-paper: #fff8e6;
}
```

## Typography direction
- **DysonFutura**: 300, 400, 500, 12px, 14px, 16px, 18px, 24px, 28px, 32px, 36px, 1.20-2.00; substitute `Futura Std`.

## Spacing / shape
- Section Gap: `48px`
- Card Padding: `16px`
- Element Gap: `8px`
- Radius: `cards: 0px, badges: 2px, images: 8px, buttons: 0px`

## Component cues
- **Product Card — Destacados**: Reference component style.
- **Promotion Banner**: Reference component style.
- **Button Group — CTA Variants**: Reference component style.
- **Primary CTA Button**: Main call to action
- **Text Only Button**: Secondary action in dark contexts

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
