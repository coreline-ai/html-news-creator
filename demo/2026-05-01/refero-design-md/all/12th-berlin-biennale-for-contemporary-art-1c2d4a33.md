# 12th Berlin Biennale for Contemporary Art - Refero Design MD

- Source: https://styles.refero.design/style/1c2d4a33-7ee4-4b61-a77e-dab91631d19b
- Original site: https://12.berlinbiennale.de
- Theme: `light`
- Industry: `design`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Underground gallery, high contrast, stark violet punctuation

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight | `#000000` | neutral | Primary text or dark surface |
| Canvas | `#ffffff` | neutral | Page background or card surface |
| Fog | `#f2f2f2` | neutral | Page background or card surface |
| Ash | `#e7e7e7` | neutral | Page background or card surface |
| Vivid Violet | `#7373ff` | brand | Action accent / signal color |
| Muted Violet | `#23234d` | brand | Action accent / signal color |

```css
:root {
  --ref-midnight: #000000;
  --ref-canvas: #ffffff;
  --ref-fog: #f2f2f2;
  --ref-ash: #e7e7e7;
  --ref-vivid-violet: #7373ff;
  --ref-muted-violet: #23234d;
}
```

## Typography direction
- **ABCMonumentGroteskWeb**: 400, 700, 12px, 14px, 16px, 17px, 19px, 20px, 22px, 25px, 29px, 32px, 1.02, 1.03, 1.15, 1.20, 2.00, 2.40; substitute `Arial, Helvetica, sans-serif`.
- **BradfordLLSub**: 400, 20px, 23px, 30px, 1.03, 1.15; substitute `Georgia, serif`.

## Spacing / shape
- Section Gap: `32px`
- Card Padding: `12px`
- Element Gap: `5px`
- Page Max Width: `1069px`
- Radius: `cards: 7px, inputs: 7px, buttons: 5px, default: 3px, roundButtons: 44.129px`

## Surface cues
- **Canvas** `#ffffff`: Dominant page background
- **Fog** `#f2f2f2`: Subtle background for interactive list items and secondary buttons
- **Ash** `#e7e7e7`: Background for navigation items, slightly more prominent than Fog

## Component cues
- **Primary Filled Button**: Standard interactive button for general actions.
- **Secondary Pill Button (Outlined)**: Secondary action or tag component, distinctly rounded.
- **Bare Text Link**: Stylized text link, often inside a component or list.
- **Vivid Violet Text Link**: Distinguished interactive text link.
- **Default Card**: Container for content, appearing as a floating panel.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
