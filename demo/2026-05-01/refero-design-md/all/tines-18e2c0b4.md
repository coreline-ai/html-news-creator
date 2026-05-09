# Tines - Refero Design MD

- Source: https://styles.refero.design/style/18e2c0b4-f29c-4e84-90b0-1d8066b59409
- Original site: https://www.tines.com
- Theme: `light`
- Industry: `saas`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Playful violet canvas, pastel cards

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Tines Violet | `#4d3e78` | brand | Action accent / signal color |
| Deep Sea Violet | `#6956a8` | brand | Action accent / signal color |
| Lavender Mist | `#7f69ce` | brand | Action accent / signal color |
| Periwinkle Accent | `#a990f5` | accent | Action accent / signal color |
| Light Orchid | `#c2aafa` | accent | Action accent / signal color |
| Powder Violet | `#d7c4fa` | accent | Action accent / signal color |
| Bubblegum Pink | `#a54b7a` | accent | Action accent / signal color |
| Sunset Orange | `#b74d1a` | accent | Action accent / signal color |
| Forest Green | `#1f7a57` | accent | Action accent / signal color |
| Sky Blue | `#3c699b` | accent | Action accent / signal color |

```css
:root {
  --ref-tines-violet: #4d3e78;
  --ref-deep-sea-violet: #6956a8;
  --ref-lavender-mist: #7f69ce;
  --ref-periwinkle-accent: #a990f5;
  --ref-light-orchid: #c2aafa;
  --ref-powder-violet: #d7c4fa;
  --ref-bubblegum-pink: #a54b7a;
  --ref-sunset-orange: #b74d1a;
}
```

## Typography direction
- **Roobert**: 400, 500, 600, 700, 900, 10px, 11px, 12px, 13px, 14px, 16px, 18px, 1.00, 1.15, 1.20, 1.25, 1.40; substitute `system-ui`.
- **Reckless**: 300, 400, 500, 600, 700, 20px, 22px, 24px, 26px, 28px, 46px, 52px, 64px, 72px, 0.90, 0.98, 1.00, 1.05, 1.10, 1.20, 1.40; substitute `serif`.

## Spacing / shape
- Section Gap: `42-64px`
- Card Padding: `24px`
- Element Gap: `12px`
- Page Max Width: `1200px`
- Radius: `tags: 7px, cards: 14px, inputs: 7px, buttons: 14px, largeFeatures: 24px`

## Surface cues
- **Hero Canvas** `#8d75e6`: Primary background for the hero section, establishing the brand's main color.
- **Panel Background** `#fcf9f5`: Subtle off-white background for secondary content panels, offering a slight contrast to pure white.
- **Primary Card** `#f3ecf7`: The default background for informational cards, providing a soft, pastel base.
- **Elevated Violet Card** `#e1d2f9`: One of several pastel backgrounds used for visual distinction in card grids.

## Component cues
- **Primary Filled Button**: Main call-to-action button, solid background.
- **Outline Ghost Button**: Secondary action or navigational link with minimal visual weight.
- **Circular Dot Button**: Small interactive elements or highlights, often containing iconography.
- **Colorful Testimonial Card**: Highlights customer testimonials or key statistics with a distinct background hue.
- **Navigation Link**: Main navigation items and inline links.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
