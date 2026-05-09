# Typeform - Refero Design MD

- Source: https://styles.refero.design/style/a0d54731-58dc-448b-a6b0-ed543f397ab1
- Original site: https://typeform.com
- Theme: `mixed`
- Industry: `saas`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Publishing house meets product dashboard — serif headlines borrowed from a literary journal, UI chrome stripped to bare minimum so the type can own every screen.

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Aubergine Ink | `#2a222b` | brand | Action accent / signal color |
| Deep Plum | `#3e3040` | brand | Action accent / signal color |
| Violet Mist | `#9454ab` | accent | Action accent / signal color |
| Lavender Whisper | `#ddb7f0` | accent | Action accent / signal color |
| Cream Canvas | `#faf9fb` | neutral | Page background or card surface |
| Pure White | `#ffffff` | neutral | Page background or card surface |
| Charcoal | `#222222` | neutral | Primary text or dark surface |
| Slate Mid | `#564b58` | neutral | Border, muted text, or supporting surface |
| Ash | `#655d67` | neutral | Border, muted text, or supporting surface |
| Fog | `#837a85` | neutral | Border, muted text, or supporting surface |

```css
:root {
  --ref-aubergine-ink: #2a222b;
  --ref-deep-plum: #3e3040;
  --ref-violet-mist: #9454ab;
  --ref-lavender-whisper: #ddb7f0;
  --ref-cream-canvas: #faf9fb;
  --ref-pure-white: #ffffff;
  --ref-charcoal: #222222;
  --ref-slate-mid: #564b58;
}
```

## Typography direction
- **Tobias**: 400, 64px, 72px, 80px, 1.00–1.10; substitute `Playfair Display, Freight Display Pro`.
- **TWK Lausanne**: 350, 14px, 16px, 20px, 1.10; substitute `Inter var at weight 350, Neue Haas Grotesk`.
- **TWK Lausanne**: 400, 16px, 1.00–1.49; substitute `Inter, Aktiv Grotesk`.

## Spacing / shape
- Section Gap: `64px`
- Element Gap: `16px`
- Page Max Width: `1536px`
- Radius: `cards: 24px, pills: 80px, images: 8px, buttons: 12px`

## Surface cues
- **Dark Canvas** `#2a222b`: Hero section, announcement banner, CTA buttons — the dominant dark surface
- **Dark Elevated** `#3e3040`: Slightly lighter dark surface within hero context
- **Cream Canvas** `#faf9fb`: Primary light page background, nav bar
- **Parchment** `#f5f3f6`: Alternate light sections, subtle differentiation from cream canvas
- **Pure White** `#ffffff`: Card surfaces, integration pills, elevated components on light backgrounds

## Component cues
- **Announcement Banner**: Reference component style.
- **Feature Content Block**: Reference component style.
- **Integrations Section**: Reference component style.
- **Primary CTA Button**: Main call to action throughout the page
- **Ghost Navigation Button**: Secondary actions, nav-level text links with chevrons

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
