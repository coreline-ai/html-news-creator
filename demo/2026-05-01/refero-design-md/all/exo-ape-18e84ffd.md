# Exo Ape - Refero Design MD

- Source: https://styles.refero.design/style/18e84ffd-4a5d-453d-aeff-dae2847aa3c9
- Original site: https://www.exoape.com
- Theme: `light`
- Industry: `agency`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Architectural grandiosity on textured paper.

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Carbon | `#0d0e13` | neutral | Primary text or dark surface |
| Paper White | `#ffffff` | neutral | Page background or card surface |
| Plaster | `#e4e0db` | neutral | Page background or card surface |
| Sandstone | `#e0ccbb` | neutral | Border, muted text, or supporting surface |
| Parchment | `#e6d7ca` | neutral | Page background or card surface |
| Ink Black | `#070707` | neutral | Primary text or dark surface |
| Slate | `#6e6e71` | neutral | Border, muted text, or supporting surface |
| Stone Gray | `#9e9fa1` | neutral | Border, muted text, or supporting surface |

```css
:root {
  --ref-carbon: #0d0e13;
  --ref-paper-white: #ffffff;
  --ref-plaster: #e4e0db;
  --ref-sandstone: #e0ccbb;
  --ref-parchment: #e6d7ca;
  --ref-ink-black: #070707;
  --ref-slate: #6e6e71;
  --ref-stone-gray: #9e9fa1;
}
```

## Typography direction
- **Lausanne-400**: 400, 14px, 2.64.
- **Lausanne**: 400, 14px, 16px, 24px, 144px, 250px, 0.73, 0.76, 0.90, 1.00, 1.33, 1.50, 1.88; substitute `Inter, Montserrat`.
- **Times**: 400, 16px, 1.20, 2.00; substitute `serif system font`.

## Spacing / shape
- Section Gap: `60px`
- Card Padding: `15px`
- Element Gap: `13px`
- Page Max Width: `1200px`

## Surface cues
- **Paper White** `#ffffff`: Primary page background, base layer.
- **Plaster** `#e4e0db`: Secondary background, often for slightly recessed content blocks.
- **Sandstone Footer** `#e0ccbb`: Distinct background for the footer, providing a grounded contrast.
- **Ink Black Surface** `#070707`: Darkest background surface, providing ultimate contrast for footer text.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
