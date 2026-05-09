# Trunk - Refero Design MD

- Source: https://styles.refero.design/style/48971df7-919d-453c-9d0b-4600cd24c583
- Original site: https://trunk.io
- Theme: `dark`
- Industry: `devtools`
- Recommended fit: **Admin console / run monitor / developer tooling**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Midnight command center, energetic pulse.

## Apply to
- Admin run monitor and review states
- Compact evidence cards and source inspection panels
- Dark-mode operational dashboards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Carbon | `#08090b` | neutral | Primary text or dark surface |
| Obsidian | `#000000` | neutral | Primary text or dark surface |
| Frost | `#ffffff` | neutral | Page background or card surface |
| Steel Gray | `#232323` | neutral | Primary text or dark surface |
| Outline Gray | `#e2e8f0` | neutral | Page background or card surface |
| Muted Silver | `#b3b3b5` | neutral | Border, muted text, or supporting surface |
| Ghost Gray | `#c1c5c8` | neutral | Border, muted text, or supporting surface |
| Whisper White | `#dddddd` | neutral | Page background or card surface |
| Slate Shadow | `#89898d` | neutral | Border, muted text, or supporting surface |
| Vivid Blue | `#2f6eeb` | brand | Action accent / signal color |

```css
:root {
  --ref-carbon: #08090b;
  --ref-obsidian: #000000;
  --ref-frost: #ffffff;
  --ref-steel-gray: #232323;
  --ref-outline-gray: #e2e8f0;
  --ref-muted-silver: #b3b3b5;
  --ref-ghost-gray: #c1c5c8;
  --ref-whisper-white: #dddddd;
}
```

## Typography direction
- **neue**: 300, 400, 500, 700, 11px, 12px, 14px, 15px, 16px, 17px, 18px, 24px, 36px, 45px, 56px, 60px, 0.94, 1.00, 1.18, 1.20, 1.25, 1.30, 1.40, 1.50, 1.60; substitute `system-ui, sans-serif`.

## Spacing / shape
- Section Gap: `48px`
- Card Padding: `18px`
- Element Gap: `12px`
- Radius: `cards: 24px, buttons: 18px, heroAccent: 999px, interactiveElements: 12px`

## Surface cues
- **Obsidian Canvas** `#000000`: Base page background, deepest interactive zones.
- **Carbon Surface** `#08090b`: Primary component backgrounds like cards, default dark container background.
- **Steel Gray Component** `#232323`: Subtle interactive element backgrounds, specific hovered states, background for circular buttons.
- **Slate Shadow Accent** `#89898d`: Minor accent element backgrounds, subtle visual anchors.
- **Frost Hover** `#ffffff`: Primary button fill on dark, elevated hover states for interactive elements.

## Component cues
- **Primary Action Button**: Main call to action
- **Ghost Secondary Button**: Secondary action or navigation
- **Dark Filled Accent Button**: Contextual action on dark surfaces
- **Circular Icon Button**: Navigation or small interactive elements
- **Elevated Content Card**: Displaying features or testimonials with visual separation

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
