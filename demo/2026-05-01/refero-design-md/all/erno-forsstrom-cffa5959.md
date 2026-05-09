# Erno Forsström - Refero Design MD

- Source: https://styles.refero.design/style/cffa5959-4283-41d2-ad11-bada2d731419
- Original site: https://erno.works
- Theme: `light`
- Industry: `design`
- Recommended fit: **Research brief / AI trend page**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Gallery exhibition, typographic precision

## Apply to
- Research section pages and model-release briefs
- Lab-note style cards
- AI product/research trend summaries

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Lead Graphite | `#202020` | neutral | Primary text or dark surface |
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Whisper Gray | `#cdcecf` | neutral | Border, muted text, or supporting surface |

```css
:root {
  --ref-lead-graphite: #202020;
  --ref-canvas-white: #ffffff;
  --ref-whisper-gray: #cdcecf;
}
```

## Typography direction
- **Nb akademie pro book webfont**: 400, 21px, 43px, 58px, 0.93, 1.00, 1.10, 1.33; substitute `Inter`.

## Spacing / shape
- Section Gap: `31px`
- Card Padding: `18px`
- Element Gap: `18px`
- Radius: `none: 0px`

## Component cues
- **Minimal Navigation Link**: Text link for primary navigation (header, footers)
- **Featured Project Card**: Showcase individual portfolio projects with a large image and descriptive text.
- **Category Heading**: Divides content sections

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
