# Grafbase - Refero Design MD

- Source: https://styles.refero.design/style/1c1d3939-8d82-4907-aa3c-c9b2fcfbab4f
- Original site: https://grafbase.com
- Theme: `light`
- Industry: `devtools`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Architectural blueprint on white marble. The interface feels like a meticulously drafted technical diagram, laid out on a clean, bright surface.

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Ink | `#1b1b1b` | neutral | Primary text or dark surface |
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Cloud Gray | `#eaeaea` | neutral | Page background or card surface |
| Slate Text | `#60646c` | neutral | Border, muted text, or supporting surface |
| Ash Gray | `#7c7c7c` | neutral | Border, muted text, or supporting surface |
| Cloud Border | `#e0e1e6` | neutral | Page background or card surface |
| System Mint | `#8dc63f` | accent | Action accent / signal color |
| System Sky | `#27aae1` | accent | Action accent / signal color |
| Plasma Teal Gradient | `#19a05f` | brand | Action accent / signal color |

```css
:root {
  --ref-midnight-ink: #1b1b1b;
  --ref-canvas-white: #ffffff;
  --ref-cloud-gray: #eaeaea;
  --ref-slate-text: #60646c;
  --ref-ash-gray: #7c7c7c;
  --ref-cloud-border: #e0e1e6;
  --ref-system-mint: #8dc63f;
  --ref-system-sky: #27aae1;
}
```

## Typography direction
- **Inter**: 400, 500, 600, 700, 13px, 14px, 16px, 20px, 24px, 40px, 90px, 1.00, 1.10, 1.43, 1.50, 2.00; substitute `system-ui, sans-serif`.

## Spacing / shape
- Section Gap: `64px`
- Card Padding: `24px`
- Element Gap: `8px`
- Radius: `misc: 20px, cards: 12px, buttons: 6px`

## Component cues
- **CTA Button Group**: Reference component style.
- **Announcement Banner**: Reference component style.
- **Feature Comparison Cards**: Reference component style.
- **Primary Action Button**: Call to action
- **Secondary Ghost Button**: Alternative action

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
