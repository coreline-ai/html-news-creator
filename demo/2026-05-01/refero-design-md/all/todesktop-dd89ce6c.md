# ToDesktop - Refero Design MD

- Source: https://styles.refero.design/style/dd89ce6c-f0aa-4ca8-bd63-19dcd81920a7
- Original site: https://www.todesktop.com
- Theme: `mixed`
- Industry: `devtools`
- Recommended fit: **Admin console / run monitor / developer tooling**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Digital engineering lab

## Apply to
- Admin run monitor and review states
- Compact evidence cards and source inspection panels
- Dark-mode operational dashboards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Void | `#05061b` | neutral | Primary text or dark surface |
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Silver Mist | `#e5e7eb` | neutral | Page background or card surface |
| Ink Black | `#000000` | neutral | Primary text or dark surface |
| Graphite | `#141414` | neutral | Primary text or dark surface |
| Cloud Gray | `#656565` | neutral | Border, muted text, or supporting surface |
| Faded White | `#e6fff7` | neutral | Page background or card surface |
| Light Steel | `#c2c2c9` | neutral | Border, muted text, or supporting surface |
| Polar Mist | `#d6d6db` | neutral | Border, muted text, or supporting surface |
| Electric Blue | `#0036ff` | brand | Action accent / signal color |

```css
:root {
  --ref-midnight-void: #05061b;
  --ref-canvas-white: #ffffff;
  --ref-silver-mist: #e5e7eb;
  --ref-ink-black: #000000;
  --ref-graphite: #141414;
  --ref-cloud-gray: #656565;
  --ref-faded-white: #e6fff7;
  --ref-light-steel: #c2c2c9;
}
```

## Typography direction
- **Inter**: 400, 500, 600, 700, 9px, 10px, 12px, 13px, 14px, 16px, 1.07, 1.33, 1.43, 1.50, 1.54, 1.57, 1.63, 1.67, 1.78, 1.83, 2.40; substitute `system-ui, sans-serif`.
- **Aeonik Pro**: 400, 500, 18px, 24px, 36px, 48px, 64px, 74px, 1.08, 1.13, 1.14, 1.22, 1.33, 1.78; substitute `Inter, system-ui, sans-serif`.
- **Geist Mono**: 400, 500, 10px, 11px, 12px, 14px, 16px, 1.45, 1.50, 1.57, 2.00, 2.40, 2.67; substitute `ui-monospace, monospace`.

## Spacing / shape
- Section Gap: `64px`
- Card Padding: `12px`
- Element Gap: `8px`
- Radius: `none: 0px, cards: 24px, large: 32px, small: 6px, badges: 999px, medium: 14px, buttons: 999px, content: 20px`

## Surface cues
- **Deep Space** `#05061b`: Base background for dark sections, especially hero and commanding areas, with a subtle texture/gradient.
- **Canvas White** `#ffffff`: Primary background for light themed sections, offering a clean, expansive content area.
- **Frosted Card** `#ffffff`: Elevated white cards (with 0.88 opacity) that appear 'frosted' with soft shadows for content grouping.
- **Dark Commander Card** `#05061b`: High-prominence dark cards (with 0.5 opacity) for key feature blocks, featuring complex inner and outer shadows.

## Component cues
- **Primary Action Button**: Filled button indicating primary calls to action.
- **Ghost Button**: Secondary action button, visually lighter.
- **Pill Outline Button**: Outlined button with a distinct pill shape.
- **Navigation Link Button**: Small, subtly interactive navigation button.
- **Hero Card - Dark Elevated**: Prominent card for key product features, elevated in background.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
