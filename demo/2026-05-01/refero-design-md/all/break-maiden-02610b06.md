# Break Maiden - Refero Design MD

- Source: https://styles.refero.design/style/02610b06-d16e-47bd-a1ea-18979a9ed4f5
- Original site: https://www.breakmaiden.co
- Theme: `dark`
- Industry: `agency`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
High-contrast cinematic dark

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Canvas | `#000000` | neutral | Primary text or dark surface |
| Ghostly White | `#ffffff` | neutral | Page background or card surface |
| Muted Stone | `#8e8e8e` | neutral | Border, muted text, or supporting surface |

```css
:root {
  --ref-midnight-canvas: #000000;
  --ref-ghostly-white: #ffffff;
  --ref-muted-stone: #8e8e8e;
}
```

## Typography direction
- **Martin**: 400, 153px; substitute `Anton`.
- **Helvetica Neue**: 400, 500, 25px, 1.00; substitute `Arial`.
- **America**: 400, 19px, 22px, 1.00, 1.25, 1.50; substitute `Open Sans`.

## Spacing / shape
- Section Gap: `43px`
- Card Padding: `0px`
- Element Gap: `18px`
- Radius: `none: 0px`

## Component cues
- **Primary Ghost Button**: Subtle interactive element for primary actions.
- **Navigation Link**: Top-level navigation items.
- **Product Grid Card**: Container for showcasing product imagery.
- **Hero Headline**: Dominant text element at the top of the page.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
