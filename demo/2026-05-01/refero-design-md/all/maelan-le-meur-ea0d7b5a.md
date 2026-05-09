# Maëlan Le Meur - Refero Design MD

- Source: https://styles.refero.design/style/ea0d7b5a-c887-4b6b-9260-6ca4d1fd7caa
- Original site: https://maelanlemeur.com
- Theme: `dark`
- Industry: `agency`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Sepia-toned literary journal

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Inkwell | `#1e1915` | neutral | Primary text or dark surface |
| Parchment Cream | `#eee9cc` | brand | Action accent / signal color |
| Antique Ivory | `#cecab1` | neutral | Border, muted text, or supporting surface |
| Burnt Umber | `#674825` | accent | Action accent / signal color |

```css
:root {
  --ref-inkwell: #1e1915;
  --ref-parchment-cream: #eee9cc;
  --ref-antique-ivory: #cecab1;
  --ref-burnt-umber: #674825;
}
```

## Typography direction
- **PP Neue Montreal**: 400, 15px, 16px, 26px, 30px, 58px, 115px, 225px, 317px, 0.95, 1.00, 1.20, 1.50; substitute `Inter`.

## Spacing / shape
- Section Gap: `60px`
- Card Padding: `0px`
- Element Gap: `10-20px`
- Radius: `links: 40px, default: 0px`

## Component cues
- **Services Category List**: Reference component style.
- **Réalisations Project Table**: Reference component style.
- **Hero Statement Block**: Reference component style.
- **Navigation Link**: Interactive element (e.g. 'V', 'o', 'u', 's' in nav)
- **Menu Item Highlight Button**: Highlighting a currently selected menu item.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
