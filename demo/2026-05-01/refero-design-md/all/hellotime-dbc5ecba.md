# Hellotime - Refero Design MD

- Source: https://styles.refero.design/style/dbc5ecba-7309-456f-93b4-4356c6b0d293
- Original site: https://www.hellotime.io
- Theme: `light`
- Industry: `productivity`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
White canvas, graphite precision

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Fog Gray | `#f3f3f5` | neutral | Page background or card surface |
| Border Ash | `#e1e2e5` | neutral | Page background or card surface |
| Graphite Ink | `#151619` | neutral | Primary text or dark surface |
| Steel Gray | `#7f8491` | neutral | Border, muted text, or supporting surface |
| Slate Blue | `#c8cad0` | neutral | Action accent / signal color |
| Charcoal Button | `#25272d` | neutral | Primary text or dark surface |
| Accent Green | `#059669` | accent | Action accent / signal color |
| Link Gray | `#363940` | neutral | Primary text or dark surface |
| Button Border | `#b0b3bb` | neutral | Border, muted text, or supporting surface |

```css
:root {
  --ref-canvas-white: #ffffff;
  --ref-fog-gray: #f3f3f5;
  --ref-border-ash: #e1e2e5;
  --ref-graphite-ink: #151619;
  --ref-steel-gray: #7f8491;
  --ref-slate-blue: #c8cad0;
  --ref-charcoal-button: #25272d;
  --ref-accent-green: #059669;
}
```

## Typography direction
- **SF Pro Display**: 500, 600, 700, 24px, 40px, 48px, 64px, 80px, 0.90, 1.00, 1.33, 1.50; substitute `Inter`.
- **SF Pro Text**: 400, 500, 600, 700, 14px, 16px, 18px, 20px, 0.80, 1.00, 1.14, 1.20, 1.33, 1.50, 1.60; substitute `Inter`.

## Spacing / shape
- Section Gap: `40px`
- Card Padding: `32px`
- Element Gap: `16px`
- Radius: `body: 12px, cards: 16px, links: 12px, buttons: 8px, headings: 20px, navigation: 8px`

## Surface cues
- **Canvas White** `#ffffff`: Base page background, light frames for main content areas.
- **Fog Gray** `#f3f3f5`: Secondary background for cards, feature blocks, and distinct content sections.
- **Border Ash** `#e1e2e5`: Very subtle background for hovered states or very light bordering elements; visually above Fog Gray but rarely a full surface.

## Component cues
- **Primary Filled Button**: Call-to-action button for initiating key user flows.
- **Ghost Button**: Secondary action or navigational link with minimal visual weight.
- **Outlined Button**: Tertiary action with a clear boundary but less prominence than a filled button.
- **Content Card**: Container for grouped information, feedback, or features.
- **Timeline Card**: Specific card variant for product UI, demonstrating a feature.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
