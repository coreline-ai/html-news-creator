# Stryds - Refero Design MD

- Source: https://styles.refero.design/style/6b4e6620-5c06-4dc1-931b-82265116f6f2
- Original site: https://stryds.com
- Theme: `dark`
- Industry: `other`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Neon rings in midnight

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Deep Space | `#040126` | neutral | Primary text or dark surface |
| Neon Green | `#a6ff00` | brand | Action accent / signal color |
| Dark Matter | `#333333` | neutral | Primary text or dark surface |
| Midnight Canvas | `#000000` | neutral | Primary text or dark surface |
| Graphite Border | `#3d3d3d` | neutral | Primary text or dark surface |
| Muted Ash | `#6f6f6f` | neutral | Border, muted text, or supporting surface |
| Card Surface | `#171717` | neutral | Primary text or dark surface |
| Bright Text | `#fdfdfd` | neutral | Page background or card surface |
| Component Dark | `#101010` | neutral | Primary text or dark surface |

```css
:root {
  --ref-deep-space: #040126;
  --ref-neon-green: #a6ff00;
  --ref-dark-matter: #333333;
  --ref-midnight-canvas: #000000;
  --ref-graphite-border: #3d3d3d;
  --ref-muted-ash: #6f6f6f;
  --ref-card-surface: #171717;
  --ref-bright-text: #fdfdfd;
}
```

## Typography direction
- **Arial**: 400, 500, 14px, 1.43; substitute `Helvetica Neue`.
- **Sf Pro Display**: 500, 600, 16px, 21px, 36px, 44px, 78px, 109px, 148px, 184px, 0.95, 1.00, 1.10, 1.20, 1.25; substitute `Inter`.

## Spacing / shape
- Section Gap: `80px`
- Card Padding: `80px`
- Element Gap: `16px`
- Radius: `misc: 100px, cards: 40px, buttons: 100px`

## Component cues
- **Primary Action Button**: Call to action button
- **Ghost Icon Button**: Secondary action or branding button
- **Elevated Card**: Content container for featured sections
- **Transparent Content Card**: Subtle content grouping within larger sections

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
