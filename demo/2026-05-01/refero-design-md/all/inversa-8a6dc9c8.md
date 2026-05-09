# INVERSA - Refero Design MD

- Source: https://styles.refero.design/style/8a6dc9c8-7892-4eab-baaa-3c342d5671f2
- Original site: https://inversa.com
- Theme: `dark`
- Industry: `other`
- Recommended fit: **Admin console / run monitor / developer tooling**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Wilderness at dusk

## Apply to
- Admin run monitor and review states
- Compact evidence cards and source inspection panels
- Dark-mode operational dashboards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Creme Paper | `#f4f3e8` | neutral | Page background or card surface |
| Lime Accent | `#ebfc72` | accent | Action accent / signal color |
| Stone Grey | `#404040` | neutral | Border, muted text, or supporting surface |
| Muddy Banks | `#84837b` | neutral | Border, muted text, or supporting surface |
| Lime Gradient | `#ebfc72` | accent | Action accent / signal color |
| Inverse Lime Gradient | `#ebfc72` | accent | Action accent / signal color |

```css
:root {
  --ref-creme-paper: #f4f3e8;
  --ref-lime-accent: #ebfc72;
  --ref-stone-grey: #404040;
  --ref-muddy-banks: #84837b;
  --ref-lime-gradient: #ebfc72;
  --ref-inverse-lime-gradient: #ebfc72;
}
```

## Typography direction
- **NB International Pro**: 400, 13px, 14px, 18px, 58px, 72px, 0.90, 1.06, 1.20, 1.25, 1.62; substitute `Inter`.
- **JetBrains Mono**: 300, 400, 700, 13px, 14px, 18px, 29px, 65px, 1.20, 1.25, 1.28; substitute `Fira Code`.

## Spacing / shape
- Section Gap: `59px`
- Card Padding: `18px`
- Element Gap: `14px`
- Page Max Width: `810px`
- Radius: `buttons: 3.6px`

## Component cues
- **Lime CTA Button Group**: Reference component style.
- **Stat / Metric Block**: Reference component style.
- **Alert / Notification Banner**: Reference component style.
- **Ghost Navigation Button**: Primary navigation interaction
- **Dark Solid Button**: Secondary action items

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
