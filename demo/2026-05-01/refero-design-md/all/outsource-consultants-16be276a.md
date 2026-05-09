# Outsource Consultants - Refero Design MD

- Source: https://styles.refero.design/style/16be276a-d8ce-484e-8f7a-cbbb09f717f7
- Original site: https://oci.madebybuzzworthy.com
- Theme: `light`
- Industry: `other`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Architectural Blueprint on Stark Grey

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Blueprint Violet | `#1925aa` | brand | Action accent / signal color |
| Deep Violet | `#0d1355` | brand | Action accent / signal color |
| Base Graphite | `#000000` | neutral | Primary text or dark surface |
| Blueprint Gray | `#e8e6e0` | neutral | Action accent / signal color |
| Paper White | `#ffffff` | neutral | Page background or card surface |

```css
:root {
  --ref-blueprint-violet: #1925aa;
  --ref-deep-violet: #0d1355;
  --ref-base-graphite: #000000;
  --ref-blueprint-gray: #e8e6e0;
  --ref-paper-white: #ffffff;
}
```

## Typography direction
- **PP Neue Montreal**: 400, 500, 12px, 16px, 18px, 24px, 30px, 36px, 46px, 160px, 0.94, 1.00, 1.50; substitute `system-ui`.
- **GT America Mono**: 400, 500, 10px, 12px, 14px, 1.00, 1.30, 1.33, 1.50; substitute `ui-monospace`.
- **ui-sans-serif**: 400, 16px, 1.50; substitute `system-ui`.

## Spacing / shape
- Section Gap: `40px`
- Element Gap: `10px`
- Radius: `all: 0px`

## Component cues
- **Services Accordion**: Reference component style.
- **About Stat Block**: Reference component style.
- **CTA Button Group**: Reference component style.
- **Navigation Link – Menu**: Primary navigation item
- **Primary Header Link**: Interactive menu item

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
