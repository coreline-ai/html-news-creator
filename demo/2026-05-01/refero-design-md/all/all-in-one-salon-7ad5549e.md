# All-In-One Salon - Refero Design MD

- Source: https://styles.refero.design/style/7ad5549e-9baa-4fda-ac43-79d568a86b98
- Original site: https://glossgenius.com
- Theme: `light`
- Industry: `saas`
- Recommended fit: **Source ledger / evidence dashboard**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Crisp digital ledger, with neon highlights guiding the way.

## Apply to
- Source ledger, ranking, and verification screens
- Cluster evidence dashboards
- Dense data tables with clear hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Cloud White | `#ffffff` | neutral | Page background or card surface |
| Porcelain Gray | `#f0f7f6` | neutral | Page background or card surface |
| Obsidian Black | `#000000` | neutral | Primary text or dark surface |
| Silver Mist | `#e2e2e2` | neutral | Page background or card surface |
| Genius Yellow | `#cccc25` | brand | Action accent / signal color |
| Genius Yellow Gradient | `#cccc25` | brand | Action accent / signal color |
| Sky Violet | `#9fa6ff` | accent | Action accent / signal color |
| Sky Violet Gradient | `#9fa6ff` | accent | Action accent / signal color |

```css
:root {
  --ref-cloud-white: #ffffff;
  --ref-porcelain-gray: #f0f7f6;
  --ref-obsidian-black: #000000;
  --ref-silver-mist: #e2e2e2;
  --ref-genius-yellow: #cccc25;
  --ref-genius-yellow-gradient: #cccc25;
  --ref-sky-violet: #9fa6ff;
  --ref-sky-violet-gradient: #9fa6ff;
}
```

## Typography direction
- **Basel Grotesk Book**: 400, 500, 600, 13px, 14px, 16px, 18px, 22px, 32px, 40px, 48px, 72px, 0.97, 1.02, 1.05, 1.10, 1.13, 1.20, 1.40; substitute `Inter`.
- **Basel Classic Book**: 400, 96px, 144px, 0.80, 0.90; substitute `Playfair Display`.

## Spacing / shape
- Section Gap: `72-96px`
- Card Padding: `20px`
- Element Gap: `8px`
- Radius: `nav: 40px, cards: 8px, badges: 8px, buttons: 1440px, interactiveElements: 1440px`

## Component cues
- **Hero CTA Button Group**: Reference component style.
- **Feature Card — Boost Online Traffic**: Reference component style.
- **FAQ Accordion**: Reference component style.
- **Primary Call to Action Button**: Interactive element
- **Secondary Ghost Button**: Interactive element

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
