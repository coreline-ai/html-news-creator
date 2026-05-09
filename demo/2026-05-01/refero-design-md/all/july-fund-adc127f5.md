# July Fund - Refero Design MD

- Source: https://styles.refero.design/style/adc127f5-c6ec-4892-984d-5445c2b6104e
- Original site: https://july.fund
- Theme: `dark`
- Industry: `fintech`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Warm parchment in a dark library

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Background Charcoal | `#221f1e` | neutral | Primary text or dark surface |
| Paper White | `#f0e7e4` | neutral | Page background or card surface |
| Text Dark | `#433e3c` | neutral | Primary text or dark surface |
| Text Light | `#ffffff` | neutral | Page background or card surface |
| Shadow Ink | `#000000` | neutral | Primary text or dark surface |
| Midtone Gray | `#898989` | neutral | Border, muted text, or supporting surface |
| Deep Plum | `#322b66` | brand | Action accent / signal color |
| Forest Green | `#113619` | brand | Action accent / signal color |
| Muted Espresso | `#2e2909` | brand | Action accent / signal color |
| Vivid Green | `#56d270` | semantic | Action accent / signal color |

```css
:root {
  --ref-background-charcoal: #221f1e;
  --ref-paper-white: #f0e7e4;
  --ref-text-dark: #433e3c;
  --ref-text-light: #ffffff;
  --ref-shadow-ink: #000000;
  --ref-midtone-gray: #898989;
  --ref-deep-plum: #322b66;
  --ref-forest-green: #113619;
}
```

## Typography direction
- **Portrait**: 400, 18px, 30px, 34px, 35px, 40px, 1.20, 1.30; substitute `Playfair Display`.
- **Helvetica Neue**: 400, 700, 8px, 10px, 15px, 16px, 18px, 1.15, 1.20, 1.30; substitute `Arial`.

## Spacing / shape
- Section Gap: `40px`
- Card Padding: `20px`
- Element Gap: `20px`
- Radius: `cards: 12px, badges: 8px, buttons: 24px, largeCards: 20px`

## Surface cues
- **Background Charcoal** `#221f1`: Dominant page background, deepest visible surface level.
- **Muted Espresso Card** `#2e2909`: Container cards that are slightly lighter than the background, creating a subtle lift.
- **Deep Plum Card** `#322b66`: Accentuated cards, often for specific thematic content, offering a richer background color.
- **Paper White Card** `#f0e7e4`: Elevated, light-themed cards that stand out against the dark background, for news or prominent features.

## Component cues
- **Outline Button (Dark)**: Secondary action button for general use on light backgrounds.
- **Outline Button (Light)**: Secondary action button for general use on dark backgrounds.
- **Minimal Link Button**: Tertiary action or navigational link with minimal styling.
- **Content Card (Paper White)**: Standard information card for displaying content sections.
- **Content Card (Charcoal)**: Standard information card for displaying content sections on dark backgrounds.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
