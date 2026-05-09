# destroytoday.com - Refero Design MD

- Source: https://styles.refero.design/style/b8fd5772-ac2b-4bfd-b5e5-d182261b09c5
- Original site: https://destroytoday.com
- Theme: `light`
- Industry: `design`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Crisp White Blueprint

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Ink Black | `#222222` | neutral | Primary text or dark surface |
| Ash Grey | `#d8d4cf` | neutral | Border, muted text, or supporting surface |
| True Blue | `#0000ff` | brand | Action accent / signal color |
| Deep Violet | `#555abf` | accent | Action accent / signal color |
| Path Gold | `#fcd669` | accent | Action accent / signal color |
| Path Orange | `#f79a59` | accent | Action accent / signal color |
| Shaded Navy | `#000080` | accent | Action accent / signal color |

```css
:root {
  --ref-canvas-white: #ffffff;
  --ref-ink-black: #222222;
  --ref-ash-grey: #d8d4cf;
  --ref-true-blue: #0000ff;
  --ref-deep-violet: #555abf;
  --ref-path-gold: #fcd669;
  --ref-path-orange: #f79a59;
  --ref-shaded-navy: #000080;
}
```

## Typography direction
- **-apple-system**: 400, 600, 700, 16px, 24px, 1.20, 1.40, 1.50; substitute `system-ui`.

## Spacing / shape
- Section Gap: `64px`
- Card Padding: `32px`
- Element Gap: `16px`
- Page Max Width: `1200px`
- Radius: `default: 0px`

## Component cues
- **Header Navigation Link**: Top-level navigation items
- **Primary Outlined Link**: Key interactive links and call-to-actions
- **Secondary Outlined Link**: Subtle interactive links within content
- **Page Title**: Main heading for content blocks
- **Body Paragraph**: Standard text content

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
