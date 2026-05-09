# Fable - Refero Design MD

- Source: https://styles.refero.design/style/ab650279-aa18-43e5-a998-34190d7bedc7
- Original site: https://fable.co
- Theme: `light`
- Industry: `media`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
whimsical storybook canvas

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Forest Canopy | `#064c37` | brand | Action accent / signal color |
| Ocean Deep | `#43a1d7` | accent | Action accent / signal color |
| Midnight Ink | `#161015` | neutral | Primary text or dark surface |
| Deep Space | `#070607` | neutral | Primary text or dark surface |
| Slate Shadow | `#292229` | neutral | Primary text or dark surface |
| Pearl White | `#ffffff` | neutral | Page background or card surface |
| Parchment | `#f7f4ee` | neutral | Page background or card surface |
| Ghost Gray | `#ededed` | neutral | Page background or card surface |
| Ink Wash | `#3f383d` | neutral | Primary text or dark surface |

```css
:root {
  --ref-forest-canopy: #064c37;
  --ref-ocean-deep: #43a1d7;
  --ref-midnight-ink: #161015;
  --ref-deep-space: #070607;
  --ref-slate-shadow: #292229;
  --ref-pearl-white: #ffffff;
  --ref-parchment: #f7f4ee;
  --ref-ghost-gray: #ededed;
}
```

## Typography direction
- **Inter**: 400, 500, 600, 700, 8px, 10px, 12px, 14px, 15px, 16px, 18px, 20px, 24px, 30px, 1.00, 1.13, 1.17, 1.25, 1.33, 1.42, 1.43, 1.50, 1.60; substitute `system-ui, sans-serif`.
- **Heldane Display**: 400, 500, 22px, 26px, 48px, 72px, 80px, 0.86, 0.88, 0.94, 1.08, 1.09; substitute `serif`.
- **Aktiv Grotesk**: 400, 13px, 1.50; substitute `system-ui, sans-serif`.

## Spacing / shape
- Section Gap: `24px`
- Card Padding: `24px`
- Element Gap: `24px`
- Radius: `cards: 12px, buttons: 60px, largeCards: 48px, mediumCards: 24px`

## Surface cues
- **Ocean Deep Canvas** `#43a1d7`: Base background for prominent sections, providing a strong visual anchor.
- **Parchment Surface** `#f7f4ee`: Primary card and content block background, offering a warm, light surface.
- **Pearl White Element** `#ffffff`: Background for interactive elements, buttons, and focused content, providing highest contrast.
- **Midnight Ink Elevated** `#161015`: Background for deeply embedded cards or sections, using a dark tone to create visual depth, often with a shadow.

## Component cues
- **Primary Filled Button**: Call to action button
- **Navigation Link**: Header and footer navigation
- **Light Theme Filled Button**: Secondary call to action, interactive elements on dark backgrounds
- **Card with Shadow**: Featured content card, elevated interactive elements
- **Product Display Card**: Book cover display, content grid item

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
