# Contractbook - Refero Design MD

- Source: https://styles.refero.design/style/fbc60c55-da20-4684-a279-0ed86590272e
- Original site: https://contractbook.com
- Theme: `light`
- Industry: `saas`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Playful professionalism, high-contrast clarity.

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Washed Black | `#1a1a1a` | neutral | Primary text or dark surface |
| Pure White | `#ffffff` | neutral | Page background or card surface |
| Pearl | `#f7f7f3` | neutral | Page background or card surface |
| Beige | `#f0f0ec` | neutral | Page background or card surface |
| Ink Black | `#000000` | neutral | Primary text or dark surface |
| Concrete | `#d4d4d0` | neutral | Border, muted text, or supporting surface |
| Dim Grey | `#6d6868` | neutral | Border, muted text, or supporting surface |
| Silver Mist | `#b3b3b3` | neutral | Border, muted text, or supporting surface |
| Royal Blue | `#1009f6` | brand | Action accent / signal color |
| Energy Gold | `#ffba09` | brand | Action accent / signal color |

```css
:root {
  --ref-washed-black: #1a1a1a;
  --ref-pure-white: #ffffff;
  --ref-pearl: #f7f7f3;
  --ref-beige: #f0f0ec;
  --ref-ink-black: #000000;
  --ref-concrete: #d4d4d0;
  --ref-dim-grey: #6d6868;
  --ref-silver-mist: #b3b3b3;
}
```

## Typography direction
- **Abcwhyte**: 400, 700, 11px, 12px, 14px, 16px, 25px, 28px, 32px, 40px, 48px, 1.00, 1.20, 1.24, 1.25, 1.30, 1.40, 1.43, 1.50, 1.60, 1.87; substitute `Inter`.

## Spacing / shape
- Section Gap: `60px`
- Card Padding: `14px`
- Element Gap: `14px`
- Radius: `tags: 9999px, cards: 24px, images: 40px, inputs: 4.375px, buttons: 999px`

## Surface cues
- **Page Canvas** `#ffffff`: Dominant background for the entire page, providing a clean base.
- **Subtle Section** `#f7f7f3`: Background for alternating content sections, offering a gentle visual break.
- **Interactive Surface** `#f0f0ec`: Background for input fields and secondary cards, hinting at interactivity and slightly receding.

## Component cues
- **Primary Action Button**: Call to action
- **Secondary Ghost Button (Dark Text)**: Secondary action
- **Secondary Ghost Button (Light Text)**: Secondary action
- **Accent Card - Royal Blue**: Content container
- **Accent Card - Beige**: Content container

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
