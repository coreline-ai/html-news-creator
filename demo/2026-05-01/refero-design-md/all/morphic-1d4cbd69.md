# Morphic - Refero Design MD

- Source: https://styles.refero.design/style/1d4cbd69-ee0f-4f13-ba7d-14d3eaed7349
- Original site: https://morphic.com
- Theme: `dark`
- Industry: `ai`
- Recommended fit: **Admin console / run monitor / developer tooling**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Midnight Command Canvas — a high-contrast dark mode for creative focus.

## Apply to
- Admin run monitor and review states
- Compact evidence cards and source inspection panels
- Dark-mode operational dashboards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Absolute Zero | `#0075ff` | brand | Action accent / signal color |
| Ebony Canvas | `#000000` | neutral | Primary text or dark surface |
| Nightfall Gray | `#212121` | neutral | Primary text or dark surface |
| Charcoal Surface | `#292929` | neutral | Primary text or dark surface |
| Deep Graphite | `#333333` | neutral | Primary text or dark surface |
| Cloud White | `#ffffff` | neutral | Page background or card surface |
| Light Mist | `#f5f5f5` | neutral | Page background or card surface |
| Outline Haze | `#e5e7eb` | neutral | Page background or card surface |
| Muted Silver | `#999999` | neutral | Border, muted text, or supporting surface |
| Subtle Gray | `#737373` | neutral | Border, muted text, or supporting surface |

```css
:root {
  --ref-absolute-zero: #0075ff;
  --ref-ebony-canvas: #000000;
  --ref-nightfall-gray: #212121;
  --ref-charcoal-surface: #292929;
  --ref-deep-graphite: #333333;
  --ref-cloud-white: #ffffff;
  --ref-light-mist: #f5f5f5;
  --ref-outline-haze: #e5e7eb;
}
```

## Typography direction
- **Inter**: 400, 500, 600, 700, 10px, 12px, 14px, 16px, 18px, 20px, 40px, 52px, 1.00, 1.15, 1.17, 1.20, 1.29, 1.33, 1.38, 1.40, 1.44, 1.48, 1.50; substitute `system-ui, sans-serif`.

## Spacing / shape
- Section Gap: `96px`
- Card Padding: `12px`
- Element Gap: `8px`
- Radius: `pill: 100px, cards: 10px, buttons: 7px, heroCards: 32px, largeElements: 16px, superLargeElements: 24px`

## Component cues
- **Primary Action Button**: Filled button for main calls to action.
- **Secondary Ghost Button**: Outline button for secondary actions, often in groups with a primary button.
- **Muted Ghost Button**: Low-prominence buttons in interface sections, such as action bars or content filters.
- **Card without Background**: Content card with no visible background, relying on content for definition, often used for image grids.
- **Content Thumbnail Card**: Interactive cards displaying visual content, often with overlaid text.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
