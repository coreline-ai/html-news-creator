# Orderful - Refero Design MD

- Source: https://styles.refero.design/style/d95a35c2-d3f7-49e7-9ba7-282d52d3211d
- Original site: https://www.orderful.com
- Theme: `light`
- Industry: `saas`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Precision on White Canvas

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas Fog | `#f5f5f5` | neutral | Page background or card surface |
| Surface Snow | `#ffffff` | neutral | Page background or card surface |
| Ink Black | `#000000` | neutral | Primary text or dark surface |
| Graphite Text | `#4a5565` | neutral | Border, muted text, or supporting surface |
| Slate Gray | `#364153` | neutral | Border, muted text, or supporting surface |
| Whisper Gray | `#99a1af` | neutral | Border, muted text, or supporting surface |
| Subdued Gray | `#676767` | neutral | Border, muted text, or supporting surface |
| Border Ash | `#d4d4d4` | neutral | Border, muted text, or supporting surface |
| Deep Shadow | `#1f1f1f` | neutral | Primary text or dark surface |
| Action Blaze | `#e42b0c` | brand | Action accent / signal color |

```css
:root {
  --ref-canvas-fog: #f5f5f5;
  --ref-surface-snow: #ffffff;
  --ref-ink-black: #000000;
  --ref-graphite-text: #4a5565;
  --ref-slate-gray: #364153;
  --ref-whisper-gray: #99a1af;
  --ref-subdued-gray: #676767;
  --ref-border-ash: #d4d4d4;
}
```

## Typography direction
- **telegraf**: 100, 300, 400, 500, 600, 700, 12px, 14px, 16px, 18px, 20px, 24px, 30px, 48px, 60px, 72px, 1.00, 1.20, 1.33, 1.38, 1.40, 1.43, 1.50, 1.56, 1.63; substitute `Montserrat, Raleway`.
- **modernGothic**: 300, 14px, 1.43; substitute `IBM Plex Sans Light`.

## Spacing / shape
- Section Gap: `40px`
- Card Padding: `16px`
- Element Gap: `16px`
- Page Max Width: `1440px`
- Radius: `all: 8px`

## Component cues
- **Primary Action Button**: CTA button
- **Secondary Action Button**: Secondary button
- **Ghost Button**: Tertiary button
- **Card - Default**: Content container
- **Card - Elevated**: Accentuated content container

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
