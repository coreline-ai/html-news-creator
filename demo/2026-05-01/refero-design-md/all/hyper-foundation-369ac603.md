# Hyper Foundation - Refero Design MD

- Source: https://styles.refero.design/style/369ac603-c1e9-4231-9369-a198493f8e47
- Original site: https://hyperliquid.xyz
- Theme: `dark`
- Industry: `fintech`
- Recommended fit: **Admin console / run monitor / developer tooling**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Deep emerald command center.

## Apply to
- Admin run monitor and review states
- Compact evidence cards and source inspection panels
- Dark-mode operational dashboards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Emerald | `#072724` | neutral | Primary text or dark surface |
| Ghost Jade | `#23524c` | neutral | Border, muted text, or supporting surface |
| Aura Mint | `#97fcd7` | accent | Action accent / signal color |
| Ceramic White | `#ffffff` | neutral | Page background or card surface |
| Slate Border | `#2c2e33` | neutral | Primary text or dark surface |
| Platinum Ghost | `#b0c5c1` | neutral | Border, muted text, or supporting surface |
| Ash Text | `#0f3933` | neutral | Primary text or dark surface |
| Deep Teal | `#33998c` | accent | Action accent / signal color |

```css
:root {
  --ref-midnight-emerald: #072724;
  --ref-ghost-jade: #23524c;
  --ref-aura-mint: #97fcd7;
  --ref-ceramic-white: #ffffff;
  --ref-slate-border: #2c2e33;
  --ref-platinum-ghost: #b0c5c1;
  --ref-ash-text: #0f3933;
  --ref-deep-teal: #33998c;
}
```

## Typography direction
- **Teodor**: 400, 24px, 55px, 60px, 90px, 0.75, 1.00, 1.50; substitute `Poly`.
- **Inter**: 300, 400, 12px, 16px, 20px, 28px, 35px, 1.00, 1.30, 1.50; substitute `System Font`.

## Spacing / shape
- Section Gap: `100px`
- Card Padding: `14px`
- Element Gap: `24px`
- Radius: `cards: 12px, forms: 37px, buttons: 60px, default: 12px`

## Surface cues
- **Page Canvas** `#072724`: The primary background for the entire application, providing a deep, consistent dark base.
- **Subtle Card** `#23524c`: Used for secondary cards or content sections that require a slightly distinct background from the main canvas without strong contrast.

## Component cues
- **Primary Action Button**: Call-to-action button, highlighted interaction.
- **Ghost Action Button**: Secondary action button, less prominent interaction.
- **Navigation Link**: Top navigation items.
- **Header Branding**: Brand logo and text in header.
- **Hero Section Headline**: Main title on the landing page.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
