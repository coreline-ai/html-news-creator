# Leonardo.ai - Refero Design MD

- Source: https://styles.refero.design/style/8c3f2805-dfce-4edd-8a9c-946bee4f1cff
- Original site: https://leonardo.ai
- Theme: `dark`
- Industry: `ai`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Luminous Digital Void: vibrant hues punching through deep darkness.

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Void | `#000000` | neutral | Primary text or dark surface |
| Ghostly Gray | `#e5e5e5` | neutral | Page background or card surface |
| Off-Black Text | `#0a0a0a` | neutral | Primary text or dark surface |
| Pure White | `#ffffff` | neutral | Page background or card surface |
| Subtle Surface | `#353535` | neutral | Primary text or dark surface |
| Muted Ash | `#999999` | neutral | Border, muted text, or supporting surface |
| Luminous Green | `#03e65b` | brand | Action accent / signal color |
| Deep Violet | `#6e60ee` | brand | Action accent / signal color |
| Electric Yellow | `#ffc533` | brand | Action accent / signal color |
| Vivid Crimson | `#ff3386` | brand | Action accent / signal color |

```css
:root {
  --ref-midnight-void: #000000;
  --ref-ghostly-gray: #e5e5e5;
  --ref-off-black-text: #0a0a0a;
  --ref-pure-white: #ffffff;
  --ref-subtle-surface: #353535;
  --ref-muted-ash: #999999;
  --ref-luminous-green: #03e65b;
  --ref-deep-violet: #6e60ee;
}
```

## Typography direction
- **canvaSans**: 400, 500, 700, 10px, 12px, 14px, 16px, 18px, 19px, 1.10, 1.15, 1.20, 1.25, 1.33; substitute `system-ui, sans-serif`.
- **leoSans**: 500, 800, 900, 14px, 22px, 34px, 35px, 39px, 44px, 45px, 48px, 50px, 51px, 59px, 65px, 66px, 68px, 75px, 76px, 78px, 79px, 85px, 86px, 90px, 98px, 165px, 0.80, 0.85, 0.90, 0.93, 1.00, 1.25; substitute `Georgia, serif`.
- **ufficioDisplay**: 500, 34px, 0.92; substitute `serif`.

## Spacing / shape
- Section Gap: `34-37px`
- Card Padding: `17-20px`
- Element Gap: `7-10px`
- Radius: `tags: 270px, cards: 8.4375px, buttons: 60px`

## Surface cues
- **Midnight Void** `#000000`: Primary page background, the base canvas.
- **Subtle Surface** `#353535`: Elevated card backgrounds, offering slight differentiation from the base.

## Component cues
- **Ghost Pill Button**: Secondary action button for navigation or tertiary interactions.
- **Filled Pill Button (Light)**: Primary action button, high contrast.
- **Icon-only Button**: Navigation or small interactive elements where size is minimal.
- **Horizontal Tab Button**: Segmented control for filtering or switching views.
- **Basic Content Card**: Container for secondary content like descriptions or detailed information.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
