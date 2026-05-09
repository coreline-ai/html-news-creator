# Swwim - Refero Design MD

- Source: https://styles.refero.design/style/5cb1fbe8-b539-4482-b645-74a745332965
- Original site: https://www.weswwim.com
- Theme: `light`
- Industry: `agency`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Deep Ocean Canvas

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Ocean Blue | `#1658b3` | brand | Action accent / signal color |
| Midnight Indigo | `#0d3c88` | brand | Action accent / signal color |
| Sky Blue | `#015fee` | brand | Action accent / signal color |
| Horizon Blue | `#01295f` | brand | Action accent / signal color |
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Smoke Grey | `#e5e7eb` | neutral | Page background or card surface |
| Jet Black | `#000000` | neutral | Primary text or dark surface |
| Parchment | `#eee1d9` | neutral | Page background or card surface |

```css
:root {
  --ref-ocean-blue: #1658b3;
  --ref-midnight-indigo: #0d3c88;
  --ref-sky-blue: #015fee;
  --ref-horizon-blue: #01295f;
  --ref-canvas-white: #ffffff;
  --ref-smoke-grey: #e5e7eb;
  --ref-jet-black: #000000;
  --ref-parchment: #eee1d9;
}
```

## Typography direction
- **Greycliff**: 400, 500, 700, 14px, 16px, 18px, 20px, 24px, 30px, 1.20, 1.25, 1.33, 1.40, 1.43, 1.50, 1.56; substitute `system-ui, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif`.
- **Baton Turbo**: 400, 14px, 16px, 18px, 29px, 36px, 48px, 151px, 1.00, 1.11, 1.43, 1.50, 1.56; substitute `Impact, 'Arial Black', sans-serif`.

## Spacing / shape
- Section Gap: `24px`
- Card Padding: `24px`
- Element Gap: `4px`
- Page Max Width: `1080px`
- Radius: `tags: 9999px, cards: 0px, buttons: 9999px`

## Surface cues
- **Canvas White** `#ffffff`: Default page background for general content areas, providing a clean base.
- **Smoke Grey** `#e5e7eb`: Subtle background for UI elements like borders and inactive states, hinting at depth.
- **Ocean Blue** `#1658b3`: Prominent background for hero sections, interactive blocks, and key informational areas.
- **Midnight Indigo** `#0d3c88`: Darker background for footers and rich content sections, providing strong visual contrast.

## Component cues
- **Outline Ghost Button**: Interactive element for secondary actions.
- **Solid White Button**: Primary Call to Action.
- **Text Link Button**: Minor interactive elements and navigation links.
- **Hero Headline**: Primary visual communication on section headers.
- **Body Text**: Standard conveying informational detail.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
