# Clay - Refero Design MD

- Source: https://styles.refero.design/style/b5ca4e9a-2322-4796-b4c5-3b3bf194821f
- Original site: https://clay.com
- Theme: `light`
- Industry: `saas`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Playful Precision Playground. A brightly lit space filled with meticulously arranged, colorful building blocks.

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Pitch Black | `#000000` | neutral | Primary text or dark surface |
| Ghost White | `#ffffff` | neutral | Page background or card surface |
| Cloud Gray | `#f9f8f6` | neutral | Page background or card surface |
| Platinum Gray | `#e6e8ec` | neutral | Page background or card surface |
| Oatmeal | `#dad4c8` | neutral | Border, muted text, or supporting surface |
| Clay Violet | `#3859f9` | brand | Action accent / signal color |
| Vivid Sky | `#429dff` | accent | Action accent / signal color |
| Tangerine | `#ff7614` | accent | Action accent / signal color |
| Lime Pop | `#cbd810` | accent | Action accent / signal color |
| Azure Glow | `#3bd3fd` | accent | Action accent / signal color |

```css
:root {
  --ref-pitch-black: #000000;
  --ref-ghost-white: #ffffff;
  --ref-cloud-gray: #f9f8f6;
  --ref-platinum-gray: #e6e8ec;
  --ref-oatmeal: #dad4c8;
  --ref-clay-violet: #3859f9;
  --ref-vivid-sky: #429dff;
  --ref-tangerine: #ff7614;
}
```

## Typography direction
- **Roobert**: 400, 500, 600, 700, 10px, 11px, 12px, 13px, 14px, 15px, 16px, 18px, 20px, 32px, 44px, 60px, 80px, 1.00, 1.10, 1.20, 1.40, 1.50, 1.60; substitute `Arial`.
- **Phosphor**: 400, 13px, 16px, 20px, 1.00; substitute `system-ui`.
- **Phosphor-Bold**: 400, 16px, 1.00; substitute `system-ui`.

## Spacing / shape
- Section Gap: `64px`
- Card Padding: `20px`
- Element Gap: `8px`
- Page Max Width: `1200px`
- Radius: `pill: 1584px, cards: 12px, buttons: 12px, largeCards: 40px, interactiveElements: 8px`

## Component cues
- **CTA Button Group**: Reference component style.
- **Feature Bullet Card with Stat**: Reference component style.
- **Testimonial Cards**: Reference component style.
- **Primary Action Button**: Button
- **Secondary Outline Button**: Button

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
