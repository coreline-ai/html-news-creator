# Mercury - Refero Design MD

- Source: https://styles.refero.design/style/3172cd4d-118a-4a16-a259-6b634d32322e
- Original site: https://mercury.com
- Theme: `dark`
- Recommended fit: **Boardroom Deck / Premium Dashboard**
- Priority: **Supporting**

## Why this fits html-news-creator
Spacious premium dark direction for executive dashboard and presentation use: twilight palette, restrained typography, single blue CTA.

## Apply to
- Boardroom deck
- Monthly or weekly executive dashboard
- Premium dark landing for subscribers

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Mercury Blue | `#5266eb` | brand | Primary CTA buttons - the single, vivid accent in a muted palette, focusing user action. |
| Ghost Blue | `#cdddff` | accent | Secondary button backgrounds, hover states - a desaturated, ethereal blue suggesting interaction. |
| Deep Space | `#171721` | neutral | Outermost page background layer, providing depth. |
| Midnight Slate | `#1e1e2a` | neutral | Primary page and section backgrounds. |
| Graphite | `#272735` | neutral | Subtle button backgrounds and interactive surfaces. |
| Lead | `#70707d` | neutral | Borders, dividers, subtle UI accents. |
| Starlight | `#ededf3` | neutral | Primary text color for headlines, body, and navigation. |
| Silver | `#c3c3cc` | neutral | Secondary text, footer copy, disabled states. |

```css
:root {
  --ref-mercury-blue: #5266eb;
  --ref-ghost-blue: #cdddff;
  --ref-deep-space: #171721;
  --ref-midnight-slate: #1e1e2a;
  --ref-graphite: #272735;
  --ref-lead: #70707d;
  --ref-starlight: #ededf3;
}
```

## Typography direction
- Primary: **arcadiaDisplay**; substitute `Inter, Manrope`.
- Secondary/code: **arcadia**; substitute `Inter, Manrope`.

## Spacing / shape
- Section gap: `80-120px`
- Card padding: ``
- Element gap: `12-32px`
- Radius: `{'cards': '0px', 'inputs': '32px', 'buttons': '32px, 40px', 'containers': '4px'}`

## Agent notes
- Do not apply this wholesale to templates/report_newsstream.html.j2 unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- Keep the project content hierarchy first: section title, why it matters, source evidence, confidence, and image evidence.
