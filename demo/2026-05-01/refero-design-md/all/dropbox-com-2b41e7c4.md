# Dropbox.com - Refero Design MD

- Source: https://styles.refero.design/style/2b41e7c4-1e8c-4ea2-a87f-51e24c57886e
- Original site: https://dropbox.com
- Theme: `light`
- Industry: `saas`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Pristine Digital Workspace. A highly organized, clean desktop environment where every element has its place and purpose.

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Graphite Black | `#000000` | neutral | Primary text or dark surface |
| Cloud White | `#ffffff` | neutral | Page background or card surface |
| Off-White Canvas | `#f7f5f2` | neutral | Page background or card surface |
| Deep Graphite | `#1e1919` | neutral | Primary text or dark surface |
| Royal Blue | `#0061fe` | brand | Action accent / signal color |
| Muted Grey | `#716b61` | neutral | Border, muted text, or supporting surface |
| Almond Dust | `#eee9e2` | neutral | Page background or card surface |
| Blush Pink | `#cd2f7b` | accent | Action accent / signal color |
| Ash Border | `#c6c4c3` | neutral | Border, muted text, or supporting surface |
| Dark Overlay Gradient | `#292c31` | neutral | Primary text or dark surface |

```css
:root {
  --ref-graphite-black: #000000;
  --ref-cloud-white: #ffffff;
  --ref-off-white-canvas: #f7f5f2;
  --ref-deep-graphite: #1e1919;
  --ref-royal-blue: #0061fe;
  --ref-muted-grey: #716b61;
  --ref-almond-dust: #eee9e2;
  --ref-blush-pink: #cd2f7b;
}
```

## Typography direction
- **Sharp Grotesk**: 500, 18px, 26px, 40px, 1.20, 1.30; substitute `Montserrat`.
- **Sharp Grotesk 23**: 400, 32px, 1.20; substitute `Montserrat`.
- **Atlas Grotesk Web**: 400, 500, 700, 12px, 14px, 16px, 20px, 1.20, 1.43, 1.50, 1.57; substitute `Inter`.

## Spacing / shape
- Section Gap: `48px`
- Card Padding: `12px`
- Element Gap: `12px`
- Page Max Width: `1150px`
- Radius: `large: 20px, links: 16px, buttons: 16px, default: 8px, navigation: 12px`

## Surface cues
- **Cloud White** `#ffffff`: Default page background, base canvas
- **Off-White Canvas** `#f7f5f2`: Secondary background, subtle content areas, large sections
- **Almond Dust** `#eee9e2`: Elevated card surfaces, distinct content blocks

## Component cues
- **Primary CTA Button**: Calls to action, 'Get started' type buttons
- **Navigation Link Button**: Top navigation items, secondary actions
- **Dark Navigation Link Button**: Navigation items for dark mode or contrasting sections
- **Informational Card**: Feature blocks, content organization
- **Lightweight Text Link Card**: Content container for simple text lists or outlines

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
