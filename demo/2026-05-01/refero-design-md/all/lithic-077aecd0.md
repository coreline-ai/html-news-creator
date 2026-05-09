# Lithic - Refero Design MD

- Source: https://styles.refero.design/style/077aecd0-4401-4696-a196-164d74ac8746
- Original site: https://www.lithic.com
- Theme: `light`
- Industry: `fintech`
- Recommended fit: **Admin console / run monitor / developer tooling**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
High-contrast developer portal.

## Apply to
- Admin run monitor and review states
- Compact evidence cards and source inspection panels
- Dark-mode operational dashboards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Obsidian | `#000000` | neutral | Primary text or dark surface |
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Faint Bronze | `#f6f3ee` | neutral | Page background or card surface |
| Faint Amethyst | `#f6f1fe` | neutral | Page background or card surface |
| Muted Ash | `#e5e5e5` | neutral | Page background or card surface |
| Mid Grey | `#888888` | neutral | Border, muted text, or supporting surface |
| Warm Copper | `#ff6600` | brand | Action accent / signal color |
| Muted Bronze | `#aa8855` | accent | Action accent / signal color |
| Emerald Green | `#00cc88` | accent | Action accent / signal color |
| Dark Amethyst | `#5c2999` | accent | Action accent / signal color |

```css
:root {
  --ref-obsidian: #000000;
  --ref-canvas-white: #ffffff;
  --ref-faint-bronze: #f6f3ee;
  --ref-faint-amethyst: #f6f1fe;
  --ref-muted-ash: #e5e5e5;
  --ref-mid-grey: #888888;
  --ref-warm-copper: #ff6600;
  --ref-muted-bronze: #aa8855;
}
```

## Typography direction
- **ABC Monument Grotesk**: 400, 500, 14px, 16px, 20px, 24px, 36px, 64px, 1.00, 1.20, 1.40, 1.50, 1.52, 1.71; substitute `Arial`.
- **ABC Monument Grotesk**: 400, 500, 14px, 16px, 20px, 24px, 36px, 64px, 1.00, 1.20, 1.40, 1.50, 1.52, 1.71; substitute `Arial`.

## Spacing / shape
- Section Gap: `24px`
- Card Padding: `40px`
- Element Gap: `24px`
- Radius: `cards: 24px, icons: 800px, images: 21.6px, buttons: 8px`

## Surface cues
- **Obsidian Base** `#000000`: Primary background for hero sections and dark content blocks, providing a high-contrast starting point.
- **Canvas White** `#ffffff`: Dominant background for most content sections, providing a clean, bright canvas.
- **Cream Tint Card** `#ebfef6`: Subtle, slightly warm background tint for certain information cards.
- **Faint Bronze Card** `#f6f3ee`: Mildly textured, warm card background for highlighting specific content areas.
- **Faint Amethyst Card** `#f6f1fe`: Cool-tinted card background for distinct feature blocks.

## Component cues
- **Primary Action Button**: Filled button for primary calls to action.
- **Ghost Action Button**: Outlined button for secondary actions or navigation.
- **Pill Ghost Button (Hero)**: Large, ghosted button used in hero sections.
- **Neutral Tag Button**: Small, light grey button for tags or metadata.
- **Feature Card - Faint Bronze**: Card for showcasing features with a warm background tint.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
