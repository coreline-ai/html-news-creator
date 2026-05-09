# ElevenReader - Refero Design MD

- Source: https://styles.refero.design/style/c51c8371-0e42-4bdf-9766-c9eac5eee9a5
- Original site: https://elevenreader.io
- Theme: `light`
- Industry: `productivity`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
diffused light on a minimalist stage

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Ink | `#000000` | neutral | Primary text or dark surface |
| Cloud White | `#ffffff` | neutral | Page background or card surface |
| Ash Gray | `#e5e5e5` | neutral | Page background or card surface |
| Pale Mist | `#f2f2f2` | neutral | Page background or card surface |
| Faded Sky | `#f2f5fc` | neutral | Page background or card surface |
| Steel Gray | `#767676` | neutral | Border, muted text, or supporting surface |
| Muted Lavender | `#c8d5f4` | neutral | Border, muted text, or supporting surface |
| Verdant Aura | `#243f2b` | accent | Action accent / signal color |
| Forest Dew | `#c6e7d6` | accent | Action accent / signal color |

```css
:root {
  --ref-midnight-ink: #000000;
  --ref-cloud-white: #ffffff;
  --ref-ash-gray: #e5e5e5;
  --ref-pale-mist: #f2f2f2;
  --ref-faded-sky: #f2f5fc;
  --ref-steel-gray: #767676;
  --ref-muted-lavender: #c8d5f4;
  --ref-verdant-aura: #243f2b;
}
```

## Typography direction
- **WaldenburgHF**: 700, 28px, 32px, 48px, 1.10; substitute `Inter`.
- **Inter**: 400, 700, 12px, 14px, 16px, 18px, 1.10, 1.40, 1.43, 1.60; substitute `system-ui`.

## Spacing / shape
- Section Gap: `40px`
- Card Padding: `0px`
- Element Gap: `8px`
- Page Max Width: `1304px`
- Radius: `cards: 16px, links: 2px, buttons: 9999px, ctaCard: 30px`

## Component cues
- **CTA Button Group**: Reference component style.
- **FAQ Accordion**: Reference component style.
- **App Download QR Card**: Reference component style.
- **Secondary Action Button**: Filled button for secondary actions.
- **Tertiary Action Button**: Outline button for less prominent actions.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
