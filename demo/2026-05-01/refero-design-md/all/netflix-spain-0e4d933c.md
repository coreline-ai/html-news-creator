# Netflix Spain - Refero Design MD

- Source: https://styles.refero.design/style/0e4d933c-aa07-4787-9884-40a0e6c338e4
- Original site: https://www.netflix.com
- Theme: `dark`
- Industry: `media`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Cinematic Dark Canvas – a deep, rich dark mode experience designed to make content pop like a spotlight on a stage.

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Absolute Zero | `#000000` | neutral | Primary text or dark surface |
| Ghost Gray | `#0f0f0f` | neutral | Primary text or dark surface |
| Charcoal Black | `#232323` | neutral | Primary text or dark surface |
| Slate Shadow | `#2d2d2d` | neutral | Primary text or dark surface |
| Ash Gray | `#323232` | neutral | Primary text or dark surface |
| Stone Gray | `#393939` | neutral | Primary text or dark surface |
| Medium Gray | `#414141` | neutral | Border, muted text, or supporting surface |
| Silver Mist | `#5a5a5a` | neutral | Border, muted text, or supporting surface |
| Dove Gray | `#808080` | neutral | Border, muted text, or supporting surface |
| Cloud White | `#ffffff` | neutral | Page background or card surface |

```css
:root {
  --ref-absolute-zero: #000000;
  --ref-ghost-gray: #0f0f0f;
  --ref-charcoal-black: #232323;
  --ref-slate-shadow: #2d2d2d;
  --ref-ash-gray: #323232;
  --ref-stone-gray: #393939;
  --ref-medium-gray: #414141;
  --ref-silver-mist: #5a5a5a;
}
```

## Typography direction
- **Netflix Sans**: 400, 10px, 12px, 13px, 14px, 16px, 20px, 24px, 1.00, 1.17, 1.20, 1.25, 1.50, 1.60; substitute `Inter`.
- **Netflix Sans**: 500, 10px, 12px, 13px, 14px, 1.00, 1.17, 1.20, 1.25, 1.50, 1.60; substitute `Inter`.
- **Netflix Sans**: 700, 10px, 12px, 13px, 14px, 16px, 20px, 24px, 56px, 1.00, 1.17, 1.20, 1.25, 1.50, 1.60; substitute `Inter`.

## Spacing / shape
- Section Gap: `64px`
- Card Padding: `12px`
- Element Gap: `12px`
- Radius: `cards: 8px, links: 2px, inputs: 0px, buttons: 4px`

## Component cues
- **Primary Action Button**: Button
- **Secondary Action Button**: Button
- **Ghost Button (White Border)**: Button
- **Muted Action Button**: Button
- **Media Carousel Card**: Card

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
