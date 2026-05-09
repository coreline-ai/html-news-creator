# LaunchDarkly - Refero Design MD

- Source: https://styles.refero.design/style/18a75348-513a-49d8-94f5-e2df8c118b6b
- Original site: https://launchdarkly.com
- Theme: `dark`
- Industry: `saas`
- Recommended fit: **Admin console / run monitor / developer tooling**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Midnight Terminal, Violet Haze

## Apply to
- Admin run monitor and review states
- Compact evidence cards and source inspection panels
- Dark-mode operational dashboards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Carbon Black | `#191919` | neutral | Primary text or dark surface |
| Graphite | `#414042` | neutral | Border, muted text, or supporting surface |
| Deep Space Gray | `#2c2c2c` | neutral | Primary text or dark surface |
| Mercury White | `#ffffff` | neutral | Page background or card surface |
| Stardust Gray | `#f8f8f2` | neutral | Page background or card surface |
| Cadet Gray | `#a7a9ac` | neutral | Border, muted text, or supporting surface |
| Silver Mist | `#d1d3d4` | neutral | Border, muted text, or supporting surface |
| Input Gray | `#58595b` | neutral | Border, muted text, or supporting surface |
| Launch Violet | `#7084ff` | brand | Action accent / signal color |
| Orbital Blue | `#405bff` | accent | Action accent / signal color |

```css
:root {
  --ref-carbon-black: #191919;
  --ref-graphite: #414042;
  --ref-deep-space-gray: #2c2c2c;
  --ref-mercury-white: #ffffff;
  --ref-stardust-gray: #f8f8f2;
  --ref-cadet-gray: #a7a9ac;
  --ref-silver-mist: #d1d3d4;
  --ref-input-gray: #58595b;
}
```

## Typography direction
- **bodyFont**: 400, 500, 600, 700, 12px, 13px, 14px, 15px, 16px, 18px, 20px, 22px, 24px, 26px, 28px, 32px, 36px, 40px, 66px, 84px, 85px, 100px, 125px, 1.00, 1.09, 1.20, 1.30, 1.40, 1.50, 1.60, 1.71; substitute `system-ui, sans-serif`.
- **bodyFont**: 400, 500, 600, 700, 12px, 13px, 14px, 15px, 16px, 18px, 20px, 22px, 24px, 26px, 28px, 32px, 36px, 40px, 66px, 84px, 85px, 100px, 125px, 1.00, 1.09, 1.20, 1.30, 1.40, 1.50, 1.60, 1.71; substitute `system-ui, sans-serif`.
- **bodyFont**: 400, 500, 600, 700, 12px, 13px, 14px, 15px, 16px, 18px, 20px, 22px, 24px, 26px, 28px, 32px, 36px, 40px, 66px, 84px, 85px, 100px, 125px, 1.00, 1.09, 1.20, 1.30, 1.40, 1.50, 1.60, 1.71; substitute `system-ui, sans-serif`.

## Spacing / shape
- Section Gap: `32px`
- Card Padding: `16px`
- Element Gap: `16px`
- Page Max Width: `1188px`
- Radius: `tags: 60px, cards: 30px, input: 10px, buttons: 30px, navigation: 4px`

## Surface cues
- **Graphite** `#414042`: Base page background
- **Carbon Black** `#191919`: Card and button backgrounds, Footer
- **Deep Space Gray** `#2c2c2c`: Subtle border/divider on cards

## Component cues
- **Navigation Link**: Top navigation items with ghost styling
- **Primary Action Button**: Calls to action with filled background
- **Outlined Action Button**: Secondary action buttons with a border
- **Toggle Button**: Segmented control option
- **Feature Card**: Container for feature descriptions or callouts

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
