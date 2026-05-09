# Evermade - Refero Design MD

- Source: https://styles.refero.design/style/b22f68eb-7ed1-47b6-995e-2c0afc79ac7e
- Original site: https://evermade.fi
- Theme: `light`
- Industry: `agency`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Burgundy Canvas, Vivid Pink Accents

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| White Canvas | `#ffffff` | neutral | Page background or card surface |
| Rich Burgundy | `#2d070b` | brand | Action accent / signal color |
| Vivid Pink | `#ff0389` | accent | Action accent / signal color |
| Blush Sand | `#fef0e6` | neutral | Page background or card surface |
| Pale Rose | `#ffdce2` | neutral | Page background or card surface |
| Ash Black | `#000000` | neutral | Primary text or dark surface |
| Hint of Rose | `#ffc7de` | accent | Action accent / signal color |

```css
:root {
  --ref-white-canvas: #ffffff;
  --ref-rich-burgundy: #2d070b;
  --ref-vivid-pink: #ff0389;
  --ref-blush-sand: #fef0e6;
  --ref-pale-rose: #ffdce2;
  --ref-ash-black: #000000;
  --ref-hint-of-rose: #ffc7de;
}
```

## Typography direction
- **Instrument Serif**: 400, 32px, 48px, 128px, 1.10, 1.40; substitute `Playfair Display`.
- **Manrope**: 400, 12px, 14px, 18px, 22px, 1.10, 1.20, 1.40; substitute `Inter`.
- **DM Mono**: 300, 400, 500, 11px, 14px, 16px, 32px, 1.25, 1.40, 1.60; substitute `IBM Plex Mono`.

## Spacing / shape
- Section Gap: `178px`
- Card Padding: `12px`
- Element Gap: `4px`
- Radius: `pill: 9999px, soft: 8px, default: 0px`

## Surface cues
- **White Canvas** `#ffffff`: Base page background
- **Blush Sand** `#fef0e6`: Secondary background for content sections and cards
- **Pale Rose** `#ffdce2`: Tertiary background for nested cards or subtle differentiation
- **Rich Burgundy** `#2d070b`: Primary background for dark, impactful sections and footers

## Component cues
- **Outlined Button Primary**: Primary Call to Action
- **Outlined Button Secondary**: Secondary Call to Action, larger variant
- **Pill Tag**: Categorization and filter tags
- **Content Card Default**: Standalone content block
- **Content Card with Soft Corners**: Elevated content block for articles/insights

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
