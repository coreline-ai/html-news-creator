# Sauce Labs - Refero Design MD

- Source: https://styles.refero.design/style/d271a6c4-942f-4abf-a3de-66795f15f031
- Original site: https://saucelabs.com
- Theme: `dark`
- Industry: `devtools`
- Recommended fit: **Admin console / run monitor / developer tooling**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Dark teal command center

## Apply to
- Admin run monitor and review states
- Compact evidence cards and source inspection panels
- Dark-mode operational dashboards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Deep Teal | `#132322` | neutral | Primary text or dark surface |
| White Canvas | `#ffffff` | neutral | Page background or card surface |
| Black Ink | `#000000` | neutral | Primary text or dark surface |
| Fog | `#edf7f5` | neutral | Page background or card surface |
| Charcoal Grey | `#0e1a19` | neutral | Primary text or dark surface |
| Medium Grey | `#666666` | neutral | Border, muted text, or supporting surface |
| Light Grey | `#b2b6b4` | neutral | Border, muted text, or supporting surface |
| Silver Mist | `#d0d3d3` | neutral | Border, muted text, or supporting surface |
| Cool Stone | `#828786` | neutral | Border, muted text, or supporting surface |
| Vibrant Green | `#3ddc91` | brand | Action accent / signal color |

```css
:root {
  --ref-deep-teal: #132322;
  --ref-white-canvas: #ffffff;
  --ref-black-ink: #000000;
  --ref-fog: #edf7f5;
  --ref-charcoal-grey: #0e1a19;
  --ref-medium-grey: #666666;
  --ref-light-grey: #b2b6b4;
  --ref-silver-mist: #d0d3d3;
}
```

## Typography direction
- **Aeonik**: 400, 15px, 16px, 18px, 20px, 24px, 1.20, 1.25, 1.40, 1.45, 1.50; substitute `Inter`.
- **AeonikFono**: 400, 500, 9px, 14px, 16px, 24px, 32px, 40px, 48px, 64px, 1.10, 1.12, 1.20, 1.22, 1.30, 1.75; substitute `Space Mono`.

## Spacing / shape
- Section Gap: `24px`
- Card Padding: `24px`
- Element Gap: `24px`
- Radius: `cards: 20px, buttons: 32px, large-cards: 60px, round-elements: 56px`

## Surface cues
- **Deep Teal Canvas** `#132322`: Primary page and section background, often providing the dark base.
- **Overlay Card (Deep Teal)** `#132322`: Slightly elevated, semi-transparent card surfaces on the primary background.
- **Accent Card (Slate Green)** `#243b3a`: Distinct, darker card backgrounds for specific content blocks.
- **White Canvas (Light)** `#ffffff`: Primary light surface for content sections, contrasting with dark elements.
- **Fog (Light Elevated)** `#edf7f5`: Subtly elevated light card backgrounds.

## Component cues
- **Ghost Button (Accent Border)**: Secondary action button for dark backgrounds.
- **Ghost Button (White Border)**: Secondary action button for dark backgrounds.
- **Primary Action Button**: Main call-to-action.
- **Icon Button (Circular)**: Small, interactive icon container.
- **Overlay Card (Dark)**: Content card above dark section backgrounds.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
