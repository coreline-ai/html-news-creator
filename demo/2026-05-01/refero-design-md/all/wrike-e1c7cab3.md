# Wrike - Refero Design MD

- Source: https://styles.refero.design/style/e1c7cab3-dae7-47c3-bb2c-c8f616a8124f
- Original site: https://wrike.com
- Theme: `light`
- Industry: `productivity`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Organized Digital Workspace — like well-lit, interactive blueprints on a high-resolution display.

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Graphite | `#162136` | neutral | Primary text or dark surface |
| Cloud White | `#ffffff` | neutral | Page background or card surface |
| Subtle Gray | `#f2f5fa` | neutral | Page background or card surface |
| Slate Indigo | `#2b3a57` | neutral | Primary text or dark surface |
| System Blue | `#0073d3` | accent | Action accent / signal color |
| Wrike Green | `#00e05c` | brand | Action accent / signal color |
| Ash Gray | `#657694` | neutral | Border, muted text, or supporting surface |
| Light Cloud | `#c1c9d8` | neutral | Border, muted text, or supporting surface |
| Deep Space Gradient | `#00b259` | brand | Action accent / signal color |

```css
:root {
  --ref-midnight-graphite: #162136;
  --ref-cloud-white: #ffffff;
  --ref-subtle-gray: #f2f5fa;
  --ref-slate-indigo: #2b3a57;
  --ref-system-blue: #0073d3;
  --ref-wrike-green: #00e05c;
  --ref-ash-gray: #657694;
  --ref-light-cloud: #c1c9d8;
}
```

## Typography direction
- **TT Norms Pro**: 400, 600, 700, 12px, 13px, 14px, 16px, 18px, 20px, 24px, 32px, 48px, 64px, 1.10, 1.20, 1.25, 1.30, 1.38, 1.40, 1.50, 1.60, 2.00; substitute `Inter`.

## Spacing / shape
- Section Gap: `64px`
- Element Gap: `4px`
- Page Max Width: `1220px`
- Radius: `cards: 20px, input: 0px, buttons: 12px, largeButton: 40px, smallButton: 4px`

## Component cues
- **CTA Button Group**: Reference component style.
- **AI Feature Cards**: Reference component style.
- **Dark CTA Banner with Email Input**: Reference component style.
- **Secondary Ghost Button**: Subordinate action
- **Pill Ghost Button**: Navigation or tertiary action

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
