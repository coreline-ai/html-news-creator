# Eduardo del Fraile - Refero Design MD

- Source: https://styles.refero.design/style/e11be5e4-cd8f-410e-bfe1-8763ed62fac3
- Original site: https://www.eduardodelfraile.com
- Theme: `dark`
- Industry: `design`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Gallery Black Canvas

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Void Black | `#000000` | neutral | Primary text or dark surface |
| Ghost White | `#ffffff` | neutral | Page background or card surface |
| Muted Gray | `#888888` | neutral | Border, muted text, or supporting surface |

```css
:root {
  --ref-void-black: #000000;
  --ref-ghost-white: #ffffff;
  --ref-muted-gray: #888888;
}
```

## Typography direction
- **AkzidenzGrotesk**: 400, 700, 14px, 15px, 20px, 21px, 1.30; substitute `Inter`.

## Spacing / shape
- Section Gap: `20px`
- Card Padding: `15px`
- Element Gap: `10px`

## Component cues
- **Header Navigation Link**: Primary navigation element
- **Brand Logo Text**: Site identifier
- **Muted Helper Text**: Contextual navigation or instructional text

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
