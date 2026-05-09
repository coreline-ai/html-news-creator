# International Magic - Refero Design MD

- Source: https://styles.refero.design/style/c406697b-677f-40c7-a3a2-10ea545278f1
- Original site: https://intmagic.com
- Theme: `dark`
- Industry: `other`
- Recommended fit: **Admin console / run monitor / developer tooling**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Midnight Terminal, Pixelated Echoes

## Apply to
- Admin run monitor and review states
- Compact evidence cards and source inspection panels
- Dark-mode operational dashboards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Ink | `#0a0a0a` | neutral | Primary text or dark surface |
| Ghost White | `#f7f7f7` | neutral | Page background or card surface |
| Ash Gray | `#7c7c7c` | neutral | Border, muted text, or supporting surface |
| Steel Gray | `#4d4d4d` | neutral | Border, muted text, or supporting surface |
| Porcelain | `#ebebeb` | neutral | Page background or card surface |
| Muted Slate | `#616161` | neutral | Border, muted text, or supporting surface |
| Shadowened Clay | `#585858` | neutral | Border, muted text, or supporting surface |
| Faded Silver | `#707070` | neutral | Border, muted text, or supporting surface |

```css
:root {
  --ref-midnight-ink: #0a0a0a;
  --ref-ghost-white: #f7f7f7;
  --ref-ash-gray: #7c7c7c;
  --ref-steel-gray: #4d4d4d;
  --ref-porcelain: #ebebeb;
  --ref-muted-slate: #616161;
  --ref-shadowened-clay: #585858;
  --ref-faded-silver: #707070;
}
```

## Typography direction
- **Wand UI Pro**: 400, 475, 500, 550, 650, 10px, 11px, 15px, 16px, 32px, 96px, 1.00, 1.10, 1.20, 1.25, 1.40, 1.60; substitute `Inter`.

## Spacing / shape
- Section Gap: `64px`
- Card Padding: `16px`
- Element Gap: `16px`
- Radius: `badges: 9999px, images: 20px, buttons: 9999px, default: 24px`

## Component cues
- **Ghost Header Button**: Navigation links and primary actions in headers
- **Secondary Filled Button**: Subtle interactive elements, 'Subscribe' button
- **Badge**: Categorization and metadata labels

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
