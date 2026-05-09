# Metaview - Refero Design MD

- Source: https://styles.refero.design/style/f99856e1-3627-4624-a811-f6053a978b62
- Original site: https://metaview.ai
- Theme: `dark`
- Industry: `ai`
- Recommended fit: **Admin console / run monitor / developer tooling**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Midnight Command Center

## Apply to
- Admin run monitor and review states
- Compact evidence cards and source inspection panels
- Dark-mode operational dashboards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Void Black | `#000000` | neutral | Primary text or dark surface |
| Ghost White | `#ffffff` | neutral | Page background or card surface |
| Carbon | `#161818` | neutral | Primary text or dark surface |
| Deep Space | `#0a1a14` | neutral | Primary text or dark surface |
| Twilight Slate | `#01051b` | neutral | Primary text or dark surface |
| Ash Gray | `#5e6262` | neutral | Border, muted text, or supporting surface |
| Slate Border | `#828282` | neutral | Border, muted text, or supporting surface |
| Cloud Gray | `#d9d9d9` | neutral | Page background or card surface |
| Mint Glare | `#7affb4` | brand | Action accent / signal color |
| Soft Mint | `#e3ffef` | accent | Action accent / signal color |

```css
:root {
  --ref-void-black: #000000;
  --ref-ghost-white: #ffffff;
  --ref-carbon: #161818;
  --ref-deep-space: #0a1a14;
  --ref-twilight-slate: #01051b;
  --ref-ash-gray: #5e6262;
  --ref-slate-border: #828282;
  --ref-cloud-gray: #d9d9d9;
}
```

## Typography direction
- **Euclid Circular A**: 300, 400, 500, 700, 12px, 14px, 15px, 16px, 18px, 20px, 22px, 28px, 36px, 48px, 68px, 72px, 1.00, 1.04, 1.10, 1.12, 1.16, 1.20, 1.30, 1.34, 1.42, 1.48, 1.50, 1.60; substitute `system-ui, sans-serif`.
- **Onsite SemiMono**: 400, 12px, 16px, 1.48, 1.60; substitute `Menlo, Consolas, monospace`.

## Spacing / shape
- Section Gap: `40px`
- Card Padding: `16px`
- Element Gap: `8px`
- Radius: `misc: 12px, tags: 8px, cards: 16px, icons: 4px, buttons: 999px`

## Component cues
- **Primary Action Button**: Call to action
- **Secondary Action Button**: Alternative action
- **Ghost Button**: Tertiary action, navigation
- **Navigation Link**: Primary navigation
- **Dark Card (Product View)**: Content container for product features/data

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
