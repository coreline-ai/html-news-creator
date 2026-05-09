# Yuga - Refero Design MD

- Source: https://styles.refero.design/style/5f2dd17d-72e6-4aa4-88e6-6be9e41299ab
- Original site: https://yuga.com
- Theme: `dark`
- Industry: `crypto`
- Recommended fit: **Admin console / run monitor / developer tooling**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Blocky digital canvas

## Apply to
- Admin run monitor and review states
- Compact evidence cards and source inspection panels
- Dark-mode operational dashboards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Void | `#000000` | neutral | Primary text or dark surface |
| Cloud Canvas | `#ffffff` | neutral | Page background or card surface |
| Digital Gray | `#131313` | neutral | Primary text or dark surface |
| Lime Glow | `#d3de5d` | accent | Action accent / signal color |

```css
:root {
  --ref-midnight-void: #000000;
  --ref-cloud-canvas: #ffffff;
  --ref-digital-gray: #131313;
  --ref-lime-glow: #d3de5d;
}
```

## Typography direction
- **AK Monument Grotesk**: 200, 400, 700, 800, 14px, 16px, 24px, 26px, 32px, 52px, 102px, 160px, 0.78, 0.82, 0.83, 0.90, 0.94, 1.00, 1.10; substitute `Monument Extended or Space Grotesk`.

## Spacing / shape
- Section Gap: `40px`
- Card Padding: `20px`
- Element Gap: `15px`
- Radius: `cards: 30px, links: 40px, buttons: 90px, elements: 30px`

## Component cues
- **Primary Filled Button**: Call to action button
- **Navigation Link**: Primary navigation item
- **Product Display Card**: Container for product imagery or information
- **Footer Link**: Secondary navigation or informational link

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
