# Legora - Refero Design MD

- Source: https://styles.refero.design/style/f89bad29-019a-48d7-9724-c40a0d7d8171
- Original site: https://legora.com
- Theme: `light`
- Industry: `ai`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Warm monochrome legal canvas

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Inkwell Black | `#000000` | neutral | Primary text or dark surface |
| Canvas White | `#fefefc` | neutral | Page background or card surface |
| Text Gray | `#0a0a0a` | neutral | Primary text or dark surface |
| Pale Ash | `#ebf5ed` | neutral | Page background or card surface |
| Shadowstone Gray | `#6b6b6b` | neutral | Border, muted text, or supporting surface |
| Whisper Gray | `#444444` | neutral | Border, muted text, or supporting surface |
| Parchment Tan | `#e1d5b6` | accent | Action accent / signal color |
| Sky Tint | `#bdd4f0` | accent | Action accent / signal color |
| Steel Blue | `#98a7aa` | accent | Action accent / signal color |

```css
:root {
  --ref-inkwell-black: #000000;
  --ref-canvas-white: #fefefc;
  --ref-text-gray: #0a0a0a;
  --ref-pale-ash: #ebf5ed;
  --ref-shadowstone-gray: #6b6b6b;
  --ref-whisper-gray: #444444;
  --ref-parchment-tan: #e1d5b6;
  --ref-sky-tint: #bdd4f0;
}
```

## Typography direction
- **sans-serif**: 400, 12px, 1.20; substitute `Arial, Helvetica`.
- **Suisse Intl Book**: 450, 11px, 13px, 14px, 16px, 0.80, 1.25, 1.30; substitute `Inter`.
- **Aktiv Grotesk VF Variable Regular**: 400, 15px, 20px, 1.30; substitute `Inter`.

## Spacing / shape
- Section Gap: `80px`
- Card Padding: `16px`
- Element Gap: `10px`
- Radius: `cards: 8px, images: 8px, inputs: 8px, buttons: 2px, cookieConsent: 4px`

## Surface cues
- **Canvas White** `#fefefc`: Primary page background and default light surface.
- **Pale Ash** `#ebf5ed`: Subtle elevated surface for input fields and alternating content blocks.
- **Parchment Tan** `#e1d5b6`: Accent background for specific content sections, providing a warm, slightly higher-level background.

## Component cues
- **Ghost Navigation Link**: Primary navigation item
- **Filled Action Button**: Call to action button
- **Outlined Cookie Consent Button**: Secondary action in cookie consent
- **Text Input Field**: User input control
- **Cookie Consent Banner**: Legal disclosure pop-up

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
