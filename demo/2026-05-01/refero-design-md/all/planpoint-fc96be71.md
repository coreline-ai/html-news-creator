# Planpoint - Refero Design MD

- Source: https://styles.refero.design/style/fc96be71-d71b-4fc1-a041-f13b3eae7dd5
- Original site: https://www.planpoint.io
- Theme: `light`
- Industry: `other`
- Recommended fit: **Design reference / webapp exploration**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Architectural blueprint on white marble

## Apply to
- General webapp UI exploration
- Demo cards and catalog surfaces
- Future admin/subscriber UI references

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Ink | `#00051a` | neutral | Primary text or dark surface |
| Royal Blue | `#0f68ea` | brand | Action accent / signal color |
| Sky Blue | `#007aff` | accent | Action accent / signal color |
| Sunburst Yellow | `#ffcb00` | accent | Action accent / signal color |
| White Canvas | `#ffffff` | neutral | Page background or card surface |
| Pewter Gray | `#1d1d1f` | neutral | Primary text or dark surface |
| White Smoke | `#f0f2f4` | neutral | Page background or card surface |
| Slate Blue | `#000a3b` | neutral | Action accent / signal color |
| Soft Gray | `#e5e6e8` | neutral | Page background or card surface |

```css
:root {
  --ref-midnight-ink: #00051a;
  --ref-royal-blue: #0f68ea;
  --ref-sky-blue: #007aff;
  --ref-sunburst-yellow: #ffcb00;
  --ref-white-canvas: #ffffff;
  --ref-pewter-gray: #1d1d1f;
  --ref-white-smoke: #f0f2f4;
  --ref-slate-blue: #000a3b;
}
```

## Typography direction
- **Inter**: 400, 500, 600, 700, 14px, 16px, 18px, 22px, 23px, 29px, 32px, 43px, 50px, 72px, 144px, 0.90, 1.00, 1.10, 1.20, 1.25, 1.30, 1.55, 1.60; substitute `system-ui`.
- **system-ui**: 500, 14px, 1.5.

## Spacing / shape
- Section Gap: `72px`
- Card Padding: `72px`
- Element Gap: `14px`
- Radius: `cards: 28.8px, links: 160px, badges: 16px, buttons_chip: 46.8px, buttons_pill: 57.6px`

## Component cues
- **Primary Action Button**: Filled button for primary calls to action
- **Secondary Action Button**: Ghost button for secondary actions or links
- **Tertiary Action Button**: Filled button for less prominent actions, often within content blocks
- **Navigation Link Button**: Minimal button within navigation or content-dense areas
- **Promotional Card**: Informational card with a strong background accent

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
