# AI for Business - Refero Design MD

- Source: https://styles.refero.design/style/ee403055-480e-4bd4-9216-07c9ae2dde2e
- Original site: https://www.dayos.com
- Theme: `light`
- Industry: `ai`
- Recommended fit: **Research brief / AI trend page**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
High-contrast precision tooling

## Apply to
- Research section pages and model-release briefs
- Lab-note style cards
- AI product/research trend summaries

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas Ice | `#e5e7eb` | neutral | Page background or card surface |
| Midnight Ink | `#000000` | neutral | Primary text or dark surface |
| Paper White | `#ffffff` | neutral | Page background or card surface |
| Fog Gray | `#979797` | neutral | Border, muted text, or supporting surface |
| Ash Gray | `#444444` | neutral | Border, muted text, or supporting surface |
| Faint Mist | `#f3f3f3` | neutral | Page background or card surface |
| Deep Smoke | `#2f2f2f` | neutral | Primary text or dark surface |
| Action Green | `#d1ffca` | accent | Action accent / signal color |
| Alert Yellow | `#fff100` | accent | Action accent / signal color |

```css
:root {
  --ref-canvas-ice: #e5e7eb;
  --ref-midnight-ink: #000000;
  --ref-paper-white: #ffffff;
  --ref-fog-gray: #979797;
  --ref-ash-gray: #444444;
  --ref-faint-mist: #f3f3f3;
  --ref-deep-smoke: #2f2f2f;
  --ref-action-green: #d1ffca;
}
```

## Typography direction
- **SuisseIntl**: 400, 450, 500, 14px, 16px, 18px, 20px, 28px, 40px, 1.10, 1.14, 1.20, 1.25, 1.30, 1.33; substitute `Inter`.
- **SuisseIntlCond**: 700, 48px, 64px, 80px, 130px, 0.90; substitute `Bebas Neue`.
- **SuisseIntlMono**: 400, 12px, 1.30, 1.60; substitute `IBM Plex Mono`.

## Spacing / shape
- Section Gap: `80px`
- Card Padding: `16px`
- Element Gap: `24px`
- Radius: `cards: 32px, buttons: 8px, heroElements: 64px, navigationItems: 12px`

## Component cues
- **Navigation Link Default**: Standard navigation item for top-level menus.
- **Navigation Link Active**: Active or selected navigation item, visually distinct.
- **Schedule Demo Button**: Primary call to action button.
- **Ghost Button**: Secondary action button with a transparent background.
- **Solid Card**: Content card with a dark background.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
