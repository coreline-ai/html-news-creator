# Phantom - Refero Design MD

- Source: https://styles.refero.design/style/6144c3ae-fc57-4efe-b6ed-2b5eab2dc108
- Original site: https://phantom.com
- Theme: `light`
- Industry: `crypto`
- Recommended fit: **Design reference / webapp exploration**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Muted violet canvas

## Apply to
- General webapp UI exploration
- Demo cards and catalog surfaces
- Future admin/subscriber UI references

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#fdfcfe` | neutral | Page background or card surface |
| Phantom Violet | `#3c315b` | brand | Action accent / signal color |
| Ghost Button Violet | `#e2dffe` | brand | Action accent / signal color |
| Deep Sea | `#1c1c1c` | neutral | Primary text or dark surface |
| Slate Gray | `#e9e8ea` | neutral | Page background or card surface |
| Sky Lavender | `#ab9ff2` | brand | Action accent / signal color |
| Soft Fog | `#f4f2f4` | neutral | Page background or card surface |
| Cool Gray | `#86848d` | neutral | Border, muted text, or supporting surface |
| Success Green | `#2ec08b` | semantic | Action accent / signal color |

```css
:root {
  --ref-canvas-white: #fdfcfe;
  --ref-phantom-violet: #3c315b;
  --ref-ghost-button-violet: #e2dffe;
  --ref-deep-sea: #1c1c1c;
  --ref-slate-gray: #e9e8ea;
  --ref-sky-lavender: #ab9ff2;
  --ref-soft-fog: #f4f2f4;
  --ref-cool-gray: #86848d;
}
```

## Typography direction
- **Phantom**: 350, 400, 13px, 15px, 16px, 20px, 24px, 30px, 64px, 80px, 96px, 1.00, 1.10, 1.20, 1.21, 1.25, 1.35, 1.40.
- **Phantom**: 350, 400, 13px, 15px, 16px, 20px, 24px, 30px, 64px, 80px, 96px, 1.00, 1.10, 1.20, 1.21, 1.25, 1.35, 1.40.

## Spacing / shape
- Section Gap: `32px`
- Card Padding: `48px`
- Element Gap: `4px`
- Radius: `cards: 24px, header: 100px, buttons: 32px, largeElements: 24px, smallElements: 4px`

## Surface cues
- **Canvas White** `#fdfcfe`: Primary page background and base for cards
- **Soft Fog** `#f4f2f4`: Subtle background for distinct content sections

## Component cues
- **Primary Action Button**: Calls to action, e.g., 'Download Phantom'
- **Inverted Dark Button**: Alternative action buttons on darker backgrounds
- **Ghost Outline Button**: Subtle secondary actions or links
- **Muted Button**: Less prominent actions, often within a card or section
- **Content Card**: Information grouping and background for features

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
