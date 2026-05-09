# Checkly - Refero Design MD

- Source: https://styles.refero.design/style/78558b01-c101-4b8e-8401-db91269b1150
- Original site: https://www.checklyhq.com
- Theme: `dark`
- Industry: `devtools`
- Recommended fit: **Admin console / run monitor / developer tooling**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Midnight Terminal Canvas

## Apply to
- Admin run monitor and review states
- Compact evidence cards and source inspection panels
- Dark-mode operational dashboards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Deep Space Blue | `#041734` | brand | Action accent / signal color |
| Midnight Ink | `#002652` | brand | Action accent / signal color |
| Charcoal Slate | `#0f172a` | neutral | Primary text or dark surface |
| Storm Gray | `#374151` | neutral | Border, muted text, or supporting surface |
| Dark Steel | `#1f2937` | neutral | Primary text or dark surface |
| Light Ash | `#a7babe` | neutral | Border, muted text, or supporting surface |
| Electric Blue | `#0075ff` | accent | Action accent / signal color |
| Subtle Gray | `#445458` | neutral | Border, muted text, or supporting surface |
| Navy Black | `#061220` | neutral | Primary text or dark surface |
| Code Block Gray | `#1a1f36` | neutral | Primary text or dark surface |

```css
:root {
  --ref-deep-space-blue: #041734;
  --ref-midnight-ink: #002652;
  --ref-charcoal-slate: #0f172a;
  --ref-storm-gray: #374151;
  --ref-dark-steel: #1f2937;
  --ref-light-ash: #a7babe;
  --ref-electric-blue: #0075ff;
  --ref-subtle-gray: #445458;
}
```

## Typography direction
- **Inter**: 300, 400, 500, 600, 700, 10px, 12px, 14px, 16px, 18px, 20px, 24px, 30px, 32px, 48px, 60px, 1.00, 1.20, 1.25, 1.33, 1.40, 1.43, 1.50, 1.56, 1.63, 2.40; substitute `system-ui`.
- **ui-monospace**: 400, 500, 11px, 12px, 14px, 1.33, 1.43, 1.63; substitute `monospace`.
- **JetBrains Mono**: 400, 10px, 12px, 16px, 1.50, 1.63; substitute `monospace`.

## Spacing / shape
- Section Gap: `48px`
- Element Gap: `12px`
- Radius: `tags: 9999px, cards: 12px, inputs: 4px, buttons: 8px`

## Surface cues
- **Deep Space Blue Canvas** `#041734`: Primary page background for hero sections and base content.
- **Dark Steel Card Surface** `#1f2937`: Default background for major content cards and information panels.
- **Charcoal Slate Code Surface** `#0f172a`: Elevated surface for code blocks and console-like displays.
- **Deep Ocean Blue Inset Card** `#001027`: Highest elevation for detailed data cards with an inset shadow effect.

## Component cues
- **Floating Action Button**: Key action buttons with a distinct, larger appearance.
- **Solid Action Button**: Primary interactive buttons for calls to action.
- **Ghost Outline Button**: Secondary or tertiary actions, often subtle.
- **Text Link Button**: Inline actions or navigation items that act as buttons.
- **Default Card**: Base container for content, appearing within sections.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
