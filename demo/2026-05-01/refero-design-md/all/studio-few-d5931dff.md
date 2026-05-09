# Studio Few - Refero Design MD

- Source: https://styles.refero.design/style/d5931dff-2ae3-44c7-b76f-9e5936f90611
- Original site: https://studiofew.com
- Theme: `light`
- Industry: `design`
- Recommended fit: **Design reference / webapp exploration**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Gallery of Type on White Canvas

## Apply to
- General webapp UI exploration
- Demo cards and catalog surfaces
- Future admin/subscriber UI references

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Midnight Black | `#000000` | neutral | Primary text or dark surface |
| Subtle Gray | `#b7b7b7` | neutral | Border, muted text, or supporting surface |
| Anchor Gray | `#333333` | neutral | Primary text or dark surface |
| Faded Gray | `#858585` | neutral | Border, muted text, or supporting surface |

```css
:root {
  --ref-canvas-white: #ffffff;
  --ref-midnight-black: #000000;
  --ref-subtle-gray: #b7b7b7;
  --ref-anchor-gray: #333333;
  --ref-faded-gray: #858585;
}
```

## Typography direction
- **SterlingVF**: 300, 400, 500, 12px, 14px, 158px, 1.00, 1.20, 1.25, 1.33, 1.43, 1.50, 1.57, 1.60, 1.71, 1.75, 1.86, 2.00; substitute `Inter`.
- **Formative**: 400, 14px, 158px, 1.00; substitute `Bebas Neue`.
- **Voyager**: 400, 14px, 158px, 0.70, 1.00; substitute `Space Mono`.

## Spacing / shape
- Section Gap: `64px`
- Card Padding: `24px`
- Element Gap: `16px`
- Radius: `links: 6px, buttons: 6px, general: 2px`

## Surface cues
- **Canvas White** `#ffffff`: Primary page background and default UI surface, providing a clean, expansive foundation.

## Component cues
- **Primary Filled Button**: Main call-to-action button, indicating primary actions.
- **Navigation Link**: Header navigation items and inline links.
- **Input Field**: Text input areas for filtering or data entry.
- **Type Specimen Panel**: Container for individual typeface demonstrations.
- **Ghost Button**: Secondary action or trial options.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
