# Galileo-ft - Refero Design MD

- Source: https://styles.refero.design/style/10a77cbd-7847-4e1b-a09e-447ebad0f7c6
- Original site: https://www.galileo-ft.com
- Theme: `dark`
- Industry: `fintech`
- Recommended fit: **Admin console / run monitor / developer tooling**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Deep-space command center

## Apply to
- Admin run monitor and review states
- Compact evidence cards and source inspection panels
- Dark-mode operational dashboards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Ink | `#03081a` | neutral | Primary text or dark surface |
| Void Shadow | `#020626` | neutral | Primary text or dark surface |
| Galileo Violet | `#3d50fc` | brand | Action accent / signal color |
| Cosmic Gray | `#292f66` | neutral | Primary text or dark surface |
| Starlight Blue | `#aab1f2` | accent | Action accent / signal color |
| Neon Aqua | `#05cee0` | accent | Action accent / signal color |
| Nebula Blue | `#4d5499` | neutral | Action accent / signal color |
| Deep Space Blue | `#080f4d` | neutral | Action accent / signal color |
| Lunar Dust | `#d9ddff` | neutral | Page background or card surface |
| Flux Orange | `#d80c9a` | accent | Action accent / signal color |

```css
:root {
  --ref-midnight-ink: #03081a;
  --ref-void-shadow: #020626;
  --ref-galileo-violet: #3d50fc;
  --ref-cosmic-gray: #292f66;
  --ref-starlight-blue: #aab1f2;
  --ref-neon-aqua: #05cee0;
  --ref-nebula-blue: #4d5499;
  --ref-deep-space-blue: #080f4d;
}
```

## Typography direction
- **Plain Ultrathin**: 100, 42px, 56px, 83px, 147px, 0.80, 1.00, 1.10, 1.20; substitute `Montserrat, sans-serif`.
- **Plain Ultralight**: 100, 28px, 1.30; substitute `Montserrat, sans-serif`.
- **Plain Light**: 300, 12px, 14px, 1.40, 1.50, 1.80; substitute `Montserrat, sans-serif`.

## Spacing / shape
- Section Gap: `26px`
- Card Padding: `35px`
- Element Gap: `9px`
- Page Max Width: `1200px`
- Radius: `cards: 34.704px, buttons: 47.7072px, interactive: 17.352px`

## Surface cues
- **Canvas** `#03081a`: The deepest background layer for the entire page, setting the dark theme.
- **Base Surface** `#020626`: Used for sections and cards that visually lift slightly from the canvas, providing a subtle layer differentiation.
- **Elevated Surface** `#FFFFFF`: A contrasting light surface for distinct content blocks, often used in alternating sections to break the dark theme.

## Component cues
- **Ghost Navigation Button**: Primary navigation and links within dark context.
- **Primary Action Button**: Key calls to action requiring prominence.
- **Secondary Action Button**: Calls to action on lighter backgrounds that need to stand out.
- **Subtle Card**: Container for secondary content or feature blocks.
- **Product Insight Card**: Informational cards within a feature section.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
