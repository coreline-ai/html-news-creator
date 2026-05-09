# Handsome Frank - Refero Design MD

- Source: https://styles.refero.design/style/19d4103a-9f4a-49f0-ad7d-af6588bab904
- Original site: https://www.handsomefrank.com
- Theme: `light`
- Industry: `design`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Artistic Jungle Canvas

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Ink | `#160572` | brand | Action accent / signal color |
| Fiery Red | `#ea0706` | brand | Action accent / signal color |
| Warm Ginger | `#e29675` | accent | Action accent / signal color |
| Terracotta Orange | `#d64e2e` | accent | Action accent / signal color |
| Crimson Edge | `#df1a19` | accent | Action accent / signal color |
| Aqua Glow | `#24e3dc` | accent | Action accent / signal color |
| Sunny Marigold | `#f9e44d` | accent | Action accent / signal color |
| Warm Canvas Yellow | `#fffac2` | accent | Action accent / signal color |
| Illustrator Blue | `#2544a0` | accent | Action accent / signal color |
| Pumpkin Swirl | `#ff7701` | accent | Action accent / signal color |

```css
:root {
  --ref-midnight-ink: #160572;
  --ref-fiery-red: #ea0706;
  --ref-warm-ginger: #e29675;
  --ref-terracotta-orange: #d64e2e;
  --ref-crimson-edge: #df1a19;
  --ref-aqua-glow: #24e3dc;
  --ref-sunny-marigold: #f9e44d;
  --ref-warm-canvas-yellow: #fffac2;
}
```

## Typography direction
- **Arial**: 400, 700, 13px, 1.2.
- **Millik**: 400, 700, 20px, 22px, 32px, 38px, 42px, 54px, 70px, 80px, 88px, 0.95, 0.96, 0.98, 1.00, 1.10, 1.36; substitute `Playfair Display`.
- **Klarheit Grotesk**: 400, 600, 700, 12px, 14px, 16px, 22px, 24px, 1.20, 1.28, 1.36; substitute `Inter`.

## Spacing / shape
- Section Gap: `24px`
- Card Padding: `24px`
- Element Gap: `20px`
- Radius: `inputs: 30px, buttons: 30px, bodyElements: 10px, circularElements: 50%`

## Surface cues
- **Pure White Canvas** `#ffffff`: Default page background, providing a clean base for most content.
- **Cream Canvas** `#fef9ee`: Slightly warmer off-white background for secondary sections, offering subtle visual separation.
- **Fog Canvas** `#f2ebe6`: Cool-toned off-white background for content blocks, providing an alternative subtle contrast.
- **Accent Surface** `#ffff00`: Vivid yellow surface used for warning badges or highlight elements.

## Component cues
- **Ghost Button**: Interactive elements that blend into the background, often for discrete actions or navigation.
- **Circular Ghost Button**: Small, discreet interactive elements, often used for icon-only actions.
- **Pill Accent Button**: Prominent calls to action with rounded edges, standing out against darker backgrounds.
- **Illustrator Block Button**: Primary action button for navigating to illustrator portfolios, using specific brand colors.
- **Illustration Card**: Container for showcasing artist work, designed to let the artwork be the focus.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
