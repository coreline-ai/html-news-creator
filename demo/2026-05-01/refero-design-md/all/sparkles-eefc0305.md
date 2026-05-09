# Sparkles - Refero Design MD

- Source: https://styles.refero.design/style/eefc0305-818c-4f57-80ce-a4bc1f7aac92
- Original site: https://sparkles.dev
- Theme: `light`
- Industry: `devtools`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Whiteboard of playful engineering

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Ink | `#0a0a0a` | neutral | Primary text or dark surface |
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Steel Gray | `#18181b` | neutral | Primary text or dark surface |
| Cloud Cover | `#e5e5e5` | neutral | Page background or card surface |
| Pale Ash | `#f4f4f5` | neutral | Page background or card surface |
| Soft Fog | `#fafafa` | neutral | Page background or card surface |
| Pale Stone | `#d4d4d8` | neutral | Border, muted text, or supporting surface |
| Cool Graphite | `#52525c` | neutral | Border, muted text, or supporting surface |
| Icon Stroke | `#71717b` | neutral | Border, muted text, or supporting surface |
| Input Fill | `#27272a` | neutral | Primary text or dark surface |

```css
:root {
  --ref-midnight-ink: #0a0a0a;
  --ref-canvas-white: #ffffff;
  --ref-steel-gray: #18181b;
  --ref-cloud-cover: #e5e5e5;
  --ref-pale-ash: #f4f4f5;
  --ref-soft-fog: #fafafa;
  --ref-pale-stone: #d4d4d8;
  --ref-cool-graphite: #52525c;
}
```

## Typography direction
- **Articulat CF**: 400, 500, 600, 12px, 14px, 16px, 18px, 20px, 1.33, 1.40, 1.43, 1.50, 1.56, 1.60, 1.75, 1.78; substitute `Inter`.
- **Gelica**: 600, 36px, 48px, 60px, 1.00, 1.11; substitute `Georgia`.

## Spacing / shape
- Section Gap: `40px`
- Card Padding: `24px`
- Element Gap: `16px`
- Radius: `cards: 10px, forms: 10px, buttons: 10px, default: 10px, largeCards: 14px`

## Surface cues
- **Canvas White** `#ffffff`: Primary page background
- **Pale Ash** `#f4f4f5`: Subtle background for specific sections or cards to create visual separation without high contrast
- **Soft Fog** `#fafafa`: Alternative subtle background for cards or containers, slightly off-white

## Component cues
- **Primary Filled Button**: Call to action button
- **Text Only Button**: Secondary action or ghost button
- **Navigation Link Button**: Header navigation item, text-based action
- **Informational Card**: Content container for features or pricing
- **Alt Background Card**: Content container with subtle background

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
