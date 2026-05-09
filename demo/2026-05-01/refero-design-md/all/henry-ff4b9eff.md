# Henry - Refero Design MD

- Source: https://styles.refero.design/style/ff4b9eff-dc0b-4886-bd65-c2f5e9069318
- Original site: https://henry.codes
- Theme: `light`
- Industry: `design`
- Recommended fit: **Admin console / run monitor / developer tooling**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Distressed newsprint, black-and-white grid

## Apply to
- Admin run monitor and review states
- Compact evidence cards and source inspection panels
- Dark-mode operational dashboards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Ink | `#2a2722` | neutral | Primary text or dark surface |
| Canvas White | `#fafafa` | neutral | Page background or card surface |
| Graphite Text | `#3e3b36` | neutral | Primary text or dark surface |
| Ash Gray | `#9f9f9f` | neutral | Border, muted text, or supporting surface |
| Light Border | `#eeeeee` | neutral | Page background or card surface |
| Midtone Text | `#666666` | neutral | Border, muted text, or supporting surface |
| Muted Silver | `#b3b3b3` | neutral | Border, muted text, or supporting surface |
| Faded Gray | `#a9a9a9` | neutral | Border, muted text, or supporting surface |
| Rainbow Band | `#c679c4` | accent | Action accent / signal color |

```css
:root {
  --ref-midnight-ink: #2a2722;
  --ref-canvas-white: #fafafa;
  --ref-graphite-text: #3e3b36;
  --ref-ash-gray: #9f9f9f;
  --ref-light-border: #eeeeee;
  --ref-midtone-text: #666666;
  --ref-muted-silver: #b3b3b3;
  --ref-faded-gray: #a9a9a9;
}
```

## Typography direction
- **Neue Montreal**: 400, 700, 12px, 16px, 20px, 24px, 32px, 1.00, 1.10, 1.20, 1.50; substitute `Inter`.
- **Louize Display**: 400, 32px, 35px, 77px, 116px, 126px, 132px, 0.80, 0.90, 1.10, 1.20; substitute `Anton`.
- **Louize**: 400, 16px, 20px, 24px, 1.20, 1.30; substitute `Merriweather`.

## Spacing / shape
- Section Gap: `32px`
- Card Padding: `16px`
- Element Gap: `16px`
- Radius: `cards: 12px, other: 12px`

## Component cues
- **Text Content Card, Default**: Container for articles or body text.
- **Text Content Card, Rounded**: Container for 'Brief Letter' and similar self-contained content.
- **Navigation Link, Primary**: Main navigation items in the sidebar or header.
- **Section Divider Line**: Visual separation between major content blocks.
- **Ghost Button / Outlined Link**: Interactive elements with a minimal footprint, such as 'read more' or external links.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
