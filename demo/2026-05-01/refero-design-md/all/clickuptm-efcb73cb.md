# ClickUp™ - Refero Design MD

- Source: https://styles.refero.design/style/efcb73cb-b84a-4ae7-9a2b-e1116f79f130
- Original site: https://www.clickup.com
- Theme: `light`
- Industry: `productivity`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Vibrant productivity hub: a dynamic workspace with energetic highlights.

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Midnight Charcoal | `#292d34` | neutral | Primary text or dark surface |
| Dark Onyx | `#202023` | neutral | Primary text or dark surface |
| Ash Gray | `#e8e8e8` | neutral | Page background or card surface |
| Smoke Gray | `#b3b3b3` | neutral | Border, muted text, or supporting surface |
| Hint of Sky | `#e9ebf0` | neutral | Page background or card surface |
| Shadow Tint Blue | `#edf6fd` | neutral | Action accent / signal color |
| Deep Violet | `#7b68ee` | brand | Action accent / signal color |
| Electric Blue | `#0091ff` | brand | Action accent / signal color |
| Rich Plum | `#514b81` | brand | Action accent / signal color |

```css
:root {
  --ref-canvas-white: #ffffff;
  --ref-midnight-charcoal: #292d34;
  --ref-dark-onyx: #202023;
  --ref-ash-gray: #e8e8e8;
  --ref-smoke-gray: #b3b3b3;
  --ref-hint-of-sky: #e9ebf0;
  --ref-shadow-tint-blue: #edf6fd;
  --ref-deep-violet: #7b68ee;
}
```

## Typography direction
- **Plus Jakarta Sans**: 400, 500, 650, 700, 800, 14px, 16px, 26px, 34px, 40px, 42px, 48px, 52px, 60px, 76px, 1.05, 1.10, 1.12, 1.14, 1.18, 1.20, 1.25, 1.43, 1.50; substitute `system-ui, sans-serif`.
- **Inter**: 400, 500, 600, 650, 700, 8px, 9px, 12px, 13px, 14px, 15px, 16px, 17px, 18px, 19px, 1.00, 1.14, 1.33, 1.37, 1.38, 1.43, 1.50; substitute `system-ui, sans-serif`.
- **Sometype Mono**: 400, 500, 12px, 14px, 16px, 24px, 40px, 1.25, 1.29, 1.38, 1.43; substitute `monospace`.

## Spacing / shape
- Section Gap: `24px`
- Card Padding: `12px`
- Element Gap: `9px`
- Page Max Width: `1px`
- Radius: `cards: 12px, pills: 54px, buttons: 9px, default: 9px, largeCards: 24px, circularElements: 653px`

## Surface cues
- **Canvas White** `#ffffff`: Primary page background and default container surface.
- **Hint of Sky** `#e9ebf0`: Subtle background for alternating content sections, providing a soft shift in visual depth.
- **Feature Card Surface** `#ffffff`: Elevated card backgrounds with a soft shadow to indicate interactive or contained content.
- **Shadow Tint Blue** `#edf6fd`: Light background for interactive states or subtle focus elements.

## Component cues
- **Primary Filled Button**: Call to action
- **Ghost Button**: Secondary action
- **Pill Button**: Tertiary action/Tag
- **Outline Button**: Bordered action/Navigation element
- **Feature Card**: Content container

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
