# Acceptandproceed - Refero Design MD

- Source: https://styles.refero.design/style/f63b4703-db8b-4bc9-8d8f-17262b12d4b3
- Original site: https://www.acceptandproceed.com
- Theme: `light`
- Industry: `agency`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Gallery Canvas, Subtle Presence

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Ink | `#000000` | neutral | Primary text or dark surface |
| Fog | `#8c8c8c` | neutral | Border, muted text, or supporting surface |
| Cloud Cover | `#ecebe7` | neutral | Page background or card surface |
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Warm Linen | `#f9f7f3` | neutral | Page background or card surface |
| Steel Gaze | `#a2a1a1` | neutral | Border, muted text, or supporting surface |
| Carbon Text | `#333333` | neutral | Primary text or dark surface |

```css
:root {
  --ref-midnight-ink: #000000;
  --ref-fog: #8c8c8c;
  --ref-cloud-cover: #ecebe7;
  --ref-canvas-white: #ffffff;
  --ref-warm-linen: #f9f7f3;
  --ref-steel-gaze: #a2a1a1;
  --ref-carbon-text: #333333;
}
```

## Typography direction
- **Messina Sans**: 400, 8px, 10px, 14px, 17px, 20px, 24px, 34px, 50px, 72px, 1.00, 1.28, 1.29, 1.33, 1.40, 1.41, 1.43, 1.60, 1.71; substitute `Inter`.
- **Letterformvariations 04 Dmgx**: 400, 34px, 1.00; substitute `PT Serif`.

## Spacing / shape
- Section Gap: `48px`
- Card Padding: `12px`
- Element Gap: `8px`
- Radius: `cards: 8px, badges: 3.4px, inputs: 100px, buttons: 20px`

## Surface cues
- **Canvas White** `#ffffff`: Base page background
- **Warm Linen** `#f9f7f3`: Secondary background layer, often for content sections or cards
- **Cloud Cover** `#ecebe7`: Interactive elements like filled buttons, providing a subtle pop over backgrounds

## Component cues
- **Filled Button: Read Story Large**: Primary interactive button for calls to action.
- **Ghost Button: Navigation Link**: Subtle navigation or secondary action within content. Inherits text color from parent context.
- **Pill Button: Curved Left**: Unique interactive element, often for specialized actions or tags, with an asymmetric pill shape.
- **Project Card: Image Top**: Container for project previews, featuring an imagery block and descriptive text.
- **Soft Badge: Outlined Text**: Categorization or tagging element, visually lightweight.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
