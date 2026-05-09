# Automate Supplier Payments - Refero Design MD

- Source: https://styles.refero.design/style/dfbcffc2-79a3-4349-b5c6-1aa9fae4fcf4
- Original site: https://getapron.com
- Theme: `light`
- Industry: `fintech`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
sunlit productivity canvas

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Amber Pop | `#ffd801` | brand | Action accent / signal color |
| Canvas Gold | `#fbefaf` | neutral | Page background or card surface |
| Paper Buff | `#fff6d2` | neutral | Page background or card surface |
| Midnight Ink | `#000000` | neutral | Primary text or dark surface |
| Fog | `#cccbc7` | neutral | Border, muted text, or supporting surface |
| Frost | `#ffffff` | neutral | Page background or card surface |
| Charcoal Haze | `#666664` | neutral | Border, muted text, or supporting surface |

```css
:root {
  --ref-amber-pop: #ffd801;
  --ref-canvas-gold: #fbefaf;
  --ref-paper-buff: #fff6d2;
  --ref-midnight-ink: #000000;
  --ref-fog: #cccbc7;
  --ref-frost: #ffffff;
  --ref-charcoal-haze: #666664;
}
```

## Typography direction
- **sans-serif**: 400, 16px, 1.15.
- **Champ**: 500, 800, 26px, 38px, 54px, 72px, 1.01, 1.16, 1.20, 1.40; substitute `Montserrat`.
- **DM Sans**: 400, 500, 700, 10px, 16px, 20px, 1.00, 1.40, 1.50, 2.33; substitute `Open Sans`.

## Spacing / shape
- Section Gap: `80px`
- Card Padding: `32px`
- Element Gap: `24px`
- Radius: `cards: 20px, buttons: 9999px, general: 16px`

## Surface cues
- **Canvas Gold** `#fbefaf`: Base page background
- **Paper Buff** `#fff6d2`: Card and content block backgrounds
- **Frost** `#ffffff`: Occasional elevated sections or modal backgrounds used against a dark overlay

## Component cues
- **Primary Action Button**: Main call-to-action button for initiating key actions
- **Ghost Button**: Secondary action button, typically for navigation or less emphasized actions
- **Text Link Button**: Hyperlink-style button for quick navigation or inline actions
- **Information Card**: Container for grouped content or features in a section
- **Elevated Box**: Decorative or content-containing box that stands out slightly

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
