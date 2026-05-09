# Glein - Refero Design MD

- Source: https://styles.refero.design/style/2e4ce685-9f49-47a3-9577-bc4f196bd8f7
- Original site: https://glein.wien
- Theme: `light`
- Industry: `ecommerce`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Monochromatic architectural clarity: product as sculpture, framed by pure light and shadow.

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Raven Black | `#000000` | neutral | Primary text or dark surface |
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Warm Parchment | `#ebe6dc` | neutral | Page background or card surface |
| Muted Ash | `#b3b3b3` | neutral | Border, muted text, or supporting surface |

```css
:root {
  --ref-raven-black: #000000;
  --ref-canvas-white: #ffffff;
  --ref-warm-parchment: #ebe6dc;
  --ref-muted-ash: #b3b3b3;
}
```

## Typography direction
- **F-Grotesk**: 400, 13px, 15px, 20px, 30px, 111px, 1.00, 1.19, 1.20, 1.30; substitute `Inter`.
- **Maison-Neue-Mono**: 400, 13px, 15px, 20px, 1.00, 1.19, 1.20, 1.30; substitute `Space Mono`.

## Spacing / shape
- Section Gap: `42px`
- Card Padding: `24px`
- Element Gap: `13px`
- Radius: `default: 0px`

## Surface cues
- **Canvas White** `#ffffff`: Primary page background, default content surfaces
- **Warm Parchment** `#ebe6dc`: Secondary background, subtle content block separation, card backgrounds
- **Overlay/Active** `#000000`: Full-bleed hero sections, solid button fills, active states, text against light backgrounds

## Component cues
- **Filled Primary Button**: Primary Call to Action
- **Ghost Button**: Secondary Action
- **Navigation Link**: Primary Navigation
- **Callout Badge**: Informational Display
- **Cookie Consent Modal**: Privacy Notice

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
