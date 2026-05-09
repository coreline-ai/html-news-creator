# Figma Config - Refero Design MD

- Source: https://styles.refero.design/style/8caa5004-a8cc-4c7e-a2bb-00ff60618729
- Original site: https://config.figma.com/events/figma-config-2022
- Theme: `dark`
- Industry: `design`
- Recommended fit: **Admin console / run monitor / developer tooling**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
monochrome command console

## Apply to
- Admin run monitor and review states
- Compact evidence cards and source inspection panels
- Dark-mode operational dashboards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Void | `#000000` | neutral | Primary text or dark surface |
| Ghost White | `#e2e2e2` | neutral | Page background or card surface |
| Shadow Charcoal | `#3d3d3d` | neutral | Primary text or dark surface |
| Polar Mist | `#ffffff` | neutral | Page background or card surface |

```css
:root {
  --ref-midnight-void: #000000;
  --ref-ghost-white: #e2e2e2;
  --ref-shadow-charcoal: #3d3d3d;
  --ref-polar-mist: #ffffff;
}
```

## Typography direction
- **figmaSans**: 400, 16px, 18px, 20px, 32px, 80px, 0.95, 1.00, 1.10, 1.25, 1.30; substitute `Inter`.
- **figmaMono**: 400, 16px, 1.30; substitute `Menlo`.

## Spacing / shape
- Section Gap: `40px`
- Card Padding: `12px`
- Element Gap: `12px`
- Radius: `buttons: 0px, navPills: 50%`

## Surface cues
- **Canvas** `#000000`: Primary page background for most sections.
- **Dialog** `#ffffff`: Background for overlay elements like cookie consent pop-ups, providing a contrast to the dark canvas.

## Component cues
- **Primary Filled Button**: Main call-to-action on dark backgrounds.
- **Ghost Button**: Secondary action or navigable link that appears as a button.
- **Cookie Consent Button**: Button within the cookie consent dialog.
- **Navigation Link**: Top-level navigation items.
- **Cookie Consent Panel**: Floating informational message.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
