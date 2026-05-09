# INFRINGE - Refero Design MD

- Source: https://styles.refero.design/style/36e7c3f9-b7cb-48a2-9695-db726e3dccdb
- Original site: https://www.infringe.com
- Theme: `light`
- Industry: `media`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Graphic Brutalism, Yellow Accent

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Midnight Black | `#000000` | neutral | Primary text or dark surface |
| Ash Gray | `#666666` | neutral | Border, muted text, or supporting surface |
| Vivid Marigold | `#ffff01` | accent | Action accent / signal color |

```css
:root {
  --ref-canvas-white: #ffffff;
  --ref-midnight-black: #000000;
  --ref-ash-gray: #666666;
  --ref-vivid-marigold: #ffff01;
}
```

## Typography direction
- **Archivo Black**: 100, 400, 700, 12px, 16px, 32px, 48px, 108px, 252px, 0.80, 1.00, 1.20; substitute `Anton`.

## Spacing / shape
- Section Gap: `32px`
- Card Padding: `16px`
- Element Gap: `16px`
- Radius: `none: 0px`

## Component cues
- **Mega Headline Block**: Primary page titles and section headers
- **Navigation Link**: Primary navigation and interactive menu items
- **Content Block Headline**: Headings within content sections
- **Muted Input Field**: Form input elements
- **Footer Link/Item**: Informational or secondary navigation links in the footer

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
