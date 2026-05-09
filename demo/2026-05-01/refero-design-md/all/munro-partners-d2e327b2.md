# Munro Partners - Refero Design MD

- Source: https://styles.refero.design/style/d2e327b2-1181-4203-82a6-2dc15a72078a
- Original site: https://www.munropartners.com.au
- Theme: `light`
- Industry: `fintech`
- Recommended fit: **Research brief / AI trend page**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
earthy minimalist canvas

## Apply to
- Research section pages and model-release briefs
- Lab-note style cards
- AI product/research trend summaries

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Peat Ink | `#3f322a` | neutral | Primary text or dark surface |
| Oat Canvas | `#fff9ee` | neutral | Page background or card surface |
| Silver Clay | `#c5bdb3` | neutral | Border, muted text, or supporting surface |
| Winter Marble | `#ffffff` | neutral | Page background or card surface |
| Whisper Gray | `#e5e5e5` | neutral | Page background or card surface |
| Stone Dust | `#b3aea7` | neutral | Border, muted text, or supporting surface |
| Forest Teal | `#004e4e` | brand | Action accent / signal color |
| Amethyst Glow | `#a56eff` | accent | Action accent / signal color |
| Berry Shadow | `#560e4b` | accent | Action accent / signal color |
| Sky Glaze | `#bfebfe` | accent | Action accent / signal color |

```css
:root {
  --ref-peat-ink: #3f322a;
  --ref-oat-canvas: #fff9ee;
  --ref-silver-clay: #c5bdb3;
  --ref-winter-marble: #ffffff;
  --ref-whisper-gray: #e5e5e5;
  --ref-stone-dust: #b3aea7;
  --ref-forest-teal: #004e4e;
  --ref-amethyst-glow: #a56eff;
}
```

## Typography direction
- **neue-haas-grotesk-display**: 400, 600, 700, 12px, 13px, 14px, 16px, 22px, 24px, 30px, 43px, 68px, 0.75, 0.81, 1.00, 1.05, 1.09, 1.10, 1.13, 1.17, 1.20, 1.30, 1.41, 1.43, 1.50; substitute `Inter`.
- **neue-haas-grotesk-text**: 400, 500, 10px, 11px, 12px, 1.00, 1.50, 1.80; substitute `Inter`.
- **Font Awesome 5 Brands**: 400, 18px, 1.

## Spacing / shape
- Section Gap: `40px`
- Card Padding: `0px`
- Element Gap: `20px`
- Radius: `misc: 20px, cards: 0px, badges: 2px, images: 15px, buttons: 2px, default: 2px`

## Surface cues
- **Oat Canvas** `#fff9ee`: Base page background, providing a warm, inviting canvas for all content.
- **Winter Marble** `#ffffff`: Secondary background surfaces, typically for header, navigation, and specific interactive elements, offering a crisp layer above the main canvas.

## Component cues
- **Ghost Outline Button**: Secondary action button, 'See more' prompts
- **Primary Action Button**: Main call-to-action button
- **Accent Button (Amethyst)**: Specific action button, highlighted features
- **White Nav Button**: Navigation, 'Skip to content' calls to action.
- **Information Input Field**: User input fields.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
