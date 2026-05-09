# Home page | Impossible Foods - Refero Design MD

- Source: https://styles.refero.design/style/04961c7d-8ca6-4e87-ba88-6ad7ffa3b245
- Original site: https://impossiblefoods.com
- Theme: `dark`
- Industry: `other`
- Recommended fit: **Admin console / run monitor / developer tooling**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Saturated Night Butcher

## Apply to
- Admin run monitor and review states
- Compact evidence cards and source inspection panels
- Dark-mode operational dashboards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Butcher Shop Crimson | `#4f0423` | brand | Action accent / signal color |
| Deep Berry | `#260212` | brand | Action accent / signal color |
| Impossible Red | `#e10600` | brand | Action accent / signal color |
| Pale Flesh | `#ffc7c6` | accent | Action accent / signal color |
| Rich Mahogany | `#8f6174` | brand | Action accent / signal color |
| Midnight Ink | `#000000` | neutral | Primary text or dark surface |
| Ghost White | `#ffffff` | neutral | Page background or card surface |

```css
:root {
  --ref-butcher-shop-crimson: #4f0423;
  --ref-deep-berry: #260212;
  --ref-impossible-red: #e10600;
  --ref-pale-flesh: #ffc7c6;
  --ref-rich-mahogany: #8f6174;
  --ref-midnight-ink: #000000;
  --ref-ghost-white: #ffffff;
}
```

## Typography direction
- **sans-meat**: 400, 500, 700, 10px, 12px, 14px, 18px, 20px, 22px, 24px, 28px, 32px, 40px, 48px, 103px, 126px, 149px, 150px, 153px, 160px, 161px, 185px, 189px, 204px, 226px, 228px, 231px, 0.73, 0.75, 0.90, 1.10, 1.15, 1.40, 1.70; substitute `Bebas Neue`.

## Spacing / shape
- Section Gap: `40px`
- Card Padding: `32px`
- Element Gap: `6px`
- Radius: `misc: 5px, cards: 37.8889px, buttons: 15px, navItems: 15px`

## Surface cues
- **Butcher Shop Crimson Canvas** `#4f0423`: Primary page background and large section fills, establishing the dark, immersive brand environment.
- **Deep Berry Card Surface** `#260212`: Background for product cards and footers, providing minimal elevation and a slightly different tone from the canvas.
- **Ghost White Interaction Surface** `#ffffff`: Background for specific input fields or detailed content cards, offering a high-contrast reading experience.

## Component cues
- **Hero Section Headline**: Dominant page title
- **Navigation Link**: Primary site navigation
- **Outlined Call to Action Button**: Secondary action or informational button
- **Filled Action Button**: Primary call to action button
- **Product Category Badge**: Filters and content categorization

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
