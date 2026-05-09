# Cron Calendar - Refero Design MD

- Source: https://styles.refero.design/style/476184db-a4e6-440b-aa53-27294668361c
- Original site: https://cron.com
- Theme: `dark`
- Industry: `productivity`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Minimal dark cockpit. Clean contrast of white text on deep gray surfaces, punctuated by a vivid orange accent.

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Cron Black | `#0f0d0a` | neutral | Primary text or dark surface |
| Deep Graphite | `#161412` | neutral | Primary text or dark surface |
| Bright White | `#ffffff` | neutral | Page background or card surface |
| Subtle Gray | `#cccccc` | neutral | Border, muted text, or supporting surface |
| Action Orange | `#ff4700` | accent | Action accent / signal color |
| Deep Ember | `#8b2e09` | accent | Action accent / signal color |

```css
:root {
  --ref-cron-black: #0f0d0a;
  --ref-deep-graphite: #161412;
  --ref-bright-white: #ffffff;
  --ref-subtle-gray: #cccccc;
  --ref-action-orange: #ff4700;
  --ref-deep-ember: #8b2e09;
}
```

## Typography direction
- **Helvetica Neue**: 400, 500, 700, 13px, 15px, 22px, 140px, 0.90, 1.00, 1.50, 1.70, 2.88; substitute `system-ui, sans-serif`.

## Spacing / shape
- Section Gap: `80px`
- Element Gap: `16px`
- Radius: `buttons: 4px, navigationPills: 9999px`

## Component cues
- **Announcement Pill Banner**: Reference component style.
- **Button Group — Primary & Secondary**: Reference component style.
- **Feature Stat / Metric Cards**: Reference component style.
- **Primary Call-to-Action Button**: Interactive element
- **Secondary Button**: Interactive element

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
