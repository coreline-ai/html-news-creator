# WhatsApp.com - Refero Design MD

- Source: https://styles.refero.design/style/a643f3a0-6c99-4076-b03f-6f0691c21bd0
- Original site: https://www.whatsapp.com
- Theme: `light`
- Industry: `media`
- Recommended fit: **Design reference / webapp exploration**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Warm, secure communication.

## Apply to
- General webapp UI exploration
- Demo cards and catalog surfaces
- Future admin/subscriber UI references

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Forest Green | `#25d366` | brand | Action accent / signal color |
| Link Blue | `#0373e9` | accent | Action accent / signal color |
| Midnight Graphite | `#1c1e21` | neutral | Primary text or dark surface |
| Dark Forest | `#111b21` | neutral | Primary text or dark surface |
| Warm Canvas | `#fcf5eb` | neutral | Page background or card surface |
| Pure White | `#ffffff` | neutral | Page background or card surface |
| Stone Gray | `#5e5e5e` | neutral | Border, muted text, or supporting surface |
| Light Fog | `#f0f4f9` | neutral | Page background or card surface |

```css
:root {
  --ref-forest-green: #25d366;
  --ref-link-blue: #0373e9;
  --ref-midnight-graphite: #1c1e21;
  --ref-dark-forest: #111b21;
  --ref-warm-canvas: #fcf5eb;
  --ref-pure-white: #ffffff;
  --ref-stone-gray: #5e5e5e;
  --ref-light-fog: #f0f4f9;
}
```

## Typography direction
- **WhatsApp Sans Var**: 400, 700, 12px, 16px, 18px, 48px, 60px, 80px, 1.00, 1.10, 1.20, 1.30, 1.33, 1.34, 1.38, 1.39; substitute `system-ui, sans-serif`.

## Spacing / shape
- Section Gap: `64px`
- Card Padding: `32px`
- Element Gap: `16px`
- Radius: `input: 50px, images: 25px, buttons: 50px, heroContainer: 25px, messageBubbles: 25px`

## Surface cues
- **Warm Canvas** `#fcf5eb`: Primary page background, soft and inviting.
- **Pure White** `#ffffff`: Raised card surfaces, navigation background, offering a clean, distinct content area.
- **Dark Forest** `#111b21`: Elevated section background (e.g., footer), interactive input fields, creating deep contrast for specific elements.

## Component cues
- **Primary Action Button**: Filled button for main calls to action
- **Secondary Ghost Button**: Outlined button for less prominent actions, often paired with primary
- **White Background Button**: Alternative interaction button against darker backgrounds
- **Navigation Link**: Text link within the main navigation bar
- **Card Surface**: Content containers

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
