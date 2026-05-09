# Prevalent - Refero Design MD

- Source: https://styles.refero.design/style/b1e0a894-7440-44b8-9737-0ea4c988fc24
- Original site: https://prevalent.ai
- Theme: `light`
- Industry: `ai`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Indigo & Violet Precision

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Indigo | `#060b25` | brand | Action accent / signal color |
| Action Violet | `#6360d8` | brand | Action accent / signal color |
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Text Black | `#000000` | neutral | Primary text or dark surface |
| Shadow Gray | `#383c51` | neutral | Primary text or dark surface |
| Light Highlight | `#dad9ed` | neutral | Page background or card surface |
| Muted Swiper Accent | `#007aff` | accent | Action accent / signal color |

```css
:root {
  --ref-midnight-indigo: #060b25;
  --ref-action-violet: #6360d8;
  --ref-canvas-white: #ffffff;
  --ref-text-black: #000000;
  --ref-shadow-gray: #383c51;
  --ref-light-highlight: #dad9ed;
  --ref-muted-swiper-accent: #007aff;
}
```

## Typography direction
- **Tiempos Headline**: 400, 16px, 30px, 45px, 48px, 50px, 80px, 0.98, 1.00, 1.10, 1.55; substitute `Playfair Display`.
- **Matter**: 400, 500, 12px, 14px, 16px, 18px, 20px, 50px, 1.00, 1.22, 1.33, 1.40, 1.43, 1.55, 1.60; substitute `Inter`.

## Spacing / shape
- Section Gap: `48px`
- Card Padding: `48px`
- Element Gap: `24px`
- Page Max Width: `1200px`
- Radius: `hero: 60px, cards: 10px, links: 4px, footer: 20px, buttons: 4px`

## Surface cues
- **Canvas White** `#ffffff`: Primary background for most page content.
- **Midnight Indigo** `#060b25`: Darker background for prominent sections like hero and footer, providing stark contrast.
- **Hero Transparent Overlay** `#ffffff1f`: Cards or containers within the hero, offering a subtle frosted appearance.

## Component cues
- **Primary Call to Action Button**: Key interactive elements for driving user action.
- **Header Navigation Link**: Top-level navigation items.
- **Feature Card**: Content presentation for features or articles.
- **Hero Section Card**: Transparent card elements within the hero section.
- **Inline Text Link**: Text-based navigation or references within body content.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
