# Raad Cycling - Refero Design MD

- Source: https://styles.refero.design/style/a59e7f31-1fca-46c1-a6b0-8d1294b33a7c
- Original site: https://www.raad.cc
- Theme: `dark`
- Industry: `ecommerce`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Monochromatic Performance Canvas

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Ink | `#000000` | neutral | Primary text or dark surface |
| Arctic White | `#ffffff` | neutral | Page background or card surface |
| Ash Gray | `#333333` | neutral | Primary text or dark surface |
| Deep Gray | `#181818` | neutral | Primary text or dark surface |
| Muted Stone | `#666666` | neutral | Border, muted text, or supporting surface |

```css
:root {
  --ref-midnight-ink: #000000;
  --ref-arctic-white: #ffffff;
  --ref-ash-gray: #333333;
  --ref-deep-gray: #181818;
  --ref-muted-stone: #666666;
}
```

## Typography direction
- **Arial**: 400, 10px, 1.20; substitute `Arial`.
- **wfont_8b8bfe_cd7287b5071a4785a78bba57128a74e2**: 400, 12px, 13px, 16px, 18px, 50px, 54px, 1.00, 1.20, 1.40, 2.50; substitute `Montserrat`.

## Spacing / shape
- Section Gap: `120px`
- Card Padding: `20px`
- Element Gap: `20px`
- Radius: `pill: 100px, default: 0px`

## Component cues
- **Ghost Button**: Primary interactive element.
- **Main Navigation Link**: Top-level navigation items.
- **Product Category Link**: Product discovery links.
- **Body Text Block**: Informational paragraphs.
- **Footer Link**: Secondary navigation and legal links.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
