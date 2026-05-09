# AutoSend - Refero Design MD

- Source: https://styles.refero.design/style/3d6eda0c-16ab-4e7e-aca6-5f9a5432bfd1
- Original site: https://autosend.com
- Theme: `light`
- Industry: `saas`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Crisp White Canvas

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Ink | `#292524` | neutral | Primary text or dark surface |
| Paper | `#fafaf9` | neutral | Page background or card surface |
| Whisper | `#e7e5e4` | neutral | Page background or card surface |
| Snow | `#ffffff` | neutral | Page background or card surface |
| Graphite | `#79716b` | neutral | Border, muted text, or supporting surface |
| Stone | `#a6a09b` | neutral | Border, muted text, or supporting surface |
| Ebony | `#0c0a09` | neutral | Primary text or dark surface |
| Violet Action | `#615fff` | brand | Action accent / signal color |
| Violet Accent | `#4f39f6` | brand | Action accent / signal color |
| Sunset Orange | `#d97757` | accent | Action accent / signal color |

```css
:root {
  --ref-ink: #292524;
  --ref-paper: #fafaf9;
  --ref-whisper: #e7e5e4;
  --ref-snow: #ffffff;
  --ref-graphite: #79716b;
  --ref-stone: #a6a09b;
  --ref-ebony: #0c0a09;
  --ref-violet-action: #615fff;
}
```

## Typography direction
- **Geist**: 400, 600, 12px, 14px, 16px, 18px, 20px, 40px, 1.20, 1.33, 1.38, 1.43, 1.50, 1.56; substitute `Inter`.
- **Geist Mono**: 400, 500, 600, 12px, 13px, 14px, 16px, 1.00, 1.14, 1.33, 1.43, 1.50, 1.54; substitute `JetBrains Mono`.
- **cooperLtBT**: 400, 18px, 80px, 1.10, 1.33; substitute `serif font like Playfair Display`.

## Spacing / shape
- Section Gap: `80px`
- Card Padding: `16px`
- Element Gap: `24px`
- Page Max Width: `1200px`
- Radius: `tags: 12px, cards: 16px, buttons: 8px, interactiveElements: 8px`

## Surface cues
- **Page Background** `#fafaf9`: The primary canvas for content, providing a light, airy foundation.
- **Card Surface** `#ffffff`: Used for content cards and elevated elements, creating a sense of lift from the page background.
- **Subtle Background** `#e7e5e4`: An even lighter neutral used for subtle background variations or muted sections.

## Component cues
- **Primary Filled Button**: Primary call-to-action button.
- **Ghost Button**: Secondary action button.
- **Text Button**: Minimal interactive element, inline actions.
- **Feature Card**: Content container for features or articles with subtle elevation.
- **Minimal Card**: Flat content container without elevation.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
