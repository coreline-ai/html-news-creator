# Piet Oudolf - Refero Design MD

- Source: https://styles.refero.design/style/3cc1d30c-3b08-48af-bbf0-df195d77835f
- Original site: https://oudolf.com
- Theme: `light`
- Industry: `design`
- Recommended fit: **Research brief / AI trend page**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Typographic whisper on textured canvas

## Apply to
- Research section pages and model-release briefs
- Lab-note style cards
- AI product/research trend summaries

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Textured Gray | `#808080` | neutral | Action accent / signal color |
| Muted Gray | `#b3b3b3` | neutral | Border, muted text, or supporting surface |
| Outline Gray | `#999999` | neutral | Border, muted text, or supporting surface |
| Icon Black | `#000000` | neutral | Primary text or dark surface |

```css
:root {
  --ref-canvas-white: #ffffff;
  --ref-textured-gray: #808080;
  --ref-muted-gray: #b3b3b3;
  --ref-outline-gray: #999999;
  --ref-icon-black: #000000;
}
```

## Typography direction
- **UniversLTStd-Light**: 400, 12px, 15px, 1.60, 1.87, 2.33; substitute `Helvetica Neue Light`.
- **Maison Neue Book**: 300, 60px, 1.25; substitute `Inter Light`.

## Spacing / shape
- Section Gap: `40px`
- Card Padding: `21px`
- Element Gap: `6px`
- Radius: `none: 0px`

## Component cues
- **Header Navigation Link**: Interactive text link in the page header.
- **Main Project Text Link**: Primary interactive text links for project names.
- **Small Country Code Label**: Contextual label for project locations.
- **Footer Navigation Link**: Secondary navigation in the page footer.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
