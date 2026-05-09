# Joby Aviation - Refero Design MD

- Source: https://styles.refero.design/style/c1052d8d-3663-46a4-a882-e50d9b8a1166
- Original site: https://www.jobyaviation.com
- Theme: `light`
- Industry: `other`
- Recommended fit: **Research brief / AI trend page**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Skyward Glide

## Apply to
- Research section pages and model-release briefs
- Lab-note style cards
- AI product/research trend summaries

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Ink | `#0e1620` | neutral | Primary text or dark surface |
| Cloud Whisper | `#f5f4df` | neutral | Page background or card surface |
| Skybound Blue | `#007ae5` | brand | Action accent / signal color |
| Cosmic Violet | `#1c3f99` | brand | Action accent / signal color |
| Sunset Orange | `#eb6110` | accent | Action accent / signal color |
| Horizon Blue | `#083e6f` | accent | Action accent / signal color |
| Pale Peach | `#ffd9c9` | accent | Action accent / signal color |
| Shadow Grey | `#abab9c` | neutral | Border, muted text, or supporting surface |

```css
:root {
  --ref-midnight-ink: #0e1620;
  --ref-cloud-whisper: #f5f4df;
  --ref-skybound-blue: #007ae5;
  --ref-cosmic-violet: #1c3f99;
  --ref-sunset-orange: #eb6110;
  --ref-horizon-blue: #083e6f;
  --ref-pale-peach: #ffd9c9;
  --ref-shadow-grey: #abab9c;
}
```

## Typography direction
- **JobyDisplay**: 500, 550, 10px, 18px, 24px, 28px, 40px, 48px, 64px, 80px, 141px, 207px, 1.00, 1.05, 1.20; substitute `Inter`.
- **jobyText**: 400, 450, 500, 550, 12px, 14px, 16px, 18px, 0.89, 1.00, 1.20, 1.30, 1.40; substitute `Inter`.
- **Arial**: 400, 13px, 1.20; substitute `Arial`.

## Spacing / shape
- Section Gap: `113px`
- Card Padding: `40px`
- Element Gap: `8px`
- Radius: `cards: 16px, default: 8px, otherLarge: 147.6px, asymmetricCards: 160px 160px 0px 0px`

## Component cues
- **Ghost Navigation Button (Light Text)**: Interactive element for navigation or secondary actions, appearing on dark backgrounds.
- **Ghost Navigation Button (Dark Text)**: Interactive element for navigation or secondary actions, appearing on light backgrounds.
- **Feature Card (Blue BG)**: Container for showcasing features or information, using the primary brand blue.
- **Hero Section Card**: Prominent card used in hero sections, often with asymmetric rounded corners.
- **Ghost Input**: Input field for user entry, designed for dark backgrounds.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
