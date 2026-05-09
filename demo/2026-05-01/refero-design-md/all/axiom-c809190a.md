# Axiom - Refero Design MD

- Source: https://styles.refero.design/style/c809190a-035c-458d-87ed-4758807dd84e
- Original site: https://axiom.co
- Theme: `dark`
- Industry: `devtools`
- Recommended fit: **Source ledger / evidence dashboard**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Dark Matter Console — a vast, organized digital workspace with critical data highlighted by a vibrant, focused glow.

## Apply to
- Source ledger, ranking, and verification screens
- Cluster evidence dashboards
- Dense data tables with clear hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Ink | `#000000` | neutral | Primary text or dark surface |
| Deep Graphite | `#111111` | neutral | Primary text or dark surface |
| Charcoal Surface | `#191919` | neutral | Primary text or dark surface |
| Dark Slate | `#202020` | neutral | Primary text or dark surface |
| Medium Gray | `#3a3a3a` | neutral | Primary text or dark surface |
| Stone Accent | `#606060` | neutral | Border, muted text, or supporting surface |
| Light Steel | `#b4b4b4` | neutral | Border, muted text, or supporting surface |
| Almost White | `#eeeeee` | neutral | Page background or card surface |
| Highlight Orange | `#da5c2c` | brand | Action accent / signal color |

```css
:root {
  --ref-midnight-ink: #000000;
  --ref-deep-graphite: #111111;
  --ref-charcoal-surface: #191919;
  --ref-dark-slate: #202020;
  --ref-medium-gray: #3a3a3a;
  --ref-stone-accent: #606060;
  --ref-light-steel: #b4b4b4;
  --ref-almost-white: #eeeeee;
}
```

## Typography direction
- **BerkeleyMono**: 400, 700, 12px, 13px, 14px, 16px, 18px, 20px, 24px, 32px, 1.00, 1.25, 1.33, 1.40, 1.43, 1.50, 1.56, 1.57, 1.71; substitute `IBM Plex Mono`.
- **Inter**: 400, 12px, 14px, 16px, 1.33, 1.43, 1.50; substitute `Inter`.

## Spacing / shape
- Section Gap: `40px`
- Card Padding: `32px`
- Element Gap: `8px`
- Radius: `pill: 9999px, default: 2px`

## Surface cues
- **Base Black** `#000000`: Primary page background, deepest layer.
- **Header & Footer** `#111111`: Main navigation and global footers, slightly lifted from the base.
- **Card & Component** `#191919`: Contained sections like feature cards, toolbars, and input fields, providing distinct content separation.

## Component cues
- **Hero CTA Button Group**: Reference component style.
- **Announcement Banner**: Reference component style.
- **Testimonial Cards**: Reference component style.
- **Primary Call-to-Action Button**: Interactive element
- **Outlined Button**: Interactive element

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
