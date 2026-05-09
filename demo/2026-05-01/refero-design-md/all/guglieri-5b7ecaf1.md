# Guglieri - Refero Design MD

- Source: https://styles.refero.design/style/5b7ecaf1-de2d-4fb9-9995-9f0665e77862
- Original site: https://guglieri.com
- Theme: `dark`
- Industry: `design`
- Recommended fit: **Admin console / run monitor / developer tooling**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Midnight Terminal, Razor Sharp

## Apply to
- Admin run monitor and review states
- Compact evidence cards and source inspection panels
- Dark-mode operational dashboards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Absolute Zero | `#000000` | neutral | Primary text or dark surface |
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Text Gray | `#454545` | neutral | Border, muted text, or supporting surface |
| Input Surface | `#111111` | neutral | Primary text or dark surface |
| Subtle Surface | `#1c1c1c` | neutral | Primary text or dark surface |
| Hairline Gray | `#575757` | neutral | Border, muted text, or supporting surface |

```css
:root {
  --ref-absolute-zero: #000000;
  --ref-canvas-white: #ffffff;
  --ref-text-gray: #454545;
  --ref-input-surface: #111111;
  --ref-subtle-surface: #1c1c1c;
  --ref-hairline-gray: #575757;
}
```

## Typography direction
- **Raveo Variable**: 1000, 12px, 14px, 22px, 32px, 64px, 1.00, 1.06, 1.18, 1.20, 1.60; substitute `system-ui, sans-serif`.
- **Inter Display**: 400, 22px, 1.18; substitute `Inter, sans-serif`.
- **Arial**: 400, 14px, 1.20; substitute `system-ui, sans-serif`.

## Spacing / shape
- Section Gap: `40px`
- Card Padding: `40px`
- Element Gap: `8px`
- Radius: `links: 8px, buttons: 28px, other-ui-elements: 4px, pill-like-elements: 40px`

## Surface cues
- **Base Canvas** `#000000`: Dominant page background, establishing the overall dark theme.
- **Interactive Surface** `#111111`: Background for interactive components like filled buttons and input fields, providing a slight visual differentiation from the base canvas.
- **Subtle Accent Surface** `#1c1c1c`: Used for minor heading backgrounds or background elements that need minimal visual separation from interactive surfaces.

## Component cues
- **Navigation Link**: Simple text link
- **Primary Ghost Button**: Actionable button with minimal visual hierarchy
- **Secondary Filled Button**: Actionable button with subtle fill
- **Minimal Input Field**: Form input field
- **Description Card**: Container for secondary information

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
