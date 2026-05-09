# Xbox.com - Refero Design MD

- Source: https://styles.refero.design/style/3792d0ca-6c74-4667-a64d-76efe9f87076
- Original site: https://xbox.com
- Theme: `light`
- Industry: `media`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Gaming console interface on a bright white canvas. Bold green accents against a stark white backdrop, with minimal rounded elements.

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Lumi Green | `#107c10` | brand | Action accent / signal color |
| Rich Meadow | `#054b16` | brand | Action accent / signal color |
| Electric Lime | `#9bf00b` | brand | Action accent / signal color |
| Cyber Yellow | `#ffd800` | accent | Action accent / signal color |
| Deep Space Blue | `#0066ff` | accent | Action accent / signal color |
| Absolute Zero | `#000000` | neutral | Primary text or dark surface |
| Snowfield White | `#ffffff` | neutral | Page background or card surface |
| Charcoal Depth | `#333333` | neutral | Primary text or dark surface |
| Whisper Gray | `#f2f2f2` | neutral | Page background or card surface |
| Dark Steel | `#616161` | neutral | Border, muted text, or supporting surface |

```css
:root {
  --ref-lumi-green: #107c10;
  --ref-rich-meadow: #054b16;
  --ref-electric-lime: #9bf00b;
  --ref-cyber-yellow: #ffd800;
  --ref-deep-space-blue: #0066ff;
  --ref-absolute-zero: #000000;
  --ref-snowfield-white: #ffffff;
  --ref-charcoal-depth: #333333;
}
```

## Typography direction
- **Segoe UI**: 400, 600, 700, 11px, 13px, 15px, 16px, 20px, 24px, 46px, 1.20, 1.22, 1.25, 1.33, 1.45, 1.50, 2.27; substitute `system-ui, sans-serif`.
- **SegoeProBlack**: 600, 900, 15px, 1.23, 1.30, 1.53; substitute `system-ui, sans-serif`.

## Spacing / shape
- Section Gap: `48-80px`
- Card Padding: `12px`
- Element Gap: `4-12px`
- Radius: `default: 0px`

## Component cues
- **Game Pass Promotion Banner**: Reference component style.
- **Xbox Category Navigation Bar**: Reference component style.
- **Seasonal Sale Promo Card with Badge**: Reference component style.
- **Primary Navigation Link**: Top-level navigation items
- **Text Link Button**: Secondary action button, typically below a primary CTA

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
