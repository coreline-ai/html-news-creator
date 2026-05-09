# Evervault - Refero Design MD

- Source: https://styles.refero.design/style/03dcd158-bc4d-447b-aaf2-8e522671a109
- Original site: https://evervault.com
- Theme: `dark`
- Industry: `devtools`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Digital vault in a cosmic void. Deep indigo and rich purples glow against stark black, outlining crisp content.

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Abyss | `#010314` | neutral | Primary text or dark surface |
| Astral Black | `#171825` | neutral | Primary text or dark surface |
| Stardust White | `#ffffff` | neutral | Page background or card surface |
| Nebula Gray | `#dfe1f4` | neutral | Page background or card surface |
| Dark Matter Gray | `#2a2b3a` | neutral | Primary text or dark surface |
| Whisper Gray | `#5e6077` | neutral | Border, muted text, or supporting surface |
| Astral Purple | `#6633ee` | brand | Action accent / signal color |
| Galactic Violet | `#b88cff` | brand | Action accent / signal color |
| Infra Red | `#f92672` | semantic | Action accent / signal color |
| Cosmic Gradient A | `#6633ee` | brand | Action accent / signal color |

```css
:root {
  --ref-midnight-abyss: #010314;
  --ref-astral-black: #171825;
  --ref-stardust-white: #ffffff;
  --ref-nebula-gray: #dfe1f4;
  --ref-dark-matter-gray: #2a2b3a;
  --ref-whisper-gray: #5e6077;
  --ref-astral-purple: #6633ee;
  --ref-galactic-violet: #b88cff;
}
```

## Typography direction
- **Roobert**: 400, 500, 600, 12px, 13px, 14px, 16px, 18px, 24px, 32px, 48px, 52px, 56px, 1.00, 1.13, 1.25, 1.30; substitute `system-ui`.
- **Inter**: 400, 500, 580, 11px, 12px, 13px, 14px, 15px, 16px, 1.00, 1.55, 1.75, 1.76, 1.94, 2.00; substitute `system-ui`.
- **Roboto Mono**: 400, 500, 600, 10px, 12px, 15px, 18px, 20px, 1.00, 1.21, 1.40, 1.50; substitute `monospace`.

## Spacing / shape
- Section Gap: `64px`
- Card Padding: `16px`
- Element Gap: `12px`
- Radius: `cards: 16px, badges: 8px, buttons: 24px, default: 8px`

## Component cues
- **CTA Button Group**: Reference component style.
- **Feature Product Cards**: Reference component style.
- **Developer Code Card**: Reference component style.
- **Primary Ghost Button**: Call to Action
- **Solid Button Primary**: Call to Action

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
