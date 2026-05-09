# Discover - Refero Design MD

- Source: https://styles.refero.design/style/86de6781-d22b-4879-90df-44acb1fe20f3
- Original site: https://fonts.ninja
- Theme: `light`
- Industry: `design`
- Recommended fit: **Admin console / run monitor / developer tooling**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
High-contrast typographic command center.

## Apply to
- Admin run monitor and review states
- Compact evidence cards and source inspection panels
- Dark-mode operational dashboards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Ninja Red | `#ee585a` | brand | Action accent / signal color |
| Midnight Ink | `#121212` | neutral | Primary text or dark surface |
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Light Steel | `#dbdada` | neutral | Page background or card surface |
| Slate Gray | `#8e8e93` | neutral | Border, muted text, or supporting surface |
| Pure Black | `#000000` | neutral | Primary text or dark surface |

```css
:root {
  --ref-ninja-red: #ee585a;
  --ref-midnight-ink: #121212;
  --ref-canvas-white: #ffffff;
  --ref-light-steel: #dbdada;
  --ref-slate-gray: #8e8e93;
  --ref-pure-black: #000000;
}
```

## Typography direction
- **aeonikFont**: 400, 500, 700, 12px, 14px, 16px, 24px, 32px, 44px, 1, 1.14, 1.15, 1.2, 1.5.
- **Aeonik Pro**: use as primary family; substitute `Inter`.

## Spacing / shape
- Section Gap: `32px`
- Card Padding: `24px`
- Element Gap: `10px`
- Radius: `cards: 32px, links: 16px, buttons: 24px, input-filters: 32px, asymmetric-button-right: 0px 32px 32px 0px`

## Component cues
- **Primary Action Button (Filled)**: Main interactive element
- **Asymmetrical Primary Action Button**: Prominent directional action
- **Ghost Button (Text)**: Secondary action or navigation link
- **Font Display Card**: Content container for font examples
- **Feature Card**: Elevated content block

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
