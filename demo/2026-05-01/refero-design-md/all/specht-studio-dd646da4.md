# Specht Studio - Refero Design MD

- Source: https://styles.refero.design/style/dd646da4-36f5-42b1-83dd-6a1c90cf8983
- Original site: https://stephaniespecht.com
- Theme: `light`
- Industry: `design`
- Recommended fit: **Design reference / webapp exploration**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Gallery Grid Monochrome

## Apply to
- General webapp UI exploration
- Demo cards and catalog surfaces
- Future admin/subscriber UI references

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Black Ink | `#000000` | neutral | Primary text or dark surface |
| Midtone Gray | `#666666` | neutral | Border, muted text, or supporting surface |
| Canvas White | `#ffffff` | neutral | Page background or card surface |

```css
:root {
  --ref-black-ink: #000000;
  --ref-midtone-gray: #666666;
  --ref-canvas-white: #ffffff;
}
```

## Typography direction
- **Helvetica Neue**: 400, 15px, 16px, 25px, 1.00, 1.20, 1.40, 1.50; substitute `Arial`.

## Spacing / shape
- Section Gap: `67px`
- Card Padding: `24px`
- Element Gap: `10px`
- Radius: `default: 0px`

## Component cues
- **Navigation Link**: Primary site navigation items.
- **Image Grid Item**: Display individual portfolio pieces or art.
- **Project Title Link**: Headline for individual project entries on the grid.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
