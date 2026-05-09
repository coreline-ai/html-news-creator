# Decide AI - Refero Design MD

- Source: https://styles.refero.design/style/5d9e1cc2-4b81-40fe-aa92-640f2e1d7420
- Original site: https://decideai.xyz
- Theme: `dark`
- Industry: `ai`
- Recommended fit: **Admin console / run monitor / developer tooling**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Midnight Terminal, illuminated by a single green command prompt.

## Apply to
- Admin run monitor and review states
- Compact evidence cards and source inspection panels
- Dark-mode operational dashboards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Deep Space | `#030303` | neutral | Primary text or dark surface |
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| System Gray | `#e5e7eb` | neutral | Page background or card surface |
| Terminal Green | `#73ffb9` | accent | Action accent / signal color |

```css
:root {
  --ref-deep-space: #030303;
  --ref-canvas-white: #ffffff;
  --ref-system-gray: #e5e7eb;
  --ref-terminal-green: #73ffb9;
}
```

## Typography direction
- **PP Neue Montreal**: 400, 500, 700, 13px, 14px, 16px, 17px, 18px, 22px, 23px, 30px, 40px, 46px, 50px, 54px, 110px, 220px, 1.00, 1.27, 1.38, 1.50, 1.56, 1.62; substitute `Inter`.

## Spacing / shape
- Section Gap: `56px`
- Card Padding: `20px`
- Element Gap: `20px`
- Radius: `links: 8.64px, other: 9999px`

## Component cues
- **Ghost Border Button**: Navigation links and secondary actions
- **Horizontal Divider**: Visual separation of sections or content blocks
- **Feature Card**: Displaying product features or services
- **Inline State Text**: Highlighting status or category within content
- **Pill Accent Tag**: Categorization or short descriptive tags

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
