# iUSPC by Coinshift - Refero Design MD

- Source: https://styles.refero.design/style/46bca11b-6920-4d70-8dd7-c4e3dbc123c7
- Original site: https://www.coinshift.xyz
- Theme: `dark`
- Industry: `fintech`
- Recommended fit: **Admin console / run monitor / developer tooling**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Deep space command center.

## Apply to
- Admin run monitor and review states
- Compact evidence cards and source inspection panels
- Dark-mode operational dashboards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Ember | `#020617` | neutral | Primary text or dark surface |
| Slate Text | `#64748b` | neutral | Border, muted text, or supporting surface |
| Steel Gray | `#475569` | neutral | Border, muted text, or supporting surface |
| Divider Gray | `#353845` | neutral | Primary text or dark surface |
| Action Ember | `#651a15` | brand | Action accent / signal color |
| Frost White Light | `#f1f5f9` | neutral | Page background or card surface |
| Frost White Heavy | `#e5e7eb` | neutral | Page background or card surface |
| Cloud Gray | `#cbd5e1` | neutral | Border, muted text, or supporting surface |
| Inferno Gradient Radial | `#fa3812` | accent | Action accent / signal color |
| Horizon Gradient Conic | `#0f172a` | accent | Action accent / signal color |

```css
:root {
  --ref-midnight-ember: #020617;
  --ref-slate-text: #64748b;
  --ref-steel-gray: #475569;
  --ref-divider-gray: #353845;
  --ref-action-ember: #651a15;
  --ref-frost-white-light: #f1f5f9;
  --ref-frost-white-heavy: #e5e7eb;
  --ref-cloud-gray: #cbd5e1;
}
```

## Typography direction
- **Inter**: 300, 400, 500, 600, 11px, 12px, 14px, 16px, 18px, 20px, 24px, 30px, 36px, 48px, 56px, 1.00, 1.08, 1.11, 1.20, 1.33, 1.40, 1.43, 1.50, 1.56, 1.63; substitute `system-ui`.
- **ABCSynt**: 400, 10px, 16px, 18px, 1.00, 1.50; substitute `Inter, system-ui`.

## Spacing / shape
- Section Gap: `32px`
- Card Padding: `32px`
- Element Gap: `24px`
- Radius: `tags: 9999px, links: 12px, buttons: 9999px, general: 0px, navItems: 8px`

## Surface cues
- **Midnight Ember Canvas** `#020617`: The primary, deep background for the entire application, providing a stark, high-contrast base for all content.
- **Steel Gray Surface** `#475569`: A subtle, slightly elevated background used for contained sections or card-like elements, creating a gentle separation from the main canvas.

## Component cues
- **Navigation Link**: Header navigation item, indicating clickable sections or pages.
- **Launch App Button**: Primary call to action in the navigation bar.
- **Hero Section Headline**: Main title on the landing page, conveying the core message.
- **Hero Section Body Text**: Support text in the hero section, offering context to the headline.
- **Ghost Action Button**: Secondary call to action, offering a less prominent but still interactive option.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
