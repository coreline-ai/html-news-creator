# Shelby Kay - Refero Design MD

- Source: https://styles.refero.design/style/2ab2f666-6da7-4cd8-bc91-52a28bd560ad
- Original site: https://shelbykay.dev
- Theme: `light`
- Industry: `design`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Earthy editorial grid

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas Parchment | `#efe6d9` | neutral | Page background or card surface |
| Ashwood Grove | `#393c2a` | neutral | Primary text or dark surface |
| Forest Whisper | `#737955` | brand | Action accent / signal color |
| Soft Sienna | `#d6b292` | neutral | Border, muted text, or supporting surface |
| Dusty Rose | `#afa199` | neutral | Border, muted text, or supporting surface |
| Slate Mist | `#7b8785` | neutral | Border, muted text, or supporting surface |
| Dark Bark | `#454931` | neutral | Border, muted text, or supporting surface |
| Deep Mocha | `#2c1c03` | neutral | Primary text or dark surface |

```css
:root {
  --ref-canvas-parchment: #efe6d9;
  --ref-ashwood-grove: #393c2a;
  --ref-forest-whisper: #737955;
  --ref-soft-sienna: #d6b292;
  --ref-dusty-rose: #afa199;
  --ref-slate-mist: #7b8785;
  --ref-dark-bark: #454931;
  --ref-deep-mocha: #2c1c03;
}
```

## Typography direction
- **Ranade**: 400, 700, 24px, 83px, 158px, 265px, 0.90, 1.00, 1.20; substitute `Anton`.
- **Switzer**: 500, 600, 700, 10px, 11px, 14px, 16px, 20px, 1.00, 1.20, 1.25, 1.30; substitute `Inter`.

## Spacing / shape
- Section Gap: `36px`
- Card Padding: `20px`
- Element Gap: `12px`
- Radius: `default: 0px`

## Component cues
- **Navigation Link**: Primary navigation item
- **Hero Title**: Main branding on the landing page
- **Text Block Container**: Grouped text content
- **Work Showcase Card**: Thumbnail for portfolio projects
- **Section Separator Rule**: Visual division between content sections

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
