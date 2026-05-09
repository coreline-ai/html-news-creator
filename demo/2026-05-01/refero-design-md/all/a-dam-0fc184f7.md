# A-dam - Refero Design MD

- Source: https://styles.refero.design/style/0fc184f7-6143-4303-8e3d-0e2f075f76b2
- Original site: https://a-dam.com
- Theme: `light`
- Industry: `ecommerce`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Electric blue minimalist playground

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Ink | `#000e1f` | neutral | Primary text or dark surface |
| Ocean Blue | `#0000c5` | brand | Action accent / signal color |
| Polar White | `#ffffff` | neutral | Page background or card surface |
| Sky Blue | `#1a1acb` | brand | Action accent / signal color |
| Slate Border | `#1a2635` | neutral | Primary text or dark surface |
| Light Mist | `#e6e7e9` | neutral | Page background or card surface |
| Subtle Gray | `#dcdddf` | neutral | Page background or card surface |
| Off-White Canvas | `#f4f4f4` | neutral | Page background or card surface |
| Midtone Gray | `#666e79` | neutral | Border, muted text, or supporting surface |

```css
:root {
  --ref-midnight-ink: #000e1f;
  --ref-ocean-blue: #0000c5;
  --ref-polar-white: #ffffff;
  --ref-sky-blue: #1a1acb;
  --ref-slate-border: #1a2635;
  --ref-light-mist: #e6e7e9;
  --ref-subtle-gray: #dcdddf;
  --ref-off-white-canvas: #f4f4f4;
}
```

## Typography direction
- **GT Walsheim Pro**: 400, 500, 700, 900, 11px, 12px, 13px, 15px, 16px, 20px, 26px, 30px, 38px, 44px, 70px, 1.00, 1.10, 1.20, 1.40; substitute `system-ui, sans-serif`.
- **sans-serif**: 400, 700, 16px, 1.2.
- **Arial**: 400, 13px, 1.4.

## Spacing / shape
- Section Gap: `48px`
- Card Padding: `16px`
- Element Gap: `10px`
- Page Max Width: `1200px`
- Radius: `badges: 0px, inputs: 30px 0px 0px 30px, buttons: 30px`

## Component cues
- **Ghost Button**: Navigation links and subtle actions
- **Outline Pill Button**: Primary Call to Action
- **Product Card**: Displaying product items
- **Search Input Field**: User input for search
- **Badge (Neutral Text)**: Informational labels

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
