# Preply - Refero Design MD

- Source: https://styles.refero.design/style/476fea7c-d578-4625-b9e6-36e95faa6ca4
- Original site: https://preply.com
- Theme: `light`
- Industry: `other`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Vibrant Tutorial Pop: a playful pink canvas with bold, inviting type.

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Blackboard Ink | `#121117` | neutral | Primary text or dark surface |
| Paper White | `#ffffff` | neutral | Page background or card surface |
| Pale Canvas | `#f4f4f8` | neutral | Page background or card surface |
| Outline Gray | `#dcdce5` | neutral | Page background or card surface |
| Graphite | `#4d4c5c` | neutral | Border, muted text, or supporting surface |
| Tutor Pink | `#ff7aac` | brand | Action accent / signal color |
| Progress Teal | `#3ddabe` | accent | Action accent / signal color |
| Highlight Yellow | `#ffdf3d` | accent | Action accent / signal color |
| Action Blue | `#2885fd` | accent | Action accent / signal color |
| Light Blue | `#99c5ff` | accent | Action accent / signal color |

```css
:root {
  --ref-blackboard-ink: #121117;
  --ref-paper-white: #ffffff;
  --ref-pale-canvas: #f4f4f8;
  --ref-outline-gray: #dcdce5;
  --ref-graphite: #4d4c5c;
  --ref-tutor-pink: #ff7aac;
  --ref-progress-teal: #3ddabe;
  --ref-highlight-yellow: #ffdf3d;
}
```

## Typography direction
- **Platform**: 400, 600, 700, 14px, 16px, 20px, 24px, 32px, 48px, 64px, 96px, 1.00, 1.06, 1.08, 1.13, 1.20, 1.33, 1.50; substitute `Montserrat`.
- **Figtree**: 400, 600, 12px, 13px, 14px, 16px, 18px, 20px, 1.00, 1.14, 1.20, 1.33, 1.40, 1.43, 1.50, 1.71; substitute `Inter`.

## Spacing / shape
- Section Gap: `48px`
- Radius: `tags: 8px, cards: 4px, buttons: 4px, default: 4px`

## Component cues
- **Stats Bar**: Reference component style.
- **Language Tutor Card Grid**: Reference component style.
- **Announcement Banner + CTA Button**: Reference component style.
- **Primary CTA Button**: Primary Call to Action
- **Ghost Button**: Secondary Action

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
