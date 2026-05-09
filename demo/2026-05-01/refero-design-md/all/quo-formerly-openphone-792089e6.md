# Quo (formerly OpenPhone) - Refero Design MD

- Source: https://styles.refero.design/style/792089e6-c045-498c-8ba1-48d72c206c66
- Original site: https://www.openphone.com
- Theme: `light`
- Industry: `saas`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
High-contrast digital workspace.

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Ink Black | `#000000` | neutral | Primary text or dark surface |
| Surface Gray | `#f7f6f5` | neutral | Page background or card surface |
| Supporting Text Grey | `#4d4d4d` | neutral | Border, muted text, or supporting surface |
| Subtle Border Gray | `#cccccc` | neutral | Border, muted text, or supporting surface |
| Dark Charcoal | `#0a0a0c` | neutral | Primary text or dark surface |
| Lime Accent | `#edfc47` | accent | Action accent / signal color |

```css
:root {
  --ref-canvas-white: #ffffff;
  --ref-ink-black: #000000;
  --ref-surface-gray: #f7f6f5;
  --ref-supporting-text-grey: #4d4d4d;
  --ref-subtle-border-gray: #cccccc;
  --ref-dark-charcoal: #0a0a0c;
  --ref-lime-accent: #edfc47;
}
```

## Typography direction
- **Inter**: 400, 500, 600, 12px, 14px, 16px, 18px, 20px, 1.00, 1.20, 1.30, 1.50; substitute `system-ui`.
- **Roobert**: 500, 20px, 24px, 40px, 48px, 56px, 64px, 88px, 0.90, 1.10, 1.20; substitute `Arial`.

## Spacing / shape
- Section Gap: `48px`
- Card Padding: `16px`
- Element Gap: `16px`
- Page Max Width: `1200px`
- Radius: `tags: 100px, cards: 10px, buttons: 6px, default: 10px`

## Component cues
- **Primary Filled Button**: Call to action
- **Ghost Button**: Secondary action / navigation link
- **Soft Filled Button**: Light background action / tag
- **Default Card**: Content container
- **Surface Accent Card**: Information display

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
