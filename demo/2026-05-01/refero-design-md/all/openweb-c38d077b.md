# OpenWeb - Refero Design MD

- Source: https://styles.refero.design/style/c38d077b-3cdb-48c6-899c-e8a543508c31
- Original site: https://www.openweb.com
- Theme: `light`
- Industry: `media`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Editorial calm on parchment.

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Parchment White | `#f1e9e7` | neutral | Page background or card surface |
| Midnight Ink | `#000000` | neutral | Primary text or dark surface |
| Arctic Frost | `#ffffff` | neutral | Page background or card surface |
| Slate Gray | `#7b7f83` | neutral | Border, muted text, or supporting surface |
| Vivid Cobalt | `#0058fe` | accent | Action accent / signal color |

```css
:root {
  --ref-parchment-white: #f1e9e7;
  --ref-midnight-ink: #000000;
  --ref-arctic-frost: #ffffff;
  --ref-slate-gray: #7b7f83;
  --ref-vivid-cobalt: #0058fe;
}
```

## Typography direction
- **Copernicus**: 400, 700, 11px, 14px, 15px, 16px, 18px, 25px, 30px, 40px, 48px, 60px, 70px, 80px, 90px, 0.84, 1.00, 1.04, 1.05, 1.08, 1.10, 1.15, 1.17, 1.20, 1.21, 1.27, 1.28, 1.30; substitute `Georgia`.
- **Helvetica**: 400, 15px, 1.50; substitute `Arial`.

## Spacing / shape
- Section Gap: `50px`
- Card Padding: `30px`
- Element Gap: `15px`
- Page Max Width: `1200px`
- Radius: `misc: 40px, avatar: 50%, inputs: 0px, buttons: 0px, default: 0px`

## Surface cues
- **Parchment Canvas** `#f1e9e7`: Base page background, soft and warm.
- **Midnight Ink Surface** `#000000`: Used for hero sections and full-width dark banners, providing a deep contrast from the Parchment Canvas.

## Component cues
- **Ghost Navigation Button**: Primary navigation links and secondary actions
- **Filled Action Button**: Primary call to action.
- **Outlined Link Button (Cobalt)**: Secondary call to action, promoting related content or navigation.
- **Outlined Link Button (Ink)**: Secondary call to action, promoting related content or navigation.
- **Input Field**: Standard user input fields for text or selections.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
