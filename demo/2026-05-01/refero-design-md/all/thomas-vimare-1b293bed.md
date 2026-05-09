# Thomas Vimare - Refero Design MD

- Source: https://styles.refero.design/style/1b293bed-e6fc-4880-9691-2dbf04339bd5
- Original site: https://thms.works
- Theme: `dark`
- Industry: `design`
- Recommended fit: **Dark webapp exploration**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Minimalist gallery wall

## Apply to
- Dark theme experiments
- Operator-focused widgets
- High-contrast card systems

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Deep Night | `#171717` | neutral | Primary text or dark surface |
| Polar White | `#ffffff` | neutral | Page background or card surface |
| Quiet Fog | `#9a9a9a` | neutral | Border, muted text, or supporting surface |

```css
:root {
  --ref-deep-night: #171717;
  --ref-polar-white: #ffffff;
  --ref-quiet-fog: #9a9a9a;
}
```

## Typography direction
- **HelveticaNowDisplay-Light**: 400, 16px, 20px, 24px, 28px, 32px, 56px, 1.00, 1.20, 1.40, 1.50; substitute `system-ui, sans-serif`.

## Spacing / shape
- Section Gap: `120px`
- Card Padding: `60px`
- Element Gap: `20px`
- Page Max Width: `1600px`
- Radius: `default: 0px`

## Surface cues
- **Deep Night** `#171717`: Primary page background and all base UI surfaces

## Component cues
- **Navigation Link**: Top navigation items.
- **Project Card**: Displays individual portfolio projects.
- **Primary Heading**: Main page titles and key descriptive text.
- **Secondary Description**: Subtitles and supporting text for projects or sections.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
