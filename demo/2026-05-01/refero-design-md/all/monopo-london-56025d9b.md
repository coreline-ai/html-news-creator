# monopo london - Refero Design MD

- Source: https://styles.refero.design/style/56025d9b-3793-4303-b437-440440045d4c
- Original site: https://monopo.london
- Theme: `dark`
- Industry: `design`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Midnight gradient canvas

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Canvas | `#000000` | neutral | Primary text or dark surface |
| Ghost White | `#ffffff` | neutral | Page background or card surface |
| Subtle Gray | `#7f7f7f` | neutral | Border, muted text, or supporting surface |
| Medium Gray | `#666970` | neutral | Border, muted text, or supporting surface |
| Nebula Gradient | `#cd5a07` | neutral | Border, muted text, or supporting surface |

```css
:root {
  --ref-midnight-canvas: #000000;
  --ref-ghost-white: #ffffff;
  --ref-subtle-gray: #7f7f7f;
  --ref-medium-gray: #666970;
  --ref-nebula-gradient: #cd5a07;
}
```

## Typography direction
- **Roobert**: 300, 400, 700, 800, 12px, 14px, 16px, 17px, 22px, 33px, 45px, 1.00, 1.09, 1.15, 1.16, 1.20, 1.23, 1.44; substitute `system-ui, sans-serif or Space Grotesk`.

## Spacing / shape
- Section Gap: `111px`
- Card Padding: `15px`
- Element Gap: `8px`
- Radius: `links: 42px`

## Component cues
- **Ghost Navigation Link**: Primary navigation and footer links
- **Outlined Call to Action Button**: Secondary action button for discovering projects or general calls to action.
- **Hero Headline**: Dominant text for hero sections.
- **Sub-headline / Section Title**: Titles for section content like 'RECENT WORK'.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
