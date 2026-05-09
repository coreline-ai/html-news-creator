# MA Quilts - Refero Design MD

- Source: https://styles.refero.design/style/6d4ef8f4-badd-4e3c-a168-0cc89c833b26
- Original site: https://maquilts.com
- Theme: `light`
- Industry: `design`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Joyful Quilted Canvas

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Text Black | `#000000` | neutral | Primary text or dark surface |
| Accent Orange | `#f15a24` | brand | Action accent / signal color |
| Canary Yellow | `#ffed8c` | accent | Action accent / signal color |
| Midnight Ink | `#050133` | accent | Action accent / signal color |
| Secondary Text Gray | `#333333` | neutral | Primary text or dark surface |
| Utility Gray | `#cce1e2` | neutral | Page background or card surface |

```css
:root {
  --ref-canvas-white: #ffffff;
  --ref-text-black: #000000;
  --ref-accent-orange: #f15a24;
  --ref-canary-yellow: #ffed8c;
  --ref-midnight-ink: #050133;
  --ref-secondary-text-gray: #333333;
  --ref-utility-gray: #cce1e2;
}
```

## Typography direction
- **Manrope**: 200, 400, 700, 23px, 29px, 30px, 36px, 60px, 68px, 72px, 126px, 1.00, 1.20, 1.40, 2.00, 2.40; substitute `Inter`.
- **Roboto Mono**: 400, 700, 14px, 18px, 30px, 1.60, 2.00; substitute `Space Mono`.

## Spacing / shape
- Section Gap: `54px`
- Card Padding: `46px`
- Element Gap: `14px`
- Radius: `buttons: 66px`

## Component cues
- **Primary Outlined Button**: Call to action button
- **Hero Headline**: Largest display text
- **Section Headline**: Major section titles
- **Nav Link**: Main navigation item
- **Image Card Footer**: Caption for product or blog post image

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
