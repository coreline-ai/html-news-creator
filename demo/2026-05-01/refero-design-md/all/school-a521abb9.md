# School - Refero Design MD

- Source: https://styles.refero.design/style/a521abb9-d84b-4870-b5a8-363be7c3f94a
- Original site: https://schoooool.com
- Theme: `light`
- Industry: `other`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Digital scrapbook on a gray desktop.

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Ink | `#303030` | neutral | Primary text or dark surface |
| Paper White | `#ffffff` | neutral | Page background or card surface |
| Desktop Gray | `#f2f2f2` | neutral | Page background or card surface |
| Card Surface | `#dbdbdb` | neutral | Page background or card surface |
| Input Fill | `#ededed` | neutral | Page background or card surface |
| Border Grey | `#808080` | neutral | Border, muted text, or supporting surface |
| Badge Base | `#c2c2c2` | neutral | Border, muted text, or supporting surface |
| Attention Yellow | `#f9f5a2` | brand | Action accent / signal color |
| Sky Blue | `#648fe0` | brand | Action accent / signal color |
| Blush Sand | `#e2ceb8` | brand | Action accent / signal color |

```css
:root {
  --ref-ink: #303030;
  --ref-paper-white: #ffffff;
  --ref-desktop-gray: #f2f2f2;
  --ref-card-surface: #dbdbdb;
  --ref-input-fill: #ededed;
  --ref-border-grey: #808080;
  --ref-badge-base: #c2c2c2;
  --ref-attention-yellow: #f9f5a2;
}
```

## Typography direction
- **IBM Plex Mono**: 400, 11px, 14px, 16px, 18px, 25px, 43px, 1.40; substitute `monospace`.
- **Helvetica**: 300, 400, 700, 11px, 18px, 44px, 1.40; substitute `sans-serif`.

## Spacing / shape
- Section Gap: `24px`
- Card Padding: `12px`
- Element Gap: `8px`
- Radius: `cards: 10px, images: 10px, inputs: 25px, buttons: 20px`

## Component cues
- **Featured Project Card**: Reference component style.
- **Your Button — Clock Widget**: Reference component style.
- **Hero Headline with Highlight + Contact Badges**: Reference component style.
- **Primary Card**: Container for distinct content blocks.
- **Badge (Secondary)**: Categorization and meta-information.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
