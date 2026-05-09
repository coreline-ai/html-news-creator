# Uniswap Cup - Refero Design MD

- Source: https://styles.refero.design/style/fabb51a0-0f83-4177-b83e-4969705a389c
- Original site: https://unicup.uniswap.org
- Theme: `light`
- Industry: `crypto`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Fuchsia-accented data panel. Precise, high-contrast, and digitally sharp typography on a stark white canvas, with a single, vibrant fuchsia cutting through the cool neutrality.

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#f2f2f2` | neutral | Page background or card surface |
| Midnight Ink | `#000000` | neutral | Primary text or dark surface |
| Alabaster | `#ffffff` | neutral | Page background or card surface |
| Graphite | `#222222` | neutral | Primary text or dark surface |
| Linen Mist | `#fef4ff` | neutral | Page background or card surface |
| Fuchsia Flare | `#f50db4` | brand | Action accent / signal color |

```css
:root {
  --ref-canvas-white: #f2f2f2;
  --ref-midnight-ink: #000000;
  --ref-alabaster: #ffffff;
  --ref-graphite: #222222;
  --ref-linen-mist: #fef4ff;
  --ref-fuchsia-flare: #f50db4;
}
```

## Typography direction
- **ui-sans-serif**: 400, 500, 600, 12px, 16px, 1.33, 1.50; substitute `Inter`.
- **ui-monospace**: 500, 700, 12px, 32px, 1.00, 1.33; substitute `Space Mono`.
- **Basel**: 500, 16px, 1.50.

## Spacing / shape
- Section Gap: `48px`
- Card Padding: `16px`
- Element Gap: `8px`
- Radius: `buttons: 1.67772e+07px, default: 0px`

## Surface cues
- **Canvas Background** `#f2f2f2`: Dominant page background, foundational layer.
- **Card Surface** `#ffffff`: Primary content areas, elevated panels, or interactive elements.
- **Subtle Panel** `#fef4ff`: Ghosted backgrounds for labels or contextual blocks, providing very slight distinction.
- **Interactive Block** `#000000`: Dark mode background for functional elements or highlighted sections.
- **Accent Block** `#f50db4`: High-contrast backgrounds for active states, important labels, or winners.

## Component cues
- **Ghost Button**: Navigation and secondary actions
- **Pill Button**: Call to action or key interactive elements
- **Team Score Block**: Displays individual team scores in the bracket
- **Active Team Score Element**: Highlights the winning team or active participant in a match

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
