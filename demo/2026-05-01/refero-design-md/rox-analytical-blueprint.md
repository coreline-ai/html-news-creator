# Rox - Refero Design MD

- Source: https://styles.refero.design/style/66eb1c37-a8e5-4e6c-b17f-a75385b462e7
- Original site: https://rox.com
- Theme: `light`
- Recommended fit: **Data dashboard / source ledger**

## North star
Analytical Blueprint on Pure White. An interface that feels like a meticulously charted course on a pristine, well-lit canvas.

## Why this fits html-news-creator
Useful for evidence-heavy screens: source tables, confidence labels, cluster metrics, and verification states.

## Apply to
- Source evidence tables
- Cluster scoring dashboards
- Admin metrics and QA panels

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Page Canvas | `#f5f5f4` | neutral | Primary background for pages and major sections, providing a clean, bright foundation. |
| Surface White | `#ffffff` | neutral | Used for cards, panels, and elements needing to stand out slightly from the main background, often appearing as content. |
| Blueprint Blue | `#0b64e9` | brand | Primary brand accent, used for all calls-to-action, interactive states, and key navigational elements to draw attention. |
| Text Primary | `#0c0a09` | neutral | Main body text, headlines, and critical information for maximum readability against light backgrounds. |
| Text Secondary | `#1c1917` | neutral | Subheadings, supporting text, and less emphasized information, a subtle step lighter than primary text but still high c. |
| Text Muted | `#a6a09b` | neutral | Placeholder text, minor labels, and supplementary details, providing a softer visual presence. |
| Text Subtle | `#57534d` | neutral | Less prominent text like captions or descriptions, visually receding while remaining legible. |
| Subtle Gray | `#ececea` | neutral | Backgrounds for subtle containers like badges or minor card elements, offering a hint of differentiation. |

```css
:root {
  --ref-page-canvas: #f5f5f4;
  --ref-surface-white: #ffffff;
  --ref-blueprint-blue: #0b64e9;
  --ref-text-primary: #0c0a09;
  --ref-text-secondary: #1c1917;
  --ref-text-muted: #a6a09b;
  --ref-text-subtle: #57534d;
}
```

## Typography direction
- Primary: **FH Total Display Regular**; substitute `Playfair Display`.
- Secondary/code: **Geist**; substitute `Inter`.

## Spacing / shape
- Section gap: ``
- Card padding: `16px`
- Element gap: `4-16px`
- Radius: `{'pill': '100px', 'large': '12px', 'buttons': '8px', 'default': '6px'}`

## Agent notes
- Treat this as reference material, not a direct template copy.
- Do not apply this wholesale to templates/report_newsstream.html.j2 unless the user explicitly asks for an HTML report migration.
- Preserve the project information hierarchy: title, why it matters, source evidence, confidence, image evidence.
