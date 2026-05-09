# Turso - Refero Design MD

- Source: https://styles.refero.design/style/5a7ec81f-03b6-4d21-a706-0d1d323d8899
- Original site: https://turso.tech
- Theme: `dark`
- Industry: `devtools`
- Recommended fit: **Admin console / run monitor / developer tooling**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Electric Teal Command Center. A dark, digital workspace where a single vibrant hue highlights critical actions amid a field of deep shadows.

## Apply to
- Admin run monitor and review states
- Compact evidence cards and source inspection panels
- Dark-mode operational dashboards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Deep Space | `#0d1318` | neutral | Primary text or dark surface |
| Hacker Teal | `#4ff7d1` | accent | Action accent / signal color |
| Void Black | `#000000` | neutral | Primary text or dark surface |
| Cloud Gray | `#ffffff` | neutral | Page background or card surface |
| Slate Border | `#283945` | neutral | Primary text or dark surface |
| Charcoal Surface | `#162129` | neutral | Primary text or dark surface |
| Whisper Gray | `#86898c` | neutral | Border, muted text, or supporting surface |
| Subtle Gray | `#b6b8ba` | neutral | Border, muted text, or supporting surface |
| Electric Violet | `#d946ef` | accent | Action accent / signal color |
| Neon Pink | `#a21caf` | accent | Action accent / signal color |

```css
:root {
  --ref-deep-space: #0d1318;
  --ref-hacker-teal: #4ff7d1;
  --ref-void-black: #000000;
  --ref-cloud-gray: #ffffff;
  --ref-slate-border: #283945;
  --ref-charcoal-surface: #162129;
  --ref-whisper-gray: #86898c;
  --ref-subtle-gray: #b6b8ba;
}
```

## Typography direction
- **Inter**: 400, 12px, 14px, 16px, 18px, 1.50, 1.56, 1.60, 1.63, 1.75, 1.78, 2.00; substitute `system-ui`.
- **Inter**: 500, 12px, 14px, 16px, 18px, 1.50, 1.56, 1.60, 1.63; substitute `system-ui`.
- **Inter**: 600, 16px, 20px, 24px, 30px, 36px, 48px, 1.00, 1.11, 1.20, 1.33, 1.43, 1.50; substitute `system-ui`.

## Spacing / shape
- Section Gap: `40px`
- Radius: `cards: 12px, buttons: 9999px, general: 12px, navItems: 9999px`

## Component cues
- **Button Group — Primary, Secondary & Badge**: Reference component style.
- **Product Cards — Turso & Turso Cloud**: Reference component style.
- **Announcement Banner + Hero Badge**: Reference component style.
- **Primary Call-to-Action Button**: Main interactive button
- **Secondary Ghost Button**: Alternative or less prominent action

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
