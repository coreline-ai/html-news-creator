# Perplexity AI - Refero Design MD

- Source: https://styles.refero.design/style/e9fff87a-63ce-4c19-840f-98233db62f58
- Original site: https://www.perplexity.ai
- Theme: `light`
- Industry: `ai`
- Recommended fit: **Research brief / AI trend page**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Digital Parchment, Subtle Authority

## Apply to
- Research section pages and model-release briefs
- Lab-note style cards
- AI product/research trend summaries

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas Creme | `#faf8f5` | neutral | Page background or card surface |
| Text Charcoal | `#272510` | neutral | Primary text or dark surface |
| Accent Teal | `#016a71` | brand | Action accent / signal color |
| Secondary Text | `#72706b` | neutral | Border, muted text, or supporting surface |
| Border Slate | `#d1d1cd` | neutral | Border, muted text, or supporting surface |
| Subtle Gray | `#92918b` | neutral | Border, muted text, or supporting surface |
| Deep Black | `#000000` | neutral | Primary text or dark surface |

```css
:root {
  --ref-canvas-creme: #faf8f5;
  --ref-text-charcoal: #272510;
  --ref-accent-teal: #016a71;
  --ref-secondary-text: #72706b;
  --ref-border-slate: #d1d1cd;
  --ref-subtle-gray: #92918b;
  --ref-deep-black: #000000;
}
```

## Typography direction
- **pplxSans**: 400, 500, 12px, 14px, 16px, 1.25, 1.33, 1.43, 1.50, 2.00; substitute `Inter`.

## Spacing / shape
- Section Gap: `32px`
- Card Padding: `12px`
- Element Gap: `8px`
- Radius: `pill: 9999px, cards: 16px, buttons: 6px, inputField: 12px`

## Surface cues
- **Page Canvas** `#faf8f5`: The foundational background for the entire application, providing a soft, consistent base.
- **Component Surface** `#faf8f5`: Used for cards and other primary content blocks, subtly elevated with a shadow.
- **Interactive Accent** `#016a71`: Applied to active navigation items, serving as an indicator for selected states.
- **Interactive Fill** `#27251`: Used for filled icon buttons, providing a clear visual for direct actions.

## Component cues
- **Primary Navigation Item**: Active state navigation item
- **Text Input Field**: User input area
- **Search Query Pill**: Interactive tag within input
- **Icon Button (Default)**: Subtle interactive icon
- **Call to Action (Ghost)**: Secondary action or link

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
