# VALIENTE BRANDS - Refero Design MD

- Source: https://styles.refero.design/style/f63bf016-5b53-4ddf-9f8c-da43f75a9e2b
- Original site: https://valientebrands.com
- Theme: `light`
- Industry: `agency`
- Recommended fit: **Admin console / run monitor / developer tooling**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Raw Crimson Statement. The page feels like a manifesto etched in bold red on stark white.

## Apply to
- Admin run monitor and review states
- Compact evidence cards and source inspection panels
- Dark-mode operational dashboards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Valiente Crimson | `#ff1a00` | brand | Action accent / signal color |
| Concrete White | `#f5f5f5` | neutral | Page background or card surface |
| Charcoal Black | `#0a0a0a` | neutral | Primary text or dark surface |
| Ash Gray | `#eaeaea` | neutral | Page background or card surface |
| Pale Rose | `#e7a196` | neutral | Border, muted text, or supporting surface |

```css
:root {
  --ref-valiente-crimson: #ff1a00;
  --ref-concrete-white: #f5f5f5;
  --ref-charcoal-black: #0a0a0a;
  --ref-ash-gray: #eaeaea;
  --ref-pale-rose: #e7a196;
}
```

## Typography direction
- **GT Pressura**: 400, 12px, 14px, 16px, 18px, 20px, 24px, 48px, 95px, 128px, 190px, 245px, 0.80, 0.82, 1.00, 1.20; substitute `Inter`.
- **Monument Grotesk**: 400, 48px, 1.00; substitute `Archivo`.

## Spacing / shape
- Section Gap: `64px`
- Card Padding: `0px`
- Element Gap: `20px`
- Page Max Width: `1440px`
- Radius: `none: 0px`

## Component cues
- **Hero Tagline Bar**: Reference component style.
- **Video Play Button Block**: Reference component style.
- **Services Navigation Menu**: Reference component style.
- **Navigation Link**: Interactive text link in the header and footer navigation.
- **Hero Headline**: Main heading for the hero section.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
