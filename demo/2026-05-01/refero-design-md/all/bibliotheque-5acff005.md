# Bibliothèque - Refero Design MD

- Source: https://styles.refero.design/style/5acff005-1871-4237-bc25-cdddf50edc70
- Original site: https://bibliothequedesign.com
- Theme: `dark`
- Industry: `design`
- Recommended fit: **Admin console / run monitor / developer tooling**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Monochrome Editorial Command: Pure black and white, sharp text, and border-defined interactions create an atmosphere of focused, high-contrast authority.

## Apply to
- Admin run monitor and review states
- Compact evidence cards and source inspection panels
- Dark-mode operational dashboards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Noir | `#000000` | neutral | Primary text or dark surface |
| Canvas White | `#ffffff` | neutral | Page background or card surface |

```css
:root {
  --ref-midnight-noir: #000000;
  --ref-canvas-white: #ffffff;
}
```

## Typography direction
- **Unica77 LL**: 400, 12px, 14px, 18px, 80px, 1.00, 1.20, 1.22, 1.33; substitute `Helvetica Neue`.

## Spacing / shape
- Section Gap: `47px`
- Card Padding: `0px`
- Element Gap: `5px`
- Radius: `none: 0px`

## Surface cues
- **Midnight Noir Canvas** `#000000`: The primary background for all page content and base for components.

## Component cues
- **Project Card**: Displaying project thumbnails and titles.
- **Navigation Link**: Interactive menu items in the main navigation.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
