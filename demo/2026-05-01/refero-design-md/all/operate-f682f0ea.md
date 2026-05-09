# Operate - Refero Design MD

- Source: https://styles.refero.design/style/f682f0ea-632d-4d09-bfdf-6a43f5e5a7d8
- Original site: https://operate.so
- Theme: `light`
- Industry: `saas`
- Recommended fit: **Source ledger / evidence dashboard**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
digital ledger, subtle grid

## Apply to
- Source ledger, ranking, and verification screens
- Cluster evidence dashboards
- Dense data tables with clear hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas Fog | `#e0e0e0` | neutral | Page background or card surface |
| Inkwell | `#29211e` | neutral | Primary text or dark surface |
| Ghostly Gray | `#ffffff` | neutral | Page background or card surface |
| Shadowed Steel | `#453b41` | neutral | Primary text or dark surface |
| Ash Outline | `#e5e5e5` | neutral | Page background or card surface |
| Verdant Text | `#09352e` | brand | Action accent / signal color |
| Primary Green | `#85c093` | brand | Action accent / signal color |
| Lively Green | `#117025` | brand | Action accent / signal color |
| Deep Moss | `#007010` | brand | Action accent / signal color |
| Subtle Green Tint | `#77aa83` | brand | Action accent / signal color |

```css
:root {
  --ref-canvas-fog: #e0e0e0;
  --ref-inkwell: #29211e;
  --ref-ghostly-gray: #ffffff;
  --ref-shadowed-steel: #453b41;
  --ref-ash-outline: #e5e5e5;
  --ref-verdant-text: #09352e;
  --ref-primary-green: #85c093;
  --ref-lively-green: #117025;
}
```

## Typography direction
- **muoto**: 400, 500, 11px, 12px, 13px, 1.17, 1.18, 1.23, 1.33, 1.38, 1.46, 1.62; substitute `system-ui`.
- **denim**: 400, 500, 12px, 14px, 16px, 18px, 20px, 32px, 48px, 1.11, 1.14, 1.15, 1.17, 1.19, 1.29, 1.35, 1.40, 1.44, 1.50, 1.56, 1.63; substitute `Inter`.
- **cinetype**: 400, 14px, 16px, 1.14, 1.19; substitute `Space Mono`.

## Spacing / shape
- Section Gap: `42px`
- Card Padding: `16px`
- Element Gap: `8px`
- Radius: `cards: 12px, buttons: 12px, default: 4px, heroElement: 18px, circularElements: 9999px`

## Surface cues
- **Canvas Fog** `#e0e0e0`: Primary page background.
- **Ghostly Gray** `#ffffff`: Layered backgrounds like modals or secondary light cards.
- **Light Panel Card** `#f7f7f7`: Elevated card surfaces.
- **Dark Inset Card** `#1a191a`: Darker, inset content containers.

## Component cues
- **Ghost Button**: Minimal call to actions or secondary links that maintain visual lightness.
- **Pill Button**: Prominent actions and primary CTAs.
- **Green Accent Button**: Emphasis buttons, used for specific interactive elements.
- **Dark Inset Card**: Content container for features or pricing, subtle depth.
- **Light Panel Card**: Floating content blocks or informational panels.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
