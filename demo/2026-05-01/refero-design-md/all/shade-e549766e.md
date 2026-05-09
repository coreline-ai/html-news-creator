# Shade - Refero Design MD

- Source: https://styles.refero.design/style/e549766e-b8b1-48a2-bd72-8cc04e9e4e9d
- Original site: https://shade.inc
- Theme: `light`
- Industry: `media`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
High-contrast utility with violet accent. A clean white canvas underpins sharp black text and functional components, highlighted by a single, vivid violet.

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Midnight Ink | `#000000` | neutral | Primary text or dark surface |
| Coal Black | `#131315` | neutral | Primary text or dark surface |
| Light Fog | `#f1f1f1` | neutral | Page background or card surface |
| Steel Gray | `#717173` | neutral | Border, muted text, or supporting surface |
| Stone Gray | `#a0a0a0` | neutral | Border, muted text, or supporting surface |
| Warm Gray | `#d0d0d0` | neutral | Border, muted text, or supporting surface |
| Deep Gray | `#444444` | neutral | Border, muted text, or supporting surface |
| Dark Gray | `#333333` | neutral | Primary text or dark surface |
| Digital Violet Light | `#dacefd` | accent | Action accent / signal color |

```css
:root {
  --ref-canvas-white: #ffffff;
  --ref-midnight-ink: #000000;
  --ref-coal-black: #131315;
  --ref-light-fog: #f1f1f1;
  --ref-steel-gray: #717173;
  --ref-stone-gray: #a0a0a0;
  --ref-warm-gray: #d0d0d0;
  --ref-deep-gray: #444444;
}
```

## Typography direction
- **Inter Display**: 400, 10px, 14px, 16px, 18px, 20px, 21px, 24px, 28px, 32px, 36px, 40px, 48px, 56px, 72px, 1.00, 1.10, 1.15, 1.20, 1.22, 1.25, 1.30, 1.40, 1.43, 1.57.
- **sans-serif**: 400, 12px, 1.20.
- **Aux Mono Regular**: 400, 14px, 1.00, 1.29.

## Spacing / shape
- Section Gap: `100px`
- Card Padding: `20px`
- Element Gap: `10px`
- Radius: `cards: 14px, input: 9px, buttons: 20px, default: 9px, largeButtons: 35px`

## Surface cues
- **Canvas White** `#ffffff`: Base page background and high-contrast surfaces.
- **Light Fog** `#f1f1f1`: Subtle background for grouped UI elements or light separators.
- **Default Card** `#ffffff`: Default card background, distinguished by its subtle inset border shadow.
- **Coal Black Elevated** `#131315`: Darker background for primary filled buttons and specific elevated UI sections.

## Component cues
- **Primary Filled Button**: Main call-to-action button for initiating key flows.
- **Secondary Outlined Button**: Secondary call-to-action, less prominent than the filled primary.
- **Ghost Accent Button**: Minimal impact button, often for navigation or secondary actions, using brand accent.
- **Ghost Neutral Button**: Minimal impact button, for subtle interactive elements or navigation.
- **Search/Navigation Tab**: Interactive tabs for filtering or navigating content sections.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
