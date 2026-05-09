# ORYZO AI - Refero Design MD

- Source: https://styles.refero.design/style/1f204e95-454a-437e-845b-c1b169d35607
- Original site: https://oryzo.ai
- Theme: `dark`
- Industry: `other`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Cork-textured midnight laboratory

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Pitch Darkness | `#100904` | neutral | Primary text or dark surface |
| Cork Dust | `#ffedd7` | neutral | Page background or card surface |
| Rust Accent | `#dc5000` | brand | Action accent / signal color |
| Olive Green | `#445231` | brand | Action accent / signal color |
| Faded Bark | `#382416` | neutral | Primary text or dark surface |
| Aged Stone | `#887b6d` | neutral | Border, muted text, or supporting surface |
| Light Cork | `#f6e0c6` | neutral | Page background or card surface |
| Faint Hazel | `#bbac97` | neutral | Border, muted text, or supporting surface |
| Subtle Moss | `#5d6c49` | brand | Action accent / signal color |
| Grayscale Gray | `#808080` | neutral | Border, muted text, or supporting surface |

```css
:root {
  --ref-pitch-darkness: #100904;
  --ref-cork-dust: #ffedd7;
  --ref-rust-accent: #dc5000;
  --ref-olive-green: #445231;
  --ref-faded-bark: #382416;
  --ref-aged-stone: #887b6d;
  --ref-light-cork: #f6e0c6;
  --ref-faint-hazel: #bbac97;
}
```

## Typography direction
- **halyard-display-variable**: 400, 500, 600, 700, 10px, 12px, 14px, 15px, 16px, 17px, 18px, 23px, 24px, 29px, 34px, 41px, 49px, 51px, 64px, 123px, 147px, 227px, 410px, 0.90, 1.00, 1.09, 1.10, 1.20, 1.26, 1.33, 1.50, 1.78, 2.50, 3.00; substitute `Inter`.
- **Literata**: 200, 300, 500, 10px, 13px, 37px, 44px, 1.00, 1.20, 1.50, 2.36; substitute `Merriweather`.
- **DM Mono**: 400, 14px, 1.33; substitute `ui-monospace`.

## Spacing / shape
- Section Gap: `45px`
- Card Padding: `18px`
- Element Gap: `18px`
- Radius: `cards: 12px, badges: 36px, buttons: 36px`

## Component cues
- **Primary Action Button**: Filled button
- **Secondary Action Button**: Filled button
- **Ghost Button (Orange Border)**: Outlined button
- **Light Ghost Button**: Outlined button
- **Form Input Field**: Input element

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
