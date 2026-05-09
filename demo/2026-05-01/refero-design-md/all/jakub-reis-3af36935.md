# Jakub Reis - Refero Design MD

- Source: https://styles.refero.design/style/3af36935-8383-49e7-857e-9fb5caa06966
- Original site: https://jakubreis.com
- Theme: `light`
- Industry: `design`
- Recommended fit: **Design reference / webapp exploration**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Gallery Grid of Precision

## Apply to
- General webapp UI exploration
- Demo cards and catalog surfaces
- Future admin/subscriber UI references

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#f8f8f8` | neutral | Page background or card surface |
| Ink Black | `#000000` | neutral | Primary text or dark surface |
| Ash Black | `#080808` | neutral | Primary text or dark surface |
| Sandstone Tan | `#f8e8d8` | neutral | Page background or card surface |
| Lavendar Gray | `#e8d8f8` | neutral | Page background or card surface |
| Slate Gray | `#d8d8d8` | neutral | Border, muted text, or supporting surface |
| Electric Violet | `#7848e8` | accent | Action accent / signal color |

```css
:root {
  --ref-canvas-white: #f8f8f8;
  --ref-ink-black: #000000;
  --ref-ash-black: #080808;
  --ref-sandstone-tan: #f8e8d8;
  --ref-lavendar-gray: #e8d8f8;
  --ref-slate-gray: #d8d8d8;
  --ref-electric-violet: #7848e8;
}
```

## Typography direction
- **Degular**: 300, 400, 16px, 18px, 24px, 30px, 50px, 0.92, 1.00, 1.11, 1.25, 1.33; substitute `system-ui`.

## Spacing / shape
- Section Gap: `80px`
- Card Padding: `20px`
- Element Gap: `8px`
- Radius: `default: 0px`

## Surface cues
- **Canvas White** `#f8f8f8`: Primary page background
- **Sandstone Tan** `#f8e8d8`: Alternating background for content sections
- **Lavendar Gray** `#e8d8f8`: Background for specific content blocks or sections
- **Slate Gray** `#d8d8d8`: Subtle surface variation or divider

## Component cues
- **Primary Text**: Standard body copy and descriptive text.
- **Navigation Link**: Global header and footer navigation items.
- **Project Title**: Main heading for individual project showcases.
- **Project Metadata**: Secondary description under project titles.
- **Hero Headline**: Prominent headline on the landing screen.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
