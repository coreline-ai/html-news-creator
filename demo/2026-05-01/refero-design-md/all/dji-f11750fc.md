# DJI - Refero Design MD

- Source: https://styles.refero.design/style/f11750fc-d7c0-4d26-b32a-3b1d2098ae34
- Original site: https://dji.com
- Theme: `light`
- Industry: `ecommerce`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Precision instrument display. A stark, high-contrast digital interface where light and shadow define advanced technology.

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Void | `#000000` | neutral | Primary text or dark surface |
| Arctic Snow | `#ffffff` | neutral | Page background or card surface |
| Glacial White | `#f7f9fa` | neutral | Page background or card surface |
| Platinum Gray | `#ededed` | neutral | Page background or card surface |
| Charcoal Black | `#272727` | neutral | Primary text or dark surface |
| Shadow Ink | `#040404` | neutral | Primary text or dark surface |
| Storm Gray | `#6c7073` | neutral | Border, muted text, or supporting surface |
| Slate Text | `#595959` | neutral | Border, muted text, or supporting surface |
| Phantom Gray | `#303233` | neutral | Primary text or dark surface |
| Ash Gray | `#8c8c8c` | neutral | Border, muted text, or supporting surface |

```css
:root {
  --ref-midnight-void: #000000;
  --ref-arctic-snow: #ffffff;
  --ref-glacial-white: #f7f9fa;
  --ref-platinum-gray: #ededed;
  --ref-charcoal-black: #272727;
  --ref-shadow-ink: #040404;
  --ref-storm-gray: #6c7073;
  --ref-slate-text: #595959;
}
```

## Typography direction
- **Open Sans**: 300, 400, 500, 600, 12px, 14px, 16px, 18px, 20px, 24px, 32px, 40px, 1.00, 1.10, 1.13, 1.17, 1.20, 1.25, 1.33, 1.43, 1.50, 2.00; substitute `system-ui, sans-serif`.
- **Arial**: 400, 13px, 1.20; substitute `system-ui, sans-serif`.

## Spacing / shape
- Card Padding: `16px`
- Radius: `cards: 4px, inputs: 4px, buttons: 64px, navButtons: 99px, specialNav: 1408px, heroElements: 60px`

## Component cues
- **Product Cards Grid**: Reference component style.
- **Announcement Banner**: Reference component style.
- **Button Group & CTA**: Reference component style.
- **Primary Navigation Link**: Main navigation items
- **Global Call to Action Button (Blue)**: Main calls to action

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
