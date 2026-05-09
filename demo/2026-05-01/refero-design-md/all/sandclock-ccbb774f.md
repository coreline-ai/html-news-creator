# Sandclock - Refero Design MD

- Source: https://styles.refero.design/style/ccbb774f-d1a9-4cc6-b1be-31379ba0baf1
- Original site: https://www.sandclock.org
- Theme: `dark`
- Industry: `fintech`
- Recommended fit: **Admin console / run monitor / developer tooling**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Midnight Command Center: Tightly tracked typography and a single digital-green accent on a deep, dark canvas.

## Apply to
- Admin run monitor and review states
- Compact evidence cards and source inspection panels
- Dark-mode operational dashboards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Absolute Zero | `#0a0a0a` | neutral | Primary text or dark surface |
| Deep Space | `#171717` | neutral | Primary text or dark surface |
| Void Black | `#222222` | neutral | Primary text or dark surface |
| Cosmic Dust | `#9b9b9b` | neutral | Border, muted text, or supporting surface |
| Starlight White | `#ffffff` | neutral | Page background or card surface |
| Digital Green | `#3fe280` | accent | Action accent / signal color |

```css
:root {
  --ref-absolute-zero: #0a0a0a;
  --ref-deep-space: #171717;
  --ref-void-black: #222222;
  --ref-cosmic-dust: #9b9b9b;
  --ref-starlight-white: #ffffff;
  --ref-digital-green: #3fe280;
}
```

## Typography direction
- **Inter**: 400, 500, 14px, 16px, 20px, 24px, 36px, 1.11, 1.33, 1.40, 1.43, 1.50; substitute `system-ui`.
- **DM Sans**: 500, 16px, 1.20; substitute `sans-serif`.
- **Aeonik**: 400, 72px, 1.00; substitute `Arial`.

## Spacing / shape
- Section Gap: `48px`
- Card Padding: `16px`
- Element Gap: `16px`
- Radius: `pill: 64px, cards: 12px, buttons: 16px, bodyMask: 9999px`

## Component cues
- **Pill Ghost Button (Connect Wallet)**: Main navigation action
- **Primary Action Button (Digital Green)**: Key call to action
- **Secondary Action Button (Void Black)**: Alternative action button
- **Feature Card**: Content grouping
- **Vault Performance Card**: Key data display

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
