# Portal - Refero Design MD

- Source: https://styles.refero.design/style/b9aeb945-2f6e-4557-9115-e3ff3a8f8dc8
- Original site: https://useportal.net
- Theme: `light`
- Industry: `productivity`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Frosted glass on a gradient dawn

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Sky Canvas | `#f7f7f7` | neutral | Page background or card surface |
| White Frost | `#ffffff` | neutral | Page background or card surface |
| Ink | `#000000` | neutral | Primary text or dark surface |
| Charcoal Text | `#3e3e3e` | neutral | Primary text or dark surface |
| Muted Ash | `#636363` | neutral | Border, muted text, or supporting surface |
| Portal Blue | `#007aff` | brand | Action accent / signal color |
| Blue Aura | `#8cc2ff` | accent | Action accent / signal color |

```css
:root {
  --ref-sky-canvas: #f7f7f7;
  --ref-white-frost: #ffffff;
  --ref-ink: #000000;
  --ref-charcoal-text: #3e3e3e;
  --ref-muted-ash: #636363;
  --ref-portal-blue: #007aff;
  --ref-blue-aura: #8cc2ff;
}
```

## Typography direction
- **sans-serif**: 400, 12px, 1.2.
- **Perfectly Nineties Regular**: 400, 36px, 48px, 1.00; substitute `system-ui`.
- **Inter**: 400, 500, 600, 10px, 12px, 14px, 16px, 18px, 1.20, 1.30, 1.35; substitute `system-ui`.

## Spacing / shape
- Section Gap: `40px`
- Card Padding: `16px`
- Element Gap: `10px`
- Radius: `navs: 22px, cards: 16px, icons: 22px, other: 22px, images: 22px, buttons: 50px`

## Surface cues
- **Sky Canvas** `#f7f7f7`: Base page background. Provides a soft, clean foundation for content.
- **White Frost** `#ffffff`: Primary card and elevated component background. Often appears with translucency (rgba(255,255,255,0.6)) and features backdrop blurring for a frosted…

## Component cues
- **Primary Ghost Button**: Call to action button with high contrast text and a 'ghost' background.
- **Primary Action Button**: Filled call to action button, emphasizing interactions.
- **Default Card**: Standard content container for features or information blocks.
- **Frosted Card**: Enhanced content container with a translucent, semi-frosted appearance.
- **Elevated Bubble Card**: Prominent, rounded card with a soft shadow for hierarchy.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
