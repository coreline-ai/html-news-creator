# SoundCloud - Refero Design MD

- Source: https://styles.refero.design/style/35f89ccd-614d-4f8f-9cce-bb94309df237
- Original site: https://soundcloud.com
- Theme: `dark`
- Industry: `media`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Dark stage, glowing spotlights. A deep, consistent dark background sets the scene, with strategic, vivid accents drawing attention to key interactive elements like a spotlight.

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Pitch Black | `#121212` | neutral | Primary text or dark surface |
| Ash Gray | `#303030` | neutral | Primary text or dark surface |
| Ghost White | `#ffffff` | neutral | Page background or card surface |
| Storm Gray | `#999999` | neutral | Border, muted text, or supporting surface |
| Cloud Gray | `#999999` | neutral | Border, muted text, or supporting surface |
| Faded White | `#f2f2f2` | neutral | Page background or card surface |
| Skybound Blue | `#699fff` | brand | Action accent / signal color |
| Sunset Ember | `#ff5500` | accent | Action accent / signal color |
| Melodic Blush Gradient | `#8e8485` | brand | Action accent / signal color |
| Ocean Serenity Gradient | `#70929c` | brand | Action accent / signal color |

```css
:root {
  --ref-pitch-black: #121212;
  --ref-ash-gray: #303030;
  --ref-ghost-white: #ffffff;
  --ref-storm-gray: #999999;
  --ref-cloud-gray: #999999;
  --ref-faded-white: #f2f2f2;
  --ref-skybound-blue: #699fff;
  --ref-sunset-ember: #ff5500;
}
```

## Typography direction
- **Söhne**: 100, 400, 600, 700, 12px, 14px, 17px, 18px, 22px, 28px, 36px, 60px, 1.00, 1.20, 1.27, 1.29, 1.33, 1.41, 1.43, 1.71; substitute `system-ui, sans-serif`.

## Spacing / shape
- Section Gap: `96px`
- Card Padding: `12px`
- Element Gap: `8px`
- Page Max Width: `1240px`
- Radius: `none: 0px, images: 16px, inputs: 3px, default: 4px`

## Component cues
- **Exclusive Offer Alert Banner**: Reference component style.
- **Search Bar with Upload CTA**: Reference component style.
- **Trending Track Cards Grid**: Reference component style.
- **Primary Dark Button**: Call to Action
- **Secondary Light Button**: Secondary Action

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
