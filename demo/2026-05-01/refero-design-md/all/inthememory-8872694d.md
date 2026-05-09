# Inthememory - Refero Design MD

- Source: https://styles.refero.design/style/8872694d-261d-4eb4-b355-fb39ee4c37ad
- Original site: https://inthememory.com
- Theme: `light`
- Industry: `fintech`
- Recommended fit: **Source ledger / evidence dashboard**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
white canvas, vibrant data points

## Apply to
- Source ledger, ranking, and verification screens
- Cluster evidence dashboards
- Dense data tables with clear hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Deep Charcoal | `#102126` | neutral | Primary text or dark surface |
| Ash Gray | `#e9eef0` | neutral | Page background or card surface |
| Cloud Gray | `#f1f7f9` | neutral | Page background or card surface |
| Muted Slate | `#3d5761` | neutral | Border, muted text, or supporting surface |
| Light Slate | `#677b82` | neutral | Border, muted text, or supporting surface |
| Data Orange Strong | `#fa4e1d` | brand | Action accent / signal color |
| Data Orange Soft | `#fb6338` | brand | Action accent / signal color |
| UI Blue | `#0c67ff` | accent | Action accent / signal color |
| Badge Blue Text | `#0519d5` | semantic | Action accent / signal color |

```css
:root {
  --ref-canvas-white: #ffffff;
  --ref-deep-charcoal: #102126;
  --ref-ash-gray: #e9eef0;
  --ref-cloud-gray: #f1f7f9;
  --ref-muted-slate: #3d5761;
  --ref-light-slate: #677b82;
  --ref-data-orange-strong: #fa4e1d;
  --ref-data-orange-soft: #fb6338;
}
```

## Typography direction
- **Graphik**: 400, 500, 12px, 14px, 16px, 18px, 20px, 40px, 56px, 1.00, 1.10, 1.18, 1.20, 1.33, 1.50, 1.70; substitute `system-ui`.

## Spacing / shape
- Section Gap: `48px`
- Card Padding: `24px`
- Element Gap: `24px`
- Radius: `links: 20px, badges: 6px, buttons: 100px, default: 12px`

## Component cues
- **Primary Filled Button**: Calls to action
- **Outlined Ghost Button**: Secondary actions, filtering, navigation
- **Action Icon Button**: Small interactive icons or controls
- **Primary Card**: Content grouping, feature showcase
- **Featured Orange Card**: Highlighting key information or stats

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
