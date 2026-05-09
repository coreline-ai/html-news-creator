# Uizard - Refero Design MD

- Source: https://styles.refero.design/style/8065e38a-cdb7-4645-b168-98e6f80e7118
- Original site: https://uizard.io
- Theme: `dark`
- Industry: `ai`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Midnight AI Canvas

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Ink | `#0b0b0b` | neutral | Primary text or dark surface |
| Deep Space | `#000000` | neutral | Primary text or dark surface |
| Lunar Surface | `#f5f5f5` | neutral | Page background or card surface |
| Asteroid Dust | `#aeaeae` | neutral | Border, muted text, or supporting surface |
| Cosmic Gray | `#212121` | neutral | Primary text or dark surface |
| Eclipse Gray | `#2e2e2e` | neutral | Primary text or dark surface |
| Starlight | `#ffffff` | neutral | Page background or card surface |
| AI Violet | `#a881fe` | brand | Action accent / signal color |
| AI Violet Gradient | `#6419ff` | brand | Action accent / signal color |
| Call to Action Blue | `#1e90ff` | accent | Action accent / signal color |

```css
:root {
  --ref-midnight-ink: #0b0b0b;
  --ref-deep-space: #000000;
  --ref-lunar-surface: #f5f5f5;
  --ref-asteroid-dust: #aeaeae;
  --ref-cosmic-gray: #212121;
  --ref-eclipse-gray: #2e2e2e;
  --ref-starlight: #ffffff;
  --ref-ai-violet: #a881fe;
}
```

## Typography direction
- **Satoshi-Variable**: 400, 480, 540, 560, 640, 12px, 14px, 16px, 18px, 20px, 24px, 40px, 1.00, 1.15, 1.20, 1.25, 1.29, 1.33, 1.38, 1.40, 1.43; substitute `Inter`.
- **ClashGrotesk-Variable**: 540, 72px, 1.00; substitute `Space Mono`.

## Spacing / shape
- Section Gap: `40px`
- Card Padding: `24px`
- Element Gap: `12px`
- Radius: `tags: 4px, cards: 16px, inputs: 10px, buttons: 12px`

## Surface cues
- **Deep Space** `#000000`: Base page background for large sections and deep elevation.
- **Midnight Ink** `#0b0b0b`: Primary page background, slightly lighter than Deep Space, and for card surfaces.
- **Transparent Card** `#21212152`: Subtly elevated card surfaces with a translucent effect, allowing the background to show through.
- **Starlight** `#ffffff`: Highest contrast surface for interactive elements like input fields, standing out against dark backgrounds.

## Component cues
- **Primary Action Button**: Filled button for primary calls to action, leveraging the brand violet.
- **Secondary Action Button**: Filled button for secondary actions, using a vivid blue.
- **Ghost Navigation Button**: Text-only button for navigation, blending into the dark background.
- **Testimonial Card**: Transparent card for displaying customer testimonials.
- **Implicit Card**: Card defined by padding and rounded corners on the base background, without explicit background color.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
