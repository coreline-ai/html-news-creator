# Quicken - Refero Design MD

- Source: https://styles.refero.design/style/75eb47d6-2526-4936-b15a-7474cf4cdc69
- Original site: https://www.quicken.com
- Theme: `light`
- Industry: `fintech`
- Recommended fit: **Source ledger / evidence dashboard**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Electric violet data stream

## Apply to
- Source ledger, ranking, and verification screens
- Cluster evidence dashboards
- Dense data tables with clear hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Deep Violet | `#0f0733` | brand | Action accent / signal color |
| Electric Indigo | `#471cff` | brand | Action accent / signal color |
| Pure White | `#ffffff` | neutral | Page background or card surface |
| Charcoal Black | `#18181f` | neutral | Primary text or dark surface |
| Graphite | `#494949` | neutral | Border, muted text, or supporting surface |
| Snow Drift | `#f0f5fa` | neutral | Page background or card surface |
| Pale Lavender | `#dbd3ff` | accent | Action accent / signal color |
| Sky Mist | `#bbc5fa` | accent | Action accent / signal color |
| Crimson Alert | `#eb0130` | accent | Action accent / signal color |
| Sunny Orange | `#ff5a43` | semantic | Action accent / signal color |

```css
:root {
  --ref-deep-violet: #0f0733;
  --ref-electric-indigo: #471cff;
  --ref-pure-white: #ffffff;
  --ref-charcoal-black: #18181f;
  --ref-graphite: #494949;
  --ref-snow-drift: #f0f5fa;
  --ref-pale-lavender: #dbd3ff;
  --ref-sky-mist: #bbc5fa;
}
```

## Typography direction
- **Haffer**: 400, 600, 12px, 13px, 14px, 16px, 17px, 18px, 19px, 20px, 22px, 26px, 30px, 48px, 60px, 1.00, 1.16, 1.20, 1.24, 1.31, 1.32, 1.35, 1.40, 1.50, 2.00; substitute `system-ui`.

## Spacing / shape
- Section Gap: `24px`
- Card Padding: `16px`
- Element Gap: `8px`
- Page Max Width: `1440px`
- Radius: `cards: 16px, badges: 20px, buttons: 400px, elements-sm: 8px`

## Surface cues
- **Page Canvas** `#ffffff`: The primary background for the entire application, providing a bright, expansive foundation.
- **Content Card Surface** `#f0f5fa`: A slightly off-white background used for cards and grouped content, creating a subtle separation from the main canvas without strong contrast.
- **Elevated Card Surface** `#ffffff`: Pure white cards that stand out on the 'Content Card Surface', often with a distinct shadow to denote interaction or importance.
- **Hero Dark Background** `#0f0733`: A deep, saturated violet used for hero sections and prominent headers, creating a strong contrast and sense of depth against lighter content.

## Component cues
- **Primary Action Button**: Call to action
- **Outline Ghost Button**: Secondary action
- **Text Link Button**: Navigation or tertiary action
- **Hero Background Card**: Information display
- **Elevated Feature Card**: Product feature showcase

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
