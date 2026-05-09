# Eclipse - Refero Design MD

- Source: https://styles.refero.design/style/fd2e0187-e67b-4869-8cfd-9de9e58d2868
- Original site: https://www.eclipse.builders
- Theme: `dark`
- Industry: `crypto`
- Recommended fit: **Admin console / run monitor / developer tooling**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Cosmic Rave Command Center: stark black and white punctuated by electric green glow.

## Apply to
- Admin run monitor and review states
- Compact evidence cards and source inspection panels
- Dark-mode operational dashboards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Ink | `#000000` | neutral | Primary text or dark surface |
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Electric Mint | `#a1fea0` | brand | Action accent / signal color |
| Muted Ash | `#888680` | neutral | Border, muted text, or supporting surface |
| Pale Stone | `#dfddd6` | neutral | Page background or card surface |
| Graphite | `#302f2c` | neutral | Primary text or dark surface |

```css
:root {
  --ref-midnight-ink: #000000;
  --ref-canvas-white: #ffffff;
  --ref-electric-mint: #a1fea0;
  --ref-muted-ash: #888680;
  --ref-pale-stone: #dfddd6;
  --ref-graphite: #302f2c;
}
```

## Typography direction
- **Gt Alpina Condensed**: 100, 200, 24px, 33px, 44px, 46px, 61px, 64px, 88px, 120px, 562px, 0.80, 1.00, 1.10, 1.13, 1.16, 1.20; substitute `Montserrat Condensed`.
- **Barlow Condensed**: 400, 500, 700, 12px, 16px, 32px, 44px, 48px, 80px, 96px, 120px, 182px, 0.80, 0.83, 0.90, 1.00, 1.19, 1.20, 1.25, 1.50, 1.60; substitute `Oswald`.
- **Atlas Typewriter**: 400, 12px, 16px, 18px, 1.00, 1.56, 1.60; substitute `Space Mono`.

## Spacing / shape
- Section Gap: `24px`
- Card Padding: `32px`
- Element Gap: `10px`
- Page Max Width: `1200px`
- Radius: `cards: 0px, other: 25px, buttons: 100px, navItems: 100px`

## Component cues
- **Ghost Navigation Button**: Primary navigation links and secondary actions, typically found in headers or footers.
- **Mint Pill Button**: Prominent calls to action.
- **Dark Pill Button**: Secondary calls to action or alternative actions.
- **Framed Text Button**: General interactive elements or links with emphasis.
- **Outline Investor Card**: Listing partners or investors with a subtle visual presence.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
