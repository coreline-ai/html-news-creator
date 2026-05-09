# Promova - Refero Design MD

- Source: https://styles.refero.design/style/dae5e893-ca18-44c3-8f83-358cb52af237
- Original site: https://promova.com
- Theme: `dark`
- Industry: `other`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
layered pastel blocks on a dark canvas

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Ink | `#000000` | neutral | Primary text or dark surface |
| Cloud White | `#ffffff` | neutral | Page background or card surface |
| Pebble Gray | `#595959` | neutral | Border, muted text, or supporting surface |
| Soft Mist | `#f5f5f5` | neutral | Page background or card surface |
| Limoncello | `#fff050` | brand | Action accent / signal color |
| Sky Haze | `#eceeff` | accent | Action accent / signal color |
| Misty Meadow | `#f4f9e7` | accent | Action accent / signal color |
| Lavender Dream | `#dfe3ff` | accent | Action accent / signal color |
| Periwinkle Charm | `#bec8ff` | accent | Action accent / signal color |

```css
:root {
  --ref-midnight-ink: #000000;
  --ref-cloud-white: #ffffff;
  --ref-pebble-gray: #595959;
  --ref-soft-mist: #f5f5f5;
  --ref-limoncello: #fff050;
  --ref-sky-haze: #eceeff;
  --ref-misty-meadow: #f4f9e7;
  --ref-lavender-dream: #dfe3ff;
}
```

## Typography direction
- **Manrope**: 200, 400, 500, 700, 10px, 14px, 15px, 16px, 18px, 20px, 24px, 25px, 140px, 1.00, 1.20, 1.40, 1.42, 1.44, 1.50, 1.67; substitute `system-ui`.
- **Nekst**: 400, 14px, 15px, 16px, 18px, 19px, 24px, 40px, 50px, 60px, 70px, 100px, 120px, 1.00, 1.20, 1.67.

## Spacing / shape
- Section Gap: `40px`
- Card Padding: `30px`
- Element Gap: `10px`
- Radius: `cards: 30px, small: 4px, buttons: 20px, general: 10px`

## Component cues
- **Promotional Modal Card**: Reference component style.
- **Button Group — Primary & Secondary**: Reference component style.
- **FAQ Accordion**: Reference component style.
- **Secondary Outlined Button**: Secondary action button with border
- **Ghost Navigation Button**: Minimal navigation item or tertiary action

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
