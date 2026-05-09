# Mother Design - Refero Design MD

- Source: https://styles.refero.design/style/f40e6a6c-1704-407a-b21b-6141fb90adfe
- Original site: https://www.motherdesign.com
- Theme: `light`
- Industry: `design`
- Recommended fit: **Design reference / webapp exploration**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Architectural blueprint on white marble

## Apply to
- General webapp UI exploration
- Demo cards and catalog surfaces
- Future admin/subscriber UI references

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Ink Black | `#000000` | neutral | Primary text or dark surface |
| Smoke Grey | `#f4f4f4` | neutral | Page background or card surface |
| Muted Stone | `#808080` | neutral | Border, muted text, or supporting surface |
| Divider Line | `#262626` | neutral | Primary text or dark surface |

```css
:root {
  --ref-canvas-white: #ffffff;
  --ref-ink-black: #000000;
  --ref-smoke-grey: #f4f4f4;
  --ref-muted-stone: #808080;
  --ref-divider-line: #262626;
}
```

## Typography direction
- **Basis**: 400, 600, 10px, 14px, 16px, 48px, 60px, 110px, 226px, 1.00, 1.10, 1.20, 1.50; substitute `Inter`.
- **Basis Mono**: 400, 14px, 1.20; substitute `Space Mono`.
- **Times**: 400, 14px, 1.20; substitute `Georgia`.

## Spacing / shape
- Section Gap: `200px`
- Card Padding: `16px`
- Element Gap: `20px`
- Radius: `default: 0px`

## Surface cues
- **Canvas White** `#ffffff`: Primary page background, default surface for most content blocks.
- **Smoke Grey** `#f4f4f4`: Secondary background for specific hero sections or content areas to create subtle visual separation.

## Component cues
- **Navigation Link**: Text-based navigation item in header
- **Subtle Accent Button**: Button with background but no visible border or padding beyond text.
- **Ghost Bordered Button**: Transparent button with 1px black border. Used for generic interactive elements.
- **Muted Ghost Button**: Transparent button with grey text and border, indicating a less prominent action or disabled state.
- **Input Field**: Standard text input field

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
