# Loops - Refero Design MD

- Source: https://styles.refero.design/style/4d832c12-dd14-45b0-bba7-2d3bc25d8264
- Original site: https://loops.so
- Theme: `light`
- Industry: `saas`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Architectural blueprint on white marble. Sharp, clean, and formally structured.

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Ink | `#000000` | neutral | Primary text or dark surface |
| Greige Canvas | `#faf9f7` | neutral | Page background or card surface |
| Whisper White | `#ffffff` | neutral | Page background or card surface |
| Slate Gray | `#1c1917` | neutral | Primary text or dark surface |
| Fog | `#d6d3d1` | neutral | Border, muted text, or supporting surface |
| Ash | `#e7e5e4` | neutral | Page background or card surface |
| Stone | `#44403c` | neutral | Border, muted text, or supporting surface |
| Pewter | `#a8a29e` | neutral | Border, muted text, or supporting surface |
| Warm Gray | `#292524` | neutral | Primary text or dark surface |
| Steel | `#57534e` | neutral | Border, muted text, or supporting surface |

```css
:root {
  --ref-midnight-ink: #000000;
  --ref-greige-canvas: #faf9f7;
  --ref-whisper-white: #ffffff;
  --ref-slate-gray: #1c1917;
  --ref-fog: #d6d3d1;
  --ref-ash: #e7e5e4;
  --ref-stone: #44403c;
  --ref-pewter: #a8a29e;
}
```

## Typography direction
- **Newsreader**: 600, 28px, 34px, 80px, 1.00, 1.20, 1.25.
- **sans-serif**: 400, 600, 12px, 16px, 1.20; substitute `system-ui`.
- **ui-sans-serif**: 400, 500, 600, 700, 12px, 13px, 14px, 15px, 16px, 17px, 1.00, 1.20, 1.25, 1.30, 1.35; substitute `system-ui`.

## Spacing / shape
- Section Gap: `40px`
- Card Padding: `12px`
- Element Gap: `12px`
- Radius: `pill: 999px, cards: 8px, buttons: 8px, default: 8px, elevatedCards: 12px`

## Surface cues
- **Greige Canvas** `#faf9f7`: Dominant page background, a subtle off-white base.
- **Whisper White** `#ffffff`: Primary surface for cards, content blocks, and interactive components. Appears brighter against the canvas.
- **Elevated Card** `#ffffff`: Key information cards, subtly lifted using a soft shadow, maintaining Whisper White as the background.

## Component cues
- **Pill Ghost Button**: Secondary action or tag within content.
- **Standard Ghost Button**: Informational or subtle action within the UI.
- **Outlined Card**: Content container with an emphasis on its contained nature.
- **Navigation Link**: Primary navigation item.
- **Hero Action Button**: Primary Call to Action.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
