# David Kirschberg - Refero Design MD

- Source: https://styles.refero.design/style/004f4856-4b01-4c23-a9fb-866303d5013b
- Original site: https://kirschberg.co.nz
- Theme: `dark`
- Industry: `design`
- Recommended fit: **Admin console / run monitor / developer tooling**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Minimalist Dark Canvas — bold text on deep charcoal.

## Apply to
- Admin run monitor and review states
- Compact evidence cards and source inspection panels
- Dark-mode operational dashboards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Core | `#181818` | neutral | Primary text or dark surface |
| Frost White | `#fafafa` | neutral | Page background or card surface |
| Slate Surface | `#262626` | neutral | Primary text or dark surface |
| Ash Muted | `#a3a3a3` | neutral | Border, muted text, or supporting surface |

```css
:root {
  --ref-midnight-core: #181818;
  --ref-frost-white: #fafafa;
  --ref-slate-surface: #262626;
  --ref-ash-muted: #a3a3a3;
}
```

## Typography direction
- **Inter**: 400, 16px, 17px, 1.18, 1.29, 1.50; substitute `system-ui`.
- **twkLausanne**: 400, 32px, 1.10; substitute `Arial`.

## Spacing / shape
- Section Gap: `45px`
- Card Padding: `16px`
- Element Gap: `8px`
- Radius: `default: 16px, surfaces: 24px`

## Component cues
- **Ghost Button**: Interactive elements with minimal visual weight.
- **Work Item Card**: Cards for showcasing portfolio pieces.
- **Navigation Bar**: Sticky header for site navigation.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
