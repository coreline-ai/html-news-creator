# Canva - Refero Design MD

- Source: https://styles.refero.design/style/17d0a00e-5de6-48c7-9f3b-25b04f7dab4c
- Original site: https://www.canva.com
- Theme: `light`
- Industry: `design`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Vibrant creative toolkit on a clean canvas.

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Ink Black | `#000000` | neutral | Primary text or dark surface |
| Midnight Graphite | `#0f1015` | neutral | Primary text or dark surface |
| Storm Gray | `#575a5f` | neutral | Border, muted text, or supporting surface |
| Porcelain Accent | `#d7d9de` | neutral | Page background or card surface |
| Canva Violet | `#8b3dff` | brand | Action accent / signal color |
| Subtle Violet | `#a370fc` | accent | Action accent / signal color |
| Deep Violet | `#9729ff` | accent | Action accent / signal color |
| Coral Glow | `#ff6105` | accent | Action accent / signal color |
| Passion Red | `#ff3d4d` | accent | Action accent / signal color |

```css
:root {
  --ref-canvas-white: #ffffff;
  --ref-ink-black: #000000;
  --ref-midnight-graphite: #0f1015;
  --ref-storm-gray: #575a5f;
  --ref-porcelain-accent: #d7d9de;
  --ref-canva-violet: #8b3dff;
  --ref-subtle-violet: #a370fc;
  --ref-deep-violet: #9729ff;
}
```

## Typography direction
- **Times**: 400, 10px, 1.20; substitute `serif`.
- **Canva Sans**: 400, 500, 600, 14px, 16px, 18px, 21px, 24px, 28px, 32px, 36px, 56px, 64px, 84px, 1.06, 1.10, 1.25, 1.33, 1.38, 1.40, 1.50, 1.57; substitute `ui-sans-serif, system-ui`.
- **Arial**: 400, 13px, 1.20; substitute `sans-serif`.

## Spacing / shape
- Section Gap: `54px`
- Card Padding: `12px`
- Element Gap: `4px`
- Radius: `cards: 8px, default: 8px, buttonsIcon: 48px, buttonsLarge: 9999px, buttonsSmall: 8px, interactiveElements: 16px`

## Surface cues
- **Canvas White** `#ffffff`: Primary page background and default light surfaces.
- **Midnight Graphite** `#0f1015`: Dominant background for elevated feature cards and other content blocks, creating visual distinction during marketing flows.
- **Canva Violet** `#8b3dff`: Background for primary interactive elements, some hero section content, and accent areas, introducing brand color as an elevated visual layer.

## Component cues
- **Filled White Button**: Call to action, primary navigation elements.
- **Ghost White Button**: Secondary calls to action, navigation overlays.
- **Pill Ghost Black Button**: Subtle interactive elements, filter chips, category selectors.
- **Ghost Dark Button**: Secondary interactive elements, internal navigation in dark sections.
- **Dark Feature Card**: Content containers for prominent features or sections.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
