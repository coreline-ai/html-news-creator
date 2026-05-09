# Nakedcityfilms - Refero Design MD

- Source: https://styles.refero.design/style/b7fc2173-c9b1-45ed-bd3a-9999320b3248
- Original site: https://www.nakedcityfilms.com
- Theme: `mixed`
- Industry: `media`
- Recommended fit: **Research brief / AI trend page**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Electric-Blue Street Art. Graffiti against a raw concrete wall, stark and direct.

## Apply to
- Research section pages and model-release briefs
- Lab-note style cards
- AI product/research trend summaries

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Electric Blue | `#0004eb` | brand | Action accent / signal color |
| Midnight Ink | `#050516` | neutral | Primary text or dark surface |
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Pallid Gray | `#e6e6e6` | neutral | Page background or card surface |
| Ash Dust | `#979797` | neutral | Border, muted text, or supporting surface |

```css
:root {
  --ref-electric-blue: #0004eb;
  --ref-midnight-ink: #050516;
  --ref-canvas-white: #ffffff;
  --ref-pallid-gray: #e6e6e6;
  --ref-ash-dust: #979797;
}
```

## Typography direction
- **Haas Grotesk Medium**: 100, 500, 12px, 13px, 16px, 18px, 26px, 44px, 68px, 1.00, 1.10, 1.11, 1.20, 1.67, 2.31; substitute `Inter`.
- **TRJNDaVinci Medium Trial Italic**: 500, 26px, 44px, 68px, 1.10, 1.20; substitute `Georgia Italic`.

## Spacing / shape
- Section Gap: `40px`
- Card Padding: `20px`
- Element Gap: `12px`

## Component cues
- **Scroll Indicator Bar**: Reference component style.
- **Feature Link Block — Studio Work Cards**: Reference component style.
- **About Section — Display Headline Block**: Reference component style.
- **Primary Navigation Link**: Interactive menu item
- **Hero Section Overlay Card**: Central content display on hero

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
