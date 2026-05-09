# Readymag - Refero Design MD

- Source: https://styles.refero.design/style/1287abc9-da90-410d-a997-96b8b11ad646
- Original site: https://readymag.com
- Theme: `light`
- Industry: `design`
- Recommended fit: **Source ledger / evidence dashboard**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Vibrant digital gallery. Each content block is a self-contained, high-contrast visual statement.

## Apply to
- Source ledger, ranking, and verification screens
- Cluster evidence dashboards
- Dense data tables with clear hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Type Black | `#000000` | neutral | Primary text or dark surface |
| Charcoal Text | `#282828` | neutral | Primary text or dark surface |
| Surface Gray | `#f4f4f4` | neutral | Page background or card surface |
| Light Gray | `#e7e7e7` | neutral | Page background or card surface |
| UI Gray | `#808080` | neutral | Border, muted text, or supporting surface |
| Accent Grape | `#8800ff` | brand | Action accent / signal color |
| Electric Violet | `#2c0fb1` | brand | Action accent / signal color |
| Sunset Orange | `#ec520b` | brand | Action accent / signal color |
| Warning Orange | `#ff5000` | accent | Action accent / signal color |

```css
:root {
  --ref-canvas-white: #ffffff;
  --ref-type-black: #000000;
  --ref-charcoal-text: #282828;
  --ref-surface-gray: #f4f4f4;
  --ref-light-gray: #e7e7e7;
  --ref-ui-gray: #808080;
  --ref-accent-grape: #8800ff;
  --ref-electric-violet: #2c0fb1;
}
```

## Typography direction
- **-apple-system**: 400, 16px, 1.00, 1.25; substitute `system-ui`.
- **custom_37866**: 400, 700, 12px, 14px, 18px, 30px, 32px, 40px, 80px, 1.00, 1.43, 1.83, 2.67, 2.70; substitute `Helvetica Neue, Arial`.
- **Graphik**: 400, 12px, 16px, 1.50, 2.00; substitute `Graphik`.

## Spacing / shape
- Card Padding: `0px`
- Element Gap: `6px`
- Radius: `tags: 10px, buttons: 200px, modules: 20px, illustrations: 16px`

## Component cues
- **Call-to-Action Hero Headline Block**: Reference component style.
- **Feature Cards Row — Attract & Streamline**: Reference component style.
- **Navigation Pill Bar**: Reference component style.
- **Primary Call to Action Button**: Critical user actions to advance through the site.
- **Pill Navigation Button**: Main navigation and secondary actions in headers.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
