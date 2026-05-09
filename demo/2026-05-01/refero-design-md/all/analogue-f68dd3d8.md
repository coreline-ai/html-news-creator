# Analogue - Refero Design MD

- Source: https://styles.refero.design/style/f68dd3d8-e8fa-4d2c-8c59-28aba06c9d8a
- Original site: https://analogueagency.com
- Theme: `dark`
- Industry: `design`
- Recommended fit: **Admin console / run monitor / developer tooling**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Midnight data stream

## Apply to
- Admin run monitor and review states
- Compact evidence cards and source inspection panels
- Dark-mode operational dashboards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Deep Space | `#000000` | neutral | Primary text or dark surface |
| Ghostly Gray | `#ededed` | neutral | Page background or card surface |
| Shadow | `#1c1c1c` | neutral | Primary text or dark surface |
| Stone | `#b8b8b8` | neutral | Border, muted text, or supporting surface |
| Cloud | `#ffffff` | neutral | Page background or card surface |
| Ash | `#7a7a7a` | neutral | Border, muted text, or supporting surface |
| Horizon | `#a6a6a6` | neutral | Border, muted text, or supporting surface |

```css
:root {
  --ref-deep-space: #000000;
  --ref-ghostly-gray: #ededed;
  --ref-shadow: #1c1c1c;
  --ref-stone: #b8b8b8;
  --ref-cloud: #ffffff;
  --ref-ash: #7a7a7a;
  --ref-horizon: #a6a6a6;
}
```

## Typography direction
- **Graphik Medium**: 400, 500, 11px, 13px, 17px, 18px, 40px, 60px, 1.00, 1.05, 1.10, 1.18, 1.25, 1.30; substitute `system-ui`.
- **sans-serif**: 400, 12px, 1.20.
- **LCDDot TR Regular**: 400, 20px, 1.00; substitute `monospace`.

## Spacing / shape
- Section Gap: `40px`
- Card Padding: `20px`
- Element Gap: `10px`
- Radius: `pill: 1000px, badges: 100px, buttons: 13px, default: 10px`

## Component cues
- **Ghost Navigation Item**: Navigation links in the header
- **Text Link**: Inline textual hyperlinks
- **Hero Headline**: Primary heading in the hero section
- **Body Text**: General paragraph content
- **Navigation Bar**: Main top-level persistent navigation

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
