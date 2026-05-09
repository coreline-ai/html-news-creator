# WalletConnect - Refero Design MD

- Source: https://styles.refero.design/style/29392960-0acf-4891-ad33-28a72f6a9b75
- Original site: https://walletconnect.com
- Theme: `light`
- Industry: `fintech`
- Recommended fit: **Admin console / run monitor / developer tooling**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Digital ledger on white marble.

## Apply to
- Admin run monitor and review states
- Compact evidence cards and source inspection panels
- Dark-mode operational dashboards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Paper White | `#f9f9f9` | neutral | Page background or card surface |
| Ash Gray | `#e9e9e9` | neutral | Page background or card surface |
| Graphite | `#202020` | neutral | Primary text or dark surface |
| Midnight Ink | `#1b2045` | neutral | Primary text or dark surface |
| Slate Gray | `#4f4f4f` | neutral | Border, muted text, or supporting surface |
| Silver Mist | `#787878` | neutral | Border, muted text, or supporting surface |
| Light Steel | `#bbbbbb` | neutral | Border, muted text, or supporting surface |
| Sky Blue | `#cce2ff` | brand | Action accent / signal color |
| Azure Blue | `#006cff` | brand | Action accent / signal color |

```css
:root {
  --ref-canvas-white: #ffffff;
  --ref-paper-white: #f9f9f9;
  --ref-ash-gray: #e9e9e9;
  --ref-graphite: #202020;
  --ref-midnight-ink: #1b2045;
  --ref-slate-gray: #4f4f4f;
  --ref-silver-mist: #787878;
  --ref-light-steel: #bbbbbb;
}
```

## Typography direction
- **KHTeka**: 400, 13px, 14px, 16px, 18px, 20px, 24px, 30px, 36px, 1.00, 1.11, 1.20, 1.33, 1.40, 1.43, 1.46, 1.50, 1.56, 1.71; substitute `Inter`.
- **Roboto**: 400, 500, 700, 12px, 16px, 17px, 1.41, 1.50, 2.00; substitute `Roboto`.
- **KHTekaMono**: 400, 12px, 14px, 1.33, 1.43; substitute `Fira Code`.

## Spacing / shape
- Section Gap: `32px`
- Card Padding: `12px`
- Element Gap: `8px`
- Page Max Width: `1600px`
- Radius: `default: 3px, heroElement: 40px, interactive: 16px`

## Surface cues
- **Canvas White** `#ffffff`: Base page background
- **Paper White** `#f9f9f9`: Default surface for cards and modals
- **Ash Gray** `#e9e9e9`: Secondary background for distinguished sections or cards
- **Light Steel** `#bbbbbb`: Tertiary background for specific accented areas or larger cards

## Component cues
- **Ghost Navigation Button**: Top navigation links, secondary calls to action.
- **Default Small Button**: General purpose action button.
- **Primary Action Button (Filled)**: Main call to action.
- **Outline CTA Button**: Secondary call to action.
- **Subtle Padding Card**: Generic card for content regions.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
