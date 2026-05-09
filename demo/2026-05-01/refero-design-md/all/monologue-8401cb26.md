# Monologue - Refero Design MD

- Source: https://styles.refero.design/style/8401cb26-91a3-4b46-941e-1c75790821eb
- Original site: https://www.monologue.to
- Theme: `dark`
- Industry: `productivity`
- Recommended fit: **Admin console / run monitor / developer tooling**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Midnight Terminal with Aqua Glow. A luminous aqua cursor on a deep, textured black screen, where retro-futuristic forms hint at precision and understated power.

## Apply to
- Admin run monitor and review states
- Compact evidence cards and source inspection panels
- Dark-mode operational dashboards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Absolute Zero | `#000000` | neutral | Primary text or dark surface |
| Deep Graphite | `#010101` | neutral | Primary text or dark surface |
| Carbon Black | `#191919` | neutral | Primary text or dark surface |
| Dark Charcoal | `#282828` | neutral | Primary text or dark surface |
| Slate Gray | `#3f3f3f` | neutral | Primary text or dark surface |
| Ash Gray | `#7f7f7f` | neutral | Border, muted text, or supporting surface |
| Near White | `#ffffff` | neutral | Page background or card surface |
| Sea Glass | `#062f34` | accent | Action accent / signal color |
| Electric Aqua | `#19d0e8` | brand | Action accent / signal color |
| Sky Burst | `#44ccff` | accent | Action accent / signal color |

```css
:root {
  --ref-absolute-zero: #000000;
  --ref-deep-graphite: #010101;
  --ref-carbon-black: #191919;
  --ref-dark-charcoal: #282828;
  --ref-slate-gray: #3f3f3f;
  --ref-ash-gray: #7f7f7f;
  --ref-near-white: #ffffff;
  --ref-sea-glass: #062f34;
}
```

## Typography direction
- **sans-serif**: 400, 12px, 1.2.
- **Instrument Serif**: 400, 28px, 30px, 32px, 40px, 48px, 64px, 70px, 72px, 96px, 393px, 403px, 0.90, 1.00, 1.10, 1.20, 1.30, 1.40.
- **DM Mono**: 400, 10px, 12px, 14px, 15px, 16px, 18px, 20px, 32px, 0.80, 1.00, 1.20, 1.40, 1.50.

## Spacing / shape
- Section Gap: `40px`
- Card Padding: `16px`
- Element Gap: `10px`
- Page Max Width: `1200px`
- Radius: `cards: 10px, avatars: 900px, buttons: 100000px, default: 8px, largeCards: 40px, smallElements: 4px`

## Surface cues
- **Canvas** `#000000`: Primary page background, deepest layer.
- **Base Surface** `#010101`: Dominant background for content sections and large panels.
- **Card Surface** `#191919`: Background for individual cards and feature blocks.
- **Interactive Surface** `#282828`: Background for filled buttons and active input fields.

## Component cues
- **Filled Dark Button**: Primary action button
- **Ghost Accent Button**: Secondary action or featured link
- **Info Card**: Content container for features or testimonials
- **Highlight Card - Sea Glass**: Emphasized feature card
- **Highlight Card - Sky Burst**: Prominent feature card

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
