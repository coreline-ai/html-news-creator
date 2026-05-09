# AngelList - Refero Design MD

- Source: https://styles.refero.design/style/c75603c7-492d-4c26-9744-9acc22fe6225
- Original site: https://www.angellist.com
- Theme: `dark`
- Industry: `fintech`
- Recommended fit: **Source ledger / evidence dashboard**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Midnight Ledger, luminous script.

## Apply to
- Source ledger, ranking, and verification screens
- Cluster evidence dashboards
- Dense data tables with clear hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Ink | `#001d21` | neutral | Primary text or dark surface |
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Ash Cloud | `#e1e3e3` | neutral | Page background or card surface |
| Smoke Gray | `#68706f` | neutral | Border, muted text, or supporting surface |
| Pale Stone | `#f1f3f2` | neutral | Page background or card surface |
| Charcoal Tint | `#002b31` | neutral | Primary text or dark surface |
| Silver Thread | `#ccd5d6` | neutral | Border, muted text, or supporting surface |
| Mint Glaze | `#e0fee6` | brand | Action accent / signal color |
| Verdant Mist | `#cdeed3` | brand | Action accent / signal color |
| Lavender Haze | `#cdcbff` | brand | Action accent / signal color |

```css
:root {
  --ref-midnight-ink: #001d21;
  --ref-canvas-white: #ffffff;
  --ref-ash-cloud: #e1e3e3;
  --ref-smoke-gray: #68706f;
  --ref-pale-stone: #f1f3f2;
  --ref-charcoal-tint: #002b31;
  --ref-silver-thread: #ccd5d6;
  --ref-mint-glaze: #e0fee6;
}
```

## Typography direction
- **angellist**: 400, 500, 600, 700, 11px, 12px, 13px, 14px, 16px, 18px, 90px, 216px, 0.90, 1.10, 1.20, 1.40, 1.45, 1.50, 1.60, 2.64; substitute `Inter, Arial, sans-serif`.
- **angellistDisplay**: 400, 28px, 38px, 60px, 90px, 112px, 216px, 0.90, 1.10, 1.15, 1.25, 1.30; substitute `Inter, Arial, sans-serif`.

## Spacing / shape
- Section Gap: `48px`
- Card Padding: `16px`
- Element Gap: `4px`
- Radius: `cards: 12px, buttons: 9999px, default: 4px`

## Surface cues
- **Midnight Ink Canvas** `#001d21`: Primary page background, providing a deep, consistent base.
- **Charcoal Tint Card** `#002b31`: Elevated cards and contextual content containers, offering a subtle visual lift from the canvas.
- **Pale Stone Accent** `#f1f3f2`: Used for navigation elements or subtle ghost button backgrounds, providing a lighter contrast without being stark white.
- **Canvas White Overlay** `#ffffff`: Rarely used on body elements for high contrast sections or specific content framing, visible in footer/cookie consent.

## Component cues
- **Navigation Link (Active/Hover)**: Top navigation item, highlighted state
- **Primary Ghost Button**: Call to action, less prominent
- **Outlined Button**: Secondary action, distinctive outline
- **Primary Filled Button**: Primary call to action (e.g. 'Contact sales')
- **Card - Dark Surface**: Content container with elevated dark surface

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
