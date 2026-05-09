# Co Projects - Refero Design MD

- Source: https://styles.refero.design/style/5c9743ad-fe33-4d21-9185-db012f6f96c7
- Original site: https://co-projects.xyz
- Theme: `light`
- Industry: `agency`
- Recommended fit: **Design reference / webapp exploration**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Gallery Wall Typography - Massive typographic elements dominate minimal structure, creating visual weight and focus.

## Apply to
- General webapp UI exploration
- Demo cards and catalog surfaces
- Future admin/subscriber UI references

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Coal Black | `#000000` | neutral | Primary text or dark surface |
| Borderline Gray | `#e5e7eb` | neutral | Page background or card surface |

```css
:root {
  --ref-canvas-white: #ffffff;
  --ref-coal-black: #000000;
  --ref-borderline-gray: #e5e7eb;
}
```

## Typography direction
- **Alpha**: 400, 16px, 29px, 60px, 1.00, 1.10, 1.50; substitute `Inter`.
- **Takt**: 400, 16px, 36px, 1.10, 1.11; substitute `Open Sans`.

## Spacing / shape
- Section Gap: `96px`
- Card Padding: `12px`
- Element Gap: `4px`
- Radius: `default: 0px`

## Component cues
- **Navigation Bar**: Reference component style.
- **Display Logo Mark — Co Graphic**: Reference component style.
- **Project Card — Bordered Content Block**: Reference component style.
- **Body Text**: General content text
- **Bordered Element**: Implicit container or divider

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
