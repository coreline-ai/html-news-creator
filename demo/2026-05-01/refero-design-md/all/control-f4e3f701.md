# Control - Refero Design MD

- Source: https://styles.refero.design/style/f4e3f701-0fa0-4601-b652-ecfc5c573f86
- Original site: https://cntrl.site
- Theme: `light`
- Industry: `design`
- Recommended fit: **Admin console / run monitor / developer tooling**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Terminal aesthetic, industrial, high-contrast, no-frills

## Apply to
- Admin run monitor and review states
- Compact evidence cards and source inspection panels
- Dark-mode operational dashboards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Ink Black | `#000000` | neutral | Primary text or dark surface |
| Smoke Gray | `#f5f5f4` | neutral | Page background or card surface |
| Ghost Gray | `#d2d2d2` | neutral | Border, muted text, or supporting surface |
| Utility Gray | `#3d3d3d` | neutral | Primary text or dark surface |
| Subtle Gray | `#c6c6c0` | neutral | Border, muted text, or supporting surface |
| Muted Gray | `#babab9` | neutral | Border, muted text, or supporting surface |
| Inert Gray | `#acaca6` | neutral | Border, muted text, or supporting surface |
| Action Orange | `#ff5c02` | accent | Action accent / signal color |
| Highlight Green | `#01ea40` | accent | Action accent / signal color |

```css
:root {
  --ref-canvas-white: #ffffff;
  --ref-ink-black: #000000;
  --ref-smoke-gray: #f5f5f4;
  --ref-ghost-gray: #d2d2d2;
  --ref-utility-gray: #3d3d3d;
  --ref-subtle-gray: #c6c6c0;
  --ref-muted-gray: #babab9;
  --ref-inert-gray: #acaca6;
}
```

## Typography direction
- **Melange**: 500, 16px, 25px, 36px, 71px, 146px, 1.01, 1.03, 1.06, 1.07, 1.52, 2.38; substitute `Georgia Pro`.
- **Favorit Mono**: 400, 9px, 10px, 16px, 1.20, 1.33, 2.00, 2.20, 2.38, 2.40; substitute `Space Mono`.
- **Arial**: 400, 16px, 1.20; substitute `Helvetica Neue`.

## Spacing / shape
- Section Gap: `64px`
- Card Padding: `0px`
- Element Gap: `15px`
- Radius: `none: 0px, pill: 273px, large: 40px, small: 8px, button: 0px`

## Surface cues
- **Canvas White** `#ffffff`: Primary page background, base layer for all content.
- **Smoke Gray** `#f5f5f4`: Slightly elevated card backgrounds, secondary sections for visual separation without direct elevation.

## Component cues
- **Primary Action Button (Filled)**: CTA button for primary actions
- **Secondary Action Button (Filled)**: CTA button for secondary actions
- **Ghost Link Button**: Tertiary navigation or interactive elements
- **Info Card**: Content container for information grouping
- **Elevated Card**: Content container with slight visual separation

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
