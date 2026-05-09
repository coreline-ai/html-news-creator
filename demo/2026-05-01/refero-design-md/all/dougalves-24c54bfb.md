# Doug–Alves - Refero Design MD

- Source: https://styles.refero.design/style/24c54bfb-959d-4ca3-b274-e76ba823f3c0
- Original site: https://dougalves.work
- Theme: `light`
- Industry: `design`
- Recommended fit: **Design reference / webapp exploration**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Type-driven architectural blueprint

## Apply to
- General webapp UI exploration
- Demo cards and catalog surfaces
- Future admin/subscriber UI references

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Ink | `#282828` | neutral | Primary text or dark surface |
| Canvas | `#ffffff` | neutral | Page background or card surface |
| Deep Space | `#000000` | neutral | Primary text or dark surface |
| Charcoal | `#333333` | neutral | Primary text or dark surface |

```css
:root {
  --ref-ink: #282828;
  --ref-canvas: #ffffff;
  --ref-deep-space: #000000;
  --ref-charcoal: #333333;
}
```

## Typography direction
- **wtqc**: 300, 400, 12px, 28px, 72px, 197px, 1.00, 1.04, 1.29, 1.33; substitute `Arial, sans-serif`.
- **Inter**: 400, 18px, 0.89, 2.00; substitute `Helvetica Neue, Arial, sans-serif`.
- **-apple-system**: 400, 16px, 1.00; substitute `Arial, sans-serif`.

## Spacing / shape
- Section Gap: `64px`
- Card Padding: `0px`
- Element Gap: `24px`
- Radius: `other: 20px`

## Surface cues
- **Deep Space Canvas** `#000000`: Base background for hero sections and main navigation.
- **Ink Interface** `#282828`: Primary background for informational sections and interactive areas.
- **White Canvas** `#ffffff`: Background for detailed content pages and card-like containers.

## Component cues
- **Information Card Group**: Container for related text and links, often appearing in horizontal grids.
- **Text Link**: Interactive text elements.
- **Header Title**: Prominent page titles and section headers.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
