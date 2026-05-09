# Motto® - Refero Design MD

- Source: https://styles.refero.design/style/6eb5fc89-d0db-4293-8bff-13c5aa530a28
- Original site: https://wearemotto.com
- Theme: `light`
- Industry: `agency`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Architectural Blueprint on White Canvas. Black lines and precise typography articulate structure and ideas against an expansive, bright background.

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Pitch Black | `#000000` | neutral | Primary text or dark surface |
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Charcoal Surface | `#1b1b1c` | neutral | Primary text or dark surface |
| Cloud Gray | `#f2f2f2` | neutral | Page background or card surface |
| Stone Accent | `#d8d8d8` | neutral | Border, muted text, or supporting surface |
| Ash Text | `#4d5153` | neutral | Border, muted text, or supporting surface |
| Silver Text | `#848484` | neutral | Border, muted text, or supporting surface |
| Input Border | `#c8cacd` | neutral | Border, muted text, or supporting surface |
| Faint Gray | `#717476` | neutral | Border, muted text, or supporting surface |
| Vivid Purple | `#9c98ef` | accent | Action accent / signal color |

```css
:root {
  --ref-pitch-black: #000000;
  --ref-canvas-white: #ffffff;
  --ref-charcoal-surface: #1b1b1c;
  --ref-cloud-gray: #f2f2f2;
  --ref-stone-accent: #d8d8d8;
  --ref-ash-text: #4d5153;
  --ref-silver-text: #848484;
  --ref-input-border: #c8cacd;
}
```

## Typography direction
- **sans**: 500, 14px, 15px, 17px, 18px, 20px, 25px, 34px, 48px, 1.14, 1.26, 1.30, 1.38, 1.40, 1.60; substitute `Inter, Arial, Helvetica, sans-serif`.
- **disp**: 500, 61px, 99px, 138px, 139px, 154px, 1.00, 1.10; substitute `Oswald, Impact, sans-serif`.

## Spacing / shape
- Section Gap: `48px`
- Card Padding: `0px`
- Radius: `cards: 0px, buttons: 9999px`

## Component cues
- **Services Tag Strip**: Reference component style.
- **Testimonial Card**: Reference component style.
- **Section Header with CTA**: Reference component style.
- **Navigation Link**: Standard interactive navigation item
- **Ghost Button (Text)**: Secondary action or informational link styled as a button

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
