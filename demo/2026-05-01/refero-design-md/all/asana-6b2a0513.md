# Asana - Refero Design MD

- Source: https://styles.refero.design/style/6b2a0513-df80-4140-87a8-38b1fef34313
- Original site: https://asana.com
- Theme: `light`
- Industry: `productivity`
- Recommended fit: **Admin console / run monitor / developer tooling**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Productivity whiteboard lit by a coral lamp — authoritative black type on a breathing white field, with a warm coral flash and a deep-navy flicker to signal where action lives.

## Apply to
- Admin run monitor and review states
- Compact evidence cards and source inspection panels
- Dark-mode operational dashboards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Ink Black | `#0d0d0d` | neutral | Primary text or dark surface |
| Pure White | `#ffffff` | neutral | Page background or card surface |
| Mist | `#f3f3f3` | neutral | Page background or card surface |
| Cloud | `#e7e7e7` | neutral | Page background or card surface |
| Stone | `#e0dedc` | neutral | Page background or card surface |
| Slate | `#646f79` | neutral | Border, muted text, or supporting surface |
| Charcoal | `#3d3d3d` | neutral | Primary text or dark surface |
| Iron | `#474748` | neutral | Border, muted text, or supporting surface |
| Ash | `#9ca6af` | neutral | Border, muted text, or supporting surface |
| Asana Violet | `#222875` | brand | Action accent / signal color |

```css
:root {
  --ref-ink-black: #0d0d0d;
  --ref-pure-white: #ffffff;
  --ref-mist: #f3f3f3;
  --ref-cloud: #e7e7e7;
  --ref-stone: #e0dedc;
  --ref-slate: #646f79;
  --ref-charcoal: #3d3d3d;
  --ref-iron: #474748;
}
```

## Typography direction
- **Ghost**: 500, 60px, 72px, 1.00; substitute `Neue Haas Grotesk Display, Aktiv Grotesk Ex`.
- **TWK Lausanne**: 300, 400, 500, 11px, 12px, 13px, 14px, 16px, 20px, 22px, 24px, 30px, 36px, 1.20 – 2.57 depending on size (large sizes ~1.20, body ~1.50, captions ~1.75); substitute `Lausanne (Weltkern), Inter, DM Sans`.

## Spacing / shape
- Section Gap: `80-120px`
- Card Padding: `24px`
- Element Gap: `16px`
- Page Max Width: `1200px`
- Radius: `tags: 999px, cards: 10-16px, inputs: 4px, modals: 20px, buttons-pill: 100px, buttons-pill-xl: 146px`

## Component cues
- **CTA Button Group**: Reference component style.
- **Filter Chip Tab Bar**: Reference component style.
- **Use Case Feature Cards**: Reference component style.
- **Primary CTA Button (Pill)**: Main calls to action: 'Get started', primary conversion points
- **Secondary Outline Button (Pill)**: Secondary actions: 'View demo', alternate CTAs alongside primary

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
