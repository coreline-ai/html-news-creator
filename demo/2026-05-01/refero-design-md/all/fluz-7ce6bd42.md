# Fluz - Refero Design MD

- Source: https://styles.refero.design/style/7ce6bd42-e498-47c0-ad02-7b3a0f5d94e0
- Original site: https://fluz.app/us
- Theme: `light`
- Industry: `fintech`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Vivid gradient playground

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Money Max Black | `#1a0000` | brand | Action accent / signal color |
| Sky Blue | `#98bbf4` | accent | Action accent / signal color |
| Forest Noir | `#11190c` | neutral | Primary text or dark surface |
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Mist Gray | `#f2f2f2` | neutral | Page background or card surface |
| Light Cloud | `#ededec` | neutral | Page background or card surface |
| Iron Slate | `#3a3a3a` | neutral | Primary text or dark surface |
| Onyx Shadow | `#221919` | neutral | Primary text or dark surface |
| Subtle Ash | `#514f4c` | neutral | Border, muted text, or supporting surface |
| Pebble Gray | `#aeaea6` | neutral | Border, muted text, or supporting surface |

```css
:root {
  --ref-money-max-black: #1a0000;
  --ref-sky-blue: #98bbf4;
  --ref-forest-noir: #11190c;
  --ref-canvas-white: #ffffff;
  --ref-mist-gray: #f2f2f2;
  --ref-light-cloud: #ededec;
  --ref-iron-slate: #3a3a3a;
  --ref-onyx-shadow: #221919;
}
```

## Typography direction
- **Area Semibold**: 400, 700, 16px, 17px, 20px, 1.40, 1.45, 1.50; substitute `Inter`.
- **Greed Condensed SemiBold**: 400, 700, 16px, 24px, 1.17, 1.25, 1.50; substitute `Bebas Neue`.
- **Greed-CondensedSemiBold**: 400, 700, 16px, 24px, 1.17, 1.25, 1.50; substitute `Bebas Neue`.

## Spacing / shape
- Section Gap: `40px`
- Card Padding: `20px`
- Element Gap: `5px`
- Page Max Width: `1750px`
- Radius: `cards: 20px, images: 20px, buttons: 100px`

## Component cues
- **Primary Action Button**: High-impact call to action
- **Outline Ghost Button**: Secondary or tertiary action
- **Light Muted Button**: Informational or inactive states
- **Floating Content Card**: Showcasing features or content blocks
- **Product Display Card**: Presenting product visuals

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
