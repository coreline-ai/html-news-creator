# Drepute - Refero Design MD

- Source: https://styles.refero.design/style/523d3e7b-b0a2-4979-a626-00f1487b6e4d
- Original site: https://drepute.xyz
- Theme: `dark`
- Industry: `other`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Midnight Lake Serenity: a tranquil, dark expanse punctuated by crisp, minimal text and subtle, interactive glints of light.

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Lake | `#161616` | neutral | Primary text or dark surface |
| Night Sky | `#000000` | neutral | Primary text or dark surface |
| Snow Drift | `#ffffff` | neutral | Page background or card surface |
| Ash Gray | `#bfbfbf` | neutral | Border, muted text, or supporting surface |
| Slate Dew | `#a9a9a9` | neutral | Border, muted text, or supporting surface |
| Pebble Stone | `#7f8080` | neutral | Border, muted text, or supporting surface |
| Teal Accent | `#00a4a6` | accent | Action accent / signal color |
| Mountain Mist | `#8995a9` | neutral | Border, muted text, or supporting surface |

```css
:root {
  --ref-midnight-lake: #161616;
  --ref-night-sky: #000000;
  --ref-snow-drift: #ffffff;
  --ref-ash-gray: #bfbfbf;
  --ref-slate-dew: #a9a9a9;
  --ref-pebble-stone: #7f8080;
  --ref-teal-accent: #00a4a6;
  --ref-mountain-mist: #8995a9;
}
```

## Typography direction
- **Source Sans Pro**: 400, 700, 14px, 16px, 1.20, 1.50; substitute `system-ui`.
- **Playfair Display**: 400, 16px, 44px, 62px, 1.20, 1.25; substitute `Times New Roman`.
- **Montserrat**: 700, 26px, 1.20; substitute `Arial`.

## Spacing / shape
- Section Gap: `32px`
- Card Padding: `24px`
- Element Gap: `24px`
- Radius: `inputs: 4px, buttons: 4px`

## Surface cues
- **Midnight Lake Canvas** `#161616`: The foundational dark background for the entire page and large hero sections, providing a deep, contemplative base.
- **Elevated Component Surface** `#000000`: Used for elements that subtly rise from the main canvas, like footers, input containers, or distinct content blocks.
- **Interactive Overlay** `#ffffff`: Applied to interactive backgrounds such as buttons or alerts that need to pop against dark surfaces, serving as a bright, crisp layer.

## Component cues
- **Light Outlined Button**: Secondary action button on dark backgrounds.
- **Solid Text Button (default)**: Primary action button, used primarily against lighter areas or when a strong contrast is needed.
- **Text Input**: Standard input field for user data.
- **Brand Logo**: Primary brand identifier in navigation.
- **Hero Headline**: Large, prominent text for hero sections.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
