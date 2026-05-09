# Era - Refero Design MD

- Source: https://styles.refero.design/style/715a3ad2-5b6d-421f-b72b-3aa6fec86351
- Original site: https://era.app
- Theme: `light`
- Industry: `fintech`
- Recommended fit: **Admin console / run monitor / developer tooling**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Swiss AI interface on frosted glass

## Apply to
- Admin run monitor and review states
- Compact evidence cards and source inspection panels
- Dark-mode operational dashboards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Charcoal | `#191a17` | neutral | Primary text or dark surface |
| Canvas Fog | `#f3f3f1` | neutral | Page background or card surface |
| Surface Mist | `#e6e6e4` | neutral | Page background or card surface |
| Snow Drift | `#ffffff` | neutral | Page background or card surface |
| Ash Gray | `#868784` | neutral | Border, muted text, or supporting surface |
| Slate Tint | `#3d3d3d` | neutral | Primary text or dark surface |
| Aqua Haze | `#add2d1` | accent | Action accent / signal color |
| Ocean Whisper | `#9dbebe` | accent | Action accent / signal color |
| Twilight Gradient | `#c9c5e1` | accent | Action accent / signal color |

```css
:root {
  --ref-midnight-charcoal: #191a17;
  --ref-canvas-fog: #f3f3f1;
  --ref-surface-mist: #e6e6e4;
  --ref-snow-drift: #ffffff;
  --ref-ash-gray: #868784;
  --ref-slate-tint: #3d3d3d;
  --ref-aqua-haze: #add2d1;
  --ref-ocean-whisper: #9dbebe;
}
```

## Typography direction
- **Saans VF**: 380, 400, 500, 600, 670, 12px, 13px, 15px, 16px, 20px, 30px, 35px, 56px, 1.15, 1.20, 1.25, 1.30, 1.38, 1.40, 1.50; substitute `Inter`.

## Spacing / shape
- Section Gap: `48px`
- Card Padding: `16px`
- Element Gap: `16px`
- Radius: `cards: 12px, badges: 6px, buttons: 9999px`

## Surface cues
- **Canvas Fog** `#f3f3f1`: Primary page background — the foundational layer of the light theme.
- **Surface Mist** `#e6e6e4`: Secondary background color for subtle differentiation of sections or ghost button fills, sitting just above the canvas.
- **Aqua Haze** `#add2d1`: Accented card backgrounds – visually distinct but still soft, used for feature highlights.
- **Snow Drift** `#ffffff`: Elevated card backgrounds, creating a clear boundary and sense of lift for important content blocks against the Canvas Fog.
- **Midnight Charcoal** `#191a17`: Darker card backgrounds for alternative feature presentation or specific UI elements like badges, creating high contrast.

## Component cues
- **Primary Filled Button**: Main call-to-action button, commands immediate attention.
- **Google Login Button**: External authentication, visually distinct from primary actions but still prominent.
- **Ghost Button**: Secondary action or navigation, minimal visual weight.
- **Outlined CTA Button**: Call to action with less emphasis than a filled button, like 'Add to Claude'.
- **Standard Card**: Container for content sections, usually on the main canvas.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
