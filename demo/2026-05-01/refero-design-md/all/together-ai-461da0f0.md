# Together AI - Refero Design MD

- Source: https://styles.refero.design/style/461da0f0-fde6-46bc-8137-7eca006260a8
- Original site: https://together.ai
- Theme: `mixed`
- Industry: `ai`
- Recommended fit: **Source ledger / evidence dashboard**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Shifting geometric planes under a deep indigo sky. Bold textual headlines punctuate against a canvas of near-black and clinical white, punctuated by soft, almost pastel blocks of color.

## Apply to
- Source ledger, ranking, and verification screens
- Cluster evidence dashboards
- Dense data tables with clear hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Ink | `#010120` | brand | Action accent / signal color |
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Void Black | `#000000` | neutral | Primary text or dark surface |
| Smoke Gray | `#4d4d4d` | neutral | Border, muted text, or supporting surface |
| Frost Gray | `#d6d6d6` | neutral | Border, muted text, or supporting surface |
| Sky Blue Block | `#c1dff9` | accent | Action accent / signal color |
| Cosmic Pink Block | `#fde3f6` | accent | Action accent / signal color |
| Dawn Orange Block | `#ffdccd` | accent | Action accent / signal color |
| Cyan Whisper | `#c8f6f9` | accent | Action accent / signal color |
| Regal Violet | `#bdbbff` | accent | Action accent / signal color |

```css
:root {
  --ref-midnight-ink: #010120;
  --ref-canvas-white: #ffffff;
  --ref-void-black: #000000;
  --ref-smoke-gray: #4d4d4d;
  --ref-frost-gray: #d6d6d6;
  --ref-sky-blue-block: #c1dff9;
  --ref-cosmic-pink-block: #fde3f6;
  --ref-dawn-orange-block: #ffdccd;
}
```

## Typography direction
- **The Future**: 400, 500, 14px, 16px, 18px, 22px, 28px, 40px, 64px, 1.00, 1.10, 1.15, 1.20, 1.25, 1.30, 1.40; substitute `Montserrat, Inter`.
- **PP Neue Montreal Mono**: 400, 500, 10px, 11px, 13px, 16px, 1.00, 1.40; substitute `IBM Plex Mono, Space Mono`.

## Spacing / shape
- Radius: `large: 16px, medium: 8px, default: 4px`

## Surface cues
- **Deep Space BG** `#010120`: Primary dark page background, foundational layer for deep sections.
- **Subtle Dark Card** `#ffffff14`: Lightly elevated cards or content blocks on dark backgrounds, providing minimal visual separation.
- **Frosted Nav** `#ffffff14`: Navigation bar background, featuring a backdrop blur to create a 'frosted glass' effect over content below.

## Component cues
- **Stat Metric Cards**: Reference component style.
- **Research Cards (Dark)**: Reference component style.
- **Button Group & Announcement Banner**: Reference component style.
- **Primary Dark Button**: Call to Action
- **Secondary Ghost Button**: Secondary Action

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
