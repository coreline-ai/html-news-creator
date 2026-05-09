# Locomotive - Refero Design MD

- Source: https://styles.refero.design/style/131d07b0-f71b-4bd2-8046-f61485ed545c
- Original site: https://locomotive.ca
- Theme: `light`
- Industry: `agency`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
monochrome editorial manifesto – where stark blocks of content meet fluid, almost invisible interactions.

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Pitch Black | `#000000` | neutral | Primary text or dark surface |
| Canvas White | `#ffffff` | neutral | Page background or card surface |

```css
:root {
  --ref-pitch-black: #000000;
  --ref-canvas-white: #ffffff;
}
```

## Typography direction
- **HelveticaNowDisplay**: 400, 15px, 26px, 1.00, 1.20, 1.30; substitute `system-ui`.
- **LocomotiveNew**: 400, 70px, 110px, 1.00, 1.10; substitute `Georgia`.

## Spacing / shape
- Section Gap: `150px`
- Card Padding: `0px`
- Radius: `all: 0px`

## Component cues
- **Article List**: Reference component style.
- **Work Card — Seven Years**: Reference component style.
- **Hero Brand Badge**: Reference component style.
- **Navigation Link**: Interactive text link
- **Ghost Button**: Call to action with minimal visual footprint

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
