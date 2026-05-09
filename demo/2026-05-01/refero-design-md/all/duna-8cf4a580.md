# Duna - Refero Design MD

- Source: https://styles.refero.design/style/8cf4a580-bfb6-4090-a899-f734ffe62370
- Original site: https://duna.com
- Theme: `light`
- Industry: `fintech`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Understated Compliance Authority

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Ink | `#000000` | neutral | Primary text or dark surface |
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Near White | `#f7f7f5` | neutral | Page background or card surface |
| Deep Charcoal | `#292421` | neutral | Primary text or dark surface |
| Subtle Gray | `#898683` | neutral | Border, muted text, or supporting surface |
| Card Wash | `#edece7` | neutral | Page background or card surface |
| Quiet Black | `#1a1816` | neutral | Primary text or dark surface |
| Medium Gray | `#444444` | neutral | Border, muted text, or supporting surface |
| Onyx Button Background | `#160f0c` | neutral | Primary text or dark surface |
| Light Steel | `#b2afae` | neutral | Border, muted text, or supporting surface |

```css
:root {
  --ref-midnight-ink: #000000;
  --ref-canvas-white: #ffffff;
  --ref-near-white: #f7f7f5;
  --ref-deep-charcoal: #292421;
  --ref-subtle-gray: #898683;
  --ref-card-wash: #edece7;
  --ref-quiet-black: #1a1816;
  --ref-medium-gray: #444444;
}
```

## Typography direction
- **sans-serif**: 400, 12px, 1.2.
- **GT America**: 400, 20px, 1.50; substitute `Inter`.
- **GT America Trial Rg**: 400, 14px, 16px, 1.50, 1.60, 1.71; substitute `Inter`.

## Spacing / shape
- Section Gap: `40px`
- Card Padding: `16px`
- Element Gap: `10px`
- Radius: `cards: 16px, images: 24px, inputs: 8px, buttons: 999px, smallElements: 12px`

## Surface cues
- **Canvas White** `#ffffff`: Primary page background, base for most content blocks.
- **Near White** `#f7f7f5`: Secondary section background, providing subtle differentiation without strong contrast.
- **Input Fill** `#eeeeee`: Background for interactive input fields.
- **Card Wash** `#edece7`: Specific card background, providing a slightly darker, more opaque surface than the canvas.

## Component cues
- **Primary Filled Button**: Main call to action button.
- **Ghost Button**: Secondary action or navigation outside of primary flows.
- **Announcement Pill**: Small, informational component to highlight news or status.
- **Simple Card**: Basic container for information, features a subtle background to distinguish from canvas.
- **Elevated Card**: Interactive or featured card with a light shadow for depth.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
