# Fly.io - Refero Design MD

- Source: https://styles.refero.design/style/0c77bb2a-c7cd-499b-b5cd-90268eefe906
- Original site: https://fly.io
- Theme: `light`
- Industry: `devtools`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Whimsical tech playground. Muted violet meets playful pastels on a clean white backdrop.

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Cloud White | `#ffffff` | neutral | Page background or card surface |
| Ghost Gray | `#e7e6f4` | neutral | Page background or card surface |
| Lavender Mist | `#f1f2f9` | neutral | Page background or card surface |
| Ash Charcoal | `#000000` | neutral | Primary text or dark surface |
| Grape Vine | `#281950` | brand | Action accent / signal color |
| Lavender Bloom | `#a39ac1` | brand | Action accent / signal color |
| Muted Violet | `#5e537c` | brand | Action accent / signal color |
| Electric Violet | `#7c3aed` | accent | Action accent / signal color |
| Deep Plum | `#191034` | brand | Action accent / signal color |
| Success Green | `#10b981` | semantic | Action accent / signal color |

```css
:root {
  --ref-cloud-white: #ffffff;
  --ref-ghost-gray: #e7e6f4;
  --ref-lavender-mist: #f1f2f9;
  --ref-ash-charcoal: #000000;
  --ref-grape-vine: #281950;
  --ref-lavender-bloom: #a39ac1;
  --ref-muted-violet: #5e537c;
  --ref-electric-violet: #7c3aed;
}
```

## Typography direction
- **Mackinac**: 500, 22px, 36px, 64px, 1.15, 1.33; substitute `Georgia, serif`.
- **Fricolage Grotesque**: 325, 450, 500, 575, 12px, 15px, 16px, 17px, 18px, 19px, 1.50, 1.66; substitute `Inter, Arial, sans-serif`.

## Spacing / shape
- Section Gap: `40px`
- Card Padding: `24px`
- Element Gap: `16px`
- Page Max Width: `1200px`
- Radius: `subtle: 4px, buttons: 9999px, navItems: 10px, defaultComponent: 16px`

## Component cues
- **Deploy CTA Button Group**: Reference component style.
- **Enterprise-Ready Feature Card**: Reference component style.
- **Trusted By Banner**: Reference component style.
- **Primary CTA Button**: Call to action
- **Outline Ghost Button**: Secondary action

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
