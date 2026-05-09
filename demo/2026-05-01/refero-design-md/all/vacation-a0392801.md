# Vacation® - Refero Design MD

- Source: https://styles.refero.design/style/a0392801-aa0f-4c0c-81e1-4e1684eb832a
- Original site: https://www.vacation.inc
- Theme: `light`
- Industry: `ecommerce`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Sun-kissed retro comfort

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midday Sand | `#f1d27a` | accent | Action accent / signal color |
| Ocean Blue | `#23659f` | accent | Action accent / signal color |
| Coral Sunset | `#d1796d` | accent | Action accent / signal color |
| Breezy Teal | `#39aaa7` | accent | Action accent / signal color |
| Electric Violet | `#0048ff` | accent | Action accent / signal color |
| Graphite | `#333333` | neutral | Primary text or dark surface |
| Parchment White | `#e5e7eb` | neutral | Page background or card surface |
| Cloud Cover | `#ffffff` | neutral | Page background or card surface |
| Faded Cinder | `#6a6966` | neutral | Border, muted text, or supporting surface |
| Pale Ash | `#dddddd` | neutral | Page background or card surface |

```css
:root {
  --ref-midday-sand: #f1d27a;
  --ref-ocean-blue: #23659f;
  --ref-coral-sunset: #d1796d;
  --ref-breezy-teal: #39aaa7;
  --ref-electric-violet: #0048ff;
  --ref-graphite: #333333;
  --ref-parchment-white: #e5e7eb;
  --ref-cloud-cover: #ffffff;
}
```

## Typography direction
- **Helvetica Neue LT Std**: 400, 700, 16px, 18px, 30px, 0.80, 1.33, 1.50; substitute `Helvetica Neue, Arial`.
- **ITCGaramondStd-LtCond**: 300, 400, 500, 700, 14px, 16px, 18px, 20px, 30px, 32px, 36px, 48px, 64px, 120px, 0.80, 0.86, 0.90, 1.00, 1.10, 1.11, 1.20, 1.33, 1.38, 1.50, 1.78; substitute `Garamond, serif`.
- **OptimaLTP**: 400, 500, 10px, 12px, 13px, 16px, 18px, 23px, 1.00, 1.04, 1.20, 1.33, 1.50, 1.85; substitute `Optima, serif`.

## Spacing / shape
- Section Gap: `30px`
- Card Padding: `27px`
- Element Gap: `20px`
- Radius: `cards: 5px, badges: 0px, inputs: 2px, buttons: 9999px`

## Surface cues
- **Canvas Base** `#e5e7eb`: Dominant page background, soft and inviting.
- **Elevated Card** `#f1d27a`: Background for primary interactive elements and promotional cards, providing visual warmth.
- **Input / Highlight** `#ffffff`: Input fields and surfaces requiring highest contrast or emphasis.
- **Secondary Card** `#b0c4de`: Background for secondary content cards, providing textural variation.

## Component cues
- **Pill Button - Midday Sand**: Primary call to action button.
- **Ghost Button - Light Text**: Secondary navigation or subtle actions on dark backgrounds.
- **Coupon Card**: Promotional modal or featured content display.
- **Text Input - Light**: Form text input field on light backgrounds.
- **Text Input - Dark**: Form text input field on dark backgrounds.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
