# North Kingdom - Refero Design MD

- Source: https://styles.refero.design/style/145e70b3-e0a4-4fbd-8d9e-23bd93dd0021
- Original site: https://www.northkingdom.com
- Theme: `dark`
- Industry: `design`
- Recommended fit: **Dark webapp exploration**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Cinematic Night Canvas

## Apply to
- Dark theme experiments
- Operator-focused widgets
- High-contrast card systems

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Ink | `#050311` | neutral | Primary text or dark surface |
| Ghost White | `#ffffff` | neutral | Page background or card surface |
| Pitch Black | `#000000` | neutral | Primary text or dark surface |
| Dusty Slate | `#9b9aa0` | neutral | Border, muted text, or supporting surface |

```css
:root {
  --ref-midnight-ink: #050311;
  --ref-ghost-white: #ffffff;
  --ref-pitch-black: #000000;
  --ref-dusty-slate: #9b9aa0;
}
```

## Typography direction
- **FKGroteskNeue**: 400, 24px, 1.15, 1.70; substitute `system-ui, sans-serif`.
- **Arial**: 400, 13px, 1.20; substitute `system-ui, sans-serif`.

## Spacing / shape
- Section Gap: `80px`
- Card Padding: `0px`
- Element Gap: `10px`
- Radius: `cards: 8px, input: 26px, buttons: 4px, general: 8px`

## Component cues
- **Ghost Border Button**: Interactive element (e.g. video controls)
- **Circular Play Button**: Video player control
- **Muted Ghost Button**: Tertiary interactive state
- **Feature Card**: Content display
- **Text Input**: Form entry

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
