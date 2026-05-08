# Enviar Dinero - Colorful Refero Design MD

- Source: https://styles.refero.design/style/46c16139-b0bb-49e6-95dc-74bef576e5ce
- Original site: https://paypal.com
- Theme: `mixed`
- Color rank: **38**
- Colorfulness score: `30.0`
- Recommended fit: **Gradient / luminous dashboard**

## North star
Electric Sky Wallet - a sky that you can spend from.

## Why this fits html-news-creator
Use for premium dashboards, boardroom decks, and hero surfaces where the product needs a stronger visual identity.

## Apply to
- Boardroom deck covers
- Trend overview hero sections
- Premium dashboard headers

## Color tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Cerulean Surge | `#60CDFF` | brand | Hero backgrounds, section backgrounds, badge borders - the dominant attention color that establishes PayPal's sky-blue. |
| Cobalt Vault | `#002991` | brand | Deep-section backgrounds, card fills, navy sections - counterpoint to Cerulean Surge, appearing in feature sections to. |
| Ice Mist | `#B8E9FF` | accent | Subtle background tints in transitional or secondary panels within the blue range |
| Cobalt Fade | `#002991` | accent | Gradient overlay used to bleed navy into transparent sections - see linear-gradient underline/band effect on interactiv. |
| Midnight | `#000000` | neutral | Page text, button borders (black variant), nav items, headings on light/sky backgrounds |
| Snow | `#FFFFFF` | neutral | Page backgrounds, card surfaces, button borders (white variant on dark/colored fields), body text on dark sections |
| Parchment | `#F1EFEA` | neutral | Warm off-white panel backgrounds - appears in transitional content sections |
| Ash | `#B3B3B3` | neutral | Inactive/ghost card backgrounds, dimmed UI state fills |

```css
:root {
  --colorful-cerulean-surge: #60CDFF;
  --colorful-cobalt-vault: #002991;
  --colorful-ice-mist: #B8E9FF;
  --colorful-cobalt-fade: #002991;
  --colorful-midnight: #000000;
  --colorful-snow: #FFFFFF;
  --colorful-parchment: #F1EFEA;
}
```

## Typography direction
- Primary: **Plain**; substitute `DM Sans, Inter`.
- Secondary/code: **PayPal Pro**; substitute `Sohne, Aktiv Grotesk ExtraBold, Neue Haas Grotesk Display 900`.

## Guardrails
- Treat these as accent and exploration references. Do not turn the production report into a rainbow UI without a separate migration request.
- Use color semantically: category, status, confidence, evidence type, or section emphasis.
- Keep report readability first; colorful surfaces should support hierarchy, not compete with source evidence.
