# TinyFaces NFT - Refero Design MD

- Source: https://styles.refero.design/style/2112d018-bf95-4a87-a1f3-6e948330b207
- Original site: https://nft.tinyfac.es
- Theme: `light`
- Industry: `crypto`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Whimsical collectibles on pastel canvas

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Ink | `#212529` | neutral | Primary text or dark surface |
| Cloud Canvas | `#f4f4f2` | neutral | Page background or card surface |
| Silver Mist | `#d4d5d4` | neutral | Border, muted text, or supporting surface |
| White Smoke | `#ffffff` | neutral | Page background or card surface |
| Coral Charm | `#ed4a29` | brand | Action accent / signal color |
| Deep Ocean | `#142855` | brand | Action accent / signal color |
| Sage Whisper | `#8d9876` | accent | Action accent / signal color |
| Sky Patch | `#a0b1cd` | accent | Action accent / signal color |
| Rose Bloom | `#e5cce0` | accent | Action accent / signal color |
| Sandstone Highlight | `#f4ddbe` | accent | Action accent / signal color |

```css
:root {
  --ref-midnight-ink: #212529;
  --ref-cloud-canvas: #f4f4f2;
  --ref-silver-mist: #d4d5d4;
  --ref-white-smoke: #ffffff;
  --ref-coral-charm: #ed4a29;
  --ref-deep-ocean: #142855;
  --ref-sage-whisper: #8d9876;
  --ref-sky-patch: #a0b1cd;
}
```

## Typography direction
- **Inter**: 300, 400, 500, 14px, 16px, 20px, 24px, 1.50, 2.25, 2.88; substitute `system-ui, sans-serif`.
- **Migra**: 500, 50px, 64px, 187px, 1.00, 1.10, 1.30; substitute `serif`.
- **Arial**: 400, 13px, 1.20; substitute `system-ui, sans-serif`.

## Spacing / shape
- Section Gap: `64px`
- Card Padding: `20px`
- Element Gap: `8px`
- Radius: `small: 2px, buttons: 23px, default: 10px`

## Surface cues
- **Cloud Canvas** `#f4f4f2`: Base page background, light sections
- **Muted Pastel Cards** `#a0b1cd`: Content containers (cards) that sit on the base background, providing visual grouping with soft, customizable hues.
- **Deep Ocean** `#142855`: Elevated background for prominent sections like the hero, creating depth and contrast.

## Component cues
- **Navigation Link**: Header and footer links
- **Filled Primary Button**: Main call-to-action
- **Ghost Primary Button**: Secondary call-to-action
- **Text Button**: Tertiary actions, links within sentences or phrases
- **Muted Pastel Card (Sky Patch)**: Content container for features or thematic sections

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
