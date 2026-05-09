# Pirsch Analytics - Refero Design MD

- Source: https://styles.refero.design/style/e4b9d41a-8165-47dd-818a-5f6810046ea9
- Original site: https://pirsch.io
- Theme: `light`
- Industry: `saas`
- Recommended fit: **Source ledger / evidence dashboard**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Warm, grounded analytics

## Apply to
- Source ledger, ranking, and verification screens
- Cluster evidence dashboards
- Dense data tables with clear hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Ink | `#000000` | neutral | Primary text or dark surface |
| Ghostly Gray | `#f8f5ed` | neutral | Page background or card surface |
| Muted Stone | `#707070` | neutral | Border, muted text, or supporting surface |
| Sunbeam Yellow | `#ffda6e` | brand | Action accent / signal color |
| Leafy Green | `#6ece9d` | brand | Action accent / signal color |

```css
:root {
  --ref-midnight-ink: #000000;
  --ref-ghostly-gray: #f8f5ed;
  --ref-muted-stone: #707070;
  --ref-sunbeam-yellow: #ffda6e;
  --ref-leafy-green: #6ece9d;
}
```

## Typography direction
- **DM Sans**: 400, 500, 14px, 16px, 18px, 20px, 24px, 28px, 64px, 1.25, 1.50, 2.22; substitute `Inter`.

## Spacing / shape
- Section Gap: `48px`
- Card Padding: `32px`
- Element Gap: `16px`
- Radius: `tags: 24px, cards: 24px, input: 6px, buttons: 12px`

## Surface cues
- **Canvas** `#FFFFFF`: Dominant page background, providing a clean, bright foundation.
- **Card Surface** `#f8f5ed`: Background for content cards, offering subtle visual depth and warmth against the pure white canvas.

## Component cues
- **Primary Action Button - Yellow**: Filled button
- **Secondary Action Button - Green**: Filled button
- **Small Tag Button**: Informational tag
- **Content Card**: Surface for grouped content
- **Text Input Field**: User data entry

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
