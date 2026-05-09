# Slab - Refero Design MD

- Source: https://styles.refero.design/style/f240ed7d-d466-478e-bbce-6c93420dfd1c
- Original site: https://slab.com
- Theme: `mixed`
- Industry: `productivity`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Warm knowledge hub behind a berry curtain. The UI feels like an organized library where key information is highlighted by vibrant accents.

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Slab Red | `#ff4143` | brand | Action accent / signal color |
| Slab Blue | `#4285f4` | brand | Action accent / signal color |
| Muted Cyan | `#00d5a0` | accent | Action accent / signal color |
| Muted Violet | `#253858` | accent | Action accent / signal color |
| Vivid Blue | `#0061ff` | accent | Action accent / signal color |
| Sky Blue | `#50c5dc` | accent | Action accent / signal color |
| Crisp White | `#ffffff` | neutral | Page background or card surface |
| Near Black | `#000000` | neutral | Primary text or dark surface |
| Slate Gray | `#455360` | neutral | Border, muted text, or supporting surface |
| Ash Gray | `#939598` | neutral | Border, muted text, or supporting surface |

```css
:root {
  --ref-slab-red: #ff4143;
  --ref-slab-blue: #4285f4;
  --ref-muted-cyan: #00d5a0;
  --ref-muted-violet: #253858;
  --ref-vivid-blue: #0061ff;
  --ref-sky-blue: #50c5dc;
  --ref-crisp-white: #ffffff;
  --ref-near-black: #000000;
}
```

## Typography direction
- **Whitney**: 400, 500, 600, 700, 12px, 16px, 18px, 20px, 24px, 1.15, 1.20, 1.33, 1.50, 1.60, 1.67, 1.75; substitute `Inter`.
- **Sentinel**: 300, 400, 16px, 42px, 53px, 1.00, 1.14, 1.24; substitute `Merriweather`.

## Spacing / shape
- Section Gap: `40-64px`
- Card Padding: `24-40px`
- Element Gap: `8-24px`
- Radius: `cards: 6px, inputs: 6px, buttons: 6px`

## Component cues
- **Sign-up Form Block**: Reference component style.
- **Feature Section — Create**: Reference component style.
- **Organize Feature Card**: Reference component style.
- **Primary Action Button**: Call to action
- **Google Sign-up Button**: Social login

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
