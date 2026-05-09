# Hugging Face - Refero Design MD

- Source: https://styles.refero.design/style/4363070d-02da-4954-88e4-d4a2101c5204
- Original site: https://huggingface.co
- Theme: `light`
- Industry: `ai`
- Recommended fit: **Source ledger / evidence dashboard**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
High-contrast data console. A brightly lit control panel with precise readouts and subtle depth.

## Apply to
- Source ledger, ranking, and verification screens
- Cluster evidence dashboards
- Dense data tables with clear hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Fog Gray | `#e5e7eb` | neutral | Page background or card surface |
| Ash Gray | `#f3f4f6` | neutral | Page background or card surface |
| Jet Black | `#000000` | neutral | Primary text or dark surface |
| Carbon | `#101828` | neutral | Primary text or dark surface |
| Slate Blue | `#4a5565` | neutral | Action accent / signal color |
| Azure Link | `#155dfc` | accent | Action accent / signal color |
| Crimson Accent | `#ff3939` | semantic | Action accent / signal color |
| Electric Blue | `#2b7fff` | semantic | Action accent / signal color |
| Sunset Orange | `#ff6900` | accent | Action accent / signal color |

```css
:root {
  --ref-canvas-white: #ffffff;
  --ref-fog-gray: #e5e7eb;
  --ref-ash-gray: #f3f4f6;
  --ref-jet-black: #000000;
  --ref-carbon: #101828;
  --ref-slate-blue: #4a5565;
  --ref-azure-link: #155dfc;
  --ref-crimson-accent: #ff3939;
}
```

## Typography direction
- **Source Sans Pro**: 400, 600, 700, 10px, 12px, 13px, 14px, 15px, 16px, 18px, 20px, 24px, 30px, 48px, 60px, 96px, 1.00, 1.20, 1.25, 1.33, 1.37, 1.40, 1.43, 1.50, 1.56; substitute `Open Sans, Lato`.
- **IBM Plex Mono**: 400, 15px, 1.60; substitute `Space Mono, Fira Code`.

## Spacing / shape
- Section Gap: `64px`
- Card Padding: `16px`
- Element Gap: `8px`
- Page Max Width: `1280px`
- Radius: `cards: 8px, inputs: 8px, buttons: 8px, 25.6px, default: 8px`

## Component cues
- **Trending Models & Spaces Cards**: Reference component style.
- **Spaces Cards — Colorful Gradient Cards**: Reference component style.
- **Search Bar + Filter Tab Bar**: Reference component style.
- **Primary Button - Dark**: Call to action
- **Secondary Button - Ghost**: Secondary action

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
