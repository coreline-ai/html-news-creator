# Stable Audio - Refero Design MD

- Source: https://styles.refero.design/style/c363a216-873c-4112-b960-8e823db76f74
- Original site: https://stableaudio.com
- Theme: `light`
- Industry: `ai`
- Recommended fit: **Source ledger / evidence dashboard**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Warm parchment; vibrant neon bursts.

## Apply to
- Source ledger, ranking, and verification screens
- Cluster evidence dashboards
- Dense data tables with clear hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Ink | `#000000` | neutral | Primary text or dark surface |
| Charcoal Accent | `#27262b` | neutral | Primary text or dark surface |
| Clean Canvas | `#ffffff` | neutral | Page background or card surface |
| Parchment Base | `#f4f1ec` | neutral | Page background or card surface |
| Subtle Ash | `#e2e2e7` | neutral | Page background or card surface |
| Pale Earth | `#e5dfc8` | neutral | Page background or card surface |
| Muted Sage | `#c9d19c` | accent | Action accent / signal color |
| Desert Sand | `#d4c9b4` | accent | Action accent / signal color |
| Deep Plum | `#c4bae3` | accent | Action accent / signal color |
| Ocean Mist | `#9fc2c7` | accent | Action accent / signal color |

```css
:root {
  --ref-midnight-ink: #000000;
  --ref-charcoal-accent: #27262b;
  --ref-clean-canvas: #ffffff;
  --ref-parchment-base: #f4f1ec;
  --ref-subtle-ash: #e2e2e7;
  --ref-pale-earth: #e5dfc8;
  --ref-muted-sage: #c9d19c;
  --ref-desert-sand: #d4c9b4;
}
```

## Typography direction
- **Inter**: 400, 700, 12px, 14px, 16px, 18px, 20px, 30px, 40px, 1.00, 1.15, 1.33, 1.50, 1.71, 1.78; substitute `system-ui, sans-serif`.

## Spacing / shape
- Section Gap: `64px`
- Card Padding: `24px`
- Element Gap: `8px`
- Page Max Width: `1764px`
- Radius: `cards: 4px, forms: 9999px, images: 4px, buttons: 9999px, default: 4px`

## Component cues
- **Primary CTA Card**: Reference component style.
- **Feature Toggle Pills + Text-to-Audio Section Card**: Reference component style.
- **Audio Track History List**: Reference component style.
- **Secondary Ghost Button**: Less prominent actions
- **Navigation Button**: Header navigation actions

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
