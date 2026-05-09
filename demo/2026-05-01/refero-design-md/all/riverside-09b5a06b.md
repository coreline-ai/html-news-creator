# Riverside - Refero Design MD

- Source: https://styles.refero.design/style/09b5a06b-29dc-4d17-8722-d29bd93010c8
- Original site: https://riverside.fm
- Theme: `dark`
- Industry: `media`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Midnight production studio

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Obsidian | `#1d1d1d` | neutral | Primary text or dark surface |
| White Canvas | `#ffffff` | neutral | Page background or card surface |
| Smokey White | `#f6f6f6` | neutral | Page background or card surface |
| Carbon Black | `#111111` | neutral | Primary text or dark surface |
| Deep Graphite | `#000000` | neutral | Primary text or dark surface |
| Silver Mist | `#bfbfbf` | neutral | Border, muted text, or supporting surface |
| Muted Grey | `#d2d2d2` | neutral | Border, muted text, or supporting surface |
| Dark Shale | `#383838` | neutral | Primary text or dark surface |
| Pale Ash | `#969696` | neutral | Border, muted text, or supporting surface |
| Electric Violet | `#9671ff` | brand | Action accent / signal color |

```css
:root {
  --ref-obsidian: #1d1d1d;
  --ref-white-canvas: #ffffff;
  --ref-smokey-white: #f6f6f6;
  --ref-carbon-black: #111111;
  --ref-deep-graphite: #000000;
  --ref-silver-mist: #bfbfbf;
  --ref-muted-grey: #d2d2d2;
  --ref-dark-shale: #383838;
}
```

## Typography direction
- **Inter**: 300, 400, 500, 600, 700, 800, 8px, 9px, 10px, 11px, 12px, 14px, 16px, 18px, 24px, 30px, 40px, 50px, 56px, 80px, 0.71, 0.72, 0.73, 0.75, 0.90, 1.00, 1.04, 1.08, 1.14, 1.16, 1.17, 1.18, 1.21, 1.22, 1.25, 1.27, 1.29, 1.38, 1.43, 1.44, 1.50, 1.57, 1.71, 1.73, 1.80, 2.00, 2.14, 2.50; substitute `system-ui`.
- **IBM Plex Sans**: 600, 16px, 1.50; substitute `Roboto`.

## Spacing / shape
- Section Gap: `43px`
- Card Padding: `12px`
- Element Gap: `10px`
- Radius: `hero: 60px, cards: 8px, badges: 100px, images: 4px, buttons: 300px, default: 8px`

## Component cues
- **Primary Call to Action Button**: Main interactive button
- **Ghost Navigation Button**: Navigation and secondary actions
- **Light Secondary Button**: Alternate call to action on light backgrounds
- **Dark Content Card**: Container for content sections
- **Subtle Feature Card**: Feature or showcase card

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
