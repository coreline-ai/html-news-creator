# Auros - Refero Design MD

- Source: https://styles.refero.design/style/21cfe0c1-778d-4613-9f47-a5718eb929b3
- Original site: https://auros.global
- Theme: `dark`
- Industry: `fintech`
- Recommended fit: **Admin console / run monitor / developer tooling**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Deep-sea radiant data

## Apply to
- Admin run monitor and review states
- Compact evidence cards and source inspection panels
- Dark-mode operational dashboards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Teal | `#012624` | neutral | Primary text or dark surface |
| Deep Ocean | `#011d1c` | neutral | Primary text or dark surface |
| Accent Teal | `#003734` | accent | Action accent / signal color |
| Soft Silver | `#bbc7c6` | neutral | Border, muted text, or supporting surface |
| Frost White | `#f2f2f2` | neutral | Page background or card surface |
| Near White | `#edfffe` | neutral | Page background or card surface |
| Slate Gray | `#333333` | neutral | Primary text or dark surface |
| Off Black | `#222222` | neutral | Primary text or dark surface |
| Pale Pink Glow | `#fde9ff` | accent | Action accent / signal color |
| Soft Gray | `#707777` | neutral | Border, muted text, or supporting surface |

```css
:root {
  --ref-midnight-teal: #012624;
  --ref-deep-ocean: #011d1c;
  --ref-accent-teal: #003734;
  --ref-soft-silver: #bbc7c6;
  --ref-frost-white: #f2f2f2;
  --ref-near-white: #edfffe;
  --ref-slate-gray: #333333;
  --ref-off-black: #222222;
}
```

## Typography direction
- **Matter**: 400, 500, 10px, 12px, 13px, 14px, 16px, 20px, 24px, 36px, 61px, 86px, 96px, 295px, 1.00, 1.30, 1.40, 1.50; substitute `Inter`.
- **Arial**: 400, 14px, 1.43; substitute `Helvetica Neue`.

## Spacing / shape
- Section Gap: `68px`
- Card Padding: `40px`
- Element Gap: `20px`
- Page Max Width: `1440px`
- Radius: `cards: 16px, forms: 6px, links: 6px, badges: 6px, images: 6px, buttons: 6px`

## Surface cues
- **Midnight Teal Surface** `#012624`: Base page background and foundational canvas.
- **Deep Ocean Surface** `#011d1c`: Slightly elevated cards, providing minimal textural difference from the base.
- **Accent Teal Surface** `#003734`: Prominent interactive cards and background for certain components, adding a subtle touch of color and depth.
- **Soft Gray Surface** `#707777`: Very subtle background for small, less emphasized UI elements or dividers.

## Component cues
- **Ghost Button - Light Text**: Secondary action button for low-priority interactions or link-like behavior.
- **Primary Action Button - Gradient Fill**: Prominent calls to action, drawing attention with its distinctive gradient.
- **Action Card - Accent Teal Background**: Interactive cards highlighting specific services or key information.
- **Ghost Card - Minimal**: Informational cards that blend with the background, using internal content for visual hierarchy.
- **Navigation Link**: Interactive navigation items in the header or footer.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
