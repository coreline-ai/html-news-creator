# GUSTAVO Faria © - Refero Design MD

- Source: https://styles.refero.design/style/cd3546fc-b6d0-4ec9-8624-580549af347d
- Original site: https://gustavo.work
- Theme: `light`
- Industry: `design`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Minimalist gallery wall

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Ink Black | `#000000` | neutral | Primary text or dark surface |
| Graphite | `#282828` | neutral | Primary text or dark surface |
| Pale Ash | `#dcdcdc` | neutral | Page background or card surface |
| Blush Tone | `#efc4b2` | accent | Action accent / signal color |

```css
:root {
  --ref-canvas-white: #ffffff;
  --ref-ink-black: #000000;
  --ref-graphite: #282828;
  --ref-pale-ash: #dcdcdc;
  --ref-blush-tone: #efc4b2;
}
```

## Typography direction
- **custom_21879**: 400, 700, 12px, 142px, 0.81, 1.00, 1.17, 1.67.
- **custom_49610**: 400, 125px, 1.02.
- **-apple-system**: 400, 16px, 1.00; substitute `system-ui`.

## Spacing / shape
- Card Padding: `0px`
- Element Gap: `1px`
- Radius: `default: 0px`

## Component cues
- **Work Entry Link**: Interactive list item
- **Navigation Link**: Top-level navigation
- **Year Range Display**: Large decorative heading

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
