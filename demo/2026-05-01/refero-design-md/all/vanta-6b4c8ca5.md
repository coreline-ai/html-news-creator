# Vanta - Refero Design MD

- Source: https://styles.refero.design/style/6b4c8ca5-476e-442b-b713-d5fc58cf04ac
- Original site: https://www.vanta.com
- Theme: `light`
- Industry: `saas`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Regal Clarity on White Canvas

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Background Snow | `#f7f8fa` | neutral | Page background or card surface |
| Cloud Gray | `#eaeaf1` | neutral | Page background or card surface |
| Border Fog | `#dfdfe9` | neutral | Page background or card surface |
| Muted Ash | `#9e9fb7` | neutral | Border, muted text, or supporting surface |
| Stone Gray | `#6d6e87` | neutral | Border, muted text, or supporting surface |
| Dark Charcoal | `#484960` | neutral | Border, muted text, or supporting surface |
| Midnight Ink | `#181822` | neutral | Primary text or dark surface |
| Deep Plum | `#260048` | brand | Action accent / signal color |
| Vanta Purple | `#5e05c4` | brand | Action accent / signal color |

```css
:root {
  --ref-canvas-white: #ffffff;
  --ref-background-snow: #f7f8fa;
  --ref-cloud-gray: #eaeaf1;
  --ref-border-fog: #dfdfe9;
  --ref-muted-ash: #9e9fb7;
  --ref-stone-gray: #6d6e87;
  --ref-dark-charcoal: #484960;
  --ref-midnight-ink: #181822;
}
```

## Typography direction
- **Inter Variable**: 400, 500, 600, 700, 10px, 12px, 14px, 16px, 18px, 20px, 24px, 32px, 40px, 1.30, 1.35, 1.43, 1.50, 1.60; substitute `system-ui`.
- **Reckless**: 400, 500, 30px, 42px, 56px, 72px, 90px, 1.10, 1.20, 1.25; substitute `serif`.

## Spacing / shape
- Section Gap: `32px`
- Card Padding: `32px`
- Element Gap: `16px`
- Radius: `cards: 16px, inputs: 999px, buttons: 999px, default: 8px`

## Surface cues
- **Background Snow** `#f7f8fa`: Primary page background
- **Canvas White** `#ffffff`: Default card surfaces, interactive containers
- **Sky Lavender** `#cdd2f8`: Accentuated section backgrounds, soft elevated areas

## Component cues
- **Primary Filled Button**: Call to action button for primary actions
- **Ghost Navigation Button**: Secondary navigation or subtle actions
- **Outlined Input Field**: Text input areas for forms
- **Elevated Content Card**: Container for features or grouped information
- **Feature Highlight Card**: Cards within hero section or for key features

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
