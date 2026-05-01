import { useMemo, useState, type ReactNode } from "react";
import { Monitor, Smartphone, Loader2, AlertCircle } from "lucide-react";
import { cn } from "@/lib/utils";

export type Viewport = "desktop" | "tablet" | "mobile";
export type PreviewTheme = "dark" | "light" | "newsroom-white";

const VIEWPORT_WIDTH: Record<Viewport, number> = {
  desktop: 1280,
  tablet: 768,
  mobile: 375,
};

export interface LivePreviewProps {
  html: string | null;
  isLoading?: boolean;
  error?: string | null;
  /** Initial viewport — desktop by default. */
  initialViewport?: Viewport;
  /** Report preview theme. This follows output settings, not a local toolbar toggle. */
  theme?: PreviewTheme;
}

const EMPTY_DOC: Record<PreviewTheme, string> = {
  dark: `<!doctype html><html data-theme="dark"><meta charset="utf-8" /><title>preview</title><style>html,body{margin:0;height:100%;font-family:ui-sans-serif,system-ui,sans-serif;background:#0a0a0a;color:#e5e5e5;display:flex;align-items:center;justify-content:center}p{opacity:.6;font-size:13px}</style><p>No preview yet — adjust options on the left.</p></html>`,
  light: `<!doctype html><html data-theme="light"><meta charset="utf-8" /><title>preview</title><style>html,body{margin:0;height:100%;font-family:ui-sans-serif,system-ui,sans-serif;background:#ffffff;color:#171717;display:flex;align-items:center;justify-content:center}p{opacity:.6;font-size:13px}</style><p>No preview yet — adjust options on the left.</p></html>`,
  "newsroom-white": `<!doctype html><html data-theme="newsroom-white"><meta charset="utf-8" /><title>preview</title><style>html,body{margin:0;height:100%;font-family:ui-serif,Georgia,serif;background:#f8fafc;color:#020617;display:flex;align-items:center;justify-content:center}p{opacity:.62;font-size:13px}</style><p>No preview yet — adjust options on the left.</p></html>`,
};

function applyPreviewTheme(html: string, theme: PreviewTheme): string {
  if (/<html\b[^>]*\bdata-theme=(["'])[^"']*\1/i.test(html)) {
    return html.replace(
      /(<html\b[^>]*\bdata-theme=)(["'])[^"']*(\2)/i,
      `$1$2${theme}$3`,
    );
  }
  if (/<html\b/i.test(html)) {
    return html.replace(/<html\b([^>]*)>/i, `<html$1 data-theme="${theme}">`);
  }
  return `<html data-theme="${theme}"><body>${html}</body></html>`;
}

export function LivePreview({
  html,
  isLoading = false,
  error = null,
  initialViewport = "desktop",
  theme = "dark",
}: LivePreviewProps) {
  const [viewport, setViewport] = useState<Viewport>(initialViewport);

  const width = VIEWPORT_WIDTH[viewport];
  const srcDoc = useMemo(
    () => (html ? applyPreviewTheme(html, theme) : EMPTY_DOC[theme]),
    [html, theme],
  );

  return (
    <section
      data-testid="live-preview"
      data-viewport={viewport}
      data-theme={theme}
      aria-label="Live preview"
      className="bg-muted/30 relative flex h-full min-h-0 min-w-0 flex-col overflow-hidden"
    >
      <header className="border-border bg-card text-card-foreground flex items-center justify-between border-b px-4 py-2">
        <div className="text-muted-foreground flex items-center gap-2 text-[11px]">
          {isLoading ? (
            <>
              <Loader2 className="size-3.5 animate-spin" aria-hidden="true" />
              <span>Rendering preview…</span>
            </>
          ) : error ? (
            <>
              <AlertCircle
                className="text-destructive size-3.5"
                aria-hidden="true"
              />
              <span className="text-destructive">{error}</span>
            </>
          ) : (
            <span>{html ? "Preview ready" : "Idle"}</span>
          )}
        </div>

        <div
          role="toolbar"
          aria-label="Preview viewport"
          className="border-border flex items-center gap-0 rounded-md border"
        >
          <ToolbarButton
            label="Desktop (1280px)"
            active={viewport === "desktop"}
            onClick={() => setViewport("desktop")}
            testid="vp-desktop"
          >
            <Monitor className="size-3.5" />
          </ToolbarButton>
          <ToolbarButton
            label="Tablet (768px)"
            active={viewport === "tablet"}
            onClick={() => setViewport("tablet")}
            testid="vp-tablet"
          >
            <Monitor className="size-3.5 rotate-90" />
          </ToolbarButton>
          <ToolbarButton
            label="Mobile (375px)"
            active={viewport === "mobile"}
            onClick={() => setViewport("mobile")}
            testid="vp-mobile"
          >
            <Smartphone className="size-3.5" />
          </ToolbarButton>
        </div>
      </header>

      <div className="flex min-h-0 flex-1 items-start justify-center overflow-auto p-4">
        <div
          className="border-border bg-background h-full border shadow-sm transition-[width]"
          style={{ width: `${width}px`, maxWidth: "100%" }}
          data-testid="preview-frame-container"
        >
          <iframe
            data-testid="preview-iframe"
            title="Live report preview"
            // Generated report HTML includes the floating 3-theme switcher
            // script. Keep the iframe sandboxed, but allow that script to
            // cycle dark/light/newsroom-white inside the report document.
            sandbox="allow-scripts"
            srcDoc={srcDoc}
            className="block h-full w-full border-0"
            style={{ minHeight: 600, width: `${width}px`, maxWidth: "100%" }}
          />
        </div>
      </div>
    </section>
  );
}

function ToolbarButton({
  active,
  onClick,
  label,
  children,
  testid,
}: {
  active: boolean;
  onClick: () => void;
  label: string;
  children: ReactNode;
  testid?: string;
}) {
  return (
    <button
      type="button"
      onClick={onClick}
      aria-label={label}
      aria-pressed={active}
      data-testid={testid}
      className={cn(
        "inline-flex h-7 w-8 items-center justify-center text-xs transition-colors",
        active
          ? "bg-primary text-primary-foreground"
          : "text-muted-foreground hover:text-foreground",
      )}
    >
      {children}
    </button>
  );
}

export default LivePreview;
