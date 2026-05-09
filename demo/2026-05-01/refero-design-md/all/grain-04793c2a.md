# Grain - Refero Design MD

- Source: https://styles.refero.design/style/04793c2a-ca1a-4edd-a661-56c965e42aec
- Original site: https://www.grain.com
- Theme: `light`
- Industry: `ai`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Bright AI green, focused workflow.

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#fafafa` | neutral | Page background or card surface |
| Rich Black | `#000000` | neutral | Primary text or dark surface |
| Deep Graphite | `#313232` | neutral | Primary text or dark surface |
| Inkwell | `#141414` | neutral | Primary text or dark surface |
| Dusk Gray | `#707070` | neutral | Border, muted text, or supporting surface |
| Cloud Gray | `#f0f0f0` | neutral | Page background or card surface |
| Muted Stone | `#545454` | neutral | Border, muted text, or supporting surface |
| Silver Dust | `#c9c9c9` | neutral | Border, muted text, or supporting surface |
| Pewter | `#949494` | neutral | Border, muted text, or supporting surface |
| Pale Ash | `#d6d6d6` | neutral | Border, muted text, or supporting surface |

```css
:root {
  --ref-canvas-white: #fafafa;
  --ref-rich-black: #000000;
  --ref-deep-graphite: #313232;
  --ref-inkwell: #141414;
  --ref-dusk-gray: #707070;
  --ref-cloud-gray: #f0f0f0;
  --ref-muted-stone: #545454;
  --ref-silver-dust: #c9c9c9;
}
```

## Typography direction
- **Inter Variablefont Slnt Wght**: 400, 500, 600, 12px, 13px, 14px, 16px, 18px, 20px, 32px, 36px, 1.30, 1.43, 1.50, 1.60; substitute `Inter`.
- **Poppins**: 600, 38px, 1.25; substitute `Poppins`.

## Spacing / shape
- Section Gap: `96px`
- Card Padding: `24px`
- Element Gap: `8px`
- Radius: `tags: 24px, cards: 10px, icons: 10px, images: 14px, buttons: 8px, default: 10px, heroElements: 2px`

## Component cues
- **Primary Filled Button**: Call to Action
- **Ghost Button**: Secondary Action
- **Tertiary Minimal Button**: Inline Action/Navigation
- **Accent Filled Button**: Contextual Action
- **Feature Card**: Content Grouping

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
