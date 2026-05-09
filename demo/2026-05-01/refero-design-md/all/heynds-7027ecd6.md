# Heynds - Refero Design MD

- Source: https://styles.refero.design/style/7027ecd6-41d9-4bc6-b919-3df5c573b950
- Original site: https://www.heynds.com/en
- Theme: `light`
- Industry: `ai`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Vibrant AI Canvas

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Ember Orange | `#f53900` | brand | Action accent / signal color |
| Pale Peach | `#ffe0d6` | accent | Action accent / signal color |
| Midnight Charcoal | `#040101` | neutral | Primary text or dark surface |
| Canvas White | `#fffafa` | neutral | Page background or card surface |
| Border Fog | `#e5e5e5` | neutral | Page background or card surface |
| Muted Ash | `#827e7e` | neutral | Border, muted text, or supporting surface |
| Divider Gray | `#c0bcbc` | neutral | Border, muted text, or supporting surface |

```css
:root {
  --ref-ember-orange: #f53900;
  --ref-pale-peach: #ffe0d6;
  --ref-midnight-charcoal: #040101;
  --ref-canvas-white: #fffafa;
  --ref-border-fog: #e5e5e5;
  --ref-muted-ash: #827e7e;
  --ref-divider-gray: #c0bcbc;
}
```

## Typography direction
- **Geist**: 400, 500, 600, 700, 12px, 14px, 16px, 20px, 24px, 32px, 36px, 40px, 48px, 64px, 80px, 1.00, 1.11, 1.25, 1.33, 1.40.

## Spacing / shape
- Section Gap: `112px`
- Card Padding: `40px`
- Element Gap: `24px`
- Radius: `tags: 9999px, cards: 8px, buttons: 4px, smallComponents: 12px`

## Component cues
- **Primary Filled Button**: Command to drive user action
- **Secondary Ghost Button**: Alternative action that is less prominent than the primary
- **Soft Secondary Button**: Subtle call to action, offering a light interactive state
- **Information Card**: Container for grouped content
- **Hero Headline**: Primary visual statement, capturing attention

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
