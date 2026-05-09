# Tilda - Refero Design MD

- Source: https://styles.refero.design/style/6d8dc9bb-78b7-4eaa-9b08-66b431760e9f
- Original site: https://tilda.cc
- Theme: `light`
- Industry: `saas`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Architectural blueprint on white marble. Clean lines and a single warm accent define a space where work feels like play.

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Arctic White | `#ffffff` | neutral | Page background or card surface |
| Ink Black | `#000000` | neutral | Primary text or dark surface |
| Cloud Gray | `#efefef` | neutral | Page background or card surface |
| Graphite | `#222222` | neutral | Primary text or dark surface |
| Pebble | `#cccccc` | neutral | Border, muted text, or supporting surface |
| Warm Peach | `#fa8669` | brand | Action accent / signal color |
| Soft Peach | `#ffa282` | accent | Action accent / signal color |

```css
:root {
  --ref-arctic-white: #ffffff;
  --ref-ink-black: #000000;
  --ref-cloud-gray: #efefef;
  --ref-graphite: #222222;
  --ref-pebble: #cccccc;
  --ref-warm-peach: #fa8669;
  --ref-soft-peach: #ffa282;
}
```

## Typography direction
- **TildaSans**: 100, 300, 400, 500, 600, 700, All headline and most body text sizes. Its range of weights from 100 to 700 allows for distinct typographic hierarchy., 1.13-2.00; substitute `Inter`.
- **Arial**: 100, 300, 400, 500, 11px, 13px, 14px, 1.20-2.00; substitute `Roboto`.
- **Times**: 400, 16px, 1.20; substitute `Merriweather`.

## Spacing / shape
- Radius: `cards: 0px, maintaining a sharp, structured aesthetic., other: Occasional 6px or 30px for specific UI elements, breaking the sharpness for specific interactive elements., buttons: 100px for pill shapes, or 60px for softer rounded rectangles.`

## Component cues
- **CTA Button Group**: Reference component style.
- **Pricing Plan Cards**: Reference component style.
- **Feature Stat Block**: Reference component style.
- **Primary Filled Button**: Call-to-action button for core actions like 'Sign up' or 'Create a website'.
- **Ghost Button (Primary)**: Secondary call-to-action or navigational element.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
