# mostlikely - Refero Design MD

- Source: https://styles.refero.design/style/4040f97b-42cf-49ef-ab2d-a77c00fe8285
- Original site: https://mostlikely.at
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

```css
:root {
  --ref-canvas-white: #ffffff;
  --ref-ink-black: #000000;
}
```

## Typography direction
- **Rondelle**: 400, 14px, 30px, 1.40; substitute `Arial`.

## Spacing / shape
- Section Gap: `70px`
- Card Padding: `20px`
- Element Gap: `10px`
- Radius: `default: 0px`

## Component cues
- **Primary Navigation Link**: Top navigation items
- **Header Bar**: Persistent top-level navigation and branding container
- **Interactive Box with Border**: Interactive elements, image containers, or content blocks

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
