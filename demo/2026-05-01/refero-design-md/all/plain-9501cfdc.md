# Plain - Refero Design MD

- Source: https://styles.refero.design/style/9501cfdc-3eb3-4b64-90f6-9afdded48945
- Original site: https://plain.com
- Theme: `light`
- Industry: `saas`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Crisp digital workbench

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Ghost Fog | `#f3fbe9` | neutral | Page background or card surface |
| Vanilla Cream | `#f9f6f1` | neutral | Page background or card surface |
| Ash Graphite | `#0a2414` | neutral | Primary text or dark surface |
| Deep Forest | `#283a2e` | neutral | Primary text or dark surface |
| Sage Green | `#607166` | neutral | Action accent / signal color |
| System Black | `#000000` | neutral | Primary text or dark surface |
| Plain Green | `#1ad379` | brand | Action accent / signal color |
| Plain Green Muted | `#17b267` | brand | Action accent / signal color |
| Alert Red | `#360003` | accent | Action accent / signal color |

```css
:root {
  --ref-canvas-white: #ffffff;
  --ref-ghost-fog: #f3fbe9;
  --ref-vanilla-cream: #f9f6f1;
  --ref-ash-graphite: #0a2414;
  --ref-deep-forest: #283a2e;
  --ref-sage-green: #607166;
  --ref-system-black: #000000;
  --ref-plain-green: #1ad379;
}
```

## Typography direction
- **sans-serif**: 400, 12px, 1.2.
- **ABC Favorit**: 400, 500, 13px, 15px, 18px, 24px, 48px, 80px, 0.95 (display), 1.00 (headings), 1.17 (subheadings), 1.33 (body), 1.46 (body); substitute `Inter`.
- **Geist Mono**: 500, 13px, 1.46; substitute `JetBrains Mono`.

## Spacing / shape
- Section Gap: `40px`
- Card Padding: `24px`
- Element Gap: `24px`
- Radius: `cards: 9px, buttons: 6px, general: 6px`

## Surface cues
- **Canvas White** `#ffffff`: Base page background
- **Ghost Fog** `#f3fbe9`: Secondary background for sections and outlined button fills
- **Vanilla Cream** `#f9f6f1`: Background for cards and elevated components
- **Deep Forest** `#283a2`: Alternative background for dark-themed cards

## Component cues
- **Primary Action Button**: Main call-to-action
- **Outlined Accent Button**: Secondary action button
- **Light Content Card**: Neutral information container
- **Dark Themed Card**: Emphasized or themed content container
- **Alert Card**: Indicator for critical or urgent information

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
