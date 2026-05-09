# Spellbook - Refero Design MD

- Source: https://styles.refero.design/style/9dced8d7-3d19-45d3-9dc5-e5906c3e1578
- Original site: https://www.spellbook.legal
- Theme: `dark`
- Industry: `ai`
- Recommended fit: **Admin console / run monitor / developer tooling**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Midnight command center, crisp and precise.

## Apply to
- Admin run monitor and review states
- Compact evidence cards and source inspection panels
- Dark-mode operational dashboards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Charcoal | `#121719` | neutral | Primary text or dark surface |
| Deep Slate | `#222729` | neutral | Primary text or dark surface |
| Pure White | `#ffffff` | neutral | Page background or card surface |
| Ghost Gray | `#f1f3f4` | neutral | Page background or card surface |
| Cool Steel | `#909394` | neutral | Border, muted text, or supporting surface |
| Input Charcoal | `#2b3133` | neutral | Primary text or dark surface |
| Sunset Orange | `#f94d1e` | accent | Action accent / signal color |
| Electric Blue | `#029cff` | brand | Action accent / signal color |
| Royal Violet | `#7834b5` | accent | Action accent / signal color |

```css
:root {
  --ref-midnight-charcoal: #121719;
  --ref-deep-slate: #222729;
  --ref-pure-white: #ffffff;
  --ref-ghost-gray: #f1f3f4;
  --ref-cool-steel: #909394;
  --ref-input-charcoal: #2b3133;
  --ref-sunset-orange: #f94d1e;
  --ref-electric-blue: #029cff;
}
```

## Typography direction
- **Soehne**: 400, 500, 600, 700, 13px, 14px, 16px, 18px, 20px, 22px, 24px, 1.00, 1.30, 1.40, 1.44, 1.50, 1.60, 1.63; substitute `system-ui, sans-serif`.
- **Arizona Mix**: 500, 28px, 51px, 67px, 77px, 1.00, 1.10, 1.15; substitute `Georgia, serif`.

## Spacing / shape
- Section Gap: `27px`
- Card Padding: `12px`
- Element Gap: `12px`
- Page Max Width: `1360px`
- Radius: `badges: 100px, buttons: 1600px, default: 4px, decorative: 320px`

## Surface cues
- **Primary Canvas** `#121719`: The foundational background for the entire page.
- **Card Surface** `#222729`: Background for content cards, feature blocks, and secondary interactive areas.
- **Input Surface** `#2b3133`: Background for form input fields, providing slight elevation from card surfaces.

## Component cues
- **Primary Action Button**: Filled button
- **Secondary Ghost Button**: Outlined button
- **Navigation Link Button**: Subtle button/link
- **Dark Card**: Content container
- **Decorative Card**: Featured content container

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
