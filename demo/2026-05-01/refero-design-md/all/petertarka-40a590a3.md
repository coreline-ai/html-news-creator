# Petertarka - Refero Design MD

- Source: https://styles.refero.design/style/40a590a3-1f0d-41ab-9c39-30adf86dd400
- Original site: https://petertarka.com
- Theme: `light`
- Industry: `design`
- Recommended fit: **Admin console / run monitor / developer tooling**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Gray canvas, vivid art

## Apply to
- Admin run monitor and review states
- Compact evidence cards and source inspection panels
- Dark-mode operational dashboards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Phantom Ink | `#000000` | neutral | Primary text or dark surface |
| Fog Bound | `#d8d8d8` | neutral | Border, muted text, or supporting surface |
| Canvas Gray | `#f0f0f0` | neutral | Page background or card surface |
| Paper White | `#ffffff` | neutral | Page background or card surface |
| Sky Gradient | `#77c1e5` | accent | Action accent / signal color |

```css
:root {
  --ref-phantom-ink: #000000;
  --ref-fog-bound: #d8d8d8;
  --ref-canvas-gray: #f0f0f0;
  --ref-paper-white: #ffffff;
  --ref-sky-gradient: #77c1e5;
}
```

## Typography direction
- **GT America**: 200, 300, 400, 16px, 21px, 38px, 1.00, 1.31, 1.32, 2.37; substitute `Inter`.

## Spacing / shape
- Card Padding: `45px`
- Element Gap: `6px`
- Radius: `none: 0px`

## Component cues
- **Main Navigation Button**: Hamburger menu button for main navigation
- **Project Card**: Container for individual project showcases
- **Project Card - Transparent**: Alternative container for specific project showcases, overlays visual content

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
