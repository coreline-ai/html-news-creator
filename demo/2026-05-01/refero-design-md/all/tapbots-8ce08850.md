# Tapbots - Refero Design MD

- Source: https://styles.refero.design/style/8ce08850-085e-4954-a2f0-16acfb8dce23
- Original site: https://tapbots.com/ivory
- Theme: `dark`
- Industry: `other`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Cosmic playful precision. Imagine floating among luminous violet and emerald constellations within a dark, welcoming void.

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Void | `#05050b` | neutral | Primary text or dark surface |
| Deep Shadow | `#1a1a1a` | neutral | Primary text or dark surface |
| Carbon Gray | `#2c2c2c` | neutral | Primary text or dark surface |
| Graphite | `#484848` | neutral | Border, muted text, or supporting surface |
| Medium Gray | `#666666` | neutral | Border, muted text, or supporting surface |
| Light Gray | `#999999` | neutral | Border, muted text, or supporting surface |
| Stone Grey | `#a3a3a3` | neutral | Border, muted text, or supporting surface |
| Silver Tone | `#b3b3b3` | neutral | Border, muted text, or supporting surface |
| Pale Gray | `#c3c3c3` | neutral | Border, muted text, or supporting surface |
| Bright Silver | `#cccccc` | neutral | Border, muted text, or supporting surface |

```css
:root {
  --ref-midnight-void: #05050b;
  --ref-deep-shadow: #1a1a1a;
  --ref-carbon-gray: #2c2c2c;
  --ref-graphite: #484848;
  --ref-medium-gray: #666666;
  --ref-light-gray: #999999;
  --ref-stone-grey: #a3a3a3;
  --ref-silver-tone: #b3b3b3;
}
```

## Typography direction
- **-apple-system**: 300, 400, 500, 600, 16px, 18px, 20px, 21px, 24px, 28px, 32px, 36px, 0.84, 1.10, 1.20, 1.29, 1.40, 1.50, 1.70, 1.80; substitute `system-ui`.

## Spacing / shape
- Section Gap: `64px`
- Card Padding: `20px`
- Element Gap: `10px`
- Radius: `icons: 40px, links: 40px, lists: 18px, buttons: 40px`

## Component cues
- **Primary Action Button Group**: Reference component style.
- **Feature List Grid**: Reference component style.
- **Testimonial Card**: Reference component style.
- **Primary Action Button**: Primary Call to Action
- **Feature List Item**: Informational Display

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
