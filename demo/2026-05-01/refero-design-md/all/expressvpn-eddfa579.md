# ExpressVPN - Refero Design MD

- Source: https://styles.refero.design/style/eddfa579-89f1-467d-a486-99a56be36c30
- Original site: https://www.expressvpn.com
- Theme: `light`
- Industry: `other`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Secure utility, bright teal highlights

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Ink | `#001d2f` | neutral | Primary text or dark surface |
| Cloud White | `#ffffff` | neutral | Page background or card surface |
| Ghost Gray | `#f7f8f9` | neutral | Page background or card surface |
| Cool Stone | `#ccd2d5` | neutral | Border, muted text, or supporting surface |
| Slate Blue | `#667782` | neutral | Action accent / signal color |
| Forest Teal | `#0f866c` | brand | Action accent / signal color |
| Dark Teal | `#00695c` | brand | Action accent / signal color |
| Warm Beige | `#f0eacf` | accent | Action accent / signal color |
| Soft Peach | `#ffe4d4` | accent | Action accent / signal color |
| Sky Mist | `#b7d1d0` | accent | Action accent / signal color |

```css
:root {
  --ref-midnight-ink: #001d2f;
  --ref-cloud-white: #ffffff;
  --ref-ghost-gray: #f7f8f9;
  --ref-cool-stone: #ccd2d5;
  --ref-slate-blue: #667782;
  --ref-forest-teal: #0f866c;
  --ref-dark-teal: #00695c;
  --ref-warm-beige: #f0eacf;
}
```

## Typography direction
- **Inter**: 400, 500, 600, 700, 10px, 12px, 14px, 16px, 18px, 20px, 24px, 1.00, 1.20, 1.33, 1.44, 1.50, 1.67, 1.72, 1.75, 1.80, 1.83, 1.90, 2.00; substitute `system-ui, sans-serif`.
- **Inter**: 400, 500, 600, 700, 10px, 12px, 14px, 16px, 18px, 20px, 24px, 1.00, 1.20, 1.33, 1.44, 1.50, 1.67, 1.72, 1.75, 1.80, 1.83, 1.90, 2.00; substitute `system-ui, sans-serif`.
- **Inter**: 400, 500, 600, 700, 10px, 12px, 14px, 16px, 18px, 20px, 24px, 1.00, 1.20, 1.33, 1.44, 1.50, 1.67, 1.72, 1.75, 1.80, 1.83, 1.90, 2.00; substitute `system-ui, sans-serif`.

## Spacing / shape
- Section Gap: `24px`
- Card Padding: `32px`
- Element Gap: `24px`
- Radius: `tags: 10px, cards: 24px, badges: 24px, inputs: 10px, buttons: 34px, navItems: 4px, extraLarge: 1132.2px`

## Surface cues
- **Page Canvas** `#f7f8f9`: The default background for the entire page, providing a light, crisp base.
- **Standard Surface** `#ffffff`: Used for main content cards, badges, and primary components, providing distinct elevation from the page canvas.
- **Accent Surface** `#0f866c`: Used for highly prominent cards or sections where immediate attention is required, leveraging the primary brand color.

## Component cues
- **Primary Action Button**: Filled button indicating primary calls to action
- **Ghost Button**: Outlined button for secondary actions or navigation.
- **Subtle Ghost Button**: Outlined button with lighter background for less prominent actions.
- **Inline Text Link**: Non-button interactive text within content.
- **Elevated Feature Card**: Prominent information card with emphasis.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
