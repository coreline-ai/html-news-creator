# Mapbox - Refero Design MD

- Source: https://styles.refero.design/style/be34bbe8-9a50-4f36-b379-840328f6350c
- Original site: https://mapbox.com
- Theme: `dark`
- Industry: `devtools`
- Recommended fit: **Dark webapp exploration**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Satellite console at midnight — a dark control room where glowing map tiles are the only light source, surrounded by near-black instrument panels.

## Apply to
- Dark theme experiments
- Operator-focused widgets
- High-contrast card systems

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Void Black | `#0e1012` | neutral | Primary text or dark surface |
| Deep Charcoal | `#15171b` | neutral | Primary text or dark surface |
| Gunmetal | `#1c1f24` | neutral | Primary text or dark surface |
| Graphite | `#23262d` | neutral | Primary text or dark surface |
| Steel | `#333943` | neutral | Primary text or dark surface |
| Pewter | `#444d5a` | neutral | Border, muted text, or supporting surface |
| Slate | `#566171` | neutral | Border, muted text, or supporting surface |
| Ash | `#8b96aa` | neutral | Border, muted text, or supporting surface |
| Fog | `#a0aaba` | neutral | Border, muted text, or supporting surface |
| Silver | `#bbc2ce` | neutral | Border, muted text, or supporting surface |

```css
:root {
  --ref-void-black: #0e1012;
  --ref-deep-charcoal: #15171b;
  --ref-gunmetal: #1c1f24;
  --ref-graphite: #23262d;
  --ref-steel: #333943;
  --ref-pewter: #444d5a;
  --ref-slate: #566171;
  --ref-ash: #8b96aa;
}
```

## Typography direction
- **Cera Pro**: 400, 500, 700, 10px, 14px, 15px, 16px, 18px, 20px, 24px, 32px, 44px, 56px, 68px, 1.00–1.60 (tighter at large sizes: 1.00–1.14 at 44–68px; looser at small: 1.40–1.60 at 14–18px); substitute `DM Sans, Plus Jakarta Sans`.

## Spacing / shape
- Section Gap: `96px`
- Card Padding: `24px`
- Element Gap: `12px`
- Page Max Width: `1344px`
- Radius: `cards: 24px, chips: 12px, badges: 4px, inputs: 6px, buttons: 100px`

## Surface cues
- **Void Floor** `#0e1012`: Page background, nav, footer — base canvas
- **Deep Panel** `#15171b`: Card backgrounds, content sections elevated from page
- **Raised Surface** `#1c1f24`: Nested panels, modal backgrounds, secondary cards
- **Overlay** `#23262d`: Dropdown menus, tooltips, hover overlays

## Component cues
- **CTA Button Group**: Reference component style.
- **Category Filter Tab Bar**: Reference component style.
- **Customer Story Card**: Reference component style.
- **Primary CTA Button**: Main call-to-action, 'Get started for free', 'Sign up'
- **Outlined Pill Button**: Secondary actions like 'Contact us', nav secondary links

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
