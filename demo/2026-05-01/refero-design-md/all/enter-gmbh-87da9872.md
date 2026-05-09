# Enter GmbH - Refero Design MD

- Source: https://styles.refero.design/style/87da9872-f6cc-4354-bf6a-1c02f0394d45
- Original site: https://enter-support.de
- Theme: `light`
- Industry: `other`
- Recommended fit: **Design reference / webapp exploration**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
High-contrast functional block

## Apply to
- General webapp UI exploration
- Demo cards and catalog surfaces
- Future admin/subscriber UI references

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Ocean Mist | `#a5d3d4` | neutral | Border, muted text, or supporting surface |
| Warm Canvas | `#f9f8ea` | neutral | Page background or card surface |
| Pure White | `#ffffff` | neutral | Page background or card surface |
| Charcoal Black | `#000000` | neutral | Primary text or dark surface |
| Graphite | `#282828` | neutral | Primary text or dark surface |
| Muted Stone | `#6a6a6a` | neutral | Border, muted text, or supporting surface |
| Flame Orange | `#ff5000` | brand | Action accent / signal color |

```css
:root {
  --ref-ocean-mist: #a5d3d4;
  --ref-warm-canvas: #f9f8ea;
  --ref-pure-white: #ffffff;
  --ref-charcoal-black: #000000;
  --ref-graphite: #282828;
  --ref-muted-stone: #6a6a6a;
  --ref-flame-orange: #ff5000;
}
```

## Typography direction
- **Helvetica**: 400, 700, 10px, 1.15; substitute `Arial`.
- **Maax Mono**: 400, 16px, 1.50, 1.60; substitute `Space Mono`.
- **Sofia-Regular**: 400, 28px, 1.29, 1.36; substitute `Work Sans`.

## Spacing / shape
- Section Gap: `24px`
- Card Padding: `13px`
- Element Gap: `24px`
- Radius: `links: 25px, buttons: 25px`

## Component cues
- **Primary Action Button**: Interactive element for key user actions.
- **Navigation Link**: Top-level navigation items.
- **Decorative Text Link**: Subtle links within body content or lists.
- **News Banner**: Informational banner at the top of the page.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
