# BelArosa Chalet - Refero Design MD

- Source: https://styles.refero.design/style/46c8dbc5-47c8-4796-b94c-5e46dcda3532
- Original site: https://www.belarosa-chalet.ch
- Theme: `light`
- Industry: `agency`
- Recommended fit: **Research brief / AI trend page**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Alpine Chalet Refinement: warm, textural, and quietly luxurious.

## Apply to
- Research section pages and model-release briefs
- Lab-note style cards
- AI product/research trend summaries

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Chalet Teal | `#193741` | brand | Action accent / signal color |
| Deep Teal | `#1d414d` | brand | Action accent / signal color |
| Alpine Gold | `#eac486` | accent | Action accent / signal color |
| Paper White | `#ffffff` | neutral | Page background or card surface |
| Warm Linen | `#ebe7e1` | neutral | Page background or card surface |
| Muted Stone | `#8c9ba0` | neutral | Border, muted text, or supporting surface |
| Rich Black | `#000000` | neutral | Primary text or dark surface |

```css
:root {
  --ref-chalet-teal: #193741;
  --ref-deep-teal: #1d414d;
  --ref-alpine-gold: #eac486;
  --ref-paper-white: #ffffff;
  --ref-warm-linen: #ebe7e1;
  --ref-muted-stone: #8c9ba0;
  --ref-rich-black: #000000;
}
```

## Typography direction
- **ITC Giovanni Std**: 700, 16px, 18px, 28px, 48px, 64px, 1.10, 1.20, 1.30, 1.40; substitute `Georgia, Playfair Display`.
- **Avenir LT Pro**: 400, 12px, 14px, 16px, 20px, 24px, 28px, 40px, 1.00, 1.20, 1.25, 1.40, 1.43, 1.50, 1.71; substitute `Open Sans, Lato`.

## Spacing / shape
- Section Gap: `48px`
- Card Padding: `16px`
- Element Gap: `24px`
- Radius: `links: 12px, buttons: 80px`

## Surface cues
- **Paper White Canvas** `#ffffff`: Primary page background for most light-themed sections.
- **Warm Linen Surface** `#ebe7e1`: Secondary background for alternating sections and subtle card surfaces in light contexts.
- **Chalet Teal Deep Surface** `#193741`: Dark background for feature sections, footer, and navigation in header, providing contrast and visual depth.

## Component cues
- **Outlined Button**: Primary action button with a luxury aesthetic
- **Text Link**: Navigation and secondary calls to action
- **Circular Card Accent**: Decorative card element for emphasis
- **Input Field (Text)**: Form input elements

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
