# B—Line - Refero Design MD

- Source: https://styles.refero.design/style/3b9ed801-511c-48b6-b516-68b1aa8a36ea
- Original site: https://www.b-line.it
- Theme: `light`
- Industry: `design`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Gallery Grid Aesthetics

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Ink Black | `#000000` | neutral | Primary text or dark surface |
| Muted Stone | `#595959` | neutral | Border, muted text, or supporting surface |

```css
:root {
  --ref-canvas-white: #ffffff;
  --ref-ink-black: #000000;
  --ref-muted-stone: #595959;
}
```

## Typography direction
- **HELVMONO**: 400, 14px, 1.00, 1.30; substitute `Space Mono`.
- **helvetica-bold**: 400, 12px, 1.13, 2.50; substitute `Helvetica Neue`.
- **-apple-system**: 700, 14px, 2.71.

## Spacing / shape
- Section Gap: `40px`
- Card Padding: `4px`
- Element Gap: `5px`
- Radius: `cards: 0px, links: 14.4px, inputs: 0px, buttons: 4px`

## Component cues
- **Primary Ghost Button**: Action button with minimal styling.
- **Product Display Card**: Container for product imagery and titles in a grid layout.
- **Navigation Link**: Interactive text links in header and footer.
- **Text Input (minimal)**: Basic text input field.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
