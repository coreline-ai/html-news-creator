# Dub Links - Refero Design MD

- Source: https://styles.refero.design/style/7bbbf1bc-e375-4200-8d71-e373a3c78654
- Original site: https://dub.sh
- Theme: `light`
- Industry: `devtools`
- Recommended fit: **Design reference / webapp exploration**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Clean workbench, energetic highlight. The interface feels like a well-organized array of digital tools on a bright surface, with a single, clear visual thread guiding user action.

## Apply to
- General webapp UI exploration
- Demo cards and catalog surfaces
- Future admin/subscriber UI references

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Ghost White | `#ffffff` | neutral | Page background or card surface |
| Ash Gray | `#fcfcfc` | neutral | Page background or card surface |
| Cloud Gray | `#e5e5e5` | neutral | Page background or card surface |
| Cool Gray | `#d4d4d4` | neutral | Border, muted text, or supporting surface |
| Steel Gray | `#a3a3a3` | neutral | Border, muted text, or supporting surface |
| Jet Black | `#171717` | neutral | Primary text or dark surface |
| Ink Black | `#0a0a0a` | neutral | Primary text or dark surface |
| Ember Glow | `#f97316` | accent | Action accent / signal color |
| Sky Blue | `#3b82f6` | semantic | Action accent / signal color |
| Forest Green | `#16a34a` | semantic | Action accent / signal color |

```css
:root {
  --ref-ghost-white: #ffffff;
  --ref-ash-gray: #fcfcfc;
  --ref-cloud-gray: #e5e5e5;
  --ref-cool-gray: #d4d4d4;
  --ref-steel-gray: #a3a3a3;
  --ref-jet-black: #171717;
  --ref-ink-black: #0a0a0a;
  --ref-ember-glow: #f97316;
}
```

## Typography direction
- **Inter**: 400, 500, 600, 700, 12px, 14px, 16px, 18px, 20px, 24px, 1.00, 1.25, 1.33, 1.40, 1.43, 1.50, 1.56; substitute `system-ui, sans-serif`.
- **Satoshi**: 500, 40px, 48px, 1.00, 1.15; substitute `system-ui, sans-serif`.
- **GeistMono**: 400, 12px, 13px, 14px, 1.00, 1.33, 1.43, 1.50; substitute `SFMono-Regular, Consolas, Liberation Mono, Menlo, monospace`.

## Spacing / shape
- Section Gap: `64px`
- Card Padding: `16px`
- Element Gap: `8px`
- Page Max Width: `1280px`
- Radius: `pill: 9999px, cards: 12px, buttons: 8px, default: 4px`

## Component cues
- **Link Shortener Input Group**: Reference component style.
- **Button Group — Primary, Secondary & Ghost**: Reference component style.
- **Link Editor Form Card**: Reference component style.
- **Primary Call-to-Action Button**: Main interactive button
- **Secondary Button**: Alternative action button

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
