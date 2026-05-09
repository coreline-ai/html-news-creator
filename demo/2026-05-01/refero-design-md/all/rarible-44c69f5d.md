# Rarible - Refero Design MD

- Source: https://styles.refero.design/style/44c69f5d-68bf-4507-8f00-e6aa1c96246b
- Original site: https://rarible.com
- Theme: `dark`
- Industry: `crypto`
- Recommended fit: **Admin console / run monitor / developer tooling**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Dark Terminal, Electric Green

## Apply to
- Admin run monitor and review states
- Compact evidence cards and source inspection panels
- Dark-mode operational dashboards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Rich Black | `#0a0a0a` | neutral | Primary text or dark surface |
| Graphite | `#27272a` | neutral | Primary text or dark surface |
| Ash Gray | `#3b3b3b` | neutral | Primary text or dark surface |
| Silver Text | `#9d9d9d` | neutral | Border, muted text, or supporting surface |
| Off White | `#cecece` | neutral | Border, muted text, or supporting surface |
| White | `#ffffff` | neutral | Page background or card surface |
| True Black | `#000000` | neutral | Primary text or dark surface |
| Dark Granite | `#18181b` | neutral | Primary text or dark surface |
| Cadmium Green | `#faff00` | brand | Action accent / signal color |

```css
:root {
  --ref-rich-black: #0a0a0a;
  --ref-graphite: #27272a;
  --ref-ash-gray: #3b3b3b;
  --ref-silver-text: #9d9d9d;
  --ref-off-white: #cecece;
  --ref-white: #ffffff;
  --ref-true-black: #000000;
  --ref-dark-granite: #18181b;
}
```

## Typography direction
- **Tomorrow**: 400, 500, 14px, 18px, 24px, 28px, 1.17, 1.29, 1.33, 1.43; substitute `Outfit, Poppins`.
- **Geist Mono**: 400, 500, 10px, 12px, 14px, 18px, 24px, 1.00, 1.17, 1.33, 1.40, 1.43; substitute `IBM Plex Mono, Fira Code`.

## Spacing / shape
- Section Gap: `32px`
- Card Padding: `16px`
- Element Gap: `8px`
- Radius: `cards: 12px, buttons: 9999px, default: 6px`

## Surface cues
- **Base Canvas** `#0a0a0a`: Primary page background and general UI container.
- **Card Surface** `#0a0a0a`: Elevated surfaces for cards and content blocks, distinguished by a 12px border radius and often bordered by Graphite.

## Component cues
- **Pill Ghost Button**: Secondary action or filter button
- **Outline Text Button**: Tertiary action or navigation link
- **Outline Rectangular Button**: Filter or category selection
- **Filled Filter Button**: Active filter or selection
- **Primary Action Button**: Prominent action button (Login, Get $RARI)

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
