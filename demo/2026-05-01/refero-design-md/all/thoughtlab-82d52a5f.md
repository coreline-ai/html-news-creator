# ThoughtLab - Refero Design MD

- Source: https://styles.refero.design/style/82d52a5f-b1bb-4a69-91a3-15a7eb8bbe99
- Original site: https://www.thoughtlab.com
- Theme: `dark`
- Industry: `design`
- Recommended fit: **Admin console / run monitor / developer tooling**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Midnight Command Center

## Apply to
- Admin run monitor and review states
- Compact evidence cards and source inspection panels
- Dark-mode operational dashboards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Black | `#000000` | neutral | Primary text or dark surface |
| Stone Grey | `#4c4c4c` | neutral | Border, muted text, or supporting surface |
| Ghost White | `#cccccc` | neutral | Border, muted text, or supporting surface |
| Snow Drift | `#ffffff` | neutral | Page background or card surface |
| Action Red | `#fc1c46` | brand | Action accent / signal color |

```css
:root {
  --ref-midnight-black: #000000;
  --ref-stone-grey: #4c4c4c;
  --ref-ghost-white: #cccccc;
  --ref-snow-drift: #ffffff;
  --ref-action-red: #fc1c46;
}
```

## Typography direction
- **sui**: 300, 400, 500, 700, 10px, 14px, 15px, 17px, 18px, 27px, 72px, 91px, 198px, 0.92, 0.96, 1.00, 1.10, 1.15, 1.20, 1.25, 1.50, 2.14; substitute `Arial, Helvetica, sans-serif`.

## Spacing / shape
- Section Gap: `65px`
- Card Padding: `22px`
- Element Gap: `9px`
- Radius: `buttons: 9999px`

## Surface cues
- **Primary Canvas** `#000000`: Dominant background for the entire application, creating a deep, dark environment.
- **Subtle Surface** `#cccccc`: Used for content backgrounds or subtle visual breaks within the dark canvas, maintaining high contrast.
- **Elevated Surface** `#ffffff`: Occasional background for sections or components that require higher visual prominence against a subtly lighter backdrop, or as a direct contrast to…

## Component cues
- **Primary Action Button**: Main call-to-action.
- **Ghost Nav Link**: Header and navigation links.
- **Text Input**: Standard input fields.
- **Content Card**: Information grouping.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
