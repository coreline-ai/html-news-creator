# Becklyn - Refero Design MD

- Source: https://styles.refero.design/style/3389358b-68b2-4fca-82a8-52c07b3a3475
- Original site: https://becklyn.com
- Theme: `dark`
- Industry: `agency`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Inky canvas, stark white lines

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Ink | `#1a1a1a` | neutral | Primary text or dark surface |
| Ghost White | `#ffffff` | neutral | Page background or card surface |
| Charcoal Gray | `#3b3b3b` | neutral | Primary text or dark surface |
| Steel Gray | `#606060` | neutral | Border, muted text, or supporting surface |
| Spectrum Burst | `#004eff` | accent | Action accent / signal color |

```css
:root {
  --ref-midnight-ink: #1a1a1a;
  --ref-ghost-white: #ffffff;
  --ref-charcoal-gray: #3b3b3b;
  --ref-steel-gray: #606060;
  --ref-spectrum-burst: #004eff;
}
```

## Typography direction
- **UniversalSans**: 400, 12px, 20px, 22px, 36px, 42px, 68px, 92px, 1.00, 1.05, 1.15, 1.20; substitute `Inter`.
- **Cambon**: 400, 22px, 68px, 92px, 1.00, 1.15; substitute `Playfair Display`.

## Spacing / shape
- Section Gap: `40px`
- Card Padding: `20px`
- Element Gap: `20px`
- Page Max Width: `503px`
- Radius: `cards: 10px, 20px, subtle: 23px, 31px, buttons: 100px`

## Surface cues
- **Midnight Canvas** `#1a1a1a`: Base page background, darkest surface layer.
- **Charcoal Card** `#3b3b3b`: Elevated card backgrounds, slightly lighter than the canvas to provide subtle depth.

## Component cues
- **Ghost Navigation Link (Dark)**: Global navigation item
- **Ghost Navigation Link (Light)**: Footer navigation item
- **Circular Toggle Button**: Interactive control or status indicator
- **Information Card (Charcoal)**: Content container, feature display
- **Information Card (Midnight)**: Prominent content container

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
