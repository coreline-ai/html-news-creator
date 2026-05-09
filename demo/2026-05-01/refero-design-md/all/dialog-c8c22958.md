# Dialog - Refero Design MD

- Source: https://styles.refero.design/style/c8c22958-ec50-47f1-aedc-a131d7aeb442
- Original site: https://askdialog.com
- Theme: `light`
- Industry: `ecommerce`
- Recommended fit: **Admin console / run monitor / developer tooling**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Neutral showroom with one warm price tag. Every surface is a different tone of off-white; the orange CTA is the only color in the room.

## Apply to
- Admin run monitor and review states
- Compact evidence cards and source inspection panels
- Dark-mode operational dashboards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Tangerine Tag | `#f69251` | brand | Action accent / signal color |
| Midnight Ink | `#181825` | neutral | Primary text or dark surface |
| Graphite | `#484758` | neutral | Border, muted text, or supporting surface |
| Deep Slate | `#242433` | neutral | Primary text or dark surface |
| Carbon | `#000000` | neutral | Primary text or dark surface |
| Stone | `#636363` | neutral | Border, muted text, or supporting surface |
| Pebble | `#949494` | neutral | Border, muted text, or supporting surface |
| Ash | `#8b8b8b` | neutral | Border, muted text, or supporting surface |
| Fog | `#f7f7f7` | neutral | Page background or card surface |
| Snow | `#ffffff` | neutral | Page background or card surface |

```css
:root {
  --ref-tangerine-tag: #f69251;
  --ref-midnight-ink: #181825;
  --ref-graphite: #484758;
  --ref-deep-slate: #242433;
  --ref-carbon: #000000;
  --ref-stone: #636363;
  --ref-pebble: #949494;
  --ref-ash: #8b8b8b;
}
```

## Typography direction
- **PP Radio Grotesk Light**: 400, 32px, 39px, 50px, 70px, 1.15–1.30; substitute `Satoshi Light, DM Sans Light`.
- **Inter**: 400, 500, 12px, 13px, 14px, 16px, 18px, 24px, 1.20–1.70; substitute `Inter (already Google-available)`.
- **Inter Variable**: 400, 15px, 1.00; substitute `Inter`.

## Spacing / shape
- Section Gap: `80-120px`
- Card Padding: `24px`
- Element Gap: `8-16px`
- Page Max Width: `1200px`
- Radius: `cards: 24px, small: 8px, badges: 100px, inputs: 0px, buttons: 28px, overlays: 32px, cardInner: 12px`

## Surface cues
- **Page Canvas** `#f7f7f7`: Full-bleed page background — the base of the entire composition
- **Card Surface** `#ffffff`: Testimonial cards, feature cards, browser mockup frames
- **Dark Card** `#242433`: Feature section dark-mode panels, contrast sections

## Component cues
- **Email Input + CTA Inline Form with Star Ratings**: Reference component style.
- **Testimonial Card**: Reference component style.
- **Product Screenshot Browser Frame**: Reference component style.
- **Primary CTA Button (Orange Pill)**: Hero and nav primary action — 'Book a demo'
- **Ghost CTA Button (White Pill)**: Secondary actions on dark or image-backed surfaces

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
