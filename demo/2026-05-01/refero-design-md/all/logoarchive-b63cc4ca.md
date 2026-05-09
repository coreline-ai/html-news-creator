# LogoArchive - Refero Design MD

- Source: https://styles.refero.design/style/b63cc4ca-52c6-4b70-9a5a-cb04bae15edb
- Original site: https://www.logo-archive.org
- Theme: `dark`
- Industry: `design`
- Recommended fit: **Admin console / run monitor / developer tooling**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Deep Digital Archive.

## Apply to
- Admin run monitor and review states
- Compact evidence cards and source inspection panels
- Dark-mode operational dashboards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Ink | `#000000` | neutral | Primary text or dark surface |
| Carbon | `#18181b` | neutral | Primary text or dark surface |
| Steel Gray | `#27272a` | neutral | Primary text or dark surface |
| Ash Gray | `#343538` | neutral | Primary text or dark surface |
| Sky Haze | `#a8afb7` | neutral | Border, muted text, or supporting surface |
| Stone | `#8c8c8d` | neutral | Border, muted text, or supporting surface |
| Porcelain | `#ffffff` | neutral | Page background or card surface |
| Polar Mist | `#dadee4` | neutral | Page background or card surface |
| Amber Glow | `#fde533` | accent | Action accent / signal color |

```css
:root {
  --ref-midnight-ink: #000000;
  --ref-carbon: #18181b;
  --ref-steel-gray: #27272a;
  --ref-ash-gray: #343538;
  --ref-sky-haze: #a8afb7;
  --ref-stone: #8c8c8d;
  --ref-porcelain: #ffffff;
  --ref-polar-mist: #dadee4;
}
```

## Typography direction
- **Suisse International**: 400, 500, 12px, 14px, 16px, 18px, 19px, 24px, 28px, 65px, 96px, 0.90, 1.00, 1.20, 1.75; substitute `Inter`.
- **Suisse Works Book**: 400, 65px, 96px, 1.00, 1.20; substitute `Lora`.

## Spacing / shape
- Section Gap: `24px`
- Card Padding: `32px`
- Element Gap: `8px`
- Radius: `tags: 999px, cards: 28px, lists: 40px, buttons: 20px`

## Component cues
- **Primary Action Button**: Call to action
- **Ghost Secondary Button**: Secondary action
- **Subtle Secondary Button**: Secondary action on dark backgrounds
- **Standard Content Card**: Content grouping
- **Elevated Content Card**: Content grouping, slightly more prominent

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
