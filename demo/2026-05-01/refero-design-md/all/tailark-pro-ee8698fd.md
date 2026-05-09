# Tailark Pro - Refero Design MD

- Source: https://styles.refero.design/style/ee8698fd-bb1e-4813-9571-5db39e508542
- Original site: https://pro.tailark.com/illustrations
- Theme: `light`
- Industry: `design`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Gallery of Digital Artifacts — like a minimalist gallery showcasing pixel-perfect UI elements on subtly textured white walls.

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Ink Black | `#09090b` | neutral | Primary text or dark surface |
| Ghost White | `#ffffff` | neutral | Page background or card surface |
| Silver Gray | `#e4e4e7` | neutral | Page background or card surface |
| Dim Gray | `#52525c` | neutral | Border, muted text, or supporting surface |
| Charcoal Black | `#404040` | neutral | Border, muted text, or supporting surface |
| Steel Gray | `#5f5f61` | neutral | Border, muted text, or supporting surface |
| Light Pearl | `#848485` | neutral | Border, muted text, or supporting surface |
| Cloud Gray | `#d4d4d8` | neutral | Border, muted text, or supporting surface |
| Pebble Gray | `#c2c2c2` | neutral | Border, muted text, or supporting surface |
| Dusty Gray | `#a6a6a6` | neutral | Border, muted text, or supporting surface |

```css
:root {
  --ref-ink-black: #09090b;
  --ref-ghost-white: #ffffff;
  --ref-silver-gray: #e4e4e7;
  --ref-dim-gray: #52525c;
  --ref-charcoal-black: #404040;
  --ref-steel-gray: #5f5f61;
  --ref-light-pearl: #848485;
  --ref-cloud-gray: #d4d4d8;
}
```

## Typography direction
- **ui-sans-serif**: 400, 500, 600, 700, 10px, 11px, 12px, 13px, 14px, 16px, 18px, 20px, 30px, 1.00, 1.20, 1.25, 1.33, 1.40, 1.43, 1.50, 1.56, 1.63, 1.71; substitute `system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol'`.
- **Geist Mono**: 100, 400, 600, 10px, 12px, 24px, 30px, 1.20, 1.33, 1.50; substitute `monospace`.
- **Mulish**: 400, 14px, 1.43; substitute `'Mulish', sans-serif`.

## Spacing / shape
- Section Gap: `48px`
- Card Padding: `12px`
- Element Gap: `8px`
- Radius: `cards: 16px, input: 4px, buttons: 6px, default: 6px, largeCards: 32px, extraLargeCards: 40px`

## Surface cues
- **Canvas Background** `#ffffff`: The foundational background for the entire page, providing a crisp, expansive white space.
- **Default Card/Surface** `#ffffff`: The primary surface for most content cards, appearing directly on the canvas.
- **Translucent Elevated Card** `#oklab(0.999994 0.0000455678 0.0000200868 / 0.75)`: A slightly translucent white background used for certain card variants, allowing a hint of the canvas to show through.
- **Subtle Elevated Card** `#oklab(0.984998 -0.00000956655 0.0000230074 / 0.75)`: A near-white background for cards with a very subtle off-white tint, providing a distinct identity while maintaining lightness.

## Component cues
- **Invoice Card**: Reference component style.
- **File Type Badge Grid**: Reference component style.
- **Chat & Notification Cards**: Reference component style.
- **Default Button**: Interactive element
- **White Text Button**: Secondary action

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
