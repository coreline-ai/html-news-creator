# Zoox - Refero Design MD

- Source: https://styles.refero.design/style/e85a82b1-c70e-42de-8c42-4bd95dd5e047
- Original site: https://zoox.com
- Theme: `light`
- Industry: `ai`
- Recommended fit: **Admin console / run monitor / developer tooling**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Muted, precise mobility.

## Apply to
- Admin run monitor and review states
- Compact evidence cards and source inspection panels
- Dark-mode operational dashboards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Ink | `#0d1212` | neutral | Primary text or dark surface |
| Cloud Canvas | `#ffffff` | neutral | Page background or card surface |
| Ash Gray | `#565959` | neutral | Border, muted text, or supporting surface |
| Slate Green | `#34484a` | neutral | Action accent / signal color |
| Pale Mint | `#d3e4df` | neutral | Page background or card surface |
| Fog | `#696969` | neutral | Border, muted text, or supporting surface |
| Stone Gray | `#7b8889` | neutral | Border, muted text, or supporting surface |
| Light Mist | `#9aa3a5` | neutral | Border, muted text, or supporting surface |
| Pale Sage | `#edf4f2` | neutral | Page background or card surface |
| Teal Accent | `#64d5b3` | brand | Action accent / signal color |

```css
:root {
  --ref-midnight-ink: #0d1212;
  --ref-cloud-canvas: #ffffff;
  --ref-ash-gray: #565959;
  --ref-slate-green: #34484a;
  --ref-pale-mint: #d3e4df;
  --ref-fog: #696969;
  --ref-stone-gray: #7b8889;
  --ref-light-mist: #9aa3a5;
}
```

## Typography direction
- **Gt Standard S**: 400, 500, 600, 700, 12px, 13px, 14px, 15px, 16px, 20px, 23px, 30px, 40px, 50px, 0.75, 1.00, 1.15, 1.20, 1.25, 1.28, 1.30, 1.40, 1.50, 1.88, 2.64; substitute `Inter`.
- **Gt Standard L**: 400, 28px, 36px, 56px, 120px, 1.10, 1.15, 1.20, 1.30; substitute `Outfit`.

## Spacing / shape
- Section Gap: `40px`
- Card Padding: `20px`
- Element Gap: `5px`
- Radius: `cards: 36px, links: 12px, badges: 20px, inputs: 18px, buttons: 16px, navigation: 16px`

## Surface cues
- **Page Canvas** `#d3e4df`: Primary page background, creating a soft, light base.
- **Base Card** `#ffffff`: Default card and input backgrounds, providing a clean, bright surface.
- **Elevated Pale Card** `#edf4f2`: Softly elevated card backgrounds, such as the banner for cookie policy, subtly distinct from the base canvas.
- **Slate Green Section** `#34484a`: Darker, contrasting section backgrounds, providing a visual anchor.
- **Midnight Ink Card** `#0d1212`: Deepest surface level, used for dark, immersive card backgrounds.

## Component cues
- **Ghost Nav Button**: Navigation and secondary actions
- **Primary Action Button**: Call to action
- **Outline Ghost Button**: Subtle secondary actions or interactive elements.
- **Neutral Card**: Content container
- **Elevated Card (Pale Mint)**: Prominent content container

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
