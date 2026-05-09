# Awesomic - Refero Design MD

- Source: https://styles.refero.design/style/8512e28d-5385-4c20-a336-214568c4370c
- Original site: https://www.awesomic.io
- Theme: `light`
- Industry: `saas`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
white canvas, bold monochrome

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Ink | `#09090b` | neutral | Primary text or dark surface |
| Graphite | `#3f3f46` | neutral | Primary text or dark surface |
| Steel Gray | `#71717a` | neutral | Border, muted text, or supporting surface |
| Silver Mist | `#a1a1aa` | neutral | Border, muted text, or supporting surface |
| Faded Gray | `#d4d4d8` | neutral | Border, muted text, or supporting surface |
| Cloud White | `#ffffff` | neutral | Page background or card surface |
| Canvas White | `#f4f4f5` | neutral | Page background or card surface |
| Whisper Gray | `#ececee` | neutral | Page background or card surface |
| Jet Black | `#18181b` | neutral | Primary text or dark surface |
| Deep Gray | `#222222` | neutral | Primary text or dark surface |

```css
:root {
  --ref-midnight-ink: #09090b;
  --ref-graphite: #3f3f46;
  --ref-steel-gray: #71717a;
  --ref-silver-mist: #a1a1aa;
  --ref-faded-gray: #d4d4d8;
  --ref-cloud-white: #ffffff;
  --ref-canvas-white: #f4f4f5;
  --ref-whisper-gray: #ececee;
}
```

## Typography direction
- **Cosmica**: 300, 400, 500, 600, 700, 10px, 12px, 13px, 14px, 15px, 16px, 18px, 20px, 32px, 40px, 56px, 64px, 1.00, 1.12, 1.25, 1.28, 1.31, 1.35, 1.45, 1.48, 1.50, 1.55, 1.56, 1.62, 1.64, 1.68, 1.80; substitute `Inter`.

## Spacing / shape
- Section Gap: `40px`
- Card Padding: `28px`
- Element Gap: `8px`
- Radius: `cards: 36px, badges: 12px, inputs: 12px, buttons: 12px, imageMasks: 48px, navigation: 12px, smallerCards: 28px, largeElements: 64px`

## Surface cues
- **Cloud White Canvas** `#ffffff`: Primary page background, base layer.
- **Canvas White Panel** `#f4f4f5`: Secondary background for sections, a subtle shift from the base canvas.
- **Whisper Gray Card** `#ececee`: Background for elevated content cards, providing a distinct, but soft, separation.

## Component cues
- **Primary Ghost Button**: Low-prominence action button for navigation or secondary actions
- **Primary Filled Button**: High-prominence call to action
- **Secondary Ghost Button**: Minimalist button for filtering or tagging
- **Filled Brand Card**: Content card with prominent background
- **Elevated Subtle Card**: Content card with slight background distinction

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
