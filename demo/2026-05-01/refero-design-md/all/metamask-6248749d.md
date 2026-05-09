# Metamask - Refero Design MD

- Source: https://styles.refero.design/style/6248749d-b440-4561-b4d7-2d39c0fd4fd3
- Original site: https://metamask.io
- Theme: `light`
- Industry: `crypto`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Playful, chunky, soft-edge vibrancy.

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Pale Canvas | `#fff1eb` | neutral | Page background or card surface |
| Ghost White | `#ffffff` | neutral | Page background or card surface |
| Pitch Black | `#0a0a0a` | neutral | Primary text or dark surface |
| Slate Gray | `#e9edf6` | neutral | Page background or card surface |
| Dusty Teal | `#013330` | neutral | Primary text or dark surface |
| Phantom Gray | `#393d46` | neutral | Primary text or dark surface |
| Lavender Bloom | `#eac2ff` | brand | Action accent / signal color |
| Electric Violet | `#3d065f` | brand | Action accent / signal color |
| Sunlit Lime | `#e5ffc3` | brand | Action accent / signal color |
| Sunset Orange | `#ffa680` | brand | Action accent / signal color |

```css
:root {
  --ref-pale-canvas: #fff1eb;
  --ref-ghost-white: #ffffff;
  --ref-pitch-black: #0a0a0a;
  --ref-slate-gray: #e9edf6;
  --ref-dusty-teal: #013330;
  --ref-phantom-gray: #393d46;
  --ref-lavender-bloom: #eac2ff;
  --ref-electric-violet: #3d065f;
}
```

## Typography direction
- **MMEuclidCircularB**: 400, 500, 700, 8px, 12px, 13px, 14px, 15px, 16px, 24px, 0.80, 1.00, 1.05, 1.20, 1.24, 1.31, 1.50, 1.65; substitute `Euclid Circular B`.
- **MMSansVariable**: 400, 500, 600, 16px, 24px, 1.00; substitute `Inter`.
- **MMPolyVariable**: 400, 32px, 48px, 75px, 127px, 158px, 1.00, 1.10, 1.16, 1.25; substitute `Oswald`.

## Spacing / shape
- Section Gap: `32px`
- Card Padding: `12px`
- Element Gap: `6px`
- Radius: `cards: 7.91667px, badges: 2.96875px, inputs: 39.5833px, buttons: 98.9583px, default: 69.2708px`

## Component cues
- **Ghost Button**: Secondary action or navigation element.
- **Pill Ghost Button**: Compact navigation or action chip.
- **Square Ghost Button**: Icon-only or minimal action button.
- **Filled Pill Button (Primary)**: Primary call to action.
- **Neutral Information Card**: Standard content grouping.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
