# Arcadia - Refero Design MD

- Source: https://styles.refero.design/style/b52981ce-fdb2-4ba0-86bb-f5ce0c27a9c6
- Original site: https://www.arcadia.com
- Theme: `light`
- Industry: `saas`
- Recommended fit: **Source ledger / evidence dashboard**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Evergreen data canvas

## Apply to
- Source ledger, ranking, and verification screens
- Cluster evidence dashboards
- Dense data tables with clear hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Evergreen Deep | `#104336` | brand | Action accent / signal color |
| Mid-Tone Charcoal | `#101f1e` | neutral | Primary text or dark surface |
| Electric Violet | `#7c18d3` | accent | Action accent / signal color |
| Verdant Accent | `#0fff87` | accent | Action accent / signal color |
| Pale Sage | `#afc4bf` | neutral | Border, muted text, or supporting surface |
| White Canvas | `#ffffff` | neutral | Page background or card surface |
| Pampas | `#f3f1ec` | neutral | Page background or card surface |
| Graphite | `#535e5d` | neutral | Border, muted text, or supporting surface |
| Dark Carbon | `#333333` | neutral | Primary text or dark surface |
| Silver Pine | `#c2cec8` | neutral | Border, muted text, or supporting surface |

```css
:root {
  --ref-evergreen-deep: #104336;
  --ref-mid-tone-charcoal: #101f1e;
  --ref-electric-violet: #7c18d3;
  --ref-verdant-accent: #0fff87;
  --ref-pale-sage: #afc4bf;
  --ref-white-canvas: #ffffff;
  --ref-pampas: #f3f1ec;
  --ref-graphite: #535e5d;
}
```

## Typography direction
- **DM Sans**: 300, 400, 500, 700, 10px, 13px, 14px, 15px, 16px, 18px, 20px, 24px, 36px, 48px, 56px, 1.00, 1.10, 1.15, 1.20, 1.29, 1.50; substitute `system-ui`.
- **Helvetica**: 400, 700, 13px, 1.20; substitute `Arial`.

## Spacing / shape
- Section Gap: `24px`
- Card Padding: `24px`
- Element Gap: `24px`
- Radius: `tags: 18px, cards: 16px, image: 8px, input: 4px, buttons: 8px`

## Surface cues
- **White Canvas** `#ffffff`: Base page background and default elevated surface for cards.
- **Pampas** `#f3f1ec`: Secondary background for alternating sections, providing subtle visual separation and warmth without stark contrast.
- **Gradient Aura** `#afc4bf`: Soft gradient background for hero sections or prominent content blocks, adding atmospheric depth.

## Component cues
- **Ghost Bordered Button**: Secondary action button
- **Request Demo Button (Filled)**: Primary Call-to-Action
- **Sign In Button (Filled)**: Secondary Call-to-Action
- **Default Card**: Content container
- **Pampas Section Card**: Section background container

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
