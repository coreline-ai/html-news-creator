# Minimal Collective - Refero Design MD

- Source: https://styles.refero.design/style/94c15607-2f19-4dc4-9aec-2b40f28b754f
- Original site: https://minimalcollective.digital
- Theme: `dark`
- Industry: `media`
- Recommended fit: **Research brief / AI trend page**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Gallery grit, monochromatic precision.

## Apply to
- Research section pages and model-release briefs
- Lab-note style cards
- AI product/research trend summaries

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Void Black | `#000000` | neutral | Primary text or dark surface |
| Graphite | `#5a5a5a` | neutral | Border, muted text, or supporting surface |
| Parchment White | `#ffffff` | neutral | Page background or card surface |

```css
:root {
  --ref-void-black: #000000;
  --ref-graphite: #5a5a5a;
  --ref-parchment-white: #ffffff;
}
```

## Typography direction
- **PolySans**: 400, 14px, 16px, 18px, 23px, 27px, 32px, 50px, 77px, 0.90, 1.00, 1.20, 1.43; substitute `Inter`.

## Spacing / shape
- Section Gap: `144px`
- Card Padding: `18px`
- Element Gap: `14px`
- Radius: `badges: 4.5px, default: 4.5px`

## Surface cues
- **Canvas** `#5a5a5a`: Base background for sections and content blocks, providing a subtle contrast to the deepest black.
- **Primary Surface** `#000000`: Dominant background for the page, cards, and interactive elements, serving as the main 'void'.

## Component cues
- **Header Navigation Link**: Primary navigation links
- **Main Heading**: Hero and major section titles
- **Project Card Link**: Interactive content blocks for projects/articles
- **Badge (Text Only)**: Categorization and metadata labels within content
- **Badge (Outlined)**: Categorization and metadata labels with visual distinction

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
