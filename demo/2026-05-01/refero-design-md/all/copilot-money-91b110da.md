# Copilot Money - Refero Design MD

- Source: https://styles.refero.design/style/91b110da-902b-4d09-8bf0-26bd1f25f8b2
- Original site: https://copilot.money
- Theme: `dark`
- Industry: `fintech`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Midnight ocean with glowing buoys

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Ink | `#000814` | neutral | Primary text or dark surface |
| Deep Space | `#010d1e` | neutral | Primary text or dark surface |
| Obsidian | `#11263b` | neutral | Primary text or dark surface |
| Mist Gray | `#ccced0` | neutral | Border, muted text, or supporting surface |
| Shadow Blue | `#29303a` | neutral | Action accent / signal color |
| Deep Shadow | `#303741` | neutral | Primary text or dark surface |
| Muted Stone | `#7f8ba4` | neutral | Border, muted text, or supporting surface |
| Platinum Ghost | `#ffffff` | neutral | Page background or card surface |
| Teal Glow | `#00cc4b` | accent | Action accent / signal color |
| Crimson Beam | `#ff4433` | accent | Action accent / signal color |

```css
:root {
  --ref-midnight-ink: #000814;
  --ref-deep-space: #010d1e;
  --ref-obsidian: #11263b;
  --ref-mist-gray: #ccced0;
  --ref-shadow-blue: #29303a;
  --ref-deep-shadow: #303741;
  --ref-muted-stone: #7f8ba4;
  --ref-platinum-ghost: #ffffff;
}
```

## Typography direction
- **Matter Variable Thin**: 100, 11px, 12px, 13px, 14px, 15px, 16px, 18px, 22px, 38px, 56px, 1.20, 1.30, 1.40, 1.60.
- **Jokker Medium**: 500, 12px, 14px, 16px, 18px, 22px, 24px, 32px, 64px, 1.00, 1.09, 1.10, 1.20, 1.40, 1.60.
- **Matter-TRIAL SemiBold**: 670, 28px, 1.00.

## Spacing / shape
- Section Gap: `40px`
- Card Padding: `16px`
- Element Gap: `16px`
- Radius: `tags: 40px, cards: 24px, buttons: 16px, smallElements: 8px, inlineElements: 12px`

## Surface cues
- **Canvas** `#000814`: Primary page background, base for all content.
- **Base Surface** `#010d1`: Slightly elevated backgrounds, subtle background differences within sections.
- **Interactive Card** `#000814`: Container for featured content, distinguished by soft shadows and rounded corners.
- **Vibrant Tag Surface** `#ff33aa`: Dynamic, colored containers for categorization, featuring prominent inset shadows and rounded forms.

## Component cues
- **Primary Filled Button**: Call to action button for primary user flows.
- **Ghost Button**: Secondary action or navigation link.
- **Floating Content Card**: Displaying featured content or information blocks.
- **Vibrant Category Tag**: Categorization of items, dynamically colored.
- **Navigation Link**: Primary navigation elements in header or footer.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
