# Le Puzz - Refero Design MD

- Source: https://styles.refero.design/style/66e7b131-d68c-4751-954c-f5d0d8869647
- Original site: https://lepuzz.com
- Theme: `light`
- Industry: `ecommerce`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Playful Pop-Art Canvas

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Sunshine Yellow | `#ffd931` | brand | Action accent / signal color |
| Midnight Ink | `#231f20` | neutral | Primary text or dark surface |
| Coal Black | `#000000` | neutral | Primary text or dark surface |
| Soft Stone | `#c8cbcd` | neutral | Border, muted text, or supporting surface |
| Badge Gray | `#a6a8aa` | neutral | Border, muted text, or supporting surface |
| Whisper White | `#d6d6d6` | neutral | Border, muted text, or supporting surface |

```css
:root {
  --ref-sunshine-yellow: #ffd931;
  --ref-midnight-ink: #231f20;
  --ref-coal-black: #000000;
  --ref-soft-stone: #c8cbcd;
  --ref-badge-gray: #a6a8aa;
  --ref-whisper-white: #d6d6d6;
}
```

## Typography direction
- **Times New Roman**: 400, 16px, 1.15; substitute `Times`.
- **Helvetica Neue**: 100, 400, 11px, 1.15, 2.27; substitute `Arial`.
- **Helvetica**: 100, 300, 400, 11px, 13px, 14px, 16px, 40px, 0.90, 1.15, 1.38, 1.56, 2.63; substitute `Arial`.

## Spacing / shape
- Section Gap: `30px`
- Card Padding: `15px`
- Element Gap: `15px`
- Radius: `cards: 0px, badges: 10px, images: 0px, buttons: 12px, pillButtons: 25px`

## Surface cues
- **Soft Stone Background** `#c8cbcd`: Default page background, providing a light, cool canvas.
- **Sunshine Canvas** `#ffd931`: Primary surface for header, footer, and prominent content blocks, drawing immediate attention.
- **Badge Gray Surface** `#a6a8aa`: Elevated informational elements like status badges, providing a distinct, darker gray surface.
- **Midnight Accent** `#231f20`: Darkest surface for text and strong accents, creating the highest contrast.

## Component cues
- **Primary Filled Button**: Call to action, primary interaction
- **Ghost Button**: Secondary action in a neutral context
- **Product Card**: Product display with minimal styling
- **Shop Badge - Sold**: Status indicator for product availability
- **Header Navigation Link**: Top-level navigation

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
