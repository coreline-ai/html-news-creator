# Raise - Refero Design MD

- Source: https://styles.refero.design/style/63d44e1f-e3e9-40dc-bba4-1aa6efc4db87
- Original site: https://opencollective.com
- Theme: `light`
- Industry: `fintech`
- Recommended fit: **Research brief / AI trend page**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Architectural Blueprint Clarity

## Apply to
- Research section pages and model-release briefs
- Lab-note style cards
- AI product/research trend summaries

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Navy Ink | `#0f172b` | neutral | Primary text or dark surface |
| Ocean Blue | `#0c2764` | brand | Action accent / signal color |
| Slate Text | `#1d293d` | neutral | Primary text or dark surface |
| Light Slate | `#62748e` | neutral | Border, muted text, or supporting surface |
| Medium Slate | `#314158` | neutral | Primary text or dark surface |
| Soft Gray Border | `#e2e8f0` | neutral | Page background or card surface |
| Lightest Gray Surface | `#f1f5f9` | neutral | Page background or card surface |
| Hint Gray | `#c3c6cb` | neutral | Border, muted text, or supporting surface |
| Inactive Chip | `#90a1b9` | neutral | Border, muted text, or supporting surface |

```css
:root {
  --ref-canvas-white: #ffffff;
  --ref-navy-ink: #0f172b;
  --ref-ocean-blue: #0c2764;
  --ref-slate-text: #1d293d;
  --ref-light-slate: #62748e;
  --ref-medium-slate: #314158;
  --ref-soft-gray-border: #e2e8f0;
  --ref-lightest-gray-surface: #f1f5f9;
}
```

## Typography direction
- **Inter**: 400, 500, 600, 700, 800, 14px, 16px, 18px, 20px, 32px, 40px, 60px, 72px, 1.00, 1.20, 1.25, 1.40, 1.43, 1.50, 1.56, 1.63, 1.71; substitute `system-ui`.

## Spacing / shape
- Section Gap: `32px`
- Card Padding: `32px`
- Element Gap: `16px`
- Page Max Width: `1200px`
- Radius: `cards: 12px, buttons: 1.67772e+07px, general: 12px`

## Surface cues
- **Canvas White** `#ffffff`: Dominant page background, primary canvas for content.
- **Lightest Gray Surface** `#f1f5f9`: Subtle background for distinct sections or very light card variations.
- **Inactive Chip** `#90a1b9`: Background for secondary or inactive visual elements, suggesting a lower hierarchy.
- **Ocean Blue** `#0c2764`: Elevated, prominent surfaces like primary action buttons.

## Component cues
- **Primary Filled Button**: Main calls to action
- **Ghost Header Button**: Secondary navigation actions in the header
- **Ghost Card Button**: Interactive elements within cards, like approval options
- **Hero Action Button**: Prominent calls to action in hero sections
- **Standard Card**: Content containers, feature blocks, data displays

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
