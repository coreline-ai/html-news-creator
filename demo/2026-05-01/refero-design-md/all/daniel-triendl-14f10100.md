# Daniel Triendl - Refero Design MD

- Source: https://styles.refero.design/style/14f10100-a102-427a-88d1-7cc80cbb332d
- Original site: https://www.danieltriendl.com
- Theme: `light`
- Industry: `design`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Gallery wall of stark contrasts

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Midnight Black | `#000000` | neutral | Primary text or dark surface |
| Soft Gray | `#f2f2f2` | neutral | Page background or card surface |
| Muted Ash | `#9b9b9b` | neutral | Border, muted text, or supporting surface |

```css
:root {
  --ref-canvas-white: #ffffff;
  --ref-midnight-black: #000000;
  --ref-soft-gray: #f2f2f2;
  --ref-muted-ash: #9b9b9b;
}
```

## Typography direction
- **Times**: 400, 14px, 1.20, 1.21; substitute `serif`.
- **UniversalSans**: 400, 14px, 1.20, 1.21; substitute `Arial, sans-serif`.
- **UniversalSans**: 500, 10px, 14px, 1.00, 1.21; substitute `Arial, sans-serif`.

## Spacing / shape
- Card Padding: `16px`
- Element Gap: `6px`
- Radius: `large: 16px, small: 4px, default: 10px, navigation: 48px`

## Component cues
- **Gallery Item Card**: Container for individual artwork previews.
- **Ghost Button**: Interactive elements for navigation or secondary actions.
- **Navigation Link**: Primary navigation items.
- **Floating Action Button (FAB)**: Circular button for main actions on an artwork detail page (e.g. 'Work', 'About', 'Contact').

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
