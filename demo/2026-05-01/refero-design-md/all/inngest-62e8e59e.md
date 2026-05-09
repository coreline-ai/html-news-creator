# Inngest - Refero Design MD

- Source: https://styles.refero.design/style/62e8e59e-17a5-4eba-a6c6-1c7f67ded518
- Original site: https://inngest.com
- Theme: `dark`
- Industry: `devtools`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Midnight Grid Console — where precision meets a soft amber glow.

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Background Charcoal | `#0c0a09` | neutral | Primary text or dark surface |
| Surface Dark Gray | `#1c1917` | neutral | Primary text or dark surface |
| Text White | `#ffffff` | neutral | Page background or card surface |
| Text Light Gray | `#f6f6f6` | neutral | Page background or card surface |
| Text Medium Gray | `#a89984` | neutral | Border, muted text, or supporting surface |
| Border Light Gray | `#e5e7eb` | neutral | Page background or card surface |
| Border Accent Gray | `#44403c` | neutral | Border, muted text, or supporting surface |
| Amber Glow | `#cab16a` | brand | Action accent / signal color |
| Highlight Green | `#59a569` | accent | Action accent / signal color |
| Muted Red | `#ea6962` | semantic | Action accent / signal color |

```css
:root {
  --ref-background-charcoal: #0c0a09;
  --ref-surface-dark-gray: #1c1917;
  --ref-text-white: #ffffff;
  --ref-text-light-gray: #f6f6f6;
  --ref-text-medium-gray: #a89984;
  --ref-border-light-gray: #e5e7eb;
  --ref-border-accent-gray: #44403c;
  --ref-amber-glow: #cab16a;
}
```

## Typography direction
- **CircularXX**: 300, 400, 500, 600, 12px, 14px, 16px, 18px, 20px, 24px, 72px, 1.00, 1.20, 1.33, 1.40, 1.43, 1.50, 1.56, 1.63, 1.64, 1.71, 1.75; substitute `Inter`.
- **CircularXXMono**: 400, 12px, 14px, 18px, 1.33, 1.43, 1.56, 1.63; substitute `Space Mono`.
- **Whyte**: 300, 400, 600, 700, 16px, 24px, 30px, 36px, 48px, 72px, 1.00, 1.11, 1.20, 1.30, 1.33, 1.50; substitute `Montserrat`.

## Spacing / shape
- Section Gap: `24-40px`
- Card Padding: `0px`
- Element Gap: `4-24px`
- Radius: `cards: 0px, buttons: 9999px, default: 4px`

## Component cues
- **CTA Button Group**: Reference component style.
- **Feature Cards — Infraless / Agnostic / Observable**: Reference component style.
- **Enterprise Trust — Built for Trust Feature Block**: Reference component style.
- **Navigation Link**: Primary navigation item
- **Primary Call to Action Button**: Key interactive element

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
