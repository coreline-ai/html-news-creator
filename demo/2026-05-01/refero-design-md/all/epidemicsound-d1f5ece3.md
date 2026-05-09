# Epidemicsound - Refero Design MD

- Source: https://styles.refero.design/style/d1f5ece3-ec6c-467d-8a59-51ee259cc023
- Original site: https://epidemicsound.com
- Theme: `light`
- Industry: `media`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Crisp Paper, Bold Ink. Like a freshly printed document with critical information highlighted in vibrant markers.

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Ink | `#000000` | neutral | Primary text or dark surface |
| Cloud White | `#ffffff` | neutral | Page background or card surface |
| Paper Gray | `#f1f0eb` | neutral | Page background or card surface |
| Ash Gray | `#efefef` | neutral | Page background or card surface |
| Light Steel | `#cfd6e5` | neutral | Border, muted text, or supporting surface |
| Rose Pop | `#ff82c2` | accent | Action accent / signal color |
| Electric Blue | `#20afff` | accent | Action accent / signal color |
| Lemon Zest | `#ffda40` | accent | Action accent / signal color |

```css
:root {
  --ref-midnight-ink: #000000;
  --ref-cloud-white: #ffffff;
  --ref-paper-gray: #f1f0eb;
  --ref-ash-gray: #efefef;
  --ref-light-steel: #cfd6e5;
  --ref-rose-pop: #ff82c2;
  --ref-electric-blue: #20afff;
  --ref-lemon-zest: #ffda40;
}
```

## Typography direction
- **Inter**: 400, 500, 600, 700, 10px, 12px, 14px, 16px, 18px, 24px, 1.00, 1.15, 1.33, 1.50, 1.56, 1.60, 1.71; substitute `system-ui, sans-serif`.
- **sebentaFont**: 500, 20px, 24px, 32px, 40px, 48px, 64px, 80px, 128px, 1.00, 1.06, 1.13, 1.20, 1.25; substitute `Georgia, serif`.

## Spacing / shape
- Section Gap: `40px`
- Card Padding: `40px`
- Element Gap: `8px`
- Radius: `cards: 0px, badges: 9999px, buttons: 0px`

## Component cues
- **CTA Button Group**: Reference component style.
- **Promotional Highlight Card (Studio Feature)**: Reference component style.
- **FAQ Accordion**: Reference component style.
- **Primary Action Button (Dark)**: Call to action
- **Secondary Action Button (Light)**: Secondary action or navigation

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
