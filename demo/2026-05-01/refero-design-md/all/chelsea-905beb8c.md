# CHELSEA - Refero Design MD

- Source: https://styles.refero.design/style/905beb8c-9788-4ff4-888b-13370cacd4b0
- Original site: https://www.chelsea.com
- Theme: `dark`
- Industry: `media`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Cinematic Night Canvas — light through shadow.

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Ink | `#000000` | neutral | Primary text or dark surface |
| Ash Gray | `#1f2937` | neutral | Primary text or dark surface |
| Ghost White | `#f4efe9` | neutral | Page background or card surface |
| Polar White | `#ffffff` | neutral | Page background or card surface |
| Pavement Gray | `#e5e7eb` | neutral | Page background or card surface |
| Electric Blue | `#4490ff` | accent | Action accent / signal color |

```css
:root {
  --ref-midnight-ink: #000000;
  --ref-ash-gray: #1f2937;
  --ref-ghost-white: #f4efe9;
  --ref-polar-white: #ffffff;
  --ref-pavement-gray: #e5e7eb;
  --ref-electric-blue: #4490ff;
}
```

## Typography direction
- **Neue Haas Unica Pro**: 400, 700, 12px, 14px, 16px, 32px, 48px, 1.00, 1.10, 1.12, 1.15, 1.43, 1.50; substitute `Helvetica Neue`.

## Spacing / shape
- Section Gap: `96px`
- Card Padding: `16px`
- Element Gap: `8px`
- Radius: `links: 9999px, buttons: 9999px`

## Surface cues
- **Canvas** `#000000`: Primary page background and large structural areas, establishing the dark mode.
- **Interactive Overlay** `#4490ff`: Used for filled buttons and active states, creating distinct interactive surface elements.

## Component cues
- **Navigation Link**: Main navigation items and sub-navigation lists.
- **Pill Accent Button**: Primary action button that stands out.
- **Ghost Border Button**: Secondary action or categorized filters.
- **Text List Item**: Displaying team members or project names in a list.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
