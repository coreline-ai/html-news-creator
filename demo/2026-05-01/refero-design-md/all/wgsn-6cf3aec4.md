# WGSN - Refero Design MD

- Source: https://styles.refero.design/style/6cf3aec4-d028-44b0-b634-cc93e6c08e3c
- Original site: https://www.wgsn.com/en
- Theme: `light`
- Industry: `other`
- Recommended fit: **Design reference / webapp exploration**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
High-contrast monochrome canvas.

## Apply to
- General webapp UI exploration
- Demo cards and catalog surfaces
- Future admin/subscriber UI references

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Ink Black | `#000000` | neutral | Primary text or dark surface |
| Graphite | `#333333` | neutral | Primary text or dark surface |
| Steel Gray | `#666666` | neutral | Border, muted text, or supporting surface |
| Ash Gray | `#999999` | neutral | Border, muted text, or supporting surface |
| Fog Gray | `#f5f5f5` | neutral | Page background or card surface |
| Divider Gray | `#cccccc` | neutral | Border, muted text, or supporting surface |
| Input Text Gray | `#495057` | neutral | Border, muted text, or supporting surface |
| Button Solid Black | `#212121` | neutral | Primary text or dark surface |

```css
:root {
  --ref-canvas-white: #ffffff;
  --ref-ink-black: #000000;
  --ref-graphite: #333333;
  --ref-steel-gray: #666666;
  --ref-ash-gray: #999999;
  --ref-fog-gray: #f5f5f5;
  --ref-divider-gray: #cccccc;
  --ref-input-text-gray: #495057;
}
```

## Typography direction
- **DM Sans**: 400, 500, 600, 700, 12px, 13px, 14px, 16px, 17px, 18px, 20px, 24px, 28px, 32px, 36px, 40px, 48px, 92px, 0.79, 1.10, 1.17, 1.18, 1.20, 1.33, 1.50, 1.60, 1.90; substitute `system-ui`.

## Spacing / shape
- Section Gap: `32px`
- Card Padding: `24px`
- Element Gap: `18px`
- Page Max Width: `1370px`
- Radius: `cards: 16px, inputs: 8px, buttons: 40px`

## Surface cues
- **Canvas White** `#ffffff`: Primary page background, base for content.
- **Fog Gray** `#f5f5f5`: Secondary background for cards and input fields, providing slight visual depth without shadows.
- **Ink Black** `#000000`: Hero sections, footers or prominent callout blocks, acting as a high-contrast anchor.

## Component cues
- **Primary Filled Button**: Call-to-action button for initiating key actions.
- **Outlined Light Button**: Secondary action button on dark backgrounds.
- **Outlined Dark Button**: Secondary action button on light backgrounds.
- **Standard Card**: Container for content sections, often with imagery.
- **Feature Card**: Prominent content card, often with an associated image.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
