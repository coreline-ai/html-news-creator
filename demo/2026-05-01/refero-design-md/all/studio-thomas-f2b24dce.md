# Studio Thomas - Refero Design MD

- Source: https://styles.refero.design/style/f2b24dce-5b1f-47c2-8ef6-bbbd08b68826
- Original site: https://studiothomas.co.uk
- Theme: `light`
- Industry: `design`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Vivid Orange Canvas

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Ink | `#000000` | neutral | Primary text or dark surface |
| Cloud Petal | `#ebe9e3` | neutral | Page background or card surface |
| Paper White | `#ffffff` | neutral | Page background or card surface |
| Titanium Grey | `#767676` | neutral | Border, muted text, or supporting surface |
| Impact Orange | `#ff4f00` | brand | Action accent / signal color |

```css
:root {
  --ref-midnight-ink: #000000;
  --ref-cloud-petal: #ebe9e3;
  --ref-paper-white: #ffffff;
  --ref-titanium-grey: #767676;
  --ref-impact-orange: #ff4f00;
}
```

## Typography direction
- **Moderat**: 300, 400, 16px, 33px, 40px, 120px, 1.00, 1.13, 1.20, 1.25, 1.60; substitute `Inter`.

## Spacing / shape
- Section Gap: `40px`
- Card Padding: `20px`
- Element Gap: `30px`
- Radius: `default: 0px`

## Component cues
- **Ghost Button**: Call-to-action or secondary navigation button
- **Project Link**: Navigation for project showcases
- **Basic Form Input**: Standard text input field
- **Main Navigation Toggle**: Hamburger icon for mobile/secondary navigation
- **Hero Headline**: Primary attention-grabbing text on the hero section

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
