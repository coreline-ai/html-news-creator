# Tana - Refero Design MD

- Source: https://styles.refero.design/style/f7bf0618-817c-4b7d-9568-cbd9c476c599
- Original site: https://tana.inc
- Theme: `dark`
- Industry: `productivity`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
infinite dark canvas

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Deep Midnight | `#000000` | neutral | Primary text or dark surface |
| Cloud Whisper | `#f0eded` | neutral | Page background or card surface |
| Graphite Base | `#0e0e0e` | neutral | Primary text or dark surface |
| Muted Silver | `#b3b3b3` | neutral | Border, muted text, or supporting surface |
| Stone Gray | `#808080` | neutral | Border, muted text, or supporting surface |
| Soft Ash | `#606060` | neutral | Border, muted text, or supporting surface |
| Lush Meadow | `#e1f0bd` | accent | Action accent / signal color |

```css
:root {
  --ref-deep-midnight: #000000;
  --ref-cloud-whisper: #f0eded;
  --ref-graphite-base: #0e0e0e;
  --ref-muted-silver: #b3b3b3;
  --ref-stone-gray: #808080;
  --ref-soft-ash: #606060;
  --ref-lush-meadow: #e1f0bd;
}
```

## Typography direction
- **SF Pro**: 300, 400, 13px, 15px, 16px, 17px, 18px, 19px, 20px, 21px, 24px, 26px, 29px, 1.20, 1.40, 1.50, 1.75; substitute `system-ui`.
- **tanaClassic**: 350, 400, 17px, 19px, 38px, 42px, 48px, 84px, 1.10, 1.20, 1.25, 1.75; substitute `serif`.
- **Arial**: 400, 17px, 1.20; substitute `system-ui`.

## Spacing / shape
- Section Gap: `24px`
- Card Padding: `16px`
- Element Gap: `6px`
- Radius: `tags: 8px, image: 10px, buttons: 12px`

## Surface cues
- **Deep Midnight Canvas** `#000000`: Dominant page and module background.
- **Graphite Base Layer** `#0e0e0`: Secondary background for containers or subtle section variations, borders.

## Component cues
- **Primary Action Button**: Call to action
- **Ghost Outline Button (small)**: Secondary action or tag
- **Ghost Text Link (minimal)**: Inline or tertiary action link
- **Navigation Link**: Main navigation item
- **Hero Headline**: Prominent page title

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
