# Obviously - Refero Design MD

- Source: https://styles.refero.design/style/c21fd0f0-1375-4094-83e7-0de484940100
- Original site: https://www.obviously.ai
- Theme: `light`
- Industry: `ai`
- Recommended fit: **Admin console / run monitor / developer tooling**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Whiteboard command center

## Apply to
- Admin run monitor and review states
- Compact evidence cards and source inspection panels
- Dark-mode operational dashboards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Ink Black | `#000000` | neutral | Primary text or dark surface |
| Graphite | `#272727` | neutral | Primary text or dark surface |
| Dark Wolf | `#5d5d5d` | neutral | Border, muted text, or supporting surface |
| Slate Gray | `#4f4f4f` | neutral | Border, muted text, or supporting surface |
| Silver Mist | `#e0e0e0` | neutral | Page background or card surface |
| Fog White | `#f6f6f6` | neutral | Page background or card surface |
| Muted Stone | `#a69ea7` | neutral | Border, muted text, or supporting surface |
| Regal Violet | `#7451f2` | brand | Action accent / signal color |
| Amethyst Border | `#5952a1` | brand | Action accent / signal color |

```css
:root {
  --ref-canvas-white: #ffffff;
  --ref-ink-black: #000000;
  --ref-graphite: #272727;
  --ref-dark-wolf: #5d5d5d;
  --ref-slate-gray: #4f4f4f;
  --ref-silver-mist: #e0e0e0;
  --ref-fog-white: #f6f6f6;
  --ref-muted-stone: #a69ea7;
}
```

## Typography direction
- **DM Sans**: 400, 500, 600, 700, 9px, 12px, 14px, 15px, 16px, 1.00, 1.10, 1.20, 1.40, 1.60; substitute `system-ui`.
- **Martian Mono**: 400, 500, 11px, 16px, 1.00, 1.10, 1.20, 1.27, 1.60; substitute `SFMono-Regular, Consolas, Liberation Mono, Menlo, monospace`.
- **Lustria**: 400, 20px, 32px, 36px, 42px, 52px, 1.10, 1.20; substitute `serif`.

## Spacing / shape
- Section Gap: `64px`
- Card Padding: `16px`
- Element Gap: `8px`
- Page Max Width: `1296px`
- Radius: `badges: 100px, buttons: 4px, navItems: 4px`

## Surface cues
- **Page Canvas** `#ffffff`: Primary page background, default content area
- **Subtle Section** `#f6f6f6`: Alternate background for distinct content sections
- **Info Card** `#d6e5ff`: Background for informational badges or temporary alerts
- **Elevated Control** `#e0e0e0`: Background for subtle controls or interactive elements
- **Dominant Action** `#7451f2`: Background for primary calls to action

## Component cues
- **Primary Action Button**: Call to action
- **Secondary Ghost Button**: Alternative action
- **Navigation Link Button**: Tertiary action with minimal styling
- **Integration Grid Item**: Interactive logo display
- **Basic Info Badge**: Informational label

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
