# SST - Refero Design MD

- Source: https://styles.refero.design/style/19f92be1-65ac-4432-a82b-0aa1e685d97d
- Original site: https://sst.dev
- Theme: `light`
- Industry: `devtools`
- Recommended fit: **Admin console / run monitor / developer tooling**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Config File on Paper — An architects precise blueprint on pristine white, using code as a primary visual element.

## Apply to
- Admin run monitor and review states
- Compact evidence cards and source inspection panels
- Dark-mode operational dashboards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Page White | `#ffffff` | neutral | Page background or card surface |
| Border Ash | `#e8e8f2` | neutral | Page background or card surface |
| Text Graphite | `#403f53` | neutral | Border, muted text, or supporting surface |
| Text Slate | `#767682` | neutral | Border, muted text, or supporting surface |
| Text Fog | `#a8a8b0` | neutral | Border, muted text, or supporting surface |
| Text Jet | `#111111` | neutral | Primary text or dark surface |
| Primary Violet | `#303055` | brand | Action accent / signal color |
| Code Rose | `#984e4d` | accent | Action accent / signal color |
| Code Magenta | `#8844ae` | accent | Action accent / signal color |
| Code Sky | `#5196b3` | accent | Action accent / signal color |

```css
:root {
  --ref-page-white: #ffffff;
  --ref-border-ash: #e8e8f2;
  --ref-text-graphite: #403f53;
  --ref-text-slate: #767682;
  --ref-text-fog: #a8a8b0;
  --ref-text-jet: #111111;
  --ref-primary-violet: #303055;
  --ref-code-rose: #984e4d;
}
```

## Typography direction
- **IBM Plex Mono**: 400, 600, 14px, 16px, 18px, 48px, 1.00, 1.10, 1.80; substitute `monospace`.
- **Rubik Variable**: 400, 500, 600, 12px, 13px, 14px, 16px, 18px, 20px, 1.00, 1.20, 1.50, 1.65, 1.78, 1.80; substitute `sans-serif`.

## Spacing / shape
- Section Gap: `64px`
- Element Gap: `3-16px`
- Radius: `cards: 8px, buttons: 4px, default: 4px`

## Component cues
- **Code Editor Card**: Reference component style.
- **npm Install CTA with Badge**: Reference component style.
- **Nav Button Group**: Reference component style.
- **Primary Heading**: Hero section titles
- **Nav Button Default**: Secondary navigation and utility buttons

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
