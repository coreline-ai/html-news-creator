# Hyper Tria - Refero Design MD

- Source: https://styles.refero.design/style/6665a3dd-606f-4fd1-80dd-a84e3b3a6226
- Original site: https://hypertria.com
- Theme: `light`
- Industry: `agency`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
monochromatic gallery, bold typography

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight | `#000000` | neutral | Primary text or dark surface |
| Canvas | `#ffffff` | neutral | Page background or card surface |
| Charcoal | `#666666` | neutral | Border, muted text, or supporting surface |
| Leaf Green | `#0fa64b` | brand | Action accent / signal color |
| Vivid Blue | `#007bff` | accent | Action accent / signal color |
| Accent Red | `#ee3a49` | accent | Action accent / signal color |

```css
:root {
  --ref-midnight: #000000;
  --ref-canvas: #ffffff;
  --ref-charcoal: #666666;
  --ref-leaf-green: #0fa64b;
  --ref-vivid-blue: #007bff;
  --ref-accent-red: #ee3a49;
}
```

## Typography direction
- **Aeonik**: 300, 400, 500, 13px, 14px, 19px, 20px, 27px, 30px, 35px, 75px, 90px, 0.90, 1.00, 1.11, 1.16, 1.45, 1.48, 1.70, 2.23; substitute `system-ui`.
- **-apple-system**: 400, 14px, 28px, 30px, 1.50, 1.70.

## Spacing / shape
- Radius: `default: 0px`

## Component cues
- **Outlined Navigation Link**: Primary navigation element
- **Text Link**: Standard interactive text link
- **Hero Headline**: Large, impactful display text
- **Section Subheading**: Secondary heading for content blocks
- **Image Outline Container**: Visual frame for images

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
