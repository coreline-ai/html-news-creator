# Google for Education - Refero Design MD

- Source: https://styles.refero.design/style/c57ba3f8-1d76-4660-8ba4-48ddce26e759
- Original site: https://classroom.google.com
- Theme: `light`
- Industry: `other`
- Recommended fit: **Design reference / webapp exploration**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Academic blueprint on a clean whiteboard. Clarity and structure in a digitally-enhanced learning space.

## Apply to
- General webapp UI exploration
- Demo cards and catalog surfaces
- Future admin/subscriber UI references

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Classroom Blue | `#1a73e8` | brand | Action accent / signal color |
| Educator Green | `#188038` | brand | Action accent / signal color |
| Interactive Blue | `#1967d2` | brand | Action accent / signal color |
| Sky Tint | `#e8f0fe` | accent | Action accent / signal color |
| Mint Glaze | `#ceead6` | accent | Action accent / signal color |
| Page White | `#f8f9fa` | neutral | Page background or card surface |
| Text Dark | `#202124` | neutral | Primary text or dark surface |
| Text Medium | `#3c4043` | neutral | Primary text or dark surface |
| Text Subtle | `#5f6368` | neutral | Border, muted text, or supporting surface |
| Border Light | `#dadce0` | neutral | Page background or card surface |

```css
:root {
  --ref-classroom-blue: #1a73e8;
  --ref-educator-green: #188038;
  --ref-interactive-blue: #1967d2;
  --ref-sky-tint: #e8f0fe;
  --ref-mint-glaze: #ceead6;
  --ref-page-white: #f8f9fa;
  --ref-text-dark: #202124;
  --ref-text-medium: #3c4043;
}
```

## Typography direction
- **Google Sans Display**: 400, 500, 700, 16px, 18px, 20px, 22px, 28px, 48px, 80px, 1.09, 1.15, 1.17, 1.20, 1.29, 1.40, 1.50, 1.56, 1.75; substitute `system-ui`.
- **Google Sans Text**: 300, 400, 500, 12px, 14px, 16px, 18px, 1.00, 1.44, 1.50, 1.56, 1.63, 1.67, 1.71; substitute `system-ui`.

## Spacing / shape
- Section Gap: `64px`
- Card Padding: `24-32px`
- Element Gap: `8px`
- Radius: `buttons: 200px, default: 8px`

## Component cues
- **Button Group — Primary + Secondary CTAs**: Reference component style.
- **AI Feature Cards — Educator + Student**: Reference component style.
- **Region Selector Modal Dialog**: Reference component style.
- **Primary Call to Action Button**: Main interactive element
- **Secondary Outline Button**: Alternative interactive element

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
