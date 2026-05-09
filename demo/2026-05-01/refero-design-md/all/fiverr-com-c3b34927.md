# Fiverr.com - Refero Design MD

- Source: https://styles.refero.design/style/c3b34927-0638-463e-bf85-180d73bfc367
- Original site: https://www.fiverr.com
- Theme: `light`
- Industry: `other`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Green accented workplace

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Fiverr Green | `#1dbf73` | brand | Action accent / signal color |
| Deep Moss | `#003912` | brand | Action accent / signal color |
| Graphite | `#222325` | neutral | Primary text or dark surface |
| Cloud White | `#ffffff` | neutral | Page background or card surface |
| Slate Gray | `#62646a` | neutral | Border, muted text, or supporting surface |
| Pebble Gray | `#c5c6c9` | neutral | Border, muted text, or supporting surface |
| Ash Gray | `#dadbdd` | neutral | Page background or card surface |
| Warm Gray | `#404145` | neutral | Border, muted text, or supporting surface |
| Cool Gray | `#74767e` | neutral | Border, muted text, or supporting surface |

```css
:root {
  --ref-fiverr-green: #1dbf73;
  --ref-deep-moss: #003912;
  --ref-graphite: #222325;
  --ref-cloud-white: #ffffff;
  --ref-slate-gray: #62646a;
  --ref-pebble-gray: #c5c6c9;
  --ref-ash-gray: #dadbdd;
  --ref-warm-gray: #404145;
}
```

## Typography direction
- **Macan**: 280, 400, 600, 700, 10px, 14px, 16px, 18px, 48px, 72px, 1.00, 1.05, 1.20, 1.50, 1.56, 1.57, 2.40; substitute `system-ui, sans-serif`.

## Spacing / shape
- Section Gap: `40px`
- Card Padding: `12px`
- Element Gap: `12px`
- Page Max Width: `1200px`
- Radius: `tags: 9999px, cards: 16px, inputs: 12px, buttons: 8px, navigation: 4px`

## Surface cues
- **Page Canvas** `#ffffff`: The default background for the majority of page content and sections, providing a clean, bright foundation.
- **Ash Shade** `#dadbdd`: Used for subtle background distinctions between sections, providing a slight visual break from the primary canvas without introducing strong color.
- **Card Base** `#003912`: Serves as the background for hero sections and prominent feature cards, offering a strong, deep-green contrast to light-colored text.

## Component cues
- **Primary Ghost Button**: Call to action; outlined button against dark backgrounds
- **Small Filter Button**: Navigation links or categorical filters within sub-sections.
- **Text Only Button**: Minimal interactive elements or navigation links that primarily use text.
- **White Filled Button**: General action button on light backgrounds.
- **Category Card**: Displays service categories with an associated image and text.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
