# The Beams - Refero Design MD

- Source: https://styles.refero.design/style/b321ca45-2971-4828-9165-82b77f676bfd
- Original site: https://thebeamslondon.com
- Theme: `light`
- Industry: `other`
- Recommended fit: **Design reference / webapp exploration**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Industrial monochrome canvas

## Apply to
- General webapp UI exploration
- Demo cards and catalog surfaces
- Future admin/subscriber UI references

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Ink Black | `#000000` | neutral | Primary text or dark surface |
| Terra Cotta | `#a05b38` | accent | Action accent / signal color |

```css
:root {
  --ref-canvas-white: #ffffff;
  --ref-ink-black: #000000;
  --ref-terra-cotta: #a05b38;
}
```

## Typography direction
- **NeueHaas-web**: 400, 19px, 29px, 38px, 95px, 160px, 0.90, 1.00, 1.10, 1.95, 2.90; substitute `Helvetica Neue`.

## Spacing / shape
- Section Gap: `46px`
- Card Padding: `19px`
- Element Gap: `19px`
- Radius: `none: 0px`

## Surface cues
- **Canvas White** `#ffffff`: Primary page background and default surface for all content.

## Component cues
- **Text Outline Button (Light)**: Secondary action button or navigation element.
- **Text Outline Button (Dark)**: Secondary action button or navigation element on dark backgrounds.
- **Text Input**: Standard text input field for forms.
- **Header Navigation Link**: Top-level navigation items.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
