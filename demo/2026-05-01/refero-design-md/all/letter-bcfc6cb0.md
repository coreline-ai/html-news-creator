# Letter - Refero Design MD

- Source: https://styles.refero.design/style/bcfc6cb0-1b39-4f3f-a95e-bd7b563b0efc
- Original site: https://letter.co
- Theme: `light`
- Industry: `fintech`
- Recommended fit: **Source ledger / evidence dashboard**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Sublime Depth, Minimal Interface

## Apply to
- Source ledger, ranking, and verification screens
- Cluster evidence dashboards
- Dense data tables with clear hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight | `#000000` | neutral | Primary text or dark surface |
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Carbon | `#191b1f` | neutral | Primary text or dark surface |
| Ghost Gray | `#f6f9f9` | neutral | Page background or card surface |
| Whisper Gray | `#e6ebec` | neutral | Page background or card surface |
| Stone Whisper | `#9fabad` | neutral | Border, muted text, or supporting surface |
| Deep Teal | `#186f64` | brand | Action accent / signal color |
| Royal Violet | `#536eff` | accent | Action accent / signal color |
| Grape Dusk | `#644bc4` | accent | Action accent / signal color |
| Ocean Gaze | `#154ea5` | accent | Action accent / signal color |

```css
:root {
  --ref-midnight: #000000;
  --ref-canvas-white: #ffffff;
  --ref-carbon: #191b1f;
  --ref-ghost-gray: #f6f9f9;
  --ref-whisper-gray: #e6ebec;
  --ref-stone-whisper: #9fabad;
  --ref-deep-teal: #186f64;
  --ref-royal-violet: #536eff;
}
```

## Typography direction
- **Albra Sans**: 600, 22px, 46px, 80px, 1.10, 1.20; substitute `Playfair Display`.
- **Neufile Grotesk Extended**: 400, 500, 13px, 16px, 28px, 1.00, 1.30, 1.40, 2.00; substitute `Inter`.

## Spacing / shape
- Section Gap: `64px`
- Card Padding: `16px`
- Element Gap: `16px`
- Page Max Width: `1440px`
- Radius: `links: 2px, buttons: 2px`

## Component cues
- **Primary Dark Button**: Call to action for joining or getting started.
- **Secondary Light Button**: Alternative call to action, often for signing in or less prominent actions.
- **Teal Action Button**: Primary action for 'Invest' or 'Browse' related features.
- **Violet Action Button**: Primary action for 'Borrow' related features.
- **Ghost Card**: Decorative card used as a background or for subtle visual separation without strong outlines.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
