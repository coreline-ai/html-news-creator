# Varo Bank - Refero Design MD

- Source: https://styles.refero.design/style/2c05cf8d-97c5-4f35-96ef-eb53fc03ea81
- Original site: https://www.varomoney.com
- Theme: `light`
- Industry: `fintech`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Vibrant Financial Canvas

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Midnight Ink | `#000000` | neutral | Primary text or dark surface |
| Graphite | `#1c1c1c` | neutral | Primary text or dark surface |
| Storm Gray | `#939393` | neutral | Border, muted text, or supporting surface |
| Pale Mist | `#eff2f5` | neutral | Page background or card surface |
| Warm Linen | `#faefdc` | neutral | Page background or card surface |
| Sunrise Yellow | `#fdf0af` | accent | Action accent / signal color |
| Deep Plum | `#42185f` | accent | Action accent / signal color |
| Regal Violet | `#8c58d0` | brand | Action accent / signal color |
| Lavender Bloom | `#cdb0fa` | brand | Action accent / signal color |

```css
:root {
  --ref-canvas-white: #ffffff;
  --ref-midnight-ink: #000000;
  --ref-graphite: #1c1c1c;
  --ref-storm-gray: #939393;
  --ref-pale-mist: #eff2f5;
  --ref-warm-linen: #faefdc;
  --ref-sunrise-yellow: #fdf0af;
  --ref-deep-plum: #42185f;
}
```

## Typography direction
- **Neue Haas Grotesk Display**: 400, 450, 500, 12px, 14px, 16px, 18px, 20px, 22px, 28px, 36px, 44px, 52px, 72px, 0.92-1.56; substitute `Helvetica Neue`.
- **National 2 Compressed**: 450, 700, 32px, 56px, 76px, 96px, 115px, 147px, 0.80-1.10; substitute `Bebas Neue`.
- **Arial**: 400, 13px, 1.20; substitute `Arial`.

## Spacing / shape
- Section Gap: `48px`
- Card Padding: `16px`
- Element Gap: `24px`
- Radius: `menus: 4px, images: 4px, inputs: 4px, buttons: 4px`

## Component cues
- **Primary Action Button**: Calls to action that drive key user journeys.
- **Text Input Field**: Standard user data entry.
- **Ghost Navigation Button**: Interactive elements within the navigation bar.
- **Feature Card (Full-Bleed Color)**: Highlighted sections promoting specific product features.
- **Feature Card (Text-Only)**: Content blocks that emphasize text and visual separation.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
