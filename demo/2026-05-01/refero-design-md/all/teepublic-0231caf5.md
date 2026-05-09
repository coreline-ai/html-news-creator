# TeePublic - Refero Design MD

- Source: https://styles.refero.design/style/0231caf5-0347-4f2d-ba20-5bab8fcaf2ce
- Original site: https://unfurproject.com
- Theme: `light`
- Industry: `ecommerce`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Vibrant Pop Canvas: Bold and graphic against bright white.

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Ink | `#151523` | neutral | Primary text or dark surface |
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Ghost Gray | `#e9e9ec` | neutral | Page background or card surface |
| Border Silver | `#d7d7db` | neutral | Border, muted text, or supporting surface |
| Cloud Whisper | `#f1f3fe` | neutral | Page background or card surface |
| Royal Indigo | `#4e64df` | brand | Action accent / signal color |
| Crimson Strike | `#ff0000` | accent | Action accent / signal color |
| Lavender Mist | `#99a7f5` | accent | Action accent / signal color |
| Electric Violet | `#6c7ee4` | brand | Action accent / signal color |
| Faded Steel | `#49495a` | neutral | Border, muted text, or supporting surface |

```css
:root {
  --ref-midnight-ink: #151523;
  --ref-canvas-white: #ffffff;
  --ref-ghost-gray: #e9e9ec;
  --ref-border-silver: #d7d7db;
  --ref-cloud-whisper: #f1f3fe;
  --ref-royal-indigo: #4e64df;
  --ref-crimson-strike: #ff0000;
  --ref-lavender-mist: #99a7f5;
}
```

## Typography direction
- **Arial**: 400, 13px, 1.2.
- **Roobert**: 400, 500, 600, 700, 11px, 12px, 13px, 14px, 16px, 18px, 20px, 24px, 40px, 1.00, 1.15, 1.17, 1.20, 1.25, 1.33, 1.43, 1.45, 1.50, 1.56, 1.67, 2.75; substitute `Inter`.
- **Roobert**: use as primary family; substitute `Inter`.

## Spacing / shape
- Section Gap: `24px`
- Card Padding: `12px`
- Element Gap: `8px`
- Page Max Width: `1440px`
- Radius: `cards: 12px, pills: 100px, inputs: 12px, buttons: 12px, largeCards: 20px`

## Surface cues
- **Canvas White** `#ffffff`: Base page background
- **Ghost Gray** `#e9e9ec`: Secondary card backgrounds, subtle dividers
- **Cloud Whisper** `#f1f3fe`: Elevated card backgrounds, grouped content areas

## Component cues
- **Ghost Button**: Secondary actions or navigation links that need less emphasis. They appear as text with a transparent background.
- **Neutral Outlined Button**: Tertiary actions or category filters, providing interaction without competing with primary calls to action.
- **Primary Filled Button**: Main calls to action.
- **Crimson Call To Action Button**: High-urgency primary actions, distinct from the brand's standard primary color.
- **Elevated Feature Card**: Highlighting key features or content, using elevation to draw attention.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
