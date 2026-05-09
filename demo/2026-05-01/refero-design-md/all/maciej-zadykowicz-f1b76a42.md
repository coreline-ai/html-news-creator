# Maciej Zadykowicz - Refero Design MD

- Source: https://styles.refero.design/style/f1b76a42-050e-4c9e-96e3-a77fbd718c68
- Original site: https://maciej.co
- Theme: `dark`
- Industry: `agency`
- Recommended fit: **Admin console / run monitor / developer tooling**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Nocturnal Data Canvas — a dark, subdued interface punctuated by bursts of algorithmic color.

## Apply to
- Admin run monitor and review states
- Compact evidence cards and source inspection panels
- Dark-mode operational dashboards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Base | `#0c0c0c` | neutral | Primary text or dark surface |
| Charcoal Surface | `#25262d` | neutral | Primary text or dark surface |
| Slate Accent | `#383a42` | neutral | Primary text or dark surface |
| Ghost Text | `#f2f2f3` | neutral | Page background or card surface |
| Cool Gray Text | `#858893` | neutral | Border, muted text, or supporting surface |
| Subtle Gray Text | `#54565f` | neutral | Border, muted text, or supporting surface |
| Indigo Button | `#384270` | brand | Action accent / signal color |

```css
:root {
  --ref-midnight-base: #0c0c0c;
  --ref-charcoal-surface: #25262d;
  --ref-slate-accent: #383a42;
  --ref-ghost-text: #f2f2f3;
  --ref-cool-gray-text: #858893;
  --ref-subtle-gray-text: #54565f;
  --ref-indigo-button: #384270;
}
```

## Typography direction
- **Replica-Regular**: 400, 20px, 36px, 1.00, 1.20; substitute `Space Mono`.
- **Replica-Mono**: 400, 20px, 1.20; substitute `Space Mono`.
- **Arial**: 400, 13px, 1.20; substitute `Arial`.

## Spacing / shape
- Section Gap: `90px`
- Card Padding: `12px`
- Element Gap: `4px`
- Radius: `buttons: 24px, default: 16px, largeButtons: 64px`

## Component cues
- **CTA Button Group**: Reference component style.
- **Project Card — Metadrop**: Reference component style.
- **About Bio Block**: Reference component style.
- **Primary Button**: Interactive element
- **Pill Button**: Interactive element

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
