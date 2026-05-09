# Status - Refero Design MD

- Source: https://styles.refero.design/style/4ce66adb-ed8b-4e71-8066-15d92c4d2be0
- Original site: https://status.app
- Theme: `dark`
- Industry: `crypto`
- Recommended fit: **Admin console / run monitor / developer tooling**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Midnight Command Center: a dark interface on deep canvas, with precise white type and select vibrant accents.

## Apply to
- Admin run monitor and review states
- Compact evidence cards and source inspection panels
- Dark-mode operational dashboards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Deep Space | `#09101c` | neutral | Primary text or dark surface |
| Ash | `#1b273d` | neutral | Primary text or dark surface |
| Cloud White | `#ffffff` | neutral | Page background or card surface |
| Off White | `#dce0e5` | neutral | Page background or card surface |
| Light Mist | `#f0f2f5` | neutral | Page background or card surface |
| Slate Fabric | `#3a4049` | neutral | Primary text or dark surface |
| Quiet Fog | `#647084` | neutral | Border, muted text, or supporting surface |
| Charcoal Black | `#000000` | neutral | Primary text or dark surface |
| Obsidian Grey | `#131d2f` | neutral | Primary text or dark surface |
| Steel Grey | `#a1abbd` | neutral | Border, muted text, or supporting surface |

```css
:root {
  --ref-deep-space: #09101c;
  --ref-ash: #1b273d;
  --ref-cloud-white: #ffffff;
  --ref-off-white: #dce0e5;
  --ref-light-mist: #f0f2f5;
  --ref-slate-fabric: #3a4049;
  --ref-quiet-fog: #647084;
  --ref-charcoal-black: #000000;
}
```

## Typography direction
- **Inter**: 400, 500, 600, 700, 11px, 13px, 15px, 16px, 19px, 27px, 64px, 88px, 0.95, 1.06, 1.19, 1.40, 1.42, 1.45, 1.47, 1.50; substitute `system-ui`.

## Spacing / shape
- Section Gap: `40px`
- Card Padding: `16px`
- Element Gap: `4px`
- Page Max Width: `1224px`
- Radius: `tags: 9999px, cards: 20px, forms: 12px, images: 24px, buttons: 12px, navigation: 4px`

## Component cues
- **Navigation Link**: Primary navigation item in the header.
- **Ghost Button**: Secondary action button, typically for 'Download' or 'Learn More' actions.
- **Filled Action Button Light**: Primary calls to action on the dark hero, contrasting with the dark background.
- **Branded Action Button**: Main call to action, utilizing the brand's vibrant blue.
- **Product Feature Card**: Displays key product features or benefits in a visually distinct manner.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
