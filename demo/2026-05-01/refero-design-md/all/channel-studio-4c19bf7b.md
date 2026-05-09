# Channel Studio - Refero Design MD

- Source: https://styles.refero.design/style/4c19bf7b-d5e8-4e2a-b3e3-69a9bde19b7a
- Original site: https://channel.studio
- Theme: `dark`
- Industry: `design`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Stark intellectual minimalism.

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Void | `#000000` | neutral | Primary text or dark surface |
| Ghost Gray | `#cacaca` | neutral | Border, muted text, or supporting surface |
| Faded Stone | `#727272` | neutral | Border, muted text, or supporting surface |
| Vanguard Red | `#ff7777` | brand | Action accent / signal color |

```css
:root {
  --ref-midnight-void: #000000;
  --ref-ghost-gray: #cacaca;
  --ref-faded-stone: #727272;
  --ref-vanguard-red: #ff7777;
}
```

## Typography direction
- **Lausanne**: 400, 13px, 15px, 16px, 18px, 45px, 75px, 0.90, 0.95, 1.19, 1.20; substitute `Inter`.

## Spacing / shape
- Section Gap: `40px`
- Card Padding: `0px`
- Element Gap: `10px`
- Radius: `none: 0px`

## Component cues
- **Ghost Navigation Link**: Primary navigation links and interactive textual elements.
- **Zero-Padding Card**: Content containers that use the background as their surface.
- **Underlined Input Field**: Input fields for data entry.
- **Highlighted Project Title**: Prominent headings for project names or content sections.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
