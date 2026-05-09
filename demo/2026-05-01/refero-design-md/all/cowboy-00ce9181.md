# Cowboy - Refero Design MD

- Source: https://styles.refero.design/style/00ce9181-45be-4340-b6a6-75a4d5d60cef
- Original site: https://cowboy.com
- Theme: `light`
- Industry: `ecommerce`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Minimalist Product Canvas

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Ink Black | `#1d1d1d` | neutral | Primary text or dark surface |
| Whisper Gray | `#e5e7eb` | neutral | Page background or card surface |
| Dim Gray | `#737373` | neutral | Border, muted text, or supporting surface |
| Ash Cloud | `#f3f4f6` | neutral | Page background or card surface |
| Stone Gray | `#a3a3a3` | neutral | Border, muted text, or supporting surface |
| Slate Border | `#6b7280` | neutral | Border, muted text, or supporting surface |
| Forest Whisper | `#569d5f` | accent | Action accent / signal color |
| Action Blue | `#2563eb` | semantic | Action accent / signal color |

```css
:root {
  --ref-canvas-white: #ffffff;
  --ref-ink-black: #1d1d1d;
  --ref-whisper-gray: #e5e7eb;
  --ref-dim-gray: #737373;
  --ref-ash-cloud: #f3f4f6;
  --ref-stone-gray: #a3a3a3;
  --ref-slate-border: #6b7280;
  --ref-forest-whisper: #569d5f;
}
```

## Typography direction
- **SuisseIntl**: 400, 500, 600, 12px, 13px, 14px, 16px, 18px, 20px, 24px, 36px, 42px, 44px, 46px, 52px, 72px, 100px, 0.90, 0.95, 1.00, 1.05, 1.25, 1.33, 1.47, 1.50; substitute `system-ui, sans-serif`.
- **ui-monospace**: 400, 64px, 1.00; substitute `monospace`.
- **intercom-font**: 400, 16px, 1.50; substitute `system-ui, sans-serif`.

## Spacing / shape
- Section Gap: `60px`
- Card Padding: `48px`
- Element Gap: `8px`
- Radius: `tags: 9999px, cards: 8px, buttons: 9999px, default: 8px`

## Surface cues
- **Page Canvas** `#e5e7eb`: The base background for many sections, providing a subtle off-white foundation.
- **Primary Surface** `#ffffff`: Standard background for cards, modals, and elements intended to appear on top of the Page Canvas.
- **Accent Surface** `#f3f4f6`: Alternative background for cards or sections, creating differentiation and depth without strong contrast.

## Component cues
- **Primary Filled Button**: Main call-to-action button, conveying primary interaction.
- **Secondary Outlined Button**: Secondary calls-to-action, less prominent but still interactive.
- **Ghost Header Button**: Navigation and utility actions within headers, minimal visual weight.
- **Feature Card**: Displaying product features or key information blocks.
- **Alternating Section Card**: Providing visual distinction between content blocks, often for related features.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
