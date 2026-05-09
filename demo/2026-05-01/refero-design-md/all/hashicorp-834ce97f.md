# HashiCorp - Refero Design MD

- Source: https://styles.refero.design/style/834ce97f-61f2-4b12-bf5c-e9fad2544456
- Original site: https://hashicorp.com
- Theme: `dark`
- Industry: `devtools`
- Recommended fit: **Admin console / run monitor / developer tooling**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Deep Space Command Center. A dark, expansive digital environment where critical data is precisely displayed and interactive elements glow with focused purpose.

## Apply to
- Admin run monitor and review states
- Compact evidence cards and source inspection panels
- Dark-mode operational dashboards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Core | `#0d0e12` | neutral | Primary text or dark surface |
| Carbon Gray | `#000000` | neutral | Primary text or dark surface |
| Silver Text | `#efeff1` | neutral | Page background or card surface |
| Ash Accent | `#b2b6bd` | neutral | Border, muted text, or supporting surface |
| Slate Text | `#d5d7db` | neutral | Border, muted text, or supporting surface |
| Stone Gray | `#656a76` | neutral | Border, muted text, or supporting surface |
| Ghost Button | `#3b3d45` | neutral | Primary text or dark surface |
| Bright White | `#ffffff` | neutral | Page background or card surface |
| Interactive Blue | `#2b89ff` | brand | Action accent / signal color |
| Link Blue | `#2264d6` | brand | Action accent / signal color |

```css
:root {
  --ref-midnight-core: #0d0e12;
  --ref-carbon-gray: #000000;
  --ref-silver-text: #efeff1;
  --ref-ash-accent: #b2b6bd;
  --ref-slate-text: #d5d7db;
  --ref-stone-gray: #656a76;
  --ref-ghost-button: #3b3d45;
  --ref-bright-white: #ffffff;
}
```

## Typography direction
- **system-ui**: 400, 500, 600, 13px, 14px, 15px, 16px, 17px, 1.14, 1.20, 1.35, 1.38, 1.50, 1.60, 1.63, 1.69, 1.71; substitute `Inter`.
- **Hashicorp Sans**: 600, 700, 13px, 17px, 19px, 26px, 34px, 42px, 52px, 82px, 1.17, 1.18, 1.19, 1.21, 1.35, 1.69; substitute `Inter`.
- **Arial**: 400, 16px, 1.20; substitute `Helvetica Neue`.

## Spacing / shape
- Section Gap: `64px`
- Card Padding: `20px`
- Element Gap: `12px`
- Radius: `input: 5px, badges: 5px, buttons: 5px, default: 4px`

## Surface cues
- **Base Surface** `#0D0E12`: Primary page background and foundational dark surface.
- **Elevated Component Surface** `#000000`: Used for some button backgrounds and areas requiring slightly more depth against the base.

## Component cues
- **Announcement Banner**: Reference component style.
- **Button Group**: Reference component style.
- **Resources Card List**: Reference component style.
- **Primary Button**: cta
- **Secondary Button**: secondary cta

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
