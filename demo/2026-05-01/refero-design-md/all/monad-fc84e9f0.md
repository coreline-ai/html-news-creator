# Monad - Refero Design MD

- Source: https://styles.refero.design/style/fc84e9f0-2058-4a0a-8d26-9cc1ba84ec9c
- Original site: https://www.monad.com
- Theme: `light`
- Industry: `ai`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Softly lit control panel

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Ink | `#000000` | neutral | Primary text or dark surface |
| Paper Canvas | `#f6f3f1` | neutral | Page background or card surface |
| Off-Black | `#242424` | neutral | Primary text or dark surface |
| Pale Stone | `#4e4d4d` | neutral | Border, muted text, or supporting surface |
| Whisper Gray | `#3d3d3d` | neutral | Primary text or dark surface |
| Atmosphere Wash | `#cfdaf5` | accent | Action accent / signal color |
| Subtle Link | `#333333` | neutral | Primary text or dark surface |
| Faint Text | `#797776` | neutral | Border, muted text, or supporting surface |
| Sunset Violet gradient | `#ffa773` | accent | Action accent / signal color |
| Sky Mint Gradient | `#a0b5eb` | accent | Action accent / signal color |

```css
:root {
  --ref-ink: #000000;
  --ref-paper-canvas: #f6f3f1;
  --ref-off-black: #242424;
  --ref-pale-stone: #4e4d4d;
  --ref-whisper-gray: #3d3d3d;
  --ref-atmosphere-wash: #cfdaf5;
  --ref-subtle-link: #333333;
  --ref-faint-text: #797776;
}
```

## Typography direction
- **ABC Diatype Mono**: 400, 500, 12px, 14px, 16px, 18px, 20px, 28px, 1.00, 1.20, 1.30, 1.35; substitute `IBM Plex Mono`.
- **Untitled Serif**: 400, 24px, 28px, 32px, 40px, 80px, 1.20; substitute `Noto Serif`.
- **Untitled Sans**: 400, 16px, 1.35; substitute `Inter`.

## Spacing / shape
- Section Gap: `40px`
- Card Padding: `40px`
- Element Gap: `16px`
- Page Max Width: `1432px`
- Radius: `tags: 2000px, cards: 40px, other: 100px, buttons: 100px`

## Surface cues
- **Paper Canvas** `#f6f3f1`: Base page background
- **Atmosphere Wash** `#cfdaf5`: Elevated card and section backgrounds
- **Off-Black** `#242424`: Primary filled button backgrounds, dark UI elements
- **Ink** `#000000`: Top-level notification bar, highest contrast elements

## Component cues
- **Primary Filled Button**: Call-to-action button for initiating primary actions.
- **Secondary Ghost Button**: Call-to-action button for secondary actions.
- **Inline Text Link**: Navigational or contextual links within body text.
- **Hero Headline**: Prominent display text for main page sections.
- **Feature Card**: Container for showcasing features or information blocks.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
