# Clerk - Refero Design MD

- Source: https://styles.refero.design/style/ed10ae04-24ec-4e42-9bf2-ea12a4b58d67
- Original site: https://clerk.com
- Theme: `mixed`
- Industry: `devtools`
- Recommended fit: **Admin console / run monitor / developer tooling**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Developer dashboard behind frosted violet glass — surfaces feel like a live IDE preview: dark product cards floating inside a light documentation shell, with one electric violet pulse marking the path forward.

## Apply to
- Admin run monitor and review states
- Compact evidence cards and source inspection panels
- Dark-mode operational dashboards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Void Black | `#131316` | neutral | Primary text or dark surface |
| Fog White | `#f7f7f8` | neutral | Page background or card surface |
| Pure White | `#ffffff` | neutral | Page background or card surface |
| Graphite | `#5e5f6e` | neutral | Border, muted text, or supporting surface |
| Ash | `#747686` | neutral | Border, muted text, or supporting surface |
| Hairline | `#d9d9de` | neutral | Page background or card surface |
| Mist | `#eeeef0` | neutral | Page background or card surface |
| Stone | `#9394a1` | neutral | Border, muted text, or supporting surface |
| Obsidian Card | `#212126` | neutral | Primary text or dark surface |
| Dark Surface | `#2f3037` | neutral | Primary text or dark surface |

```css
:root {
  --ref-void-black: #131316;
  --ref-fog-white: #f7f7f8;
  --ref-pure-white: #ffffff;
  --ref-graphite: #5e5f6e;
  --ref-ash: #747686;
  --ref-hairline: #d9d9de;
  --ref-mist: #eeeef0;
  --ref-stone: #9394a1;
}
```

## Typography direction
- **soehneMono**: 400, 500, 600, 10px, 11px, 12px, 1.33, 1.4, 1.45, 1.64, 1.82, 2.
- **Geist**: 400, 450, 500, 600, 700, 10px, 11px, 12px, 13px, 15px, 16px, 18px, 20px, 32px, 64px, 1.0–1.85 depending on size; tighter (1.0–1.25) at display sizes, looser (1.4–1.6) at body sizes; substitute `Inter, DM Sans`.
- **ui-sans-serif**: 400, 500, 700, 10px, 11px, 12px, 13px, 16px, 17px, 1.27–1.82; substitute `system-ui, -apple-system`.

## Spacing / shape
- Section Gap: `80px`
- Element Gap: `8px`
- Page Max Width: `1200px`
- Radius: `tags: 9999px, cards: 16px, badges: 9999px, inputs: 6px, modals: 16px, buttons: 6px, cardSmall: 8px, codeBlocks: 12px`

## Surface cues
- **Page Canvas** `#f7f7f8`: Base page background for light marketing sections
- **Card Surface** `#ffffff`: Default card and form surface on light backgrounds
- **Recessed Surface** `#f7f7f8`: Input backgrounds, table row fills, and secondary card insets
- **Dark Canvas** `#212126`: Product demo sections and dark-mode showcase panels
- **Elevated Dark** `#2f3037`: Elevated panels and code blocks within dark sections

## Component cues
- **Primary Violet Button**: Main CTA — 'Start building for free', 'Start building'
- **White Outlined Button**: Secondary action, navigation-adjacent controls
- **Ghost Navigation Button**: Top-level nav items and inline text-links with icons
- **Pill Tag / Badge**: Category labels, section eyebrow labels (e.g. 'Clerk Components', 'User Authentication')
- **Light Marketing Card**: Feature cards and pricing sections on white/fog surfaces

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
