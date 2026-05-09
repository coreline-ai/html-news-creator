# Refero - Refero Design MD

- Source: https://styles.refero.design/style/3f296d6e-6a1c-45db-829b-afb078d49ab4
- Original site: https://refero.design/mcp
- Theme: `light`
- Industry: `design`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Editorial ink on white marble — a typographer's product page where the serif headline IS the brand, and everything else stays out of its way.

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Pure Canvas | `#ffffff` | neutral | Page background or card surface |
| Frost Surface | `#f7f8fb` | neutral | Page background or card surface |
| Midnight Ink | `#000000` | neutral | Primary text or dark surface |
| Deep Charcoal | `#13151b` | neutral | Primary text or dark surface |
| Graphite | `#2d313f` | neutral | Primary text or dark surface |
| Slate | `#525769` | neutral | Border, muted text, or supporting surface |
| Ash | `#777d90` | neutral | Border, muted text, or supporting surface |
| Fog | `#9fa5ba` | neutral | Border, muted text, or supporting surface |
| Modal Veil | `#0c2970` | accent | Action accent / signal color |

```css
:root {
  --ref-pure-canvas: #ffffff;
  --ref-frost-surface: #f7f8fb;
  --ref-midnight-ink: #000000;
  --ref-deep-charcoal: #13151b;
  --ref-graphite: #2d313f;
  --ref-slate: #525769;
  --ref-ash: #777d90;
  --ref-fog: #9fa5ba;
}
```

## Typography direction
- **Title (custom serif)**: 400, 36px, 40px, 50px, 64px, 1.12–1.28; substitute `Playfair Display 400, or Georgia for fallback`.
- **Base-Variable (custom sans)**: 500, 600, 650, 13px, 15px, 16px, 17px, 20px, 25px, 1.40–1.60 for body, 0.96–1.20 for tight UI labels; substitute `Inter Variable or DM Sans`.

## Spacing / shape
- Section Gap: `80px`
- Card Padding: `24px`
- Element Gap: `12px`
- Page Max Width: `1200px`
- Radius: `tags: 8px, cards: 64px, small: 4px, inputs: 12px, modals: 24px, panels: 20px, buttons: 9999px`

## Surface cues
- **Page Canvas** `#ffffff`: Base page background for all content sections
- **Frost Surface** `#f7f8fb`: Secondary containers: nav segmented control background, subtle section washes
- **Card Tint** `#f4f5fb`: Feature cards at rgba(55,80,155,0.04) over white — barely-perceptible blue-gray tint distinguishing card from canvas
- **Elevated Panel** `#ffffff`: Modal dialogs, product demo frames — white surface defined by inset ring shadow rather than color change

## Component cues
- **Button Group — Primary + Secondary**: Reference component style.
- **Platform Toggle — Web / iOS Segmented Control**: Reference component style.
- **Announcement Chip + Hero Headline Block**: Reference component style.
- **Black Pill Button (Primary)**: Primary call-to-action, install/demo actions
- **Ghost Pill Button (Secondary)**: Secondary action alongside the primary pill

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
