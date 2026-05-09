# Glossier - Refero Design MD

- Source: https://styles.refero.design/style/efd8dda0-b7dc-4b0b-b65f-348849d2cd65
- Original site: https://glossier.com
- Theme: `light`
- Industry: `ecommerce`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Photographic vibrancy on crisp white canvas. Imagine a brightly lit product shot, vibrant and rich, placed on a pristine white gallery wall.

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Ink | `#000000` | neutral | Primary text or dark surface |
| Snow | `#ffffff` | neutral | Page background or card surface |
| Ash | `#666666` | neutral | Border, muted text, or supporting surface |
| Fog | `#e8e8e8` | neutral | Page background or card surface |
| Whisper | `#f7f7f7` | neutral | Page background or card surface |
| Lemon Zest | `#fff116` | brand | Action accent / signal color |
| Twilight Indigo | `#0600ff` | accent | Action accent / signal color |

```css
:root {
  --ref-ink: #000000;
  --ref-snow: #ffffff;
  --ref-ash: #666666;
  --ref-fog: #e8e8e8;
  --ref-whisper: #f7f7f7;
  --ref-lemon-zest: #fff116;
  --ref-twilight-indigo: #0600ff;
}
```

## Typography direction
- **Apercu**: 400, 500, 700, 12px, 14px, 16px, 20px, 32px, 1.00, 1.09, 1.15, 1.17, 1.20, 1.23, 1.30, 1.40, 1.43, 1.46, 1.63, 1.67, 1.70; substitute `system-ui, sans-serif`.
- **Apercu Mono**: 400, 12px, 1.40; substitute `monospace`.
- **GTStandard-M**: 400, 16px, 1.50; substitute `system-ui, sans-serif`.

## Spacing / shape
- Section Gap: `40-80px`
- Card Padding: `0px`
- Element Gap: `8px`
- Radius: `all: 0px`

## Component cues
- **Product Cards with NEW Badge**: Reference component style.
- **Promo Announcement Banner**: Reference component style.
- **Hero Promo Card with CTA**: Reference component style.
- **Primary Action Button**: Main call-to-action
- **Secondary Action Button**: Supporting call-to-action

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
