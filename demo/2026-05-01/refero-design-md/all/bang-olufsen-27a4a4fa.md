# Bang & Olufsen - Refero Design MD

- Source: https://styles.refero.design/style/27a4a4fa-4b1a-4e7e-b2c3-3e5bf57f00e5
- Original site: https://bang-olufsen.com
- Theme: `mixed`
- Industry: `ecommerce`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Gallery of precise objects. A dark, velvet-lined showcase where each product rests, spotlighted with refined exactitude.

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Indigo | `#060daa` | brand | Action accent / signal color |
| Carbon Black | `#191817` | neutral | Primary text or dark surface |
| Barely White | `#fcfaee` | neutral | Page background or card surface |
| Ash Gray | `#555555` | neutral | Border, muted text, or supporting surface |
| Pure White | `#ffffff` | neutral | Page background or card surface |
| Pale Silver | `#e5e5e5` | neutral | Page background or card surface |
| Pure Black | `#000000` | neutral | Primary text or dark surface |

```css
:root {
  --ref-midnight-indigo: #060daa;
  --ref-carbon-black: #191817;
  --ref-barely-white: #fcfaee;
  --ref-ash-gray: #555555;
  --ref-pure-white: #ffffff;
  --ref-pale-silver: #e5e5e5;
  --ref-pure-black: #000000;
}
```

## Typography direction
- **BeoSupreme**: 400, 500, 700, 12px, 14px, 16px, 24px, 36px, 1.00, 1.15, 1.25, 1.33, 1.43, 1.50, 1.63, 1.67, 1.71, 2.19; substitute `Open Sans`.

## Spacing / shape
- Section Gap: `48px`
- Card Padding: `0px`
- Element Gap: `4px`
- Radius: `badges: 2px, buttons: 40px`

## Component cues
- **Product Cards — Explore Superventas**: Reference component style.
- **Hero CTA — Beo Grace**: Reference component style.
- **Button Group — B&O Style System**: Reference component style.
- **Primary Button (Honey Tone CTA)**: Call to action
- **Ghost Button (Menu/Search)**: Navigation/Utility

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
