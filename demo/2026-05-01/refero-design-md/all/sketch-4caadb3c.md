# Sketch - Refero Design MD

- Source: https://styles.refero.design/style/4caadb3c-3865-4a4d-9e1a-46478ac71078
- Original site: https://sketch.com
- Theme: `light`
- Industry: `design`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Architectural Digital Canvas. A pristine white canvas with soft, glowing digital light, and precise typography.

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Pitch Black | `#000000` | neutral | Primary text or dark surface |
| Graphite | `#212123` | neutral | Primary text or dark surface |
| Stone Grey | `#4a4a4a` | neutral | Border, muted text, or supporting surface |
| Ash Grey | `#5c5c5c` | neutral | Border, muted text, or supporting surface |
| Silver Mist | `#a7a7a7` | neutral | Border, muted text, or supporting surface |
| Canvas White | `#fafafa` | neutral | Page background or card surface |
| Cloud White | `#e6e6e6` | neutral | Page background or card surface |
| Deep Space | `#151515` | neutral | Primary text or dark surface |
| Sky Blue | `#555dff` | accent | Action accent / signal color |
| Teal Glow | `#03cbbc` | accent | Action accent / signal color |

```css
:root {
  --ref-pitch-black: #000000;
  --ref-graphite: #212123;
  --ref-stone-grey: #4a4a4a;
  --ref-ash-grey: #5c5c5c;
  --ref-silver-mist: #a7a7a7;
  --ref-canvas-white: #fafafa;
  --ref-cloud-white: #e6e6e6;
  --ref-deep-space: #151515;
}
```

## Typography direction
- **InterVariable**: 300, 400, 500, 600, 11px, 12px, 14px, 15px, 16px, 17px, 20px, 22px, 24px, 1.00, 1.09, 1.15, 1.17, 1.25, 1.33, 1.40, 1.41, 1.43, 1.50, 1.60, 1.65; substitute `Inter`.
- **Reckless**: 500, 44px, 76px, 1.00, 1.09; substitute `Playfair Display`.

## Spacing / shape
- Section Gap: `64px`
- Card Padding: `78px`
- Element Gap: `8px`
- Radius: `cards: 20px, badges: 9999px, inputs: 16px, buttons: 24px`

## Component cues
- **Primary CTA Button Group**: Reference component style.
- **Announcement Banner Card**: Reference component style.
- **Status Badge Collection**: Reference component style.
- **Primary Filled Button**: Main call to action
- **Ghost Button with Outline**: Secondary action or link

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
