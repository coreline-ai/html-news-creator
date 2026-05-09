# T1 Energy - Refero Design MD

- Source: https://styles.refero.design/style/e79b761d-f476-4c5d-8943-e31a58664e4d
- Original site: https://t1energy.com
- Theme: `light`
- Industry: `other`
- Recommended fit: **Design reference / webapp exploration**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Industrial Blueprint on White Marble

## Apply to
- General webapp UI exploration
- Demo cards and catalog surfaces
- Future admin/subscriber UI references

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Nightfall Onyx | `#0f0e12` | neutral | Primary text or dark surface |
| Platinum White | `#ffffff` | neutral | Page background or card surface |
| Technical Carbon | `#322d2a` | neutral | Primary text or dark surface |
| Cloud Chalk | `#f0efe9` | neutral | Page background or card surface |
| Steel Gray | `#8b8b8b` | neutral | Border, muted text, or supporting surface |

```css
:root {
  --ref-nightfall-onyx: #0f0e12;
  --ref-platinum-white: #ffffff;
  --ref-technical-carbon: #322d2a;
  --ref-cloud-chalk: #f0efe9;
  --ref-steel-gray: #8b8b8b;
}
```

## Typography direction
- **T1 Sans**: 300, 400, 14px, 52px, 1.00, 1.30; substitute `Inter`.

## Spacing / shape
- Section Gap: `48px`
- Card Padding: `22px`
- Element Gap: `8px`
- Radius: `cards: 80px, buttons: 16px, elements: 12px, smallInteractive: 100px`

## Component cues
- **Ghost Header Button**: Primary navigation and action button within the hero overlay.
- **Pill Ghost Button**: Compact action button, often for secondary navigation or small interactive elements.
- **Transparent Card**: Displaying informational content without a distinct visual border or background, creating a light, airy feel.
- **Rounded Informational Card**: Content container with a distinctly large rounded corner, providing a softer boundary.
- **Learn More Button**: Secondary action button for deeper content exploration.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
