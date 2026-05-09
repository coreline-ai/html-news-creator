# Fruitful - Refero Design MD

- Source: https://styles.refero.design/style/3634d5eb-ccfa-4881-b234-3dd735fb7ae4
- Original site: https://fruitful.com
- Theme: `light`
- Industry: `fintech`
- Recommended fit: **Design reference / webapp exploration**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Calm Financial Clarity

## Apply to
- General webapp UI exploration
- Demo cards and catalog surfaces
- Future admin/subscriber UI references

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Rich Black | `#000000` | neutral | Primary text or dark surface |
| Subtle Ash | `#eceff4` | neutral | Page background or card surface |
| Cool Gray | `#5b616b` | neutral | Border, muted text, or supporting surface |
| Deep Fern Green | `#0b7443` | brand | Action accent / signal color |
| Leafy Green | `#61bc76` | brand | Action accent / signal color |
| Muted Sage | `#d1fadf` | accent | Action accent / signal color |
| Melon Tint | `#fee9d1` | accent | Action accent / signal color |
| Terra Cotta | `#715039` | accent | Action accent / signal color |
| Sky Mist | `#c7e0f8` | accent | Action accent / signal color |

```css
:root {
  --ref-canvas-white: #ffffff;
  --ref-rich-black: #000000;
  --ref-subtle-ash: #eceff4;
  --ref-cool-gray: #5b616b;
  --ref-deep-fern-green: #0b7443;
  --ref-leafy-green: #61bc76;
  --ref-muted-sage: #d1fadf;
  --ref-melon-tint: #fee9d1;
}
```

## Typography direction
- **PP Neue Montreal**: 400, 500, 600, 700, 11px, 12px, 13px, 14px, 15px, 16px, 18px, 19px, 20px, 21px, 23px, 24px, 26px, 38px, 45px, 48px, 49px, 60px, 91px, 1.2; substitute `Inter, Arial, sans-serif`.

## Spacing / shape
- Section Gap: `48px`
- Card Padding: `48px`
- Element Gap: `8px`
- Radius: `cards: 12px, badges: 80px, images: 12px, inputs: 12px, buttons: 12px, general: 12px`

## Surface cues
- **Canvas White** `#ffffff`: Base page background
- **Mint Green Glow** `#e1fdea`: Lightest section background, subtle differentiation
- **Subtle Ash** `#eceff4`: Card background, softer section backgrounds
- **Melon Tint** `#fee9d1`: Accent background for feature cards

## Component cues
- **Primary Filled Button**: Main call to action button.
- **Ghost Outline Button**: Secondary action or alternative call to action.
- **Muted Neutral Button**: Tertiary action or filter controls.
- **Feature Card (Peach)**: Highlighting key features or interactive elements.
- **Plain Content Card**: Standard content containers, often for text or simple UI groups.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
