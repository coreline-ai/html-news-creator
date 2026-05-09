# Arc - Refero Design MD

- Source: https://styles.refero.design/style/ca93daf1-daf3-41b7-8248-8f63082761e8
- Original site: https://arc.net
- Theme: `light`
- Industry: `productivity`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Playful gradient on clean slate

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas | `#ffffff` | neutral | Page background or card surface |
| Wash | `#fffcec` | neutral | Page background or card surface |
| Highlight | `#fffadd` | neutral | Page background or card surface |
| Charcoal Text | `#000000` | neutral | Primary text or dark surface |
| Body Text | `#696969` | neutral | Border, muted text, or supporting surface |
| Muted Text | `#595853` | neutral | Border, muted text, or supporting surface |
| Shadow Tint | `#bfbdb1` | neutral | Border, muted text, or supporting surface |
| Arc Violet | `#3139fb` | brand | Action accent / signal color |
| Action Violet | `#2702c2` | brand | Action accent / signal color |
| Red Accent | `#ff5060` | accent | Action accent / signal color |

```css
:root {
  --ref-canvas: #ffffff;
  --ref-wash: #fffcec;
  --ref-highlight: #fffadd;
  --ref-charcoal-text: #000000;
  --ref-body-text: #696969;
  --ref-muted-text: #595853;
  --ref-shadow-tint: #bfbdb1;
  --ref-arc-violet: #3139fb;
}
```

## Typography direction
- **Marlin Soft SQ**: 500, 700, 14px, 16px, 28px, 40px, 46px, 0.93, 0.98, 1.07, 1.10, 1.20; substitute `Montserrat`.
- **Marlin**: 400, 700, 800, 16px, 46px, 0.93, 1.20; substitute `Montserrat`.
- **InterVariable**: 500, 600, 700, 12px, 17px, 1.20, 1.50; substitute `Inter`.

## Spacing / shape
- Section Gap: `48px`
- Card Padding: `24px`
- Element Gap: `24px`
- Radius: `links: 4px, default: 8px, buttons-pill: 22px`

## Surface cues
- **Canvas** `#ffffff`: Base page background, brightest surface for content.
- **Wash** `#fffcec`: Slightly elevated background for distinct sections or cards, providing subtle depth.
- **Highlight** `#fffadd`: Accent background primarily used in the hero, creating an additional layer of soft distinction.

## Component cues
- **Primary Ghost Button**: Primary Call to Action
- **Secondary Ghost Button**: Secondary Call to Action
- **Pill Download Button**: Download / Key Action
- **Navigation Link**: Primary Navigation
- **Feature Card**: Informational Display

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
