# Ko-fi - Refero Design MD

- Source: https://styles.refero.design/style/35ae81e1-273c-43d7-9bcd-ea186d062c13
- Original site: https://ko-fi.com
- Theme: `light`
- Industry: `other`
- Recommended fit: **Design reference / webapp exploration**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Warm, creative craft studio

## Apply to
- General webapp UI exploration
- Demo cards and catalog surfaces
- Future admin/subscriber UI references

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas Oat | `#e9dfd2` | neutral | Page background or card surface |
| Background Paper | `#ffffff` | neutral | Page background or card surface |
| Text Ink | `#202020` | neutral | Primary text or dark surface |
| Border Stone | `#e5e7eb` | neutral | Page background or card surface |
| Outline Ebony | `#000000` | neutral | Primary text or dark surface |
| Action Sky | `#72a4f2` | accent | Action accent / signal color |
| Footer Slate | `#aac9f7` | neutral | Border, muted text, or supporting surface |
| Icon Ember | `#ff5a16` | brand | Action accent / signal color |

```css
:root {
  --ref-canvas-oat: #e9dfd2;
  --ref-background-paper: #ffffff;
  --ref-text-ink: #202020;
  --ref-border-stone: #e5e7eb;
  --ref-outline-ebony: #000000;
  --ref-action-sky: #72a4f2;
  --ref-footer-slate: #aac9f7;
  --ref-icon-ember: #ff5a16;
}
```

## Typography direction
- **DM Sans**: 400, 600, 14px, 16px, 20px, 24px, 30px, 1.20, 1.33, 1.40, 1.43, 1.50.
- **bogue-black**: 400, 60px, 72px, 1.00; substitute `Bungee Outline (for a similar chunky, playful feel without the specific outlined characters) or maybe Public Sans Black (for a broad bold feel)`.
- **Font Awesome 6 Pro**: 900, 20px, 1.

## Spacing / shape
- Section Gap: `40px`
- Card Padding: `20px`
- Element Gap: `20px`
- Radius: `tags: 9999px, cards: 40px, images: 40px, inputs: 9999px, buttons: 9999px, components: 24px`

## Surface cues
- **Canvas Oat** `#e9dfd2`: Base page background
- **Background Paper** `#ffffff`: Primary content cards and elevated UI elements

## Component cues
- **Primary Filled Button**: Call to action button
- **Secondary Neutral Button**: Secondary action or categorized filters
- **Dark Icon Button**: Navigation or less prominent actions
- **Hero Content Card**: Prominent information display
- **Feature Image Card**: Visual grid elements

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
