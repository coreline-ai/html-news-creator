# PlanetScale - Refero Design MD

- Source: https://styles.refero.design/style/a6771960-b826-49bc-9ee7-7f7a5e29642b
- Original site: https://planetscale.com
- Theme: `light`
- Industry: `devtools`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Architectural Blueprint; precise, high-contrast lines on a grid, picked out with sparse, functional color accents.

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Graphite | `#111111` | neutral | Primary text or dark surface |
| Ash Black | `#000000` | neutral | Primary text or dark surface |
| Cloud White | `#fafafa` | neutral | Page background or card surface |
| Steel Gray | `#414141` | neutral | Border, muted text, or supporting surface |
| Smoke Gray | `#737373` | neutral | Border, muted text, or supporting surface |
| Stone Gray | `#c1c1c1` | neutral | Border, muted text, or supporting surface |
| Electric Blue | `#0b6ec5` | brand | Action accent / signal color |
| Flame Orange | `#f35815` | accent | Action accent / signal color |
| Marigold Yellow | `#f2b600` | accent | Action accent / signal color |
| Verdant Green | `#22a652` | semantic | Action accent / signal color |

```css
:root {
  --ref-midnight-graphite: #111111;
  --ref-ash-black: #000000;
  --ref-cloud-white: #fafafa;
  --ref-steel-gray: #414141;
  --ref-smoke-gray: #737373;
  --ref-stone-gray: #c1c1c1;
  --ref-electric-blue: #0b6ec5;
  --ref-flame-orange: #f35815;
}
```

## Typography direction
- **ui-monospace**: 400, 500, 600, 700, 16px, 1.00; substitute `Recursive Mono, JetBrains Mono`.

## Spacing / shape
- Section Gap: `96px`
- Card Padding: `16px`
- Element Gap: `24px`
- Page Max Width: `1280px`
- Radius: `tags: 9999px, inputs: 0px, buttons: 0px`

## Component cues
- **Announcement Banner**: Reference component style.
- **Tabbed Content Switcher**: Reference component style.
- **Testimonial + CTA Block**: Reference component style.
- **Naked Link Button**: Navigation, inline actions, text-based CTAs.
- **Dark Overlay Button**: Contextual navigation, menu items, secondary actions.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
