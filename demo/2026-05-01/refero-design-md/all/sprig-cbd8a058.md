# Sprig - Refero Design MD

- Source: https://styles.refero.design/style/cbd8a058-6ecb-4f1b-9b5a-2bf2597826ee
- Original site: https://sprig.com
- Theme: `light`
- Industry: `ai`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
White canvas, thoughtful function

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#faf9f8` | neutral | Page background or card surface |
| Midnight Ink | `#0b2330` | neutral | Primary text or dark surface |
| Jet Black | `#000000` | neutral | Primary text or dark surface |
| Fog Gray | `#f3f3f3` | neutral | Page background or card surface |
| Graphite | `#1c1a17` | neutral | Primary text or dark surface |
| Slate Text | `#6e6d6a` | neutral | Border, muted text, or supporting surface |
| Charcoal Button | `#272420` | neutral | Primary text or dark surface |
| Border Ash | `#e8e7e6` | neutral | Page background or card surface |
| Deep Space | `#141312` | neutral | Primary text or dark surface |
| Medium Gray | `#575653` | neutral | Border, muted text, or supporting surface |

```css
:root {
  --ref-canvas-white: #faf9f8;
  --ref-midnight-ink: #0b2330;
  --ref-jet-black: #000000;
  --ref-fog-gray: #f3f3f3;
  --ref-graphite: #1c1a17;
  --ref-slate-text: #6e6d6a;
  --ref-charcoal-button: #272420;
  --ref-border-ash: #e8e7e6;
}
```

## Typography direction
- **ABC Diatype**: 400, 500, 14px, 16px, 24px, 32px, 40px, 1.20, 1.30, 1.40; substitute `Inter`.
- **TT Commons Pro**: 400, 16px, 18px, 40px, 1.50; substitute `Montserrat`.

## Spacing / shape
- Section Gap: `80px`
- Card Padding: `16px`
- Element Gap: `8px`
- Radius: `cards: 100px, badges: 4px, buttons: 32px, deepCurve: 1600px`

## Surface cues
- **Canvas White** `#faf9f8`: Primary page background and default surface for most content.
- **Fog Gray** `#f3f3f3`: Slightly elevated surfaces for badges and minor background accents.
- **Border Ash** `#e8e7e6`: Used for subtle borders and as a background for certain secondary elements.

## Component cues
- **Primary Filled Button**: Call to action button for key conversions.
- **Secondary Outlined Button**: Supporting actions or navigation links.
- **Ghost Header Button**: Subtle button with minimal styling for navigation or secondary actions in header.
- **Subtle Information Badge**: Used for categorization or small labels.
- **Product Display Card**: Highlights features or product screenshots with a curved frame.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
