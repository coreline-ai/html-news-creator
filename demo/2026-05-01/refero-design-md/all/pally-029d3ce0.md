# Pally - Refero Design MD

- Source: https://styles.refero.design/style/029d3ce0-0fe5-4a8c-99c4-4f9d704f1c60
- Original site: https://www.pally.com
- Theme: `dark`
- Industry: `productivity`
- Recommended fit: **Admin console / run monitor / developer tooling**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Deep space command center

## Apply to
- Admin run monitor and review states
- Compact evidence cards and source inspection panels
- Dark-mode operational dashboards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Slate | `#161e29` | neutral | Primary text or dark surface |
| Ghost White | `#fefcfb` | neutral | Page background or card surface |
| Off-White Canvas | `#eae5dd` | neutral | Page background or card surface |
| Carbon Text | `#1e1d1d` | neutral | Primary text or dark surface |
| Faded Steel | `#b8b9bc` | neutral | Border, muted text, or supporting surface |
| Light Steel | `#d0d0d1` | neutral | Border, muted text, or supporting surface |
| Cosmic Gradient | `#e9b3f2` | accent | Action accent / signal color |
| Deep Space Black | `#000000` | neutral | Primary text or dark surface |

```css
:root {
  --ref-midnight-slate: #161e29;
  --ref-ghost-white: #fefcfb;
  --ref-off-white-canvas: #eae5dd;
  --ref-carbon-text: #1e1d1d;
  --ref-faded-steel: #b8b9bc;
  --ref-light-steel: #d0d0d1;
  --ref-cosmic-gradient: #e9b3f2;
  --ref-deep-space-black: #000000;
}
```

## Typography direction
- **sans-serif**: 400, 12px, 1.2.
- **Test Untitled Sans**: 400, 19px, 1.00; substitute `Inter`.
- **Inter**: 500, 14px, 1.40; substitute `Inter`.

## Spacing / shape
- Section Gap: `80px`
- Card Padding: `12px`
- Element Gap: `10px`
- Radius: `cards: 12px, images: 12px, buttons: 100px, formFields: 100px`

## Component cues
- **Primary Waitlist Button**: Button
- **Dark Mode Card**: Card
- **Light Mode Feature Card**: Card
- **Navigation Link**: Link

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
