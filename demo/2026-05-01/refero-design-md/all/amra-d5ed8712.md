# amra - Refero Design MD

- Source: https://styles.refero.design/style/d5ed8712-0e42-4c6c-83b1-b3d7f27d1d10
- Original site: https://www.amra.com
- Theme: `light`
- Industry: `media`
- Recommended fit: **Design reference / webapp exploration**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Frosted glass clarity

## Apply to
- General webapp UI exploration
- Demo cards and catalog surfaces
- Future admin/subscriber UI references

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Ink | `#141414` | neutral | Primary text or dark surface |
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Subtle Gray | `#a1a1a1` | neutral | Border, muted text, or supporting surface |
| Platinum Mist | `#d0d0d0` | neutral | Border, muted text, or supporting surface |
| Ash Cloud | `#8a8a8a` | neutral | Border, muted text, or supporting surface |
| Future Violet | `#acafff` | brand | Action accent / signal color |

```css
:root {
  --ref-midnight-ink: #141414;
  --ref-canvas-white: #ffffff;
  --ref-subtle-gray: #a1a1a1;
  --ref-platinum-mist: #d0d0d0;
  --ref-ash-cloud: #8a8a8a;
  --ref-future-violet: #acafff;
}
```

## Typography direction
- **Primary Font**: 400, 20px, 30px, 50px, 1, 1.2.
- **Inter**: use as primary family; substitute `Inter`.
- **Inter**: use as primary family; substitute `Inter`.

## Spacing / shape
- Section Gap: `100px`
- Card Padding: `32px`
- Element Gap: `24px`
- Radius: `cards: 44px, forms: 8px, links: 24px, buttons: 8px, general: 16px`

## Surface cues
- **Canvas White** `#ffffff`: Primary page background
- **Card Backwash** `#f3f4f5`: Translucent background for cards, creating a frosted effect with 'rgba(243, 244, 245, 0.4)'

## Component cues
- **Primary Navigation Button**: Call to action button in the navigation bar.
- **Navigation Link**: Standard navigation items.
- **Ghost Button**: Secondary call to action, offering a less dominant interaction.
- **Feature Card with Backwash**: Container for showcasing key features or content blocks.
- **Video Player Icon**: Interactive element to trigger video content.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
