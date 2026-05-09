# Index - Refero Design MD

- Source: https://styles.refero.design/style/b1ec2120-ceb0-42d1-9f96-2c9db2bf009b
- Original site: https://index-space.org
- Theme: `light`
- Industry: `agency`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
monochrome academic journal

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| White Canvas | `#ffffff` | neutral | Page background or card surface |
| Ink Black | `#000000` | neutral | Primary text or dark surface |

```css
:root {
  --ref-white-canvas: #ffffff;
  --ref-ink-black: #000000;
}
```

## Typography direction
- **ABCDiatypeLight**: 300, 400, 12px, 16px, 24px, 30px, 50px, 56px, 80px, 0.90, 1.10, 1.20, 1.25; substitute `Arial`.
- **Times New Roman**: 400, 16px, 1.20; substitute `Times New Roman`.
- **ITCGaramondStdLtCond**: 300, 400, 20px, 24px, 40px, 50px, 75px, 1.00, 1.05, 1.20, 2.10; substitute `Georgia`.

## Spacing / shape
- Section Gap: `40px`
- Card Padding: `20px`
- Element Gap: `8px`
- Page Max Width: `520px`
- Radius: `cards: 16px, pills: 100px, buttons: 0px, default: 6px`

## Surface cues
- **White Canvas** `#ffffff`: Primary page and main content background.
- **Ink Black** `#000000`: Elevated card backgrounds, banner sections, and strong visual grouping zones.

## Component cues
- **Filled Primary Button**: Call to action, critical navigation.
- **Ghost Border Button**: Secondary actions, emphasis on linked text.
- **Pill Outline Button**: Tagging, category filters.
- **Navigation Link**: Top-level navigation and utility links.
- **Simple Card (Dark)**: Content grouping, featured sections.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
