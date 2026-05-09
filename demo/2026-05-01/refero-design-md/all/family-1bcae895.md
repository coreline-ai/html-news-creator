# Family - Refero Design MD

- Source: https://styles.refero.design/style/1bcae895-2245-4d33-aa43-1c1e80719554
- Original site: https://family.co
- Theme: `light`
- Industry: `crypto`
- Recommended fit: **Source ledger / evidence dashboard**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Pixar storyboard on cream paper — playful illustrated characters inhabit a warm off-white world where fintech feels like an adventure game.

## Apply to
- Source ledger, ranking, and verification screens
- Cluster evidence dashboards
- Dense data tables with clear hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Warm Canvas | `#fbfaf9` | neutral | Page background or card surface |
| Stone Surface | `#f2f0ed` | neutral | Page background or card surface |
| Parchment Card | `#f8f7f4` | neutral | Page background or card surface |
| Graphite | `#474645` | neutral | Border, muted text, or supporting surface |
| Charcoal Primary | `#343433` | neutral | Primary text or dark surface |
| Midnight | `#121212` | neutral | Primary text or dark surface |
| Obsidian | `#000000` | neutral | Primary text or dark surface |
| Ash | `#848281` | neutral | Border, muted text, or supporting surface |
| Fog | `#c6c6c6` | neutral | Border, muted text, or supporting surface |
| Smoke | `#a7a7a7` | neutral | Border, muted text, or supporting surface |

```css
:root {
  --ref-warm-canvas: #fbfaf9;
  --ref-stone-surface: #f2f0ed;
  --ref-parchment-card: #f8f7f4;
  --ref-graphite: #474645;
  --ref-charcoal-primary: #343433;
  --ref-midnight: #121212;
  --ref-obsidian: #000000;
  --ref-ash: #848281;
}
```

## Typography direction
- **Family**: 500, 44px, 68px, 1.09–1.10; substitute `Fraunces or Playfair Display at weight 500`.
- **Inter**: 400, 500, 600, 12px, 13px, 14px, 15px, 16px, 17px, 19px, 23px, 44px, 1.00–1.58; substitute `System UI stack or IBM Plex Sans`.

## Spacing / shape
- Section Gap: `120-180px`
- Card Padding: `32px`
- Element Gap: `8-12px`
- Page Max Width: `1200px`
- Radius: `tags: 6px, cards: 10px, icons: 40px, inputs: 10px, buttons: 32px, cardsLarge: 24px, buttonsPill: 32px, illustrations: 72px`

## Surface cues
- **Canvas** `#fbfaf9`: Page background — warm off-white with a faint cream cast, not pure white
- **Card Surface** `#ffffff`: White card faces with a warm inset stone border — floats 1px above canvas visually
- **Recessed Panel** `#f8f7f4`: Screenshot and demo container backgrounds — slightly warmer than white, sits below card level
- **Stone Tint** `#f2f0ed`: Button backgrounds (secondary), inset border reference color, hover states on cream
- **Dark Shell** `#000000`: Phone mockup cards — full inversion for product showcase moments

## Component cues
- **Primary CTA Button (Pill Dark)**: Main conversion action — 'Get Started', 'Download on iOS'
- **Secondary CTA Button (Pill Light)**: Alternative actions — 'Log In', 'Watch the Video'
- **Ghost Text Link Button**: Inline navigation links — 'Watch the demo', section CTAs
- **Outlined Navigation Button**: Tertiary actions in nav or contextual contexts
- **Feature Card (White)**: Primary content cards — feature descriptions, testimonials

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
