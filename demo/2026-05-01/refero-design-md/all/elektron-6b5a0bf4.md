# Elektron - Refero Design MD

- Source: https://styles.refero.design/style/6b5a0bf4-3d2a-4c3b-aa2e-652f1acb82c0
- Original site: https://elektron.se
- Theme: `dark`
- Industry: `other`
- Recommended fit: **Admin console / run monitor / developer tooling**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Digital console in midnight. A world of precise, glowing information contained within a dark, structured shell.

## Apply to
- Admin run monitor and review states
- Compact evidence cards and source inspection panels
- Dark-mode operational dashboards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Absolute Zero | `#000000` | neutral | Primary text or dark surface |
| Control Panel Black | `#151515` | neutral | Primary text or dark surface |
| Deep Graphite | `#222222` | neutral | Primary text or dark surface |
| Input Surface Gray | `#333337` | neutral | Primary text or dark surface |
| Input Text Gray | `#b4b4b8` | neutral | Border, muted text, or supporting surface |
| Off White Text | `#eeeef2` | neutral | Page background or card surface |
| White Glow | `#ffffff` | neutral | Page background or card surface |
| Amber Indicator | `#ffcc00` | accent | Action accent / signal color |

```css
:root {
  --ref-absolute-zero: #000000;
  --ref-control-panel-black: #151515;
  --ref-deep-graphite: #222222;
  --ref-input-surface-gray: #333337;
  --ref-input-text-gray: #b4b4b8;
  --ref-off-white-text: #eeeef2;
  --ref-white-glow: #ffffff;
  --ref-amber-indicator: #ffcc00;
}
```

## Typography direction
- **Neue Haas Grotesk Text Pro**: 400, 11px, 14px, 16px, 18px, 28px, 35px, 1.20, 1.50; substitute `Helvetica Neue, Arial`.
- **Neue Haas Grotesk Display Pro**: 400, 450, 500, 24px, 31px, 64px, 0.95, 1.33, 1.50; substitute `Helvetica Neue, Arial`.
- **NHaasGroteskDSPro**: 400, 16px, 1.00, 1.20; substitute `Helvetica Neue, Arial`.

## Spacing / shape
- Section Gap: `100-140px`
- Element Gap: `4px`
- Radius: `inputs: 7px, buttons: 0px`

## Component cues
- **CTA Button Group**: Reference component style.
- **Product Accessory Cards**: Reference component style.
- **Search Input Field**: Reference component style.
- **Call to Action Button**: Primary user interaction.
- **Default Input Field**: User data entry.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
