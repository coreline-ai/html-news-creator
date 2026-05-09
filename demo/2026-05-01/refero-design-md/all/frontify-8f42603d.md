# Frontify - Refero Design MD

- Source: https://styles.refero.design/style/8f42603d-7ff9-446e-99a3-6bdd1f388ae5
- Original site: https://www.frontify.com/en
- Theme: `light`
- Industry: `design`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Architectural blueprint on soft linen

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Inkwell Black | `#111110` | neutral | Primary text or dark surface |
| Paper White | `#f0f0eb` | neutral | Page background or card surface |
| True White | `#ffffff` | neutral | Page background or card surface |
| Canvas Muted | `#e1e1db` | neutral | Page background or card surface |
| Stone Whisper | `#d7d7cf` | neutral | Border, muted text, or supporting surface |
| Deep Pewter | `#464643` | neutral | Border, muted text, or supporting surface |
| Charcoal Grey | `#000000` | neutral | Primary text or dark surface |
| Pale Granite | `#cbcbc5` | neutral | Border, muted text, or supporting surface |
| Dusty Sage | `#bfbfb8` | neutral | Border, muted text, or supporting surface |
| Slate Echo | `#575753` | neutral | Border, muted text, or supporting surface |

```css
:root {
  --ref-inkwell-black: #111110;
  --ref-paper-white: #f0f0eb;
  --ref-true-white: #ffffff;
  --ref-canvas-muted: #e1e1db;
  --ref-stone-whisper: #d7d7cf;
  --ref-deep-pewter: #464643;
  --ref-charcoal-grey: #000000;
  --ref-pale-granite: #cbcbc5;
}
```

## Typography direction
- **ABC Diatype**: 400, 500, 14px, 18px, 1.00, 1.30, 1.35, 1.50; substitute `Inter`.
- **Cranny**: 300, 400, 16px, 18px, 20px, 24px, 28px, 32px, 40px, 61px, 80px, 96px, 0.91, 1.00, 1.10, 1.30, 1.50; substitute `Playfair Display`.
- **Satoshi**: 400, 14px, 1.30; substitute `Inter`.

## Spacing / shape
- Section Gap: `48px`
- Card Padding: `32px`
- Element Gap: `8px`
- Radius: `cards: 8px, images: 18px, inputs: 0px, buttons: 24px, navItems: 32px, smallComponents: 4px`

## Surface cues
- **Paper White** `#f0f0eb`: Primary page background, expansive content areas
- **Canvas Muted** `#e1e1db`: Card backgrounds, secondary container surfaces
- **Stone Whisper** `#d7d7cf`: Section dividers, underlying contextual elements

## Component cues
- **Primary Filled Button**: Call to action, main navigation buttons
- **Outlined Button (Dark border)**: Secondary actions, ghost buttons, calls to explore
- **Outlined Button (Light border)**: Ghost buttons on dark backgrounds
- **Subtle Card**: Content containers, feature blocks on light backgrounds
- **Ghost Card**: Decorative or transparent content groupings

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
