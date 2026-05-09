# Eindhoven Design District - Refero Design MD

- Source: https://styles.refero.design/style/c90b584e-de5b-4971-9e13-8ab991bd96c0
- Original site: https://www.eindhovendesigndistrict.com
- Theme: `light`
- Industry: `design`
- Recommended fit: **Admin console / run monitor / developer tooling**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Graphic Modernist Poster

## Apply to
- Admin run monitor and review states
- Compact evidence cards and source inspection panels
- Dark-mode operational dashboards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Ink Black | `#000000` | neutral | Primary text or dark surface |
| Ash Gray | `#e8e8e8` | neutral | Page background or card surface |
| Silver Thread | `#bfbfbf` | neutral | Border, muted text, or supporting surface |
| Focus Red | `#ff0000` | accent | Action accent / signal color |
| Blush Pink | `#ffc2eb` | accent | Action accent / signal color |
| Electric Blue | `#0f26ed` | accent | Action accent / signal color |

```css
:root {
  --ref-canvas-white: #ffffff;
  --ref-ink-black: #000000;
  --ref-ash-gray: #e8e8e8;
  --ref-silver-thread: #bfbfbf;
  --ref-focus-red: #ff0000;
  --ref-blush-pink: #ffc2eb;
  --ref-electric-blue: #0f26ed;
}
```

## Typography direction
- **Helvetica Now**: 400, 600, 14px, 16px, 18px, 19px, 23px, 35px, 46px, 50px, 0.93, 1.00, 1.15, 1.20, 1.31, 1.40, 1.47; substitute `Inter`.

## Spacing / shape
- Section Gap: `35px`
- Card Padding: `20px`
- Element Gap: `20px`
- Radius: `cards: 0px, buttons: 500px`

## Surface cues
- **Canvas White** `#ffffff`: Primary page background and default card background.
- **Ash Gray** `#e8e8e8`: Secondary background for distinct content sections and cards, providing subtle visual separation.

## Component cues
- **Ghost Button**: Navigation, secondary actions, and inline links.
- **Primary Action Button**: Key interactions and calls to action.
- **Icon Button**: Standalone interactive icons, such as menu toggles or search.
- **Plain Link Button**: Text-based actions that blend seamlessly with content.
- **Article Card**: Displaying content previews in grid layouts.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
