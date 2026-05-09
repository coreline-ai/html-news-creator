# Desktop.fm - Refero Design MD

- Source: https://styles.refero.design/style/cb266ff9-f168-4a42-a522-f0e84508f90f
- Original site: https://desktop.fm
- Theme: `light`
- Industry: `media`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Operating System Interface — clean-cut, functional, and digital.

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Cloud Cover | `#f1f2f3` | neutral | Page background or card surface |
| Graphite | `#111111` | neutral | Primary text or dark surface |
| Light Steel | `#dddddd` | neutral | Page background or card surface |
| Snow | `#ffffff` | neutral | Page background or card surface |
| Dark Slate | `#2d2d2d` | neutral | Primary text or dark surface |
| Mid Grey | `#b4b4b4` | neutral | Border, muted text, or supporting surface |
| Ash | `#777777` | neutral | Border, muted text, or supporting surface |
| Neon Green | `#009942` | accent | Action accent / signal color |

```css
:root {
  --ref-cloud-cover: #f1f2f3;
  --ref-graphite: #111111;
  --ref-light-steel: #dddddd;
  --ref-snow: #ffffff;
  --ref-dark-slate: #2d2d2d;
  --ref-mid-grey: #b4b4b4;
  --ref-ash: #777777;
  --ref-neon-green: #009942;
}
```

## Typography direction
- **-apple-system**: 500, 700, 800, 12px, 16px, 18px, 28px, 1.25; substitute `system-ui, sans-serif`.
- **monospace**: 800, 12px, 1.25; substitute `Menlo, Monaco, Consolas, 'Liberation Mono', 'Courier New', monospace`.

## Spacing / shape
- Section Gap: `30px`
- Card Padding: `0px`
- Element Gap: `2px`
- Radius: `cards: 25px, buttons: 20px, default: 1.5px`

## Component cues
- **Main CTA Card**: Reference component style.
- **Button Group — Primary & Utility**: Reference component style.
- **Status Badge & Monospace Tag Collection**: Reference component style.
- **Info Button**: Utility button
- **Selected Info Button**: Active utility button

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
