# Art In DUMBO - Refero Design MD

- Source: https://styles.refero.design/style/5d79f0c2-526e-4c37-b780-08404f60839b
- Original site: https://artindumbo.com
- Theme: `light`
- Industry: `media`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Gallery Guidebook

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Inkwell | `#000000` | neutral | Primary text or dark surface |
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Fog | `#e5e3df` | neutral | Page background or card surface |
| Whisper Gray | `#f1f2f2` | neutral | Page background or card surface |
| Driftwood | `#bdbdbd` | neutral | Border, muted text, or supporting surface |
| Charcoal Accent | `#828282` | neutral | Border, muted text, or supporting surface |
| Shadow Tint | `#b3b3b3` | neutral | Border, muted text, or supporting surface |
| Gallery Orange | `#ff7f41` | accent | Action accent / signal color |
| Beacon Green | `#71cc98` | brand | Action accent / signal color |

```css
:root {
  --ref-inkwell: #000000;
  --ref-canvas-white: #ffffff;
  --ref-fog: #e5e3df;
  --ref-whisper-gray: #f1f2f2;
  --ref-driftwood: #bdbdbd;
  --ref-charcoal-accent: #828282;
  --ref-shadow-tint: #b3b3b3;
  --ref-gallery-orange: #ff7f41;
}
```

## Typography direction
- **Helvetica N**: 500, 10px, 11px, 16px, 19px, 22px, 27px, 28px, 30px, 34px, 37px, 44px, 63px, 68px, 1.00, 1.05, 1.08, 1.09, 1.10, 1.15, 1.20, 1.27, 1.40, 1.50, 1.80; substitute `Arial, Helvetica, sans-serif`.
- **Roboto**: 400, 500, 10px, 11px, 1.20, 1.40; substitute `system-ui, sans-serif`.

## Spacing / shape
- Section Gap: `144px`
- Card Padding: `20px`
- Element Gap: `20px`
- Radius: `pill: 50px, inputs: 2px, buttons: 2px, default: 2px`

## Surface cues
- **Canvas White** `#ffffff`: Base page background and default card surfaces.
- **Whisper Gray** `#f1f2f2`: Subtle input backgrounds and secondary content blocks.
- **Fog** `#e5e3df`: Large, alternate section backgrounds to break visual monotony.

## Component cues
- **Ghost Text Button**: Interactive text links and navigation items that visually blend into the background.
- **Clear Text Button**: Interactive elements on Canvas White backgrounds that maintain a text-only appearance.
- **Circular Utility Button**: Small, functional buttons often used for icons or minimal controls.
- **Beacon Green Button**: Primary action button, visually prominent and signaling an important interaction.
- **Content Card**: Container for event listings or feature sections, visually defined by content rather than a strong border/shadow.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
