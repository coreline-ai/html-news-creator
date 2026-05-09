# Threads - Refero Design MD

- Source: https://styles.refero.design/style/3b46c64e-b733-4d70-8cd0-531ca1f92937
- Original site: https://www.threads.com
- Theme: `light`
- Industry: `media`
- Recommended fit: **Design reference / webapp exploration**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Minimalist Content Stream

## Apply to
- General webapp UI exploration
- Demo cards and catalog surfaces
- Future admin/subscriber UI references

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Graphite | `#000000` | neutral | Primary text or dark surface |
| Canvas White | `#fafafa` | neutral | Page background or card surface |
| Silver Mist | `#d5d5d5` | neutral | Border, muted text, or supporting surface |
| Platinum Gray | `#969696` | neutral | Border, muted text, or supporting surface |
| Dark Metal | `#424242` | neutral | Border, muted text, or supporting surface |
| Action Azure | `#385898` | brand | Action accent / signal color |

```css
:root {
  --ref-midnight-graphite: #000000;
  --ref-canvas-white: #fafafa;
  --ref-silver-mist: #d5d5d5;
  --ref-platinum-gray: #969696;
  --ref-dark-metal: #424242;
  --ref-action-azure: #385898;
}
```

## Typography direction
- **system-ui**: 400, 600, 12px, 13px, 15px, 1.33, 1.40; substitute `Inter, Noto Sans, Arial`.

## Spacing / shape
- Section Gap: `48px`
- Card Padding: `16px`
- Element Gap: `12px`
- Radius: `cards: 8px, images: 8px, avatars: 50%, buttons: 1000px, modules: 18px`

## Surface cues
- **Canvas White** `#fafafa`: Primary page background
- **Card Surface** `#fafafa`: Content cards, elevated through subtle shadows rather than distinct background color.
- **Hover/Focus Tint** `#efefef`: Subtle background shift for hover or active states (inferred from contrast table).

## Component cues
- **Ghost Button**: Minimal interactive element for secondary actions
- **Pill Ghost Button**: Minimal interactive element, for icon-only actions or small secondary controls where a soft touch is desired.
- **Primary Filled Button**: Main call-to-action button for critical user flows
- **Circular Icon Button**: Small, usually icon-only buttons for navigation or quick actions.
- **Feed Post Card**: Primary content container for user-generated posts

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
