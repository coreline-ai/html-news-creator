# DrawHistory - Refero Design MD

- Source: https://styles.refero.design/style/25246b10-83a4-4f51-a411-cf85503b94a8
- Original site: https://drawhistory.com
- Theme: `light`
- Industry: `agency`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Warm parchment manifesto

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas Parchment | `#e5e7eb` | neutral | Page background or card surface |
| Near Black | `#000000` | neutral | Primary text or dark surface |
| Onyx Card | `#1d1d1b` | neutral | Primary text or dark surface |
| Sage Dark | `#3d3b2f` | neutral | Primary text or dark surface |
| Paper White | `#ffffff` | neutral | Page background or card surface |
| Wet Sand | `#e1d3c7` | neutral | Border, muted text, or supporting surface |
| Steel Gray | `#999999` | neutral | Border, muted text, or supporting surface |
| Fog Input | `#b3b3b3` | neutral | Border, muted text, or supporting surface |
| Pale Clay | `#faf6f3` | neutral | Page background or card surface |
| Flame Orange | `#ff6714` | accent | Action accent / signal color |

```css
:root {
  --ref-canvas-parchment: #e5e7eb;
  --ref-near-black: #000000;
  --ref-onyx-card: #1d1d1b;
  --ref-sage-dark: #3d3b2f;
  --ref-paper-white: #ffffff;
  --ref-wet-sand: #e1d3c7;
  --ref-steel-gray: #999999;
  --ref-fog-input: #b3b3b3;
}
```

## Typography direction
- **Eloquia Text**: 300, 400, 14px, 16px, 18px, 20px, 22px, 35px, 36px, 40px, 44px, 55px, 100px, 104px, 0.95, 1.00, 1.09, 1.10, 1.11, 1.13, 1.14, 1.18, 1.40, 1.43, 1.50, 1.56; substitute `Source Serif Pro`.
- **Roboto Mono**: 400, 14px, 15px, 16px, 1.25, 1.33, 1.43, 1.50; substitute `Space Mono`.

## Spacing / shape
- Section Gap: `80px`
- Card Padding: `40px`
- Element Gap: `8px`
- Radius: `cards: 16px, images: 16px, buttons: 8px`

## Surface cues
- **Canvas Parchment** `#e5e7eb`: Base page background, light and airy foundation.
- **Wet Sand** `#e1d3c7`: Subtle background for specific content sections, providing a slight warmth and visual rhythm.
- **Sage Dark** `#3d3b2f`: Elevated card surfaces, creating a heavy, grounded visual block for key information.
- **Onyx Card** `#1d1d1b`: Deepest card background, used for maximum contrast against white text in specific contexts.

## Component cues
- **Ghost Navigation Link**: Primary navigation links and subtle inline calls to action.
- **Standard Button**: General action buttons, such as 'Read More' or 'Learn More'.
- **Dark Card Button**: Buttons within Sage Dark colored cards, offering a distinct visual cue.
- **Onyx Card Button**: Buttons within Onyx Card colored cards, ensuring visibility.
- **Card Surface - Default**: Generic display panels for content, often used without internal padding for media.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
