# BaseHub - Refero Design MD

- Source: https://styles.refero.design/style/2cfb738d-6c44-4628-a2f5-e9c9fc92a0ca
- Original site: https://basehub.com
- Theme: `dark`
- Industry: `devtools`
- Recommended fit: **Admin console / run monitor / developer tooling**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Midnight Command Center: Focused precision on a deep, organized canvas.

## Apply to
- Admin run monitor and review states
- Compact evidence cards and source inspection panels
- Dark-mode operational dashboards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Deep Space | `#000000` | neutral | Primary text or dark surface |
| Canvas Dark | `#040404` | neutral | Primary text or dark surface |
| Slate Surface | `#0c0c0c` | neutral | Primary text or dark surface |
| Elevated Ink | `#121212` | neutral | Primary text or dark surface |
| Ghost Fill | `#1b1b1b` | neutral | Primary text or dark surface |
| Border Dark | `#252525` | neutral | Primary text or dark surface |
| Faint Gray | `#303030` | neutral | Primary text or dark surface |
| Muted Ash | `#646464` | neutral | Border, muted text, or supporting surface |
| Subtle Gray | `#909090` | neutral | Border, muted text, or supporting surface |
| Light Text | `#dedede` | neutral | Page background or card surface |

```css
:root {
  --ref-deep-space: #000000;
  --ref-canvas-dark: #040404;
  --ref-slate-surface: #0c0c0c;
  --ref-elevated-ink: #121212;
  --ref-ghost-fill: #1b1b1b;
  --ref-border-dark: #252525;
  --ref-faint-gray: #303030;
  --ref-muted-ash: #646464;
}
```

## Typography direction
- **Geist**: 400, 500, 600, 11px, 12px, 13px, 14px, 16px, 18px, 24px, 32px, 48px, 60px, 1.00, 1.10, 1.14, 1.20, 1.23, 1.40, 1.50; substitute `Inter`.
- **Geist Mono**: 400, 13px, 1.50; substitute `Fira Code`.

## Spacing / shape
- Section Gap: `24px`
- Card Padding: `16px`
- Element Gap: `16px`
- Radius: `cards: 12px, badges: 9999px, images: 21px, buttons: 96px, default: 4px, small_buttons: 4px`

## Surface cues
- **Deep Space** `#000000`: Base layer for footer and full-bleed decorative elements, providing ultimate depth.
- **Canvas Dark** `#040404`: Primary page background layer, setting the dark foundation.
- **Slate Surface** `#0c0c0c`: Used for main content cards and distinct sections, offering a subtle lift from the canvas.
- **Elevated Ink** `#121212`: Further elevated elements like input fields or specific interactive components, creating a slight visual hierarchy.
- **Ghost Fill** `#1b1b1b`: Backgrounds for ghost buttons, indicating interactivity at a shallow elevation.

## Component cues
- **Primary Action Button**: Main call-to-action button
- **Secondary Ghost Button**: Alternative action button
- **Navigation Link Button**: Top navigation item
- **Standard Card**: Content container
- **Quote Card**: Testimonial or block quote

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
