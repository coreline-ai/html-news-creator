# Qatalog - Refero Design MD

- Source: https://styles.refero.design/style/7eed2626-ab11-472c-b04a-603476ff8957
- Original site: https://qatalog.com
- Theme: `light`
- Industry: `ai`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Crisp Monochrome Control Panel

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Graphite Black | `#000000` | neutral | Primary text or dark surface |
| Ink Black | `#202020` | neutral | Primary text or dark surface |
| Slate Gray | `#292d34` | neutral | Primary text or dark surface |
| Subtle Gray | `#646464` | neutral | Border, muted text, or supporting surface |
| Ash Gray | `#838383` | neutral | Border, muted text, or supporting surface |
| Whisper White | `#f0f0f0` | neutral | Page background or card surface |
| Cloud Gray | `#e8e8e8` | neutral | Page background or card surface |
| Deep Violet | `#514b81` | brand | Action accent / signal color |
| Electric Violet | `#7b68ee` | accent | Action accent / signal color |

```css
:root {
  --ref-canvas-white: #ffffff;
  --ref-graphite-black: #000000;
  --ref-ink-black: #202020;
  --ref-slate-gray: #292d34;
  --ref-subtle-gray: #646464;
  --ref-ash-gray: #838383;
  --ref-whisper-white: #f0f0f0;
  --ref-cloud-gray: #e8e8e8;
}
```

## Typography direction
- **Plus Jakarta Sans**: 400, 650, 700, 16px, 34px, 40px, 48px, 60px, 1.10, 1.15, 1.20, 1.50; substitute `system-ui`.
- **Inter**: 400, 500, 600, 650, 8px, 12px, 14px, 16px, 18px, 1.00, 1.14, 1.33, 1.38, 1.43, 1.50; substitute `sans-serif`.
- **Sometype Mono**: 500, 14px, 16px, 1.25, 1.29; substitute `monospace`.

## Spacing / shape
- Section Gap: `133px`
- Card Padding: `10px`
- Element Gap: `5px`
- Radius: `tags: 9px, cards: 18px, buttons: 9px, general: 9px`

## Surface cues
- **Page Canvas** `#ffffff`: Dominant background for the entire page, providing a bright, clean, and spacious foundation.
- **Feature Card Surface** `#ffffff`: Slightly elevated card backgrounds, appearing with 50% opacity to subtly distinguish itself from the main canvas without introducing heavy shadows.
- **Dark Content Panel** `#000000`: Used for specific content blocks or sections that require a darker backdrop, such as embedded product visuals or unique UI elements.
- **Header Action Background** `#f0f0f0`: A subtle, light gray background for ghost buttons or specific navigation elements, indicating interactive areas without being visually heavy.

## Component cues
- **Text Link Button**: Navigation, secondary actions
- **Outlined Neutral Button**: Secondary calls to action, filtering
- **Muted Outlined Button**: Tertiary actions, less prominent links
- **Filled Primary Button**: Main call to action
- **Light Header Button**: Navigation login actions

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
