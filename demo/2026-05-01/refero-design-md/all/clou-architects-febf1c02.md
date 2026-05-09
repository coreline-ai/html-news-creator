# CLOU architects - Refero Design MD

- Source: https://styles.refero.design/style/febf1c02-2c4d-46e6-ad16-8ee2a99ae0d5
- Original site: https://www.clouarchitects.com
- Theme: `light`
- Industry: `design`
- Recommended fit: **Design reference / webapp exploration**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Architectural blueprint on stark white canvas.

## Apply to
- General webapp UI exploration
- Demo cards and catalog surfaces
- Future admin/subscriber UI references

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#fffffc` | neutral | Page background or card surface |
| Ink Black | `#000000` | neutral | Primary text or dark surface |
| Arched Red | `#ff0000` | accent | Action accent / signal color |

```css
:root {
  --ref-canvas-white: #fffffc;
  --ref-ink-black: #000000;
  --ref-arched-red: #ff0000;
}
```

## Typography direction
- **Circular Std**: 400, 700, 13px, 17px, 20px, 25px, 32px, 34px, 50px, 109px, 134px, 166px, 201px, 0.80, 1.00, 1.06, 1.10, 1.15, 1.50; substitute `System UI, Montserrat`.

## Spacing / shape
- Section Gap: `25px`
- Card Padding: `17px`
- Element Gap: `17px`
- Radius: `none: 0px`

## Component cues
- **Ghost Link Button**: Navigational or secondary action button for text-based links.
- **Inline Text Button**: Simple text-based button, often used for content within sections like 'View projects +'.
- **Hero Headline Block**: Dominant textual display for key messages, designed for maximum impact.
- **Navigation Link**: Header and footer navigation menu items.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
