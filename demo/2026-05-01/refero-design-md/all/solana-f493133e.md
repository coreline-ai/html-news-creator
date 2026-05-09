# Solana - Refero Design MD

- Source: https://styles.refero.design/style/f493133e-e289-4fb1-9729-f611d9816aae
- Original site: https://solana.com
- Theme: `dark`
- Industry: `crypto`
- Recommended fit: **Admin console / run monitor / developer tooling**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Galactic Command Center. Surfaces are deep space, accents are cosmic signals.

## Apply to
- Admin run monitor and review states
- Compact evidence cards and source inspection panels
- Dark-mode operational dashboards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Deep Space | `#000000` | neutral | Primary text or dark surface |
| Dark Matter | `#121212` | neutral | Primary text or dark surface |
| Void Shadow | `#0d0c11` | neutral | Primary text or dark surface |
| Vapor Gray | `#ababba` | neutral | Border, muted text, or supporting surface |
| Polar White | `#ffffff` | neutral | Page background or card surface |
| Border Plasma | `#eaecf0` | neutral | Page background or card surface |
| Subtle Stone | `#848895` | neutral | Border, muted text, or supporting surface |
| Infrared Gradient | `#000000` | brand | Action accent / signal color |
| Cyber Lime | `#55e9ab` | accent | Action accent / signal color |
| Digital Violet | `#ca9ff5` | accent | Action accent / signal color |

```css
:root {
  --ref-deep-space: #000000;
  --ref-dark-matter: #121212;
  --ref-void-shadow: #0d0c11;
  --ref-vapor-gray: #ababba;
  --ref-polar-white: #ffffff;
  --ref-border-plasma: #eaecf0;
  --ref-subtle-stone: #848895;
  --ref-infrared-gradient: #000000;
}
```

## Typography direction
- **Diatype**: 300, 400, 500, 16px, 18px, 20px, 21px, 24px, 28px, 36px, 40px, 64px, 88px, 1.00, 1.13, 1.14, 1.20, 1.22, 1.31, 1.33, 1.40, 1.50, 1.56; substitute `Inter`.
- **DSemi**: 700, 12px, 14px, 1.14, 1.33; substitute `Roboto Slab`.

## Spacing / shape
- Card Padding: `32px`
- Element Gap: `4px`
- Radius: `cards: 12px, buttons: 9999px, containers: 12px, smallElements: 4px`

## Component cues
- **Promotion Card (Hackathon)**: Reference component style.
- **Event Cards — Meet Solana IRL**: Reference component style.
- **News Article Card — Latest on Solana**: Reference component style.
- **Primary Ghost Button**: Call to action, navigation items
- **Secondary Ghost Button**: Subtle actions, secondary navigation

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
