# Tinybird - Refero Design MD

- Source: https://styles.refero.design/style/e5d7b80d-f473-439f-87a5-84716c448a05
- Original site: https://tinybird.co
- Theme: `dark`
- Industry: `devtools`
- Recommended fit: **Source ledger / evidence dashboard**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Data noir interface — high contrast text and a single, electric green highlight on a deep, almost black background.

## Apply to
- Source ledger, ranking, and verification screens
- Cluster evidence dashboards
- Dense data tables with clear hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Ink | `#0a0a0a` | neutral | Primary text or dark surface |
| Obsidian Slate | `#262626` | neutral | Primary text or dark surface |
| Iron Oxide | `#151515` | neutral | Primary text or dark surface |
| Deep Graphite | `#353535` | neutral | Primary text or dark surface |
| Silver Mist | `#8d8d8d` | neutral | Border, muted text, or supporting surface |
| Pure White | `#ffffff` | neutral | Page background or card surface |
| Electric Green | `#27f795` | brand | Action accent / signal color |
| Deep Jade | `#008060` | semantic | Action accent / signal color |
| Alert Red | `#800000` | semantic | Action accent / signal color |
| Crimson Hue | `#ec6d62` | semantic | Action accent / signal color |

```css
:root {
  --ref-midnight-ink: #0a0a0a;
  --ref-obsidian-slate: #262626;
  --ref-iron-oxide: #151515;
  --ref-deep-graphite: #353535;
  --ref-silver-mist: #8d8d8d;
  --ref-pure-white: #ffffff;
  --ref-electric-green: #27f795;
  --ref-deep-jade: #008060;
}
```

## Typography direction
- **Roboto**: 400, 600, 700, 12px, 14px, 16px, 18px, 24px, 64px, 1.13, 1.33, 1.50, 1.57, 1.67, 1.78; substitute `system-ui, sans-serif`.
- **Roboto Mono**: 400, 12px, 14px, 16px, 56px, 1.00, 1.50, 1.57, 1.67; substitute `monospace`.

## Spacing / shape
- Card Padding: `0px`
- Element Gap: `8px`
- Radius: `cards: 8px, buttons: 0px, default: 4px`

## Component cues
- **CTA Button Group**: Reference component style.
- **Use Case Tag Selector**: Reference component style.
- **Testimonial Card Grid**: Reference component style.
- **Primary CTA Button**: Call to action
- **Ghost Navigation Link**: Navigation

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
