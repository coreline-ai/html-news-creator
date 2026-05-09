# Ordinal - Refero Design MD

- Source: https://styles.refero.design/style/4657db98-0c6c-4848-91e9-c339f3bb7815
- Original site: https://www.meetassembly.com
- Theme: `dark`
- Industry: `saas`
- Recommended fit: **Admin console / run monitor / developer tooling**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Midnight Command Center – A focused, dark interface illuminated by a singular, bright green operational light.

## Apply to
- Admin run monitor and review states
- Compact evidence cards and source inspection panels
- Dark-mode operational dashboards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Deep Night | `#151316` | neutral | Primary text or dark surface |
| Cloudburst Gray | `#444245` | neutral | Border, muted text, or supporting surface |
| Fog | `#8e8e8e` | neutral | Border, muted text, or supporting surface |
| Moonbeam White | `#ffffff` | neutral | Page background or card surface |
| Lunar Dust | `#f4f2ee` | neutral | Page background or card surface |
| Ghostly Gray | `#b9b9b9` | neutral | Border, muted text, or supporting surface |
| Jade Glow | `#8ef5b5` | brand | Action accent / signal color |
| Forest Whisper | `#24574d` | accent | Action accent / signal color |

```css
:root {
  --ref-deep-night: #151316;
  --ref-cloudburst-gray: #444245;
  --ref-fog: #8e8e8e;
  --ref-moonbeam-white: #ffffff;
  --ref-lunar-dust: #f4f2ee;
  --ref-ghostly-gray: #b9b9b9;
  --ref-jade-glow: #8ef5b5;
  --ref-forest-whisper: #24574d;
}
```

## Typography direction
- **Inter**: 400, 500, 13px, 17px, 27px, 40px, 53px, 60px, 1.00, 1.20, 1.50; substitute `system-ui`.
- **Inconsolata-Eyebrow**: 400, 500, 13px, 17px, 1.00, 1.50; substitute `monospace`.

## Spacing / shape
- Section Gap: `27px`
- Card Padding: `27px`
- Element Gap: `8px`
- Page Max Width: `1440px`
- Radius: `cards: 18.08px 0px 0px, buttons: 1440px, default: 4.96px`

## Surface cues
- **Deep Night Canvas** `#151316`: Base background for the entire application, creating a dark, immersive environment.
- **Cloudburst Gray Card** `#444245`: A slightly elevated background for secondary content blocks and cards, providing subtle separation from the primary canvas.

## Component cues
- **Primary Action Button**: Filled Call to Action Button
- **Secondary Ghost Button**: Outlined or Ghost Button
- **Text Link Button**: Minimal Interactive Link
- **Dark Surface Card**: Product content container
- **Informational Badge**: Small, functional label

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
