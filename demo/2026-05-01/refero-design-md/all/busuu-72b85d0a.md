# Busuu - Refero Design MD

- Source: https://styles.refero.design/style/72b85d0a-1ff8-4dd3-b33a-f55aad6df5c9
- Original site: https://busuu.com
- Theme: `light`
- Industry: `other`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Vibrant learning portal on a clean canvas. A spacious, friendly digital environment where interactive elements pop against a minimal backdrop.

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Ocean Blue | `#116eee` | brand | Action accent / signal color |
| Spring Green | `#11ee92` | brand | Action accent / signal color |
| Sky Tint | `#87b6f6` | brand | Action accent / signal color |
| Light Bluewash | `#b8d4fa` | brand | Action accent / signal color |
| Electric Cyan | `#06d2ff` | accent | Action accent / signal color |
| Action Red | `#fa3746` | accent | Action accent / signal color |
| Mellow Yellow | `#ffcf00` | accent | Action accent / signal color |
| Pure White | `#ffffff` | neutral | Page background or card surface |
| Cloud Gray | `#f2f7fd` | neutral | Page background or card surface |
| Border Fog | `#d6dee6` | neutral | Page background or card surface |

```css
:root {
  --ref-ocean-blue: #116eee;
  --ref-spring-green: #11ee92;
  --ref-sky-tint: #87b6f6;
  --ref-light-bluewash: #b8d4fa;
  --ref-electric-cyan: #06d2ff;
  --ref-action-red: #fa3746;
  --ref-mellow-yellow: #ffcf00;
  --ref-pure-white: #ffffff;
}
```

## Typography direction
- **Nista**: 400, 700, 800, 10px, 12px, 14px, 16px, 18px, 24px, 36px, 40px, 1.14, 1.20, 1.30, 1.33, 1.50, 1.70; substitute `system-ui, sans-serif`.

## Spacing / shape
- Section Gap: `40-60px`
- Card Padding: `20px`
- Element Gap: `8-20px`
- Radius: `inputs: 5px, buttons: 45.04px, navItems: 16px`

## Component cues
- **Primary CTA Button Group**: Reference component style.
- **Language Selector Carousel**: Reference component style.
- **Display Language Selector Form**: Reference component style.
- **Primary Call to Action Button**: Interactive element
- **Hero Section Headline**: Information display

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
