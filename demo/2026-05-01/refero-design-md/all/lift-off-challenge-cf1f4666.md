# Lift-off challenge - Refero Design MD

- Source: https://styles.refero.design/style/cf1f4666-bb5b-4fc4-a3e6-660218996cbb
- Original site: https://liftoffchallenge.hypr-space.com
- Theme: `light`
- Industry: `other`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Aircraft control panel — high-contrast modular interfaces on a rigid, light-grey chassis with urgent red signals.

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Control Panel Grey | `#e5e7eb` | neutral | Page background or card surface |
| Display Black | `#11161c` | neutral | Primary text or dark surface |
| Obsidian Grey | `#000000` | neutral | Primary text or dark surface |
| Digital White | `#ffffff` | neutral | Page background or card surface |
| Graphite | `#bbbbbb` | neutral | Border, muted text, or supporting surface |
| Steel Grey | `#a3a3a3` | neutral | Border, muted text, or supporting surface |
| Slate Blue | `#575c75` | neutral | Action accent / signal color |
| Urgency Red | `#f43325` | brand | Action accent / signal color |
| Active Blue | `#0078a8` | accent | Action accent / signal color |
| Gradient Night | `#c9cbe4` | accent | Action accent / signal color |

```css
:root {
  --ref-control-panel-grey: #e5e7eb;
  --ref-display-black: #11161c;
  --ref-obsidian-grey: #000000;
  --ref-digital-white: #ffffff;
  --ref-graphite: #bbbbbb;
  --ref-steel-grey: #a3a3a3;
  --ref-slate-blue: #575c75;
  --ref-urgency-red: #f43325;
}
```

## Typography direction
- **proxima-nova**: 400, 600, 700, 800, 11px, 12px, 14px, 15px, 16px, 18px, 36px, 40px, 48px, 56px, 1.00, 1.10, 1.16, 1.25, 1.50; substitute `system-ui`.
- **SF Mono**: 400, 500, 10px, 11px, 12px, 0.80, 1.10, 1.20, 1.50; substitute `monospace`.
- **Helvetica Neue**: 400, 11px, 1.50; substitute `system-ui`.

## Spacing / shape
- Section Gap: `48px`
- Card Padding: `8px`
- Element Gap: `8px`
- Radius: `cards: 127.397px, pills: 9999px, buttons: 270.89px, default: 4px`

## Surface cues
- **Canvas** `#e5e7eb`: The primary background, acting as the base 'metal' or chassis of the overall control panel.
- **Display** `#11161c`: Used for 'screen' elements, data readouts, and information cards, mimicking embedded digital panels.
- **Elevated Control** `#ffffff`: Used for specific interactive components like button backgrounds or subtle highlights, providing digital light.

## Component cues
- **Primary Action Button**: Main call-to-action
- **Ghost Button**: Secondary or tertiary actions
- **Dark Interface Card**: Content presentation within a dark display area
- **Pill Card**: Small, contained information units or selectors
- **Input Field**: Data entry

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
