# Chronicle - Refero Design MD

- Source: https://styles.refero.design/style/1c60b014-473b-443b-b0f5-220612feebb7
- Original site: https://chroniclehq.com
- Theme: `light`
- Industry: `saas`
- Recommended fit: **Admin console / run monitor / developer tooling**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Typographer's proof sheet — a composited page where precision of letterform carries the entire visual weight, color is an intrusion, and the grid is the design.

## Apply to
- Admin run monitor and review states
- Compact evidence cards and source inspection panels
- Dark-mode operational dashboards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Pitch Black | `#050505` | neutral | Primary text or dark surface |
| Midnight | `#000000` | neutral | Primary text or dark surface |
| Charcoal | `#151515` | neutral | Primary text or dark surface |
| Obsidian | `#292929` | neutral | Primary text or dark surface |
| Graphite | `#6b6b6b` | neutral | Border, muted text, or supporting surface |
| Pewter | `#7e7e7e` | neutral | Border, muted text, or supporting surface |
| Ash | `#929292` | neutral | Border, muted text, or supporting surface |
| Silver | `#b3b3b3` | neutral | Border, muted text, or supporting surface |
| Fog | `#e2e2e2` | neutral | Page background or card surface |
| Limestone | `#f3f3f3` | neutral | Page background or card surface |

```css
:root {
  --ref-pitch-black: #050505;
  --ref-midnight: #000000;
  --ref-charcoal: #151515;
  --ref-obsidian: #292929;
  --ref-graphite: #6b6b6b;
  --ref-pewter: #7e7e7e;
  --ref-ash: #929292;
  --ref-silver: #b3b3b3;
}
```

## Typography direction
- **Diatype**: 400, 500, 12px, 14px, 16px, 20px, 32px, 48px, 54px, 1.00–1.40 (1.00 at display, 1.05 at large headings, 1.10–1.20 at subheadings, 1.40 at body); substitute `Inter, Helvetica Neue`.

## Spacing / shape
- Section Gap: `80-128px`
- Card Padding: `24-30px`
- Element Gap: `8px`
- Page Max Width: `1212px`
- Radius: `tags: 4px, cards: 8px, images: 4px, inputs: 4px, buttons: 4px`

## Surface cues
- **Canvas** `#ffffff`: Primary page background for hero and main content sections
- **Tinted Surface** `#f3f3f3`: Alternating section backgrounds — testimonials, feature band, footer area
- **Card Surface** `#ffffff`: White cards elevated above gray sections with 8px radius and soft shadow
- **Border Plane** `#e2e2e2`: Image frames, card outlines, input borders — structural hairlines

## Component cues
- **Filled Black CTA Button**: Primary call-to-action — 'Try for free', 'Try Chronicle'
- **Ghost Underline Button**: Secondary text action — 'Watch video', tab-style navigation items
- **Muted Ghost Button**: Inactive or de-emphasized action
- **Pill Tab Button**: Horizontal tab navigation — presentation type selectors (Sales proposal, Pitch deck, etc.)
- **Testimonial Card**: Social proof — customer quote with logo, name, role

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
