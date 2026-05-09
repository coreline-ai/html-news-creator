# SpaceX - Refero Design MD

- Source: https://styles.refero.design/style/13b74e34-b824-4d1d-bd2c-bb9bfbc2d6e1
- Original site: https://spacex.com
- Theme: `dark`
- Industry: `other`
- Recommended fit: **Admin console / run monitor / developer tooling**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Deep Space Command. A minimalist, dark-mode interface designed for high-stakes, information-dense environments, where every pixel counts.

## Apply to
- Admin run monitor and review states
- Compact evidence cards and source inspection panels
- Dark-mode operational dashboards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Void | `#000000` | neutral | Primary text or dark surface |
| Lunar Dust | `#f0f0fa` | neutral | Page background or card surface |
| Interstellar Gray | `#545457` | neutral | Border, muted text, or supporting surface |
| Cosmic Gray | `#404040` | neutral | Border, muted text, or supporting surface |

```css
:root {
  --ref-midnight-void: #000000;
  --ref-lunar-dust: #f0f0fa;
  --ref-interstellar-gray: #545457;
  --ref-cosmic-gray: #404040;
}
```

## Typography direction
- **D-DIN**: 400, 700, 10px, 12px, 13px, 16px, 0.94, 1.00, 1.20, 1.50, 1.70, 2.00; substitute `Arial, sans-serif`.
- **D-DIN-Bold**: 400, 48px, 1.00, 1.25; substitute `Arial Bold, sans-serif`.

## Spacing / shape
- Section Gap: `60px`
- Card Padding: `20px`
- Element Gap: `18px`
- Radius: `buttons: 4px, navigation: 4px, pillButton: 32px`

## Component cues
- **Ghost Primary Button Group**: Reference component style.
- **Upcoming Launch Card**: Reference component style.
- **Mission Stat Block**: Reference component style.
- **Ghost Primary Button**: Primary call to action.
- **Pill Accent Button**: Secondary or alternative call to action, often for reservation or ordering.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
