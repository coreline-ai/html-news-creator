# Fuser - Refero Design MD

- Source: https://styles.refero.design/style/bf5616e4-7bd1-40ce-8b2d-aae84c2e4ebd
- Original site: https://fuser.studio
- Theme: `light`
- Industry: `ai`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Frosted glass network — a cool, translucent interface connecting modular, vivid ideas.

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Stormy Night | `#0a0a0a` | neutral | Primary text or dark surface |
| Graphite | `#171717` | neutral | Primary text or dark surface |
| Deep Space Violet | `#432dd7` | brand | Action accent / signal color |
| Violet Impulse | `#312c85` | brand | Action accent / signal color |
| Sage Bloom | `#00c950` | accent | Action accent / signal color |
| Zinc | `#262626` | neutral | Primary text or dark surface |
| Ash Charcoal | `#404040` | neutral | Border, muted text, or supporting surface |
| Slate | `#525252` | neutral | Border, muted text, or supporting surface |
| Medium Gray | `#737373` | neutral | Border, muted text, or supporting surface |
| Stone | `#828282` | neutral | Border, muted text, or supporting surface |

```css
:root {
  --ref-stormy-night: #0a0a0a;
  --ref-graphite: #171717;
  --ref-deep-space-violet: #432dd7;
  --ref-violet-impulse: #312c85;
  --ref-sage-bloom: #00c950;
  --ref-zinc: #262626;
  --ref-ash-charcoal: #404040;
  --ref-slate: #525252;
}
```

## Typography direction
- **Inter Variable**: 300, 400, 500, 600, 10px, 12px, 13px, 14px, 16px, 18px, 24px, 30px, 36px, 0.80, 1.00, 1.10, 1.20, 1.25, 1.33, 1.40, 1.43, 1.50, 1.56, 1.71; substitute `Inter`.
- **Marund**: 400, 450, 500, 600, 14px, 16px, 17px, 18px, 20px, 22px, 24px, 30px, 48px, 96px, 1.00, 1.10, 1.40, 1.43, 1.50; substitute `Playfair Display`.

## Spacing / shape
- Section Gap: `32px`
- Card Padding: `12px`
- Element Gap: `16px`
- Radius: `tags: 24px, cards: 16px, images: 12px, default: 6px`

## Surface cues
- **Canvas** `#f5f5f5`: Primary page background, expansive and neutral.
- **Fog** `#e5e5e5`: Elevated surfaces like cards and content blocks, providing a subtle visual separation from the main canvas.
- **Paper White** `#fafafa`: Component backgrounds, overlays, and the brightest content containers.

## Component cues
- **Ghost Navigation Button**: Primary navigation and subtle actions
- **Small Contained Button**: Secondary calls to action, form actions
- **Outline Accent Button**: Emphasis action, 'Get Started' button
- **Prominent Text Input**: Main form fields
- **Content Card - Minimal**: Basic display of content, images, or media

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
