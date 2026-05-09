# Koto - Refero Design MD

- Source: https://styles.refero.design/style/a88fa835-1d5e-4b8e-b3d5-602597870563
- Original site: https://koto.com
- Theme: `dark`
- Industry: `agency`
- Recommended fit: **Dark webapp exploration**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Midnight gallery, etched steel.

## Apply to
- Dark theme experiments
- Operator-focused widgets
- High-contrast card systems

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Charcoal | `#060606` | neutral | Primary text or dark surface |
| Dark Void | `#141414` | neutral | Primary text or dark surface |
| Silver Whisper | `#989898` | neutral | Border, muted text, or supporting surface |
| Ghost Gray | `#595959` | neutral | Border, muted text, or supporting surface |
| Lineage Edge | `#202020` | neutral | Primary text or dark surface |
| Pale Ash | `#b4b4b4` | neutral | Border, muted text, or supporting surface |
| White Canvas | `#ffffff` | neutral | Page background or card surface |
| Koto Yellow | `#ffe800` | accent | Action accent / signal color |

```css
:root {
  --ref-midnight-charcoal: #060606;
  --ref-dark-void: #141414;
  --ref-silver-whisper: #989898;
  --ref-ghost-gray: #595959;
  --ref-lineage-edge: #202020;
  --ref-pale-ash: #b4b4b4;
  --ref-white-canvas: #ffffff;
  --ref-koto-yellow: #ffe800;
}
```

## Typography direction
- **gtKotoheimCondensed**: 300, 38px, 48px, 1.00, 1.10; substitute `Oswald Light`.
- **gtKotoheim**: 350, 400, 12px, 14px, 16px, 1.25, 1.50; substitute `Inter`.

## Spacing / shape
- Section Gap: `48px`
- Card Padding: `36px`
- Element Gap: `8px`
- Radius: `cards: 6px, buttons: 0px, default: 2px`

## Surface cues
- **Midnight Charcoal** `#060606`: Base page background and primary content areas.
- **Dark Void (Subtle)** `#141414`: Slightly elevated surfaces for small UI elements like icons or placeholder card backgrounds (when visible).
- **Card Surface** `#0000001a`: A semi-transparent layer over Midnight Charcoal, used for content cards, giving a subtle frosted glass effect.

## Component cues
- **Ghost Navigation Link**: Primary navigation and interactive text links.
- **Footer Link**: Secondary navigation and informational links within the footer.
- **Content Card**: Container for showcasing work, content, or features.
- **Ghost Button**: Generic interactive element, with a text label.
- **Koto Logo**: Brand identification in header.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
