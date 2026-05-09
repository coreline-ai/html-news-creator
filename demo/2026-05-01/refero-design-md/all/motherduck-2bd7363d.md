# MotherDuck - Refero Design MD

- Source: https://styles.refero.design/style/2bd7363d-7aae-4b1f-9d5a-1edeb17ca567
- Original site: https://motherduck.com
- Theme: `light`
- Industry: `ai`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Playful blueprint on paper bag

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas Oat | `#f4efea` | neutral | Page background or card surface |
| Paper White | `#ffffff` | neutral | Page background or card surface |
| Smoke Gray | `#f8f8f7` | neutral | Page background or card surface |
| Ink | `#383838` | neutral | Primary text or dark surface |
| Coal | `#000000` | neutral | Primary text or dark surface |
| Slate | `#818181` | neutral | Border, muted text, or supporting surface |
| Sky Blue | `#6fc2ff` | brand | Action accent / signal color |
| Mellow Yellow | `#ffde00` | accent | Action accent / signal color |
| Ocean Teal | `#16aa98` | accent | Action accent / signal color |
| Seafoam | `#53dbc9` | accent | Action accent / signal color |

```css
:root {
  --ref-canvas-oat: #f4efea;
  --ref-paper-white: #ffffff;
  --ref-smoke-gray: #f8f8f7;
  --ref-ink: #383838;
  --ref-coal: #000000;
  --ref-slate: #818181;
  --ref-sky-blue: #6fc2ff;
  --ref-mellow-yellow: #ffde00;
}
```

## Typography direction
- **Aeonik Mono**: 300, 400, 500, 600, 11px, 12px, 14px, 16px, 18px, 20px, 24px, 32px, 40px, 56px, 1.00, 1.20, 1.30, 1.40, 1.60; substitute `Space Mono`.
- **Inter**: 300, 400, 600, 700, 12px, 14px, 16px, 18px, 20px, 22px, 24px, 32px, 44px, 1.00, 1.20, 1.30, 1.36, 1.37, 1.38, 1.40, 1.60; substitute `system-ui`.

## Spacing / shape
- Section Gap: `50px`
- Card Padding: `40px`
- Element Gap: `8px`
- Radius: `cards: 0px, inputs: 2px, buttons: 2px, default: 2px`

## Surface cues
- **Canvas Oat** `#f4efea`: Base page background, giving a warm off-white feel.
- **Paper White** `#ffffff`: Default surface for cards, panels, and input fields, offering clean contrast.
- **Smoke Gray** `#f8f8f7`: Slightly elevated background for some component variants or subtle content divisions.
- **Frost Blue** `#ebf9ff`: Used for hover states or very light background accents, hinting at interactivity.

## Component cues
- **Primary Action Button**: Main call to action for conversion.
- **Secondary Ghost Button**: Alternative or less prominent actions.
- **Muted Action Button**: Buttons for less critical functions or within contextual menus.
- **Outlined Info Card**: Clickable cards presenting information with a decorative border.
- **Decorative Border Button (Neutral)**: Used for filtering or categorization, visually distinct with a colored border but neutral text.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
