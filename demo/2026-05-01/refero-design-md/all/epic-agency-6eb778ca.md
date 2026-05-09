# EPIC agency - Refero Design MD

- Source: https://styles.refero.design/style/6eb778ca-6808-4cc6-ac8a-7beea5a25c36
- Original site: https://epic.net
- Theme: `dark`
- Industry: `agency`
- Recommended fit: **Admin console / run monitor / developer tooling**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Deep-space command center. A shimmering violet expanse punctuated by crisp text and glowing 3D objects.

## Apply to
- Admin run monitor and review states
- Compact evidence cards and source inspection panels
- Dark-mode operational dashboards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Nebula Violet | `#271a47` | brand | Action accent / signal color |
| Stardust Shimmer | `#dbc9ff` | brand | Action accent / signal color |
| Cosmos Black | `#000000` | neutral | Primary text or dark surface |

```css
:root {
  --ref-nebula-violet: #271a47;
  --ref-stardust-shimmer: #dbc9ff;
  --ref-cosmos-black: #000000;
}
```

## Typography direction
- **Inter**: 400, 600, 700, 10px, 11px, 13px, 14px, 16px, 18px, 1.00, 1.33, 1.40, 1.56, 1.65, 1.70, 3.00; substitute `Inter`.
- **Sang Bleu**: 400, 700, 900, 42px, 80px, 120px, 1.00, 1.20, 1.65; substitute `Playfair Display`.

## Spacing / shape
- Section Gap: `32px`
- Card Padding: `12-18px`
- Page Max Width: `1200px`
- Radius: `buttons: 20px, 30px, general: 10px, menu-items: 0px`

## Component cues
- **Journal Entry List**: Reference component style.
- **Button Group**: Reference component style.
- **Showreel Section**: Reference component style.
- **Primary Ghost Button**: Interactive element
- **Secondary Ghost Button**: Interactive element

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
