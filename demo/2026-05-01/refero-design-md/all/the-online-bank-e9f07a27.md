# The online bank - Refero Design MD

- Source: https://styles.refero.design/style/e9f07a27-bdd4-4f6a-8132-329d014aa5f4
- Original site: https://n26.com
- Theme: `light`
- Industry: `fintech`
- Recommended fit: **Source ledger / evidence dashboard**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Teal and White Ledger. A clear, high-contrast digital ledger laid out on a clean white page, highlighted by a single, prominent teal ink.

## Apply to
- Source ledger, ranking, and verification screens
- Cluster evidence dashboards
- Dense data tables with clear hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Arctic White | `#ffffff` | neutral | Page background or card surface |
| Deep Teal | `#088177` | brand | Action accent / signal color |
| Ink Black | `#1b1b1b` | neutral | Primary text or dark surface |
| Horizon Gray | `#e9e9e9` | neutral | Page background or card surface |
| Ghost White | `#faf8f5` | neutral | Page background or card surface |
| Slate Gray | `#6d6d6d` | neutral | Border, muted text, or supporting surface |
| Warning Red | `#d80027` | semantic | Action accent / signal color |
| Caution Yellow | `#ffda44` | semantic | Action accent / signal color |
| Accent Teal | `#06736a` | brand | Action accent / signal color |

```css
:root {
  --ref-arctic-white: #ffffff;
  --ref-deep-teal: #088177;
  --ref-ink-black: #1b1b1b;
  --ref-horizon-gray: #e9e9e9;
  --ref-ghost-white: #faf8f5;
  --ref-slate-gray: #6d6d6d;
  --ref-warning-red: #d80027;
  --ref-caution-yellow: #ffda44;
}
```

## Typography direction
- **N26**: 400, 500, 700, 11px, 14px, 16px, 18px, 20px, 24px, 1.33, 1.38, 1.43, 1.50, 1.60; substitute `Open Sans`.
- **N26-Extended**: 400, 500, 18px, 32px, 44px, 58px, 80px, 1.10, 1.20, 1.25, 1.50; substitute `Montserrat`.

## Spacing / shape
- Section Gap: `64-80px`
- Card Padding: `12-24px`
- Element Gap: `4-16px`
- Radius: `cards: 4px, images: 24px, buttons: 6px, input_fields: 4px`

## Component cues
- **Risk Indicator Cards**: Reference component style.
- **Hero CTA Section**: Reference component style.
- **Button Group**: Reference component style.
- **Primary Call-to-Action Button**: Interactive element
- **Secondary Outlined Button**: Interactive element

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
