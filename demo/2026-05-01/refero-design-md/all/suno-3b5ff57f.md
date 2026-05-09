# Suno - Refero Design MD

- Source: https://styles.refero.design/style/3b5ff57f-a371-4c7f-82ae-5fc5485da073
- Original site: https://suno.com
- Theme: `dark`
- Industry: `ai`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Dark studio, neon pulses. An expansive, dim canvas where vibrant light flickers to life.

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Pitch Black | `#101012` | neutral | Primary text or dark surface |
| Void Black | `#17171a` | neutral | Primary text or dark surface |
| Ghost White | `#f7f4ef` | neutral | Page background or card surface |
| Pure White | `#ffffff` | neutral | Page background or card surface |
| Graphite | `#000000` | neutral | Primary text or dark surface |
| Ash Gray | `#c2c2c1` | neutral | Border, muted text, or supporting surface |
| Muted Steel | `#a3a3a3` | neutral | Border, muted text, or supporting surface |
| Sunset Yellow | `#f5d907` | accent | Action accent / signal color |
| Vivid Pink | `#fd429c` | brand | Action accent / signal color |
| Electric Green | `#02d95c` | accent | Action accent / signal color |

```css
:root {
  --ref-pitch-black: #101012;
  --ref-void-black: #17171a;
  --ref-ghost-white: #f7f4ef;
  --ref-pure-white: #ffffff;
  --ref-graphite: #000000;
  --ref-ash-gray: #c2c2c1;
  --ref-muted-steel: #a3a3a3;
  --ref-sunset-yellow: #f5d907;
}
```

## Typography direction
- **Neue Montreal**: 300, 400, 500, 10px, 11px, 12px, 13px, 14px, 15px, 16px, 17px, 18px, 20px, 24px, 40px, 72px, 140px, 0.87, 0.89, 1.00, 1.14, 1.20, 1.27, 1.33, 1.40, 1.41, 1.43, 1.50, 1.55, 1.60, 1.63, 1.78; substitute `Inter`.
- **Editorial New**: 300, 24px, 1.50; substitute `Playfair Display`.

## Spacing / shape
- Section Gap: `100-150px`
- Card Padding: `20px`
- Element Gap: `4-16px`
- Radius: `cards: 12px, pills: 16777200px, small: 6px, images: 12px, inputs: 12px, buttons: 6px, default: 6px`

## Surface cues
- **Page Base** `#101012`: The foundational background for the entire page, providing a deep, dark canvas.
- **Card Surface** `#17171a`: Used for card backgrounds and grouped content, visually lifting elements slightly from the base with a subtle darker tone.
- **Interactive Overlay** `#00000040`: A semi-transparent dark shade used for interactive elements like input containers, creating a sense of depth and interactivity over the base.

## Component cues
- **Music Prompt Input**: Reference component style.
- **Song Card**: Reference component style.
- **Button Group**: Reference component style.
- **Primary Ghost Button**: Action button
- **Pill Ghost Button**: Filter/Tag button

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
