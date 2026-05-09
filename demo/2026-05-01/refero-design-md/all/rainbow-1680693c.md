# Rainbow - Refero Design MD

- Source: https://styles.refero.design/style/1680693c-aed8-47e8-917a-04eb89497b09
- Original site: https://rainbow.me
- Theme: `light`
- Industry: `crypto`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Vibrant dreamscape on cloudnine. The dominant palette of soft, often radial, gradients creates an otherworldly, playful backdrop for bold UI elements.

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Ink | `#0f101a` | neutral | Primary text or dark surface |
| Cloudburst | `#ffffff` | neutral | Page background or card surface |
| Whisper Gray | `#777885` | neutral | Border, muted text, or supporting surface |
| Pale Mist | `#f1f3f6` | neutral | Page background or card surface |
| Sunset Orange | `#ff8a00` | brand | Action accent / signal color |
| Neon Pink | `#ff54bb` | brand | Action accent / signal color |
| Sky Blue | `#33aaff` | accent | Action accent / signal color |
| Cyan Tint | `#99eeff` | accent | Action accent / signal color |
| Radiant Violet | `#8c64ff` | accent | Action accent / signal color |
| Teal Glow | `#00fff0` | accent | Action accent / signal color |

```css
:root {
  --ref-ink: #0f101a;
  --ref-cloudburst: #ffffff;
  --ref-whisper-gray: #777885;
  --ref-pale-mist: #f1f3f6;
  --ref-sunset-orange: #ff8a00;
  --ref-neon-pink: #ff54bb;
  --ref-sky-blue: #33aaff;
  --ref-cyan-tint: #99eeff;
}
```

## Typography direction
- **SF Pro Rounded**: 400, 16px, 20px, 24px, 32px, 36px, 42px, 56px, 80px, 96px, 100px, 1.00, 1.10, 1.20; substitute `system-ui, 'Avenir Next Rounded Std', 'Inter Display'`.
- **sans-serif**: 400, 12px, 1.20; substitute `system-ui`.

## Spacing / shape
- Section Gap: `48-60px`
- Card Padding: `20-32px`
- Element Gap: `8-24px`
- Radius: `pill: 50px, cards: 32px, image: 32px-100px, buttons: 40px`

## Component cues
- **Download CTA Button Group**: Reference component style.
- **Wallet Token List Card**: Reference component style.
- **Network Changed Notification Banner**: Reference component style.
- **Primary Call-to-Action Button (Orange)**: Main user action for downloads and critical steps.
- **Secondary Call-to-Action Button (Pink)**: Alternative user action for downloads or prominent selections.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
