# Sandland Sleep - Refero Design MD

- Source: https://styles.refero.design/style/be17feca-c2bd-4e17-b4d2-ed3ae019a84c
- Original site: https://sandlandsleep.com
- Theme: `light`
- Industry: `ecommerce`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Calm twilight, soft edges

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Ink | `#1a365d` | brand | Action accent / signal color |
| Amber Glow | `#fae467` | accent | Action accent / signal color |
| Scarlet Flash | `#a42325` | accent | Action accent / signal color |
| Deepest Night | `#000000` | neutral | Primary text or dark surface |
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Ghost Fog | `#f2ede8` | neutral | Page background or card surface |
| Subtle Ash | `#e6e6e6` | neutral | Page background or card surface |
| Stone Gray | `#666666` | neutral | Border, muted text, or supporting surface |
| Pale Pebble | `#faf8f6` | neutral | Page background or card surface |
| Slate Border | `#726f6d` | neutral | Border, muted text, or supporting surface |

```css
:root {
  --ref-midnight-ink: #1a365d;
  --ref-amber-glow: #fae467;
  --ref-scarlet-flash: #a42325;
  --ref-deepest-night: #000000;
  --ref-canvas-white: #ffffff;
  --ref-ghost-fog: #f2ede8;
  --ref-subtle-ash: #e6e6e6;
  --ref-stone-gray: #666666;
}
```

## Typography direction
- **Sandland-550**: 400, 500, 600, 10px, 11px, 12px, 13px, 14px, 15px, 16px, 18px, 19px, 20px, 24px, 28px, 40px, 48px, 72px, 1.00, 1.10, 1.20, 1.30, 1.40, 1.60, 1.67; substitute `Open Sans`.
- **Inter**: 400, 14px, 24px, 1.10, 1.40; substitute `Inter`.
- **GTStandard-M**: 400, 14px, 1.50; substitute `Roboto`.

## Spacing / shape
- Section Gap: `44px`
- Card Padding: `30px`
- Element Gap: `8px`
- Page Max Width: `1200px`
- Radius: `cards: 10px, input: 0px, badges: 10px, buttons: 20px, circular-elements: 999px`

## Surface cues
- **Page Canvas** `#f2ede8`: Dominant background for the overall page structure.
- **Default Card Surface** `#ffffff`: Background for most content cards, providing a soft, slightly elevated context.
- **Elevated Card Surface** `#faf8f6`: Used for specific cards that require a subtle distinction from the default card, offering faint visual layering.

## Component cues
- **Primary Action Button**: Call to action
- **Ghost Outline Button**: Secondary action
- **Neutral Button**: Tertiary action
- **Default Card**: Content container
- **Elevated Content Card**: Prominent content display

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
