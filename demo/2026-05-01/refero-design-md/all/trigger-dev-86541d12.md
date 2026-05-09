# Trigger.dev - Refero Design MD

- Source: https://styles.refero.design/style/86541d12-7870-4d51-8c47-0880fdb1ea01
- Original site: https://trigger.dev
- Theme: `dark`
- Industry: `devtools`
- Recommended fit: **Admin console / run monitor / developer tooling**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Midnight Terminal, illuminated by command prompts and spectral highlights.

## Apply to
- Admin run monitor and review states
- Compact evidence cards and source inspection panels
- Dark-mode operational dashboards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Obsidian Black | `#121317` | neutral | Primary text or dark surface |
| Charcoal Surface | `#1c1e21` | neutral | Primary text or dark surface |
| Ash Gray | `#3b3e45` | neutral | Primary text or dark surface |
| Slate Text | `#d7d9dd` | neutral | Page background or card surface |
| Whisper White | `#e5e7eb` | neutral | Page background or card surface |
| Steel Accent | `#b5b8c0` | neutral | Border, muted text, or supporting surface |
| Spring Green | `#a8ff53` | brand | Action accent / signal color |
| Cloud Violet | `#9c9af2` | accent | Action accent / signal color |
| Deep Plum | `#7655fd` | accent | Action accent / signal color |
| Fuchsia Highlight | `#fa3abf` | accent | Action accent / signal color |

```css
:root {
  --ref-obsidian-black: #121317;
  --ref-charcoal-surface: #1c1e21;
  --ref-ash-gray: #3b3e45;
  --ref-slate-text: #d7d9dd;
  --ref-whisper-white: #e5e7eb;
  --ref-steel-accent: #b5b8c0;
  --ref-spring-green: #a8ff53;
  --ref-cloud-violet: #9c9af2;
}
```

## Typography direction
- **Geist-Regular**: 300, 400, 500, 14px, 16px, 18px, 20px, 1.40, 1.43, 1.50, 1.56, 1.71; substitute `Inter`.
- **GeistMono-Regular**: 300, 400, 14px, 1.43; substitute `JetBrains Mono`.
- **Satoshi-Variable**: 500, 600, 16px, 18px, 20px, 24px, 30px, 36px, 48px, 60px, 1.00, 1.11, 1.20, 1.33, 1.38, 1.40, 1.50, 1.56; substitute `Outfit`.

## Spacing / shape
- Section Gap: `40px`
- Card Padding: `28px`
- Element Gap: `8px`
- Radius: `tags: 9999px, buttons: 4px, default: 4px`

## Component cues
- **CTA Button Group**: Reference component style.
- **Feature Tag Pills**: Reference component style.
- **Testimonial Card**: Reference component style.
- **Primary Action Button**: Main call to action
- **Ghost Navigation Button**: Secondary navigation and non-primary actions

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
