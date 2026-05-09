# Ecosia - Refero Design MD

- Source: https://styles.refero.design/style/198d4f13-0e88-4372-86fd-7abf34a668b1
- Original site: https://www.ecosia.org
- Theme: `light`
- Industry: `other`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Forest Canopy Blueprint — crisp text and vivid green for a nature-inspired search engine.

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Forest Fern | `#d7eb80` | brand | Action accent / signal color |
| Midnight Ash | `#333333` | neutral | Primary text or dark surface |
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Fog Gray | `#f0f0eb` | neutral | Page background or card surface |
| Muted Shadow | `#6c6c6c` | neutral | Border, muted text, or supporting surface |
| Soft Mist | `#f8f8f6` | neutral | Page background or card surface |
| Silver Whisper | `#bebeb9` | neutral | Border, muted text, or supporting surface |
| Stone Glaze | `#b6b6b6` | neutral | Border, muted text, or supporting surface |
| Deep Shadow | `#cccccc` | neutral | Border, muted text, or supporting surface |

```css
:root {
  --ref-forest-fern: #d7eb80;
  --ref-midnight-ash: #333333;
  --ref-canvas-white: #ffffff;
  --ref-fog-gray: #f0f0eb;
  --ref-muted-shadow: #6c6c6c;
  --ref-soft-mist: #f8f8f6;
  --ref-silver-whisper: #bebeb9;
  --ref-stone-glaze: #b6b6b6;
}
```

## Typography direction
- **Founders Grotesk**: 400, 600, 700, 16px, 24px, 36px, 48px, 54px, 1.10, 1.30, 1.40; substitute `Montserrat`.
- **Inter**: 400, 500, 600, 700, 12px, 14px, 16px, 18px, 20px, 36px, 1.15, 1.40; substitute `system-ui`.

## Spacing / shape
- Section Gap: `40px`
- Card Padding: `16px`
- Element Gap: `16px`
- Page Max Width: `1200px`
- Radius: `cards: 10-20px, links: 4px, other: 40px, buttons: 9999px`

## Component cues
- **Pill Button - Primary**: Call to action for key conversions.
- **Pill Button - Ghost**: Secondary actions or internal links where visual weight should be minimal.
- **Search Input Field**: Primary interaction for content discovery.
- **Primary Feature Card**: Highlighting key initiatives or features.
- **Data Stat Card**: Showcasing numerical impact.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
