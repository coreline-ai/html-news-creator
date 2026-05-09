# Mews - Refero Design MD

- Source: https://styles.refero.design/style/6b2777fd-7021-4a96-add3-ec4a32374214
- Original site: https://www.mews.com/en
- Theme: `light`
- Industry: `other`
- Recommended fit: **Source ledger / evidence dashboard**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Digital Ledger Precision

## Apply to
- Source ledger, ranking, and verification screens
- Cluster evidence dashboards
- Dense data tables with clear hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Midnight Ink | `#000000` | neutral | Primary text or dark surface |
| Cloud Gray | `#f4f5f9` | neutral | Page background or card surface |
| Steel Gray | `#333333` | neutral | Primary text or dark surface |
| Charcoal Black | `#161616` | neutral | Primary text or dark surface |
| Dusty Gray | `#8c8c8c` | neutral | Border, muted text, or supporting surface |
| Outline Gray | `#cccccc` | neutral | Border, muted text, or supporting surface |
| Digital Pink | `#ffc5ee` | accent | Action accent / signal color |
| Soft Lilac | `#f7e1f7` | accent | Action accent / signal color |
| Sky Tint | `#d2f4ff` | accent | Action accent / signal color |

```css
:root {
  --ref-canvas-white: #ffffff;
  --ref-midnight-ink: #000000;
  --ref-cloud-gray: #f4f5f9;
  --ref-steel-gray: #333333;
  --ref-charcoal-black: #161616;
  --ref-dusty-gray: #8c8c8c;
  --ref-outline-gray: #cccccc;
  --ref-digital-pink: #ffc5ee;
}
```

## Typography direction
- **soehne**: 400, 500, 600, 700, 900, 11px, 12px, 13px, 14px, 15px, 16px, 17px, 18px, 20px, 22px, 28px, 32px, 40px, 48px, 64px, 72px, 96px, 0.80, 0.90, 1.00, 1.03, 1.10, 1.15, 1.20, 1.35, 1.50; substitute `system-ui, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif`.

## Spacing / shape
- Section Gap: `80px`
- Card Padding: `16px`
- Element Gap: `10px`
- Page Max Width: `1278px`
- Radius: `pill: 9999px, cards: 6px, buttons: 8px, default: 4px`

## Component cues
- **Hero Dark Card**: Prominent information display
- **Primary Action Button**: Call to action
- **Ghost Pill Button**: Secondary action or tag
- **Subtle Background Button**: Informational button or filter
- **Feature Grid Card**: Display individual features or services

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
