# TWOTWO - Refero Design MD

- Source: https://styles.refero.design/style/170a690b-7424-4c2e-9d08-975725cf9261
- Original site: https://twotwo-official.com
- Theme: `light`
- Industry: `ecommerce`
- Recommended fit: **Source ledger / evidence dashboard**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Vivid chartreuse on concrete

## Apply to
- Source ledger, ranking, and verification screens
- Cluster evidence dashboards
- Dense data tables with clear hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Ink | `#000000` | neutral | Primary text or dark surface |
| Slate Text | `#323232` | neutral | Primary text or dark surface |
| Ghost Gray | `#1a1a1a` | neutral | Primary text or dark surface |
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Chartreuse Flash | `#e3fc03` | brand | Action accent / signal color |

```css
:root {
  --ref-midnight-ink: #000000;
  --ref-slate-text: #323232;
  --ref-ghost-gray: #1a1a1a;
  --ref-canvas-white: #ffffff;
  --ref-chartreuse-flash: #e3fc03;
}
```

## Typography direction
- **WhyteInktrapRegular**: 400, 16px, 1.60; substitute `DM Mono`.
- **WhyteBook**: 400, 13px, 16px, 18px, 20px, 22px, 26px, 38px, 1.30, 1.40, 1.60; substitute `Inter`.
- **WhyteRegular**: 400, 32px, 72px, 1.10, 1.15; substitute `Inter`.

## Spacing / shape
- Section Gap: `68px`
- Card Padding: `32px`
- Element Gap: `10px`
- Radius: `cards: 16px, inputs: 50px, buttons: 50px, general: 8px, productImages: 16px`

## Component cues
- **Primary Action Button**: The main call to action element, demanding attention.
- **Navigation Link / Ghost Button**: Used for navigation and secondary actions where visual weight should be minimal.
- **Search Input Field**: Standard input for user data entry.
- **Product Card**: Container for individual product listings.
- **Hero Headline**: Dominant text for primary page messages.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
