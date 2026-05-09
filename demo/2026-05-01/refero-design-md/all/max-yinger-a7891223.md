# Max Yinger - Refero Design MD

- Source: https://styles.refero.design/style/a7891223-a93e-4731-a1aa-4079f1ee928b
- Original site: https://yinger.dev
- Theme: `dark`
- Industry: `agency`
- Recommended fit: **Admin console / run monitor / developer tooling**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Terminal aesthetic, crafted in code.

## Apply to
- Admin run monitor and review states
- Compact evidence cards and source inspection panels
- Dark-mode operational dashboards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Basalt Black | `#12130f` | neutral | Primary text or dark surface |
| Quartz White | `#e4dfda` | neutral | Page background or card surface |
| Flint Gray | `#3c3c38` | neutral | Primary text or dark surface |

```css
:root {
  --ref-basalt-black: #12130f;
  --ref-quartz-white: #e4dfda;
  --ref-flint-gray: #3c3c38;
}
```

## Typography direction
- **Inline VF**: 400, 80px, 0.80; substitute `IBM Plex Mono`.
- **Arbeit Contrast**: 400, 16px, 30px, 80px, 1.13, 1.25; substitute `Space Grotesk`.
- **Arbeit Technik**: 400, 12px, 1.25; substitute `JetBrains Mono`.

## Spacing / shape
- Section Gap: `64px`
- Card Padding: `12px`
- Element Gap: `4px`
- Radius: `links: 2px, buttons: 9999px, default: 6px`

## Component cues
- **Social Link Pills**: Reference component style.
- **Local Time & Bio Block**: Reference component style.
- **Stats / Metadata Badge Row**: Reference component style.
- **Pill Ghost Button**: Interactive elements, external links.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
