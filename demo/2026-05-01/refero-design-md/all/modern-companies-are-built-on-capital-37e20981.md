# Modern companies are built on Capital - Refero Design MD

- Source: https://styles.refero.design/style/37e20981-1f35-4314-87c1-fdb61ab2f0c0
- Original site: https://capital.xyz
- Theme: `dark`
- Industry: `fintech`
- Recommended fit: **Source ledger / evidence dashboard**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Midnight Ledger, Ember Accent

## Apply to
- Source ledger, ranking, and verification screens
- Cluster evidence dashboards
- Dense data tables with clear hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Ink | `#000000` | neutral | Primary text or dark surface |
| Ash Canvas | `#efece6` | neutral | Page background or card surface |
| Charcoal Surface | `#1a1a1a` | neutral | Primary text or dark surface |
| Onyx Shadow | `#131413` | neutral | Primary text or dark surface |
| Slate Text | `#bfbcb7` | neutral | Border, muted text, or supporting surface |
| Cadet Grey | `#8e8c87` | neutral | Border, muted text, or supporting surface |
| Deep Graphite | `#302f2f` | neutral | Primary text or dark surface |
| Ember Glow | `#ed5145` | brand | Action accent / signal color |
| Crimson Shadow | `#82403a` | brand | Action accent / signal color |
| Sunset Blush | `#ff7a70` | brand | Action accent / signal color |

```css
:root {
  --ref-midnight-ink: #000000;
  --ref-ash-canvas: #efece6;
  --ref-charcoal-surface: #1a1a1a;
  --ref-onyx-shadow: #131413;
  --ref-slate-text: #bfbcb7;
  --ref-cadet-grey: #8e8c87;
  --ref-deep-graphite: #302f2f;
  --ref-ember-glow: #ed5145;
}
```

## Typography direction
- **Muoto**: 300, 400, 500, 12px, 14px, 16px, 20px, 28px, 32px, 72px, 90px, 115px, 1.15, 1.20, 1.40, 1.43, 1.50, 1.67; substitute `Open Sans`.
- **GT America Mono**: 400, 12px, 1.15, 1.60; substitute `Space Mono`.

## Spacing / shape
- Section Gap: `40px`
- Card Padding: `24px`
- Element Gap: `16px`
- Radius: `tags: 3px, cards: 16px, buttons: 8px, ghostControls: 24px`

## Surface cues
- **Midnight Ink** `#000000`: Base page background and primary dark canvas.
- **Onyx Shadow** `#131413`: Slightly elevated dark surfaces, providing subtle differentiation from the base background.
- **Charcoal Surface** `#1a1a1a`: Secondary container backgrounds for interactive elements or distinct content blocks within dark sections.
- **Ash Canvas** `#efece6`: Light background for cards and alternating content sections, creating visual breaks and high contrast.

## Component cues
- **Accent Filled Button**: Primary call-to-action button
- **Subtle Outlined Button**: Secondary action button/link
- **Monochrome Ghost Button With Border**: Tertiary action with emphasis
- **Product Feature Card**: Content grouping for features or informational blocks
- **Mini Tag**: Informational labels or status indicators

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
