# Vimeo - Refero Design MD

- Source: https://styles.refero.design/style/be6c7488-9cea-43db-bb28-2606f53ade14
- Original site: https://vimeo.com
- Theme: `light`
- Industry: `media`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Digital Atelier

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Graphite | `#141a20` | neutral | Primary text or dark surface |
| Cloud Canvas | `#fafcfd` | neutral | Page background or card surface |
| Ash Gray | `#23313b` | neutral | Primary text or dark surface |
| Steel Gray | `#3d4751` | neutral | Border, muted text, or supporting surface |
| Slate Blue | `#4c5864` | neutral | Action accent / signal color |
| Light Mist | `#dfe4ea` | neutral | Page background or card surface |
| Cosmic Teal | `#17d5ff` | brand | Action accent / signal color |
| Deep Teal | `#13b1d4` | brand | Action accent / signal color |
| Overlay Shadow | `#000000` | neutral | Primary text or dark surface |

```css
:root {
  --ref-midnight-graphite: #141a20;
  --ref-cloud-canvas: #fafcfd;
  --ref-ash-gray: #23313b;
  --ref-steel-gray: #3d4751;
  --ref-slate-blue: #4c5864;
  --ref-light-mist: #dfe4ea;
  --ref-cosmic-teal: #17d5ff;
  --ref-deep-teal: #13b1d4;
}
```

## Typography direction
- **ABCRepro**: 400, 500, 700, 10px, 12px, 13px, 14px, 16px, 18px, 19px, 20px, 24px, 32px, 40px, 72px, 1.00, 1.10, 1.14, 1.20, 1.30, 1.35, 1.40, 1.58; substitute `Inter`.
- **ABCReproMono**: 400, 16px, 1.00; substitute `Space Mono`.

## Spacing / shape
- Section Gap: `56px`
- Card Padding: `24px`
- Element Gap: `8px`
- Page Max Width: `1200px`
- Radius: `pill: 9999px, cards: 12px, badges: 16px, inputs: 0px, buttons: 12px, default: 8px`

## Surface cues
- **Cloud Canvas** `#fafcfd`: Primary page background, base for light sections.
- **Midnight Graphite** `#141a20`: Primary background for dark sections, elevated card surfaces within dark contexts.
- **Transparent Overlay** `#ffffff99`: Informational cards or overlays on image-heavy backgrounds.
- **Light Mist** `#dfe4ea`: Subtle UI elements, neutral component backgrounds, hover states.

## Component cues
- **Primary Action Button**: High-emphasis interactive element
- **Ghost Button**: Secondary action or navigation
- **Text Link Button**: Tertiary action or inline navigation
- **Transparent Card**: Informational grouping on hero/dark sections.
- **Light Surface Card**: Default informational grouping on light sections.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
