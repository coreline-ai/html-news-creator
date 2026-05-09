# Resident - Refero Design MD

- Source: https://styles.refero.design/style/f451c085-f048-4c9c-ae3b-03acc88320ab
- Original site: https://resident.co.nz
- Theme: `light`
- Industry: `ecommerce`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Gallery Grid Serenity

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Ink Black | `#000000` | neutral | Primary text or dark surface |
| Muted Ash | `#979797` | neutral | Border, muted text, or supporting surface |
| Graphite | `#333333` | neutral | Primary text or dark surface |

```css
:root {
  --ref-canvas-white: #ffffff;
  --ref-ink-black: #000000;
  --ref-muted-ash: #979797;
  --ref-graphite: #333333;
}
```

## Typography direction
- **sans-serif**: 400, 12px, 14px, 1.20, 1.30; substitute `system-ui`.
- **MessinaSansWeb**: 400, 500, 14px, 18px, 19px, 23px, 27px, 1.00, 1.20, 1.29, 1.40; substitute `Helvetica Neue`.

## Spacing / shape
- Section Gap: `35px`
- Card Padding: `14px`
- Element Gap: `21px`
- Radius: `none: 0px, pill: 50%`

## Surface cues
- **Canvas White** `#ffffff`: Primary page background and default surface for all content areas.

## Component cues
- **Primary Navigation Link**: Top-level navigation items
- **Secondary Ghost Button**: Language switcher, login links
- **Outlined Pill Button**: Small interactive elements like language selection (e.g. 'EN/DE')
- **Product Grid Card**: Displaying product images and brief descriptions in a gallery format
- **Text Input Field**: Form fields like login, password

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
