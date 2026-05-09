# Intercom - Refero Design MD

- Source: https://styles.refero.design/style/12255b63-e506-4bc1-a4cd-d05487de32f3
- Original site: https://intercom.com
- Theme: `light`
- Industry: `ai`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Architectural blueprint on white marble

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Background Off-White | `#faf9f6` | neutral | Page background or card surface |
| Surface Cream | `#f1eee9` | neutral | Page background or card surface |
| Border Sand | `#dedbd6` | neutral | Page background or card surface |
| Subtle Gray | `#e7e3db` | neutral | Page background or card surface |
| Canvas Beige | `#d3cec6` | neutral | Border, muted text, or supporting surface |
| Headline Black | `#111111` | neutral | Primary text or dark surface |
| Body Text Black | `#000000` | neutral | Primary text or dark surface |
| Subtle Graphite | `#414141` | neutral | Border, muted text, or supporting surface |
| Mid Gray | `#585858` | neutral | Border, muted text, or supporting surface |

```css
:root {
  --ref-canvas-white: #ffffff;
  --ref-background-off-white: #faf9f6;
  --ref-surface-cream: #f1eee9;
  --ref-border-sand: #dedbd6;
  --ref-subtle-gray: #e7e3db;
  --ref-canvas-beige: #d3cec6;
  --ref-headline-black: #111111;
  --ref-body-text-black: #000000;
}
```

## Typography direction
- **Saans**: 300, 400, 14px, 16px, 20px, 24px, 32px, 40px, 54px, 80px, 0.95, 1.00, 1.25, 1.40, 1.43, 1.50; substitute `system-ui, sans-serif`.
- **SaansMono**: 300, 400, 500, 12px, 14px, 1.00, 1.30, 1.40; substitute `SFMono-Regular, monospace`.
- **Serrif**: 300, 16px, 1.40; substitute `serif`.

## Spacing / shape
- Section Gap: `48px`
- Card Padding: `16px`
- Element Gap: `16px`
- Radius: `buttons: 4px, navItems: 4px`

## Surface cues
- **Canvas White** `#ffffff`: Primary page background, base layer.
- **Background Off-White** `#faf9f6`: Subtle background for distinct content sections or cards, offering minimal elevation.
- **Surface Cream** `#f1eee9`: More pronounced background for feature blocks or secondary content areas, indicating a slight lift.
- **Subtle Gray** `#e7e3db`: Used for banners or highly differentiated content blocks, suggesting a higher level of separation.

## Component cues
- **Alert Banner**: Reference component style.
- **Tab Bar**: Reference component style.
- **Button Group**: Reference component style.
- **Primary Action Button**: Call to action
- **Secondary Outline Button**: Secondary action

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
