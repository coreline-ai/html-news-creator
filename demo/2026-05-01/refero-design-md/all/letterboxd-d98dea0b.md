# Letterboxd - Refero Design MD

- Source: https://styles.refero.design/style/d98dea0b-00a4-4c15-b4a9-d196e2c3e4b4
- Original site: https://letterboxd.com
- Theme: `dark`
- Industry: `media`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Midnight Theater Screen

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Ink | `#14181c` | neutral | Primary text or dark surface |
| Charcoal Canvas | `#202830` | neutral | Primary text or dark surface |
| Shadow Gray | `#2c3440` | neutral | Primary text or dark surface |
| Ghostly Grey | `#586370` | neutral | Border, muted text, or supporting surface |
| Steel Text | `#667788` | neutral | Border, muted text, or supporting surface |
| Cloudburst Text | `#778899` | neutral | Border, muted text, or supporting surface |
| Mist Text | `#8899aa` | neutral | Border, muted text, or supporting surface |
| Ash Text | `#99aabb` | neutral | Border, muted text, or supporting surface |
| Porcelain Text | `#ddeeff` | neutral | Page background or card surface |
| Whiteout | `#ffffff` | neutral | Page background or card surface |

```css
:root {
  --ref-midnight-ink: #14181c;
  --ref-charcoal-canvas: #202830;
  --ref-shadow-gray: #2c3440;
  --ref-ghostly-grey: #586370;
  --ref-steel-text: #667788;
  --ref-cloudburst-text: #778899;
  --ref-mist-text: #8899aa;
  --ref-ash-text: #99aabb;
}
```

## Typography direction
- **GraphikWeb**: 300, 400, 700, 10px, 11px, 12px, 13px, 14px, 15px, 16px, 17px, 18px, 24px, 26px, 1.00, 1.20, 1.23, 1.25, 1.31, 1.38, 1.50, 1.54, 1.75, 2.00; substitute `Inter`.
- **TiemposTextWeb**: 400, 700, 15px, 22px, 1.20, 1.25, 1.67; substitute `Source Serif Pro`.
- **TiemposHeadlineWeb**: 700, 36px, 1.33; substitute `Playfair Display`.

## Spacing / shape
- Section Gap: `48px`
- Card Padding: `0px`
- Element Gap: `4px`
- Radius: `pill: 12-15px, buttons: 3px, default: 3px`

## Component cues
- **Primary CTA Button Group**: Reference component style.
- **Film Card Row**: Reference component style.
- **Security Check Modal**: Reference component style.
- **Primary Action Button**: Main call to action
- **Secondary Ghost Button**: Alternative actions or secondary CTA

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
