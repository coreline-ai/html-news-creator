# Adaline - Refero Design MD

- Source: https://styles.refero.design/style/312423bf-72ea-42fb-b8f5-ab0104e778f3
- Original site: https://www.adaline.ai
- Theme: `light`
- Industry: `ai`
- Recommended fit: **Research brief / AI trend page**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Mist-shrouded valley

## Apply to
- Research section pages and model-release briefs
- Lab-note style cards
- AI product/research trend summaries

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas Ice | `#fbfdf6` | neutral | Page background or card surface |
| Adaline Ink | `#0a1d08` | brand | Action accent / signal color |
| Mist Gray | `#c5ccb6` | neutral | Border, muted text, or supporting surface |
| Deep Earth | `#31200b` | neutral | Primary text or dark surface |
| Valley Green | `#203b14` | brand | Action accent / signal color |
| Stone Moss | `#e0e5d5` | neutral | Page background or card surface |
| Amber Seed | `#4a3212` | accent | Action accent / signal color |
| Forest Dew | `#d7e8b5` | neutral | Page background or card surface |
| Blackest Night | `#000000` | neutral | Primary text or dark surface |

```css
:root {
  --ref-canvas-ice: #fbfdf6;
  --ref-adaline-ink: #0a1d08;
  --ref-mist-gray: #c5ccb6;
  --ref-deep-earth: #31200b;
  --ref-valley-green: #203b14;
  --ref-stone-moss: #e0e5d5;
  --ref-amber-seed: #4a3212;
  --ref-forest-dew: #d7e8b5;
}
```

## Typography direction
- **akkurat**: 400, 700, 12px, 14px, 18px, 47px, 53px, 0.98, 1.00, 1.33, 1.43, 1.44, 1.67.
- **fragmentMono**: 400, 14px, 1.00.

## Spacing / shape
- Section Gap: `48px`
- Card Padding: `24px`
- Element Gap: `4px`
- Radius: `images: 8px, buttons: 20px, navItems: 20px`

## Component cues
- **Primary Action Button (Filled)**: Emphasized calls to action
- **Secondary Action Button (Ghost)**: Secondary calls to action, less emphasis
- **Tertiary Action Button (Ghost Thin)**: Minimal calls to action, often in navigation
- **Navigation Link**: Top-level navigation and contextual links
- **Client Logo Card**: Display partner logos

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
