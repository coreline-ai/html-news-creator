# Flutterwave Design - Refero Design MD

- Source: https://styles.refero.design/style/97bbc1bd-873f-4048-b4cc-b20ea2e70097
- Original site: https://www.flutterwave.design
- Theme: `light`
- Industry: `design`
- Recommended fit: **Design reference / webapp exploration**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
High-contrast digital artboard

## Apply to
- General webapp UI exploration
- Demo cards and catalog surfaces
- Future admin/subscriber UI references

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Cloud Canvas | `#fff9f1` | neutral | Page background or card surface |
| Storm Gray | `#171717` | neutral | Primary text or dark surface |
| Deep Ink | `#12122c` | neutral | Primary text or dark surface |
| Silver Mist | `#b5b5b5` | neutral | Border, muted text, or supporting surface |
| Ash Stone | `#8b8b8b` | neutral | Border, muted text, or supporting surface |
| Eclipse | `#000000` | neutral | Primary text or dark surface |
| Marigold Glow | `#f5a623` | accent | Action accent / signal color |

```css
:root {
  --ref-cloud-canvas: #fff9f1;
  --ref-storm-gray: #171717;
  --ref-deep-ink: #12122c;
  --ref-silver-mist: #b5b5b5;
  --ref-ash-stone: #8b8b8b;
  --ref-eclipse: #000000;
  --ref-marigold-glow: #f5a623;
}
```

## Typography direction
- **Moderat**: 400, 500, 600, 700, 12px, 14px, 16px, 18px, 20px, 22px, 1.18, 1.20, 1.60, 1.63; substitute `Inter`.
- **Millik**: 700, 800, 32px, 60px, 1.20; substitute `Montserrat`.
- **Flutterwave**: 400, 14px, 16px, 1.20; substitute `Roboto`.

## Spacing / shape
- Section Gap: `60px`
- Card Padding: `20px`
- Element Gap: `10px`
- Radius: `cards: 5px, other: 5px, inputs: 5px, buttons: 5px`

## Surface cues
- **Cloud Canvas** `#fff9f1`: Base page background, light and airy foundation.
- **Silver Mist** `#b5b5b5`: Secondary background for cards or subtle content distinctions, a slightly darker neutral tint.
- **Ash Stone** `#8b8b8b`: Tertiary background, hinting at layered depth or subtle segmentation.

## Component cues
- **Subscribe Button**: Primary call-to-action button, featuring a distinct compound radius.
- **Article Card (Curved Carousel)**: Display individual articles within a visually engaging, curved hero carousel.
- **Standard Article Card**: Display individual articles in a grid layout, focusing on visual clarity and content hierarchy.
- **Subscription Input Field**: User input field for email subscriptions, paired with a button.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
