# Figura - Refero Design MD

- Source: https://styles.refero.design/style/5e427a82-a223-4b69-be7f-01c6656ce823
- Original site: https://www.figura.digital
- Theme: `dark`
- Industry: `design`
- Recommended fit: **Admin console / run monitor / developer tooling**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Midnight Command Console: high-contrast text on deep black surfaces, punctuated by precise interactions and measured spacing.

## Apply to
- Admin run monitor and review states
- Compact evidence cards and source inspection panels
- Dark-mode operational dashboards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Absolute Zero | `#000000` | neutral | Primary text or dark surface |
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Medium Gray | `#8f8f8f` | neutral | Border, muted text, or supporting surface |
| Surface Dark | `#1f1f1f` | neutral | Primary text or dark surface |
| Sky Glint | `#d4eaef` | accent | Action accent / signal color |
| Ocean Calm | `#b3d5df` | accent | Action accent / signal color |

```css
:root {
  --ref-absolute-zero: #000000;
  --ref-canvas-white: #ffffff;
  --ref-medium-gray: #8f8f8f;
  --ref-surface-dark: #1f1f1f;
  --ref-sky-glint: #d4eaef;
  --ref-ocean-calm: #b3d5df;
}
```

## Typography direction
- **Inter Display**: 400, 500, 600, 700, 12px, 14px, 15px, 16px, 18px, 20px, 22px, 32px, 36px, 1.22, 1.33, 1.36, 1.38, 1.40, 1.43, 1.50, 1.87; substitute `Inter`.
- **Geist Mono**: 500, 600, 10px, 12px, 1.20, 1.33, 1.40; substitute `Fira Code`.
- **sans-serif**: 400, 12px, 1.20; substitute `Arial`.

## Spacing / shape
- Section Gap: `96px`
- Card Padding: `16px`
- Element Gap: `8px`
- Radius: `pill: 200px, input: 8px, badges: 40px, buttons: 56px, default: 8px, largeElement: 32px`

## Component cues
- **Ghost Border Button**: Action Element
- **Navigation Link**: Navigation Element

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
