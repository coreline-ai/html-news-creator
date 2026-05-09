# Wellfound - Refero Design MD

- Source: https://styles.refero.design/style/f8286b32-cc41-43e3-8b43-067333bb2e32
- Original site: https://wellfound.com
- Theme: `light`
- Industry: `productivity`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Startup Canvas, Clean Bold Type

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Midnight Ink | `#051316` | neutral | Primary text or dark surface |
| Smoke Gray | `#d8d8d8` | neutral | Border, muted text, or supporting surface |
| Charcoal | `#333333` | neutral | Primary text or dark surface |
| Off-Black | `#222222` | neutral | Primary text or dark surface |
| Deep Plum | `#210d25` | brand | Action accent / signal color |
| Rose Blush | `#fff4f6` | accent | Action accent / signal color |
| Vermillion Red | `#ec2e3a` | accent | Action accent / signal color |
| Burgundy Bloom | `#541142` | brand | Action accent / signal color |
| Marigold Gold | `#f4b640` | accent | Action accent / signal color |

```css
:root {
  --ref-canvas-white: #ffffff;
  --ref-midnight-ink: #051316;
  --ref-smoke-gray: #d8d8d8;
  --ref-charcoal: #333333;
  --ref-off-black: #222222;
  --ref-deep-plum: #210d25;
  --ref-rose-blush: #fff4f6;
  --ref-vermillion-red: #ec2e3a;
}
```

## Typography direction
- **Graphik**: 400, 500, 600, 14px, 16px, 17px, 21px, 22px, 24px, 30px, 40px, 72px, 100px, 0.82, 1.00, 1.13, 1.14, 1.27, 1.30, 1.36, 1.40, 1.43, 1.50, 1.71; substitute `Inter`.
- **Aeonik Fono**: 400, 14px, 1.40; substitute `Space Mono`.
- **Aeonikfono**: 400, 700, 40px, 1.3.

## Spacing / shape
- Section Gap: `40px`
- Card Padding: `22px`
- Element Gap: `20px`
- Page Max Width: `1400px`
- Radius: `tags: 1000px, cards: 16px, buttons: 12px, largeElements: 40px`

## Surface cues
- **Canvas White** `#ffffff`: Primary page background and default surface for content areas
- **Rose Blush** `#fff4f6`: Elevated card backgrounds, subtle highlight sections
- **Deep Plum** `#210d25`: Prominent dark background sections for emphasis and data display

## Component cues
- **Primary Filled Button (Dark)**: Call to action button for primary actions.
- **Ghost Button (Light Border)**: Secondary action or navigational buttons, visually lighter.
- **Ghost Button (Dark Border)**: Secondary action button on light backgrounds.
- **Feature Card (Rose Blush)**: Used for presenting key features or benefits.
- **Information Card (White)**: Standard card for content blocks and lists.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
