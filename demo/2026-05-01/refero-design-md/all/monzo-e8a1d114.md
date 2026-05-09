# Monzo - Refero Design MD

- Source: https://styles.refero.design/style/e8a1d114-6924-4f03-acd2-996dd30f15a6
- Original site: https://monzo.com
- Theme: `light`
- Industry: `fintech`
- Recommended fit: **Research brief / AI trend page**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Hot Coral Digital Craftsmanship — a meticulously crafted digital experience with vibrant accents.

## Apply to
- Research section pages and model-release briefs
- Lab-note style cards
- AI product/research trend summaries

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Charcoal | `#091723` | neutral | Primary text or dark surface |
| Snow White | `#ffffff` | neutral | Page background or card surface |
| Mist Gray | `#f2f8f3` | neutral | Page background or card surface |
| Slate Blue | `#112231` | neutral | Action accent / signal color |
| Silver Dust | `#e3ebe4` | neutral | Page background or card surface |
| Steel Gray | `#6b747b` | neutral | Border, muted text, or supporting surface |
| Ash Gray | `#b5b9bd` | neutral | Border, muted text, or supporting surface |
| Hot Coral | `#ff4f40` | brand | Action accent / signal color |
| Muted Olive | `#3b4c54` | neutral | Border, muted text, or supporting surface |

```css
:root {
  --ref-midnight-charcoal: #091723;
  --ref-snow-white: #ffffff;
  --ref-mist-gray: #f2f8f3;
  --ref-slate-blue: #112231;
  --ref-silver-dust: #e3ebe4;
  --ref-steel-gray: #6b747b;
  --ref-ash-gray: #b5b9bd;
  --ref-hot-coral: #ff4f40;
}
```

## Typography direction
- **MonzoSansText**: 400, 600, 700, 13px, 16px, 20px, 24px, 32px, 36px, 0.81, 1.15, 1.38, 1.40, 1.50; substitute `Inter, Arial`.
- **MonzoSansDisplay**: 600, 700, 800, 16px, 20px, 25px, 31px, 39px, 44px, 49px, 61px, 1.00, 1.20, 1.40; substitute `Inter, Arial`.

## Spacing / shape
- Section Gap: `64px`
- Card Padding: `30px`
- Element Gap: `24px`
- Page Max Width: `1200px`
- Radius: `cards: 32px, badges: 4px, buttons: 500px, general: 64px`

## Surface cues
- **Mist Gray** `#f2f8f3`: Page background, foundational canvas
- **Snow White** `#ffffff`: Primary content areas, default cards
- **Slate Blue** `#112231`: Elevated cards or specific dark sections

## Component cues
- **Primary Filled Button**: Call to action
- **Primary Outlined Button**: Secondary action or ghost button
- **Ghost Button with Icon**: Navigation or interactive element with subtle styling
- **Light Mode Card**: Information container, features
- **Dark Mode Card**: Information container, features

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
