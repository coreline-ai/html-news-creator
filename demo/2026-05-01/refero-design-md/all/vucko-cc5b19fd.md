# Vucko - Refero Design MD

- Source: https://styles.refero.design/style/cc5b19fd-12cf-4b30-801c-8a0363646e48
- Original site: https://vucko.co
- Theme: `light`
- Industry: `design`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
High-contrast typographic canvas.

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Ink | `#000000` | neutral | Primary text or dark surface |
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Slate Mist | `#eeeeee` | neutral | Page background or card surface |
| Warm Gray | `#888a8b` | neutral | Border, muted text, or supporting surface |
| Deep Gray | `#222222` | neutral | Primary text or dark surface |

```css
:root {
  --ref-midnight-ink: #000000;
  --ref-canvas-white: #ffffff;
  --ref-slate-mist: #eeeeee;
  --ref-warm-gray: #888a8b;
  --ref-deep-gray: #222222;
}
```

## Typography direction
- **suisse**: 400, 500, 700, 17px, 18px, 19px, 43px, 55px, 120px, 211px, 0.70, 1.00, 1.05, 1.13, 1.17, 1.21, 1.50; substitute `system-ui, sans-serif`.

## Spacing / shape
- Section Gap: `58px`
- Card Padding: `0px`
- Element Gap: `23px`
- Radius: `cards: 9.6px, buttons: 0px, navItems: 9999px, utilityElements: 4.8px`

## Surface cues
- **Canvas White** `#ffffff`: Primary page background.
- **Slate Mist** `#eeeeee`: Subtle lift for cards and contained content sections.
- **Deep Gray** `#222222`: Background for utility navigation or section separators.
- **Midnight Ink** `#000000`: Deepest background for striking contrast elements or full-bleed dark sections.

## Component cues
- **Text Link Button (Dark)**: Interactive text link, border-bottom appears on hover/focus.
- **Text Link Button (Light)**: Interactive text link within dark contexts, border-bottom appears on hover/focus.
- **Showcase Card**: Display individual portfolio items or content blocks.
- **Elevated Showcase Card**: Highlight specific content or product showcases.
- **Navigation Dot**: Indicates current section or state in compact navigation.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
