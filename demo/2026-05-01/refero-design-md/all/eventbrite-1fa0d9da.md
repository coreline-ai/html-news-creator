# Eventbrite - Refero Design MD

- Source: https://styles.refero.design/style/1fa0d9da-966f-4d43-9775-e156bec3a3b3
- Original site: https://www.eventbrite.com
- Theme: `light`
- Industry: `media`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Event listing, vibrant and clear

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Porcelain Mist | `#f8f7fa` | neutral | Page background or card surface |
| Lavender Ash | `#dbdae3` | neutral | Page background or card surface |
| Ghost Gray | `#eeedf2` | neutral | Page background or card surface |
| Inkwell Purple | `#39364f` | neutral | Primary text or dark surface |
| Shadow Graphite | `#585163` | neutral | Border, muted text, or supporting surface |
| Slate Steel | `#6f7287` | neutral | Border, muted text, or supporting surface |
| Oceanic Blue | `#3659e3` | brand | Action accent / signal color |
| Deep Plum | `#1e0a3c` | neutral | Primary text or dark surface |
| Terra Cotta | `#f05537` | brand | Action accent / signal color |

```css
:root {
  --ref-canvas-white: #ffffff;
  --ref-porcelain-mist: #f8f7fa;
  --ref-lavender-ash: #dbdae3;
  --ref-ghost-gray: #eeedf2;
  --ref-inkwell-purple: #39364f;
  --ref-shadow-graphite: #585163;
  --ref-slate-steel: #6f7287;
  --ref-oceanic-blue: #3659e3;
}
```

## Typography direction
- **Neue Plak**: 400, 600, 700, 12px, 14px, 16px, 18px, 24px, 32px, 0.75, 1.00, 1.20, 1.25, 1.33, 1.43, 1.57, 1.71, 1.83, 2.00.
- **Neue Plak Text**: 600, 14px, 1.20, 1.43.

## Spacing / shape
- Section Gap: `77px`
- Card Padding: `12px`
- Element Gap: `12px`
- Radius: `cards: 16px, badges: 20px, inputs: 4px, buttons: 360px, heroCard: 40px 40px 0px 0px, navCategory: 100px`

## Component cues
- **Ghost Button**: Outline style button for secondary actions or navigation.
- **Pill Button**: Small, contained button for filters or tags.
- **Category Navigation Link**: Navigational link within category menus, often below a main image.
- **Standard Card**: Container for event listings and general content blocks.
- **Hero Card**: Prominent card used in hero sections, often with an integrated image.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
