# Duties.xyz - Refero Design MD

- Source: https://styles.refero.design/style/e75b3106-fc5b-4bb8-8d7d-a7ab224fd27d
- Original site: https://duties.xyz
- Theme: `light`
- Industry: `other`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Raw concrete with meticulous stenciling.

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas | `#f1f0ee` | neutral | Page background or card surface |
| Inkwell | `#252525` | neutral | Primary text or dark surface |
| Pitch Black | `#000000` | neutral | Primary text or dark surface |
| Stone Wall | `#dbdad9` | neutral | Page background or card surface |
| Faded Mint | `#a7beb1` | neutral | Border, muted text, or supporting surface |
| Accent Blue | `#0000ee` | semantic | Action accent / signal color |

```css
:root {
  --ref-canvas: #f1f0ee;
  --ref-inkwell: #252525;
  --ref-pitch-black: #000000;
  --ref-stone-wall: #dbdad9;
  --ref-faded-mint: #a7beb1;
  --ref-accent-blue: #0000ee;
}
```

## Typography direction
- **AS Therma Bold Condensed**: 400, 96px, 128px, 180px, 0.80; substitute `Bebas Neue`.
- **PP Neue Montreal Mono Medium**: 400, 500, 14px, 1.00, 1.15; substitute `Space Mono`.
- **PP Neue Montreal SemiBold**: 400, 18px, 1.20; substitute `Inter`.

## Spacing / shape
- Section Gap: `40-60px`
- Card Padding: `20px`
- Radius: `small: 4px, buttons: 32px, default: 8px`

## Component cues
- **Status Bar — Duties Info Strip**: Reference component style.
- **About Section — Body + CTA Button**: Reference component style.
- **Project Card — Portfolio Item**: Reference component style.
- **Primary Action Button**: Interactive element
- **Navigation Link**: Navigation

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
