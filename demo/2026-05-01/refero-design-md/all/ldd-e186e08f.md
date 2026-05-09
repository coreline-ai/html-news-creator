# ldd - Refero Design MD

- Source: https://styles.refero.design/style/e186e08f-e7ce-4b48-bd65-68bc300d2193
- Original site: https://lorenzodaldosso.it
- Theme: `light`
- Industry: `agency`
- Recommended fit: **Admin console / run monitor / developer tooling**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Pixelated Terminal on Cream Vellum. A minimalist, high-contrast digital aesthetic set against a soft, almost analog background.

## Apply to
- Admin run monitor and review states
- Compact evidence cards and source inspection panels
- Dark-mode operational dashboards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Cream Vellum | `#fffcf0` | neutral | Page background or card surface |
| Terminal Black | `#000000` | neutral | Primary text or dark surface |
| Deep Graphite | `#000310` | neutral | Primary text or dark surface |
| Sky Blue Indicator | `#007aff` | accent | Action accent / signal color |

```css
:root {
  --ref-cream-vellum: #fffcf0;
  --ref-terminal-black: #000000;
  --ref-deep-graphite: #000310;
  --ref-sky-blue-indicator: #007aff;
}
```

## Typography direction
- **Neue Montreal**: 400, 12px, 16px, 1.00; substitute `Inter`.
- **LDD**: 400, 135px, 1.00, 2.22; substitute `Press Start 2P`.

## Spacing / shape
- Section Gap: `48px`
- Element Gap: `15-35px`
- Radius: `all: 0px`

## Component cues
- **Scroll Progress Bar with CTA**: Reference component style.
- **Giant Pixel Counter Block**: Reference component style.
- **Marquee Services Strip**: Reference component style.
- **Header Navigation Item**: Navigation link
- **Giant Pixel Heading**: Headline

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
