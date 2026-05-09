# Reducto - Refero Design MD

- Source: https://styles.refero.design/style/af55f85e-1c82-44c1-a8d0-32634bfa6296
- Original site: https://reducto.ai
- Theme: `light`
- Industry: `ai`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Crisp Data Canvas

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Ghostly Gray | `#fafaf9` | neutral | Page background or card surface |
| Reducto Black | `#292524` | neutral | Action accent / signal color |
| Subtle Ash | `#79716b` | neutral | Border, muted text, or supporting surface |
| Medium Gray | `#57534d` | neutral | Border, muted text, or supporting surface |
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Reducto Purple Dark | `#310632` | brand | Action accent / signal color |
| Reducto Purple Accent | `#9d17a0` | brand | Action accent / signal color |
| Reducto Purple Border | `#690f6b` | brand | Action accent / signal color |
| Whisper Lilac | `#dcbffb` | accent | Action accent / signal color |
| Sage Green | `#718613` | accent | Action accent / signal color |

```css
:root {
  --ref-ghostly-gray: #fafaf9;
  --ref-reducto-black: #292524;
  --ref-subtle-ash: #79716b;
  --ref-medium-gray: #57534d;
  --ref-canvas-white: #ffffff;
  --ref-reducto-purple-dark: #310632;
  --ref-reducto-purple-accent: #9d17a0;
  --ref-reducto-purple-border: #690f6b;
}
```

## Typography direction
- **Inter**: 400, 500, 14px, 15px, 16px, 17px, 18px, 20px, 24px, 1.33, 1.43, 1.50, 1.56, 1.60; substitute `system-ui, sans-serif`.
- **reductoSerif**: 400, 470, 650, 16px, 24px, 32px, 64px, 80px, 136px, 0.74, 1.13, 1.25, 1.33, 1.50; substitute `serif`.
- **reductosans**: 400, 500, 14px, 15px, 16px, 1.43, 1.50, 1.60; substitute `system-ui, sans-serif`.

## Spacing / shape
- Section Gap: `64px`
- Card Padding: `24px`
- Element Gap: `24px`
- Radius: `none: 0px`

## Surface cues
- **Page Canvas** `#fafaf9`: Dominant background for the entire application, providing a clean, bright foundation.
- **Content Card** `#ffffff`: Background for elevated content sections, cards, and interactive elements. Also serves as the secondary background.
- **Subtle Pattern** `#f5f5f4`: Used for textural background elements or subtle section distinctions, creating minor visual separation.

## Component cues
- **Primary Action Button**: Filled button for primary calls to action.
- **Ghost Action Button**: Outlined button for secondary or tertiary actions.
- **Navigation Link Button**: Small, ghost-like button for navigation items.
- **Outline Secondary Button**: Outlined button variant for less prominent actions, found in content areas.
- **Hero Headline**: Large, impactful display text for hero sections.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
