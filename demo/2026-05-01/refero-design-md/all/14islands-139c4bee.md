# 14islands - Refero Design MD

- Source: https://styles.refero.design/style/139c4bee-396d-494c-baf0-fe211bf4928d
- Original site: https://14islands.com
- Theme: `light`
- Industry: `agency`
- Recommended fit: **Admin console / run monitor / developer tooling**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Editorial Minimal Canvas — Large, impactful typography commands attention against vast, light-gray expanses.

## Apply to
- Admin run monitor and review states
- Compact evidence cards and source inspection panels
- Dark-mode operational dashboards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#f2f2f2` | neutral | Page background or card surface |
| Deep Graphite | `#070707` | neutral | Primary text or dark surface |
| Off White | `#ffffff` | neutral | Page background or card surface |
| Soft Gray Highlight | `#a2a2a9` | neutral | Border, muted text, or supporting surface |
| Medium Gray Highlight | `#797979` | neutral | Border, muted text, or supporting surface |

```css
:root {
  --ref-canvas-white: #f2f2f2;
  --ref-deep-graphite: #070707;
  --ref-off-white: #ffffff;
  --ref-soft-gray-highlight: #a2a2a9;
  --ref-medium-gray-highlight: #797979;
}
```

## Typography direction
- **AftenScreen**: 400, 27px, 75px, 100px, 180px, 0.80, 1.00, 1.30; substitute `Open Sans, Montserrat`.
- **BentonSans**: 400, 12px, 16px, 1.20, 1.40; substitute `Inter, Lato`.

## Spacing / shape
- Card Padding: `21px`
- Radius: `default: 4.16667px`

## Component cues
- **Agency Intro Block**: Reference component style.
- **Work Grid — Project Cards**: Reference component style.
- **Section Heading — Lovable Products**: Reference component style.
- **Text Link - Primary**: Interactive element, navigation links, inline text links
- **Text Link - Secondary**: Interactive element, secondary navigation links, subtle buttons

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
