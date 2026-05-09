# TWOMUCH.STUDIO - Refero Design MD

- Source: https://styles.refero.design/style/12b3e1b6-31b9-4843-9b3b-8f39c9dd1474
- Original site: https://twomuch.studio
- Theme: `light`
- Industry: `design`
- Recommended fit: **Admin console / run monitor / developer tooling**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Digital Art Assemblage

## Apply to
- Admin run monitor and review states
- Compact evidence cards and source inspection panels
- Dark-mode operational dashboards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Subtle Gray | `#f4f4f4` | neutral | Page background or card surface |
| Border Ash | `#e5e7eb` | neutral | Page background or card surface |
| Warm Gray | `#dedede` | neutral | Page background or card surface |
| Ink Black | `#000000` | neutral | Primary text or dark surface |
| Digital Lime | `#e2ff70` | brand | Action accent / signal color |
| Clay Earth | `#68340e` | accent | Action accent / signal color |

```css
:root {
  --ref-canvas-white: #ffffff;
  --ref-subtle-gray: #f4f4f4;
  --ref-border-ash: #e5e7eb;
  --ref-warm-gray: #dedede;
  --ref-ink-black: #000000;
  --ref-digital-lime: #e2ff70;
  --ref-clay-earth: #68340e;
}
```

## Typography direction
- **ABCMonumentGrotesk**: 500, 12px, 14px, 16px, 18px, 20px, 22px, 0.90, 1.00, 1.05, 1.33, 1.43; substitute `Space Grotesk`.

## Spacing / shape
- Card Padding: `8px`
- Element Gap: `4px`
- Page Max Width: `300px`
- Radius: `pill: 9999px, default: 0px, elements: 4px`

## Surface cues
- **Canvas White** `#ffffff`: Base page background
- **Subtle Gray** `#f4f4f4`: Secondary container backgrounds, default button states
- **Accent Highlight** `#e2ff70`: Active states, specific interactive elements

## Component cues
- **Default Button**: Informational or secondary action buttons
- **Hover Button**: Interacted state for informational buttons
- **Ghost Button**: Minimalist interactive elements, often for pagination or navigation
- **Accent Button**: Small, contained informational buttons often for menu or numbers
- **Menu Box**: Interactive menu indicator, often containing a numerical count

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
