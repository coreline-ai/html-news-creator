# SpatialChat - Refero Design MD

- Source: https://styles.refero.design/style/5b90e218-b325-4901-a1c5-ea1134339826
- Original site: https://spatial.chat
- Theme: `light`
- Industry: `productivity`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Violet accented white canvas. Pure white surfaces are the backdrop for precise charcoal text and interactive violet elements, recalling an architect's blueprint highlighted with a single, crucial color.

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Absolute Zero | `#ffffff` | neutral | Page background or card surface |
| Charcoal Black | `#000000` | neutral | Primary text or dark surface |
| Deep Space Charcoal | `#030712` | neutral | Primary text or dark surface |
| Slate Gray | `#4b5563` | neutral | Border, muted text, or supporting surface |
| Whisper Gray | `#f9fafb` | neutral | Page background or card surface |
| Fog | `#e5e7eb` | neutral | Page background or card surface |
| Periwinkle Mist | `#f2f2ff` | neutral | Page background or card surface |
| Steel Gray | `#d1d5db` | neutral | Border, muted text, or supporting surface |
| Majestic Violet | `#5727e7` | brand | Action accent / signal color |

```css
:root {
  --ref-absolute-zero: #ffffff;
  --ref-charcoal-black: #000000;
  --ref-deep-space-charcoal: #030712;
  --ref-slate-gray: #4b5563;
  --ref-whisper-gray: #f9fafb;
  --ref-fog: #e5e7eb;
  --ref-periwinkle-mist: #f2f2ff;
  --ref-steel-gray: #d1d5db;
}
```

## Typography direction
- **Satoshi**: 400, 500, 600, 700, 14px, 16px, 18px, 20px, 24px, 32px, 40px, 44px, 48px, 60px, 1.30, 1.38, 1.40, 1.43, 1.50, 1.56, 1.60; substitute `Inter`.

## Spacing / shape
- Section Gap: `64px`
- Card Padding: `12-24px`
- Element Gap: `8px`
- Radius: `cards: 16px, badges: 8px, inputs: 8px, buttons: 12px`

## Component cues
- **Hero CTA Button Group with Social Proof**: Reference component style.
- **Feature Section — Spatial Interaction**: Reference component style.
- **Announcement Banner + Badge Group**: Reference component style.
- **Primary Action Button**: Main call to action
- **Outline Accent Button**: Secondary action or navigation

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
