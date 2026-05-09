# Vizcom - Refero Design MD

- Source: https://styles.refero.design/style/d16b85ee-0bbc-4030-9190-71e1408ff119
- Original site: https://vizcom.com
- Theme: `dark`
- Industry: `ai`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
digital workbench, blueprint sketch

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Ink Black | `#191919` | neutral | Primary text or dark surface |
| Canvas White | `#f8f4f1` | neutral | Page background or card surface |
| Blueprint Navy | `#1145a0` | brand | Action accent / signal color |
| Input Blue | `#4c4cef` | semantic | Action accent / signal color |
| Ideation Blue | `#4586da` | brand | Action accent / signal color |
| Paper Grey | `#e8e3dd` | neutral | Page background or card surface |
| Dots Black | `#242425` | neutral | Primary text or dark surface |
| Deep Space | `#131313` | neutral | Primary text or dark surface |
| Slate Border | `#3c3c3e` | neutral | Primary text or dark surface |
| Faded Grey | `#5c5b5a` | neutral | Border, muted text, or supporting surface |

```css
:root {
  --ref-ink-black: #191919;
  --ref-canvas-white: #f8f4f1;
  --ref-blueprint-navy: #1145a0;
  --ref-input-blue: #4c4cef;
  --ref-ideation-blue: #4586da;
  --ref-paper-grey: #e8e3dd;
  --ref-dots-black: #242425;
  --ref-deep-space: #131313;
}
```

## Typography direction
- **Matter**: 400, 500, 12px, 14px, 16px, 18px, 20px, 24px, 56px, 88px, 265px, 1.00, 1.10, 1.20, 1.30, 1.40, 1.43; substitute `Inter`.
- **Tomboy LP**: 700, 56px, 265px, 1.10, 1.20; substitute `Montserrat Alternates`.

## Spacing / shape
- Section Gap: `90px`
- Card Padding: `12px`
- Element Gap: `8px`
- Radius: `pill: 1440px, tags: 8px, cards: 12px, buttons: 8px, default: 8px`

## Surface cues
- **Deep Space** `#131313`: Base canvas for the deepest background layers and primary page container.
- **Ink Black** `#191919`: Primary background for main content areas, providing a dark, immersive foundation.
- **Dots Black** `#242425`: Background for standard cards and major content blocks, creating the first layer of subtle elevation.
- **Dark Card** `#2f2f31`: Background for elevated cards, badges, and focused panels, providing a slightly lighter surface for higher hierarchy.

## Component cues
- **Primary Action Button**: Call-to-action
- **Ghost Button**: Secondary action or navigation
- **Pill Button**: Tertiary action or filter
- **Standard Card**: Content container
- **Padded Card**: Content container with integrated spacing

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
