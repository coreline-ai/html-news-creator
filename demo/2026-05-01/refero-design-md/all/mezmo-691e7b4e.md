# Mezmo - Refero Design MD

- Source: https://styles.refero.design/style/691e7b4e-fee9-4f08-a2e9-9a2742c22b7b
- Original site: https://www.mezmo.com
- Theme: `light`
- Industry: `ai`
- Recommended fit: **Source ledger / evidence dashboard**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Data-dense lavender precision

## Apply to
- Source ledger, ranking, and verification screens
- Cluster evidence dashboards
- Dense data tables with clear hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Inkwell | `#0a090c` | neutral | Primary text or dark surface |
| Canvas | `#e6e6e5` | neutral | Page background or card surface |
| Paper White | `#ffffff` | neutral | Page background or card surface |
| Ash Gray | `#f4f4f4` | neutral | Page background or card surface |
| Steel Gray | `#c3c3c3` | neutral | Border, muted text, or supporting surface |
| Grout | `#d1d5db` | neutral | Border, muted text, or supporting surface |
| Charcoal | `#2d2d2d` | neutral | Primary text or dark surface |
| Twilight Lavender | `#7561b1` | brand | Action accent / signal color |
| Cerulean Mist | `#96beca` | brand | Action accent / signal color |
| Subtle Teal | `#74a9b9` | accent | Action accent / signal color |

```css
:root {
  --ref-inkwell: #0a090c;
  --ref-canvas: #e6e6e5;
  --ref-paper-white: #ffffff;
  --ref-ash-gray: #f4f4f4;
  --ref-steel-gray: #c3c3c3;
  --ref-grout: #d1d5db;
  --ref-charcoal: #2d2d2d;
  --ref-twilight-lavender: #7561b1;
}
```

## Typography direction
- **Onest Variable**: 300, 400, 500, 600, 9px, 10px, 11px, 12px, 13px, 14px, 16px, 17px, 18px, 19px, 20px, 22px, 24px, 26px, 30px, 36px, 48px, 1.00, 1.05, 1.13, 1.20, 1.23, 1.25, 1.33, 1.45, 1.50, 1.55; substitute `Inter`.
- **monospace**: 300, 500, 600, 9px, 10px, 11px, 12px, 1.50; substitute `SF Mono, Consolas`.

## Spacing / shape
- Section Gap: `40px`
- Card Padding: `16px`
- Element Gap: `16px`
- Page Max Width: `1200px`
- Radius: `cards: 8px, input: 5px, badges: 4px, buttons: 6px`

## Component cues
- **Primary Filled Button**: Main call to action, interactive elements.
- **Ghost Button**: Secondary actions that need less emphasis.
- **Text Link Button**: Inline actions or navigation without a distinct container.
- **Elevated Card**: Container for content that requires subtle prominence, e.g., features, testimonials.
- **Subtle Elevated Card**: Secondary content cards, often within informational sections.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
