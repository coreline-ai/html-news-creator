# Patreon - Refero Design MD

- Source: https://styles.refero.design/style/bb94375b-cf09-47d4-a2e3-7b332b2c9216
- Original site: https://www.patreon.com
- Theme: `light`
- Industry: `saas`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Authentic creator stories on a clean stage.

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Ink | `#000000` | neutral | Primary text or dark surface |
| Canvas | `#ffffff` | neutral | Page background or card surface |
| Iron | `#1a1a1a` | neutral | Primary text or dark surface |
| Silver Thread | `#959595` | neutral | Border, muted text, or supporting surface |
| Sky Blue | `#5fc1f1` | accent | Action accent / signal color |
| Vivid Pink | `#f15ff1` | accent | Action accent / signal color |

```css
:root {
  --ref-ink: #000000;
  --ref-canvas: #ffffff;
  --ref-iron: #1a1a1a;
  --ref-silver-thread: #959595;
  --ref-sky-blue: #5fc1f1;
  --ref-vivid-pink: #f15ff1;
}
```

## Typography direction
- **Oracle**: 250, 300, 350, 400, 500, 8px, 14px, 15px, 22px, 26px, 27px, 39px, 54px, 128px, 188px, 0.87, 0.98, 1.00, 1.10, 1.20, 1.50; substitute `Inter`.

## Spacing / shape
- Section Gap: `38px`
- Card Padding: `14px`
- Element Gap: `7px`
- Radius: `tags: 37.5px, cards: 30px, inputs: 45px, buttons: 30px`

## Surface cues
- **Canvas** `#ffffff`: Base page background
- **Card Surface** `#ffffff`: Container cards and modular content blocks

## Component cues
- **Primary Filled Button**: Main call-to-action button, conveying confidence and directness.
- **Ghost Button**: Secondary action or navigational link within a content block, visually recessive.
- **Mini Circular Button**: Icon-only or small, self-contained actions, often navigational or functional.
- **Tag Button**: Categorization, filtering, or minor interactive elements.
- **Feature Card**: Content container for features or testimonials, elevated on the Canvas background.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
