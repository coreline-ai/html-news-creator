# Craftwork - Refero Design MD

- Source: https://styles.refero.design/style/47c9e353-bed3-4d6c-8316-63a2db5cc377
- Original site: https://craftwork.design
- Theme: `light`
- Industry: `agency`
- Recommended fit: **Research brief / AI trend page**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Crisp paper on a clean desk. A light, airy workspace where bold black text and electric lime accents pop against pristine whites and soft grays, creating an impression of organized creativity.

## Apply to
- Research section pages and model-release briefs
- Lab-note style cards
- AI product/research trend summaries

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Pitch Black | `#000000` | neutral | Primary text or dark surface |
| Cloud White | `#ffffff` | neutral | Page background or card surface |
| Slate Gray | `#606060` | neutral | Border, muted text, or supporting surface |
| Ash Gray | `#999999` | neutral | Border, muted text, or supporting surface |
| Whisper Gray | `#f9f9f9` | neutral | Page background or card surface |
| Smoke Gray | `#f2f2f2` | neutral | Page background or card surface |
| Silver Mist | `#dee0e3` | neutral | Page background or card surface |
| Electric Lime | `#cafc00` | brand | Action accent / signal color |
| Fuchsia Burst | `#df04e3` | accent | Action accent / signal color |
| Violet Splash | `#c42df9` | accent | Action accent / signal color |

```css
:root {
  --ref-pitch-black: #000000;
  --ref-cloud-white: #ffffff;
  --ref-slate-gray: #606060;
  --ref-ash-gray: #999999;
  --ref-whisper-gray: #f9f9f9;
  --ref-smoke-gray: #f2f2f2;
  --ref-silver-mist: #dee0e3;
  --ref-electric-lime: #cafc00;
}
```

## Typography direction
- **Euclid Circular A**: 400, 500, 600, 700, 11px, 12px, 14px, 15px, 16px, 18px, 20px, 22px, 24px, 32px, 36px, 42px, 62px, 72px, 1.00, 1.06, 1.10, 1.13, 1.14, 1.17, 1.22, 1.27, 1.30, 1.33, 1.38, 1.43, 1.44, 1.45, 1.50, 1.83; substitute `Inter`.

## Spacing / shape
- Section Gap: `64px`
- Card Padding: `14px`
- Element Gap: `4px`
- Radius: `cards: 10px, 33px, 9999px, inputs: 0px, buttons: 10px, 9999px`

## Component cues
- **CTA Button Group**: Reference component style.
- **Filter Pill Tags**: Reference component style.
- **Testimonial Cards**: Reference component style.
- **Primary Navigation Link**: Navigational elements in the top bar.
- **Tertiary Ghost Button**: Subtle action buttons, often alongside primary actions.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
