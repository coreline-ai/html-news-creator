# jun.works - Refero Design MD

- Source: https://styles.refero.design/style/02ba867b-49e3-4ab4-ad23-c30baf345078
- Original site: https://jun.works
- Theme: `light`
- Industry: `design`
- Recommended fit: **Research brief / AI trend page**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
typographic canvas, pill-outlined actions

## Apply to
- Research section pages and model-release briefs
- Lab-note style cards
- AI product/research trend summaries

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Ink Black | `#000000` | neutral | Primary text or dark surface |
| Muted Gray | `#cccccc` | neutral | Border, muted text, or supporting surface |

```css
:root {
  --ref-canvas-white: #ffffff;
  --ref-ink-black: #000000;
  --ref-muted-gray: #cccccc;
}
```

## Typography direction
- **Standard**: 400, 45px, 54px, 1.12, 1.15, 1.70; substitute `Arial Narrow`.
- **Times**: 400, 13px, 1.20; substitute `Times New Roman`.

## Spacing / shape
- Section Gap: `26px`
- Card Padding: `19px`
- Element Gap: `13px`
- Radius: `overall: 129.6px`

## Component cues
- **Pill Outline Button**: Primary interactive element for navigation and calls to action.
- **Section Heading Tag**: Distinctive visual tags for section titles like 'Service' or 'Recognition'.
- **Navigation Link**: Top-level navigation items.
- **Body Text Block**: General descriptive text and paragraphs.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
