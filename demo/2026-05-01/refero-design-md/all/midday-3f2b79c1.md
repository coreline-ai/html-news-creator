# Midday - Refero Design MD

- Source: https://styles.refero.design/style/3f2b79c1-d980-4380-a903-29856975fc37
- Original site: https://midday.ai
- Theme: `light`
- Industry: `fintech`
- Recommended fit: **Admin console / run monitor / developer tooling**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Achromatic ledger, crisp yet silent

## Apply to
- Admin run monitor and review states
- Compact evidence cards and source inspection panels
- Dark-mode operational dashboards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Ink Black | `#121212` | neutral | Primary text or dark surface |
| Ash Gray | `#dbdad7` | neutral | Page background or card surface |
| Deep Graphite | `#18181b` | neutral | Primary text or dark surface |
| Cool Gray Mist | `#e6e4e0` | neutral | Page background or card surface |
| Muted Stone | `#616161` | neutral | Border, muted text, or supporting surface |
| Success Green | `#4caf50` | accent | Action accent / signal color |

```css
:root {
  --ref-canvas-white: #ffffff;
  --ref-ink-black: #121212;
  --ref-ash-gray: #dbdad7;
  --ref-deep-graphite: #18181b;
  --ref-cool-gray-mist: #e6e4e0;
  --ref-muted-stone: #616161;
  --ref-success-green: #4caf50;
}
```

## Typography direction
- **Hedvig Letters Sans**: 400, 500, 10px, 11px, 12px, 14px, 16px, 18px, 20px, 24px, 48px, 508px, 1.00, 1.33, 1.40, 1.43, 1.50, 1.56, 1.63; substitute `Inter`.
- **Hedvig Letters Serif**: 400, 24px, 72px, 1.00, 1.33; substitute `Playfair Display`.

## Spacing / shape
- Section Gap: `24px`
- Card Padding: `20px`
- Element Gap: `8px`
- Page Max Width: `1280px`
- Radius: `cards: 0px, icons: 8px, input: 0px, badges: 9999px, buttons: 9999px`

## Surface cues
- **Canvas** `#ffffff`: Dominant page background, foundational for all content.
- **Card Base** `#ffffff`: Background for primary content cards and information blocks.
- **Muted Section** `#e6e4e0`: Background for subtle alternations in section backgrounds or selected interface elements.

## Component cues
- **Pill Button - Default**: Default interactive button
- **Solid Button - Primary**: Primary call to action button
- **Ghost Button**: Ghost-style button for secondary actions or toggles
- **Integration Card Variant**: Card for displaying tool integrations
- **Feature Card**: Information card for features or pricing

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
