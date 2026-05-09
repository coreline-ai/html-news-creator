# Qatchup - Refero Design MD

- Source: https://styles.refero.design/style/1b010453-80df-406a-8b1a-72630c4a5165
- Original site: https://www.qatchup.com
- Theme: `light`
- Industry: `productivity`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Whiteboard doodle transparency.

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#fafafa` | neutral | Page background or card surface |
| Absolute Zero | `#292929` | neutral | Primary text or dark surface |
| Graphite | `#696969` | neutral | Border, muted text, or supporting surface |
| Ink Black | `#080808` | neutral | Primary text or dark surface |
| Cloud White | `#f4f4f5` | neutral | Page background or card surface |
| Silver Mist | `#cccccc` | neutral | Border, muted text, or supporting surface |
| Cool Gray | `#e4e4e7` | neutral | Page background or card surface |
| Light Steel | `#b2b2b2` | neutral | Border, muted text, or supporting surface |
| Stone Gray | `#999999` | neutral | Border, muted text, or supporting surface |
| Deep Gray | `#222222` | neutral | Primary text or dark surface |

```css
:root {
  --ref-canvas-white: #fafafa;
  --ref-absolute-zero: #292929;
  --ref-graphite: #696969;
  --ref-ink-black: #080808;
  --ref-cloud-white: #f4f4f5;
  --ref-silver-mist: #cccccc;
  --ref-cool-gray: #e4e4e7;
  --ref-light-steel: #b2b2b2;
}
```

## Typography direction
- **Aspekta**: 400, 500, 12px, 14px, 16px, 18px, 20px, 24px, 32px, 40px, 48px, 56px, 1.14, 1.17, 1.20, 1.25, 1.33, 1.38, 1.40, 1.43, 1.50, 1.56, 2.00; substitute `Inter`.
- **Fasthand**: 400, 32px, 1.38; substitute `Kalam`.
- **Aspekta 500**: 400, 16px, 1.5.

## Spacing / shape
- Section Gap: `64px`
- Card Padding: `24px`
- Element Gap: `10px`
- Radius: `tags: 999px, cards: 32px, images: 16px, buttons: 100px`

## Surface cues
- **Canvas White** `#fafafa`: Primary page background and base layer for all content.
- **Cloud White** `#f4f4f5`: Slightly off-white for subtle background variations or ghost button states, creating minimal depth.
- **Absolute Zero** `#292929`: Darkest background for content blocks requiring high contrast or visual weight, often in monochromatic sections.

## Component cues
- **Primary Filled Button**: Key interactions and calls to action.
- **Ghost Button**: Secondary actions or navigation items.
- **Disabled Button**: Non-interactive elements indicating future availability.
- **Elevated Content Card**: Displaying key information with subtle separation from the background.
- **Section Divider Card**: Visually distinct blocks within a section, often serving as backgrounds for content groupings.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
