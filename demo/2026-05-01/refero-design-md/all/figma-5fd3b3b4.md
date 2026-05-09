# Figma - Refero Design MD

- Source: https://styles.refero.design/style/5fd3b3b4-02ab-456a-87aa-e4395636b671
- Original site: https://www.figma.com
- Theme: `light`
- Industry: `design`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
digital drafting board

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Ink Black | `#000000` | neutral | Primary text or dark surface |
| Figma Gray | `#595959` | neutral | Border, muted text, or supporting surface |
| Surface Off-White | `#e2e2e2` | neutral | Page background or card surface |
| Action Violet | `#4d49fc` | accent | Action accent / signal color |
| Link Blue | `#00b6ff` | brand | Action accent / signal color |
| Link Green | `#24cb71` | brand | Action accent / signal color |
| Link Orange | `#ff7237` | brand | Action accent / signal color |
| Figma Green | `#e4ff97` | brand | Action accent / signal color |
| Figma Violet | `#c4baff` | brand | Action accent / signal color |

```css
:root {
  --ref-canvas-white: #ffffff;
  --ref-ink-black: #000000;
  --ref-figma-gray: #595959;
  --ref-surface-off-white: #e2e2e2;
  --ref-action-violet: #4d49fc;
  --ref-link-blue: #00b6ff;
  --ref-link-green: #24cb71;
  --ref-link-orange: #ff7237;
}
```

## Typography direction
- **figmaSans**: 320, 330, 340, 400, 450, 480, 520, 700, 16px, 18px, 24px, 56px, 72px, 1.00, 1.10, 1.30, 1.35, 1.40, 1.45; substitute `Inter`.
- **figmaMono**: 400, 12px, 16px, 1.00, 1.30; substitute `JetBrains Mono`.

## Spacing / shape
- Section Gap: `24px`
- Card Padding: `16px`
- Element Gap: `16px`
- Radius: `cards: 16px, links: 2px, buttons: 50px, smallButtons: 8px`

## Surface cues
- **Canvas White** `#ffffff`: Primary page background, base layer.
- **Surface Off-White** `#e2e2e2`: Subtle background for distinct sections or card-like groupings without explicit borders or shadows.

## Component cues
- **Ghost Text Button**: navigation link, secondary action
- **Primary Pill Button**: primary action
- **Secondary Pill Button (Outlined)**: secondary action
- **Circular Icon Button (Transparent BG)**: icon button, subtle interaction
- **Circular Icon Button (Ghost White)**: icon button, subtle interaction on dark BG

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
