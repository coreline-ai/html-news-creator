# Clearbit - Refero Design MD

- Source: https://styles.refero.design/style/6221ba67-26e7-4657-91b7-efd77cbb1f12
- Original site: https://clearbit.com
- Theme: `light`
- Industry: `saas`
- Recommended fit: **Design reference / webapp exploration**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
White canvas, muted indigo typography, focused blue accents.

## Apply to
- General webapp UI exploration
- Demo cards and catalog surfaces
- Future admin/subscriber UI references

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Inkwell Indigo | `#091135` | brand | Action accent / signal color |
| Powder Gray | `#e1e9f0` | neutral | Page background or card surface |
| HubSpot Blue | `#127ee3` | brand | Action accent / signal color |
| Focus Blue | `#0f77ff` | accent | Action accent / signal color |
| Slate Text | `#36394a` | neutral | Primary text or dark surface |
| Lavender Mist | `#f5f3ff` | neutral | Page background or card surface |

```css
:root {
  --ref-canvas-white: #ffffff;
  --ref-inkwell-indigo: #091135;
  --ref-powder-gray: #e1e9f0;
  --ref-hubspot-blue: #127ee3;
  --ref-focus-blue: #0f77ff;
  --ref-slate-text: #36394a;
  --ref-lavender-mist: #f5f3ff;
}
```

## Typography direction
- **InterVar**: 400, 500, 600, 700, 14px, 16px, 18px, 32px, 56px, 64px, 1.25, 1.43, 1.50; substitute `Inter`.

## Spacing / shape
- Section Gap: `64px`
- Card Padding: `24px`
- Element Gap: `8px`
- Page Max Width: `1200px`
- Radius: `misc: 24px, cards: 12px, buttons: 8px`

## Surface cues
- **Canvas White** `#ffffff`: Default page background.
- **Lavender Mist** `#f5f3ff`: Alternating section backgrounds and subtle content block differentiation.
- **Elevated Card** `#ffffff`: Card backgrounds, visually separated by elevation.

## Component cues
- **Navigation Login Button**: Primary Call to Action in the header.
- **Ghost Navigation Link**: Secondary navigation and utility links.
- **Feature Card**: Container for showcasing product features or data snippets.
- **Accent Bordered Card**: Highlighting a specific card or interactive element with a strong focus.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
