# clau.as.kee - Refero Design MD

- Source: https://styles.refero.design/style/9aad4722-413d-4b32-bda7-6f94bbd9938c
- Original site: https://clauaskee.com
- Theme: `light`
- Industry: `design`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Playful Serif on Lavender

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Ink | `#1a1a1a` | neutral | Primary text or dark surface |
| Canvas Lavender | `#8e93ff` | brand | Action accent / signal color |
| Digital Green | `#47f654` | accent | Action accent / signal color |
| Paper White | `#ffffff` | neutral | Page background or card surface |

```css
:root {
  --ref-midnight-ink: #1a1a1a;
  --ref-canvas-lavender: #8e93ff;
  --ref-digital-green: #47f654;
  --ref-paper-white: #ffffff;
}
```

## Typography direction
- **Beastly clauworks**: 400, 288px, 504px, 1.00, 1.05; substitute `Playfair Display`.
- **Suisse Intl clauworks**: 400, 20px, 30px, 144px, 1.15, 1.30, 1.33, 1.50; substitute `Inter`.
- **Times**: 400, 16px, 1.15; substitute `Times New Roman`.

## Spacing / shape
- Section Gap: `130px`
- Card Padding: `58px`
- Element Gap: `30px`
- Radius: `buttons: 75px`

## Surface cues
- **Canvas Lavender** `#8e93ff`: Primary page background, expansive sections
- **Paper White** `#ffffff`: Content cards, overlaid text blocks
- **Midnight Ink Overlay** `#1a1a1a`: Accented sections, background for high-contrast text

## Component cues
- **Pill Accent Button**: Primary call to action, interactive links
- **Navigation Link**: Global navigation, secondary interactive elements
- **Text Card**: Content presentation for projects or information blocks

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
