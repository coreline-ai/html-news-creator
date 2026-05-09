# Dropmark - Refero Design MD

- Source: https://styles.refero.design/style/5618f26a-4df6-42cb-8081-15e4318b54ff
- Original site: https://dropmark.com
- Theme: `light`
- Industry: `productivity`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Architectural blueprint on white marble; precise organization within a serene, bright expanse.

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Whisper Gray | `#f7f7f1` | neutral | Page background or card surface |
| Border Fog | `#dcdcd4` | neutral | Page background or card surface |
| Text Graphite | `#404040` | neutral | Border, muted text, or supporting surface |
| Muted Black | `#111111` | neutral | Primary text or dark surface |
| Icon Gray | `#7f7f7f` | neutral | Border, muted text, or supporting surface |
| Action Blue | `#00affa` | brand | Action accent / signal color |
| Deep Violet | `#1e2554` | brand | Action accent / signal color |
| Accent Lilac | `#2c2a6c` | accent | Action accent / signal color |
| Vivid Orange | `#ff5d43` | accent | Action accent / signal color |

```css
:root {
  --ref-canvas-white: #ffffff;
  --ref-whisper-gray: #f7f7f1;
  --ref-border-fog: #dcdcd4;
  --ref-text-graphite: #404040;
  --ref-muted-black: #111111;
  --ref-icon-gray: #7f7f7f;
  --ref-action-blue: #00affa;
  --ref-deep-violet: #1e2554;
}
```

## Typography direction
- **DropmarkRealText**: 400, 600, 700, 13px, 14px, 15px, 16px, 17px, 20px, 24px, 40px, 1.20, 1.50; substitute `Inter`.
- **DropmarkRealHead**: 500, 24px, 40px, 60px, 1.20; substitute `Open Sans`.

## Spacing / shape
- Section Gap: `60px`
- Card Padding: `30px`
- Element Gap: `10px`
- Page Max Width: `1200px`
- Radius: `cards: 3px, avatars: 60px, buttons: 3px, default: 3px`

## Component cues
- **Primary Outlined Button**: Call to action button for key interactive elements.
- **Filled Navigation Button**: High-contrast action in the header, always visible.
- **Header Navigation Link**: Standard navigation item for primary site sections.
- **Feature Card**: Display individual features or content blocks.
- **Avatar/Circular Element**: User profile images or circular decorative components.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
