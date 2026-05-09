# Brand - Refero Design MD

- Source: https://styles.refero.design/style/f6fbc2fb-ea5d-44cc-a37d-d7896005acbd
- Original site: https://brand.dropbox.com
- Theme: `light`
- Industry: `design`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Shifting color block canvas

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Primary Text | `#1e1919` | neutral | Primary text or dark surface |
| Subtle Text | `#736c64` | neutral | Border, muted text, or supporting surface |
| Ocean Blue | `#0061fe` | brand | Action accent / signal color |
| Sky Blue | `#5f9dff` | brand | Action accent / signal color |
| Coral Red | `#ffafa5` | accent | Action accent / signal color |
| Spice Orange | `#6d2e09` | accent | Action accent / signal color |
| Teal Ink | `#055463` | accent | Action accent / signal color |
| Goldenrod | `#684505` | accent | Action accent / signal color |
| Indigo Magenta | `#682760` | accent | Action accent / signal color |

```css
:root {
  --ref-canvas-white: #ffffff;
  --ref-primary-text: #1e1919;
  --ref-subtle-text: #736c64;
  --ref-ocean-blue: #0061fe;
  --ref-sky-blue: #5f9dff;
  --ref-coral-red: #ffafa5;
  --ref-spice-orange: #6d2e09;
  --ref-teal-ink: #055463;
}
```

## Typography direction
- **Atlasgrotesk Web**: 400, 500, 12px, 14px, 1.43, 1.57, 1.67; substitute `Inter`.
- **Dbsharpgroteskvariable Vf**: 500, 700, 30px, 34px, 36px, 0.80, 1.20; substitute `Inter`.

## Spacing / shape
- Section Gap: `48px`
- Card Padding: `23px`
- Element Gap: `16px`
- Radius: `default: 8px`

## Component cues
- **Ghost Primary Button**: Outline button for primary actions

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
