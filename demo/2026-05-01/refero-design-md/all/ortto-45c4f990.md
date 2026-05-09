# Ortto - Refero Design MD

- Source: https://styles.refero.design/style/45c4f990-e6b4-472d-89a4-06870ac17b9f
- Original site: https://ortto.com
- Theme: `mixed`
- Industry: `saas`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Shifting canvases, vivid blue accent

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Canvas | `#14171f` | neutral | Primary text or dark surface |
| Aura Gray | `#f9f8f7` | neutral | Page background or card surface |
| Snowdrift | `#ffffff` | neutral | Page background or card surface |
| Ink Black | `#000000` | neutral | Primary text or dark surface |
| Gunmetal | `#252525` | neutral | Primary text or dark surface |
| Deep Gray | `#0d0d0d` | neutral | Primary text or dark surface |
| Muted Stone | `#6d6b70` | neutral | Border, muted text, or supporting surface |
| Porcelain | `#e9e5e2` | neutral | Page background or card surface |
| Ortto Blue | `#1070ff` | brand | Action accent / signal color |
| Vivid Violet | `#0066ff` | accent | Action accent / signal color |

```css
:root {
  --ref-midnight-canvas: #14171f;
  --ref-aura-gray: #f9f8f7;
  --ref-snowdrift: #ffffff;
  --ref-ink-black: #000000;
  --ref-gunmetal: #252525;
  --ref-deep-gray: #0d0d0d;
  --ref-muted-stone: #6d6b70;
  --ref-porcelain: #e9e5e2;
}
```

## Typography direction
- **sans-serif**: 400, 12px, 16px, 1.20; substitute `system-ui`.
- **Haas Grot Text R Web**: 400, 700, 19px, 1.20; substitute `Inter`.
- **Haas Grot Text R Web**: 400, 14px, 16px, 24px, 1.20, 1.38, 1.43; substitute `Inter Medium`.

## Spacing / shape
- Section Gap: `40px`
- Card Padding: `32px`
- Element Gap: `8px`
- Radius: `tags: 50px, buttons: 40px, default: 4px, sections: 16px`

## Surface cues
- **Snowdrift** `#ffffff`: Base page background and primary content surfaces.
- **Aura Gray** `#f9f8f7`: Secondary content containers, subtle background differentiation.
- **Porcelain** `#e9e5e2`: Tertiary backgrounds and dividers, light visual separation.
- **Midnight Canvas** `#14171f`: Dark section backgrounds, hero areas, and elements requiring strong contrast.

## Component cues
- **Primary Action Button**: Filled button for main calls-to-action.
- **Ghost Button**: Outline button for secondary actions.
- **Subtle Ghost Button**: Outline button with a soft background for less prominent secondary actions.
- **Navigation Link**: Interactive elements in the header navigation.
- **Feature Card**: Container for showcasing features or testimonials.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
