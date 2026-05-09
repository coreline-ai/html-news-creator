# Little Troop - Refero Design MD

- Source: https://styles.refero.design/style/bd62b51f-e1be-4e4f-b3d9-e9b91f817625
- Original site: https://littletroop.com
- Theme: `light`
- Industry: `design`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
monochrome playful sculpture

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Inkwell | `#000000` | neutral | Primary text or dark surface |
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Ocean Mist | `#8bc3bd` | accent | Action accent / signal color |
| Sunset Ember | `#e78f40` | accent | Action accent / signal color |

```css
:root {
  --ref-inkwell: #000000;
  --ref-canvas-white: #ffffff;
  --ref-ocean-mist: #8bc3bd;
  --ref-sunset-ember: #e78f40;
}
```

## Typography direction
- **Arial Narrow**: 400, 700, 14px, 16px, 0.86, 1.00, 1.14; substitute `Arial Condensed`.
- **Times Now**: 250, 76px, 0.79; substitute `Times New Roman`.

## Spacing / shape
- Section Gap: `100px`
- Card Padding: `20px`
- Element Gap: `20px`
- Radius: `shapes: 50px`

## Component cues
- **Navigation Link**: Header and footer navigation elements, work item links.
- **Project Index Card**: Container for individual work project previews.
- **Filter Toggle Button**: Used for filtering content, specifically on the Project Index.
- **Filter Checkbox**: Interactive element to select filter criteria.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
