# Krisp - Refero Design MD

- Source: https://styles.refero.design/style/3b3fa99e-cee4-41f3-ac26-777b4b6a8b12
- Original site: https://krisp.ai
- Theme: `light`
- Industry: `productivity`
- Recommended fit: **Admin console / run monitor / developer tooling**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Deep space command console. Information-dense, with critical functions highlighted by a bright, singular light source against a dark, expansive backdrop.

## Apply to
- Admin run monitor and review states
- Compact evidence cards and source inspection panels
- Dark-mode operational dashboards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Deep Space Indigo | `#131032` | brand | Action accent / signal color |
| Krisp Violet | `#614efa` | brand | Action accent / signal color |
| Off White Background | `#ffffff` | neutral | Page background or card surface |
| Pale Gray Surface | `#f7f7f8` | neutral | Page background or card surface |
| Subtle Accent Teal | `#eafdfa` | accent | Action accent / signal color |
| Muted Gray Text | `#918f9f` | neutral | Border, muted text, or supporting surface |
| Light Gray Border | `#e7e7ea` | neutral | Page background or card surface |
| Vivid Red Accent | `#fe6257` | semantic | Action accent / signal color |
| Crisp White Text | `#ffffff` | neutral | Page background or card surface |
| Indigo Gradient 1 | `#614efa` | brand | Action accent / signal color |

```css
:root {
  --ref-deep-space-indigo: #131032;
  --ref-krisp-violet: #614efa;
  --ref-off-white-background: #ffffff;
  --ref-pale-gray-surface: #f7f7f8;
  --ref-subtle-accent-teal: #eafdfa;
  --ref-muted-gray-text: #918f9f;
  --ref-light-gray-border: #e7e7ea;
  --ref-vivid-red-accent: #fe6257;
}
```

## Typography direction
- **Plus Jakarta Sans**: 400, 500, 600, 700, 10px, 14px, 16px, 18px, 20px, 22px, 26px, 36px, 42px, 48px, 58px, 1.14, 1.17, 1.20, 1.24, 1.25, 1.33, 1.40, 1.43, 1.45, 1.50, 1.60, 1.62, 1.63, 1.70, 1.73, 1.75, 1.78, 1.86, 1.89, 2.00, 2.63; substitute `system-ui`.

## Spacing / shape
- Section Gap: `64-80px`
- Card Padding: `24px`
- Element Gap: `8px`
- Page Max Width: `1280px`
- Radius: `pill: 9999px, cards: 16px, badges: 12px, buttons: 8px`

## Component cues
- **Tab Pill Selector + Feature Card**: Reference component style.
- **Feature Cards Grid**: Reference component style.
- **Button Group + Announcement Badge**: Reference component style.
- **Primary Action Button (Violet Filled)**: Call to action
- **Secondary Action Button (Indigo Filled)**: Secondary action

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
