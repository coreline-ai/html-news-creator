# Things - Refero Design MD

- Source: https://styles.refero.design/style/ec0f5bca-8367-49e7-b8aa-73b3fa09a4a0
- Original site: https://culturedcode.com/things
- Theme: `light`
- Industry: `productivity`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
organized desktop, clean and bright

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Ink | `#303336` | neutral | Primary text or dark surface |
| Charcoal Text | `#44474b` | neutral | Border, muted text, or supporting surface |
| Subtle Ash | `#838b96` | neutral | Border, muted text, or supporting surface |
| Silver Mist | `#9299a4` | neutral | Border, muted text, or supporting surface |
| Off-White Canvas | `#ffffff` | neutral | Page background or card surface |
| Cloud Gray | `#f2f5f7` | neutral | Page background or card surface |
| Frost Border | `#dfe3e8` | neutral | Page background or card surface |
| Ocean Blue | `#2576eb` | brand | Action accent / signal color |
| Sky Link Blue | `#5c9cf5` | brand | Action accent / signal color |
| Action Button Blue | `#4f91fb` | brand | Action accent / signal color |

```css
:root {
  --ref-midnight-ink: #303336;
  --ref-charcoal-text: #44474b;
  --ref-subtle-ash: #838b96;
  --ref-silver-mist: #9299a4;
  --ref-off-white-canvas: #ffffff;
  --ref-cloud-gray: #f2f5f7;
  --ref-frost-border: #dfe3e8;
  --ref-ocean-blue: #2576eb;
}
```

## Typography direction
- **ui-sans-serif**: 400, 600, 700, 800, 13px, 14px, 15px, 16px, 17px, 18px, 20px, 24px, 36px, 1.00, 1.20, 1.25, 1.30, 1.35, 1.40, 1.60; substitute `system-ui, sans-serif`.

## Spacing / shape
- Section Gap: `48px`
- Card Padding: `18px`
- Element Gap: `4-14px`
- Page Max Width: `900px`
- Radius: `cards: 18px, icons: 3px, inputs: 6px, buttons: 6px, hero-label: 12.8px`

## Component cues
- **Watch Introduction Video Button**: Reference component style.
- **Simply Powerful Section Card**: Reference component style.
- **App Sidebar Navigation Card**: Reference component style.
- **Primary Action Button**: Call to action.
- **Section Separator Card**: Organizing content blocks.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
