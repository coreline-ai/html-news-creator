# Subframe - Refero Design MD

- Source: https://styles.refero.design/style/c65db621-7faa-45f3-8e30-dc3ef9ffe660
- Original site: https://www.subframe.com
- Theme: `light`
- Industry: `ai`
- Recommended fit: **Admin console / run monitor / developer tooling**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
engineered clarity on frosted glass. A clean, bright surface for complex tools.

## Apply to
- Admin run monitor and review states
- Compact evidence cards and source inspection panels
- Dark-mode operational dashboards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas Fog | `#e5e7eb` | neutral | Page background or card surface |
| Inkwell | `#242424` | neutral | Primary text or dark surface |
| Ghost White | `#fafafa` | neutral | Page background or card surface |
| Surface Frost | `#ededed` | neutral | Page background or card surface |
| Code Black | `#171717` | neutral | Primary text or dark surface |
| Muted Ash | `#a3a3a3` | neutral | Border, muted text, or supporting surface |
| Subtle Gray | `#bdbdbd` | neutral | Border, muted text, or supporting surface |
| Helper Gray | `#5c5c5c` | neutral | Border, muted text, or supporting surface |
| Whisper Gray | `#737373` | neutral | Border, muted text, or supporting surface |

```css
:root {
  --ref-canvas-fog: #e5e7eb;
  --ref-inkwell: #242424;
  --ref-ghost-white: #fafafa;
  --ref-surface-frost: #ededed;
  --ref-code-black: #171717;
  --ref-muted-ash: #a3a3a3;
  --ref-subtle-gray: #bdbdbd;
  --ref-helper-gray: #5c5c5c;
}
```

## Typography direction
- **Inter**: 500, 600, 700, 12px, 14px, 18px, 24px, 28px, 48px, 96px, 1.00, 1.13, 1.14, 1.17, 1.33, 1.43; substitute `system-ui`.
- **ui-monospace**: 500, 10px, 1.70; substitute `monospace`.
- **Fragment Mono**: 400, 18px, 1.33; substitute `monospace`.

## Spacing / shape
- Section Gap: `24-64px`
- Card Padding: `16px`
- Element Gap: `8px`
- Radius: `tags: 9999px, cards: 24px, buttons: 16px, navigation: 9999px`

## Surface cues
- **Canvas** `#fafafa`: Base background for sections and general page canvas, providing a bright, airy foundation.
- **Base Surface** `#e5e7eb`: Dominant background for the overall page, creating a slightly desaturated, muted base.
- **Card Surface** `#ededed`: Background for cards and elevated content blocks, providing a subtle visual distinction from the base page.

## Component cues
- **Filled Primary Button**: Main call to action button.
- **Outlined Secondary Button**: Secondary action button, less prominent than primary.
- **Subtle Interaction Button**: Ghost button with a light hover state.
- **Nav Button**: Navigation links styled as buttons.
- **Feature Card**: Container for showcasing product features or content blocks.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
