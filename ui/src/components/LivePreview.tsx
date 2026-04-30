import { useState } from "react";
import { Monitor, Smartphone, Moon, Sun, Loader2, AlertCircle } from "lucide-react";
import { cn } from "@/lib/utils";

export type Viewport = "desktop" | "tablet" | "mobile";

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
}

const EMPTY_DOC = `<!doctype html><meta charset="utf-8" /><title>preview</title><style>html,body{margin:0;height:100%;font-family:ui-sans-serif,system-ui,sans-serif;background:#0a0a0a;color:#e5e5e5;display:flex;align-items:center;justify-content:center}p{opacity:.6;font-size:13px}</style><p>No preview yet — adjust options on the left.</p>`;

export function LivePreview({
  html,
  isLoading = false,
  error = null,
  initialViewport = "desktop",
}: LivePreviewProps) {
  const [viewport, setViewport] = useState<Viewport>(initialViewport);
  const [dark, setDark] = useState(true);

  const width = VIEWPORT_WIDTH[viewport];
  const srcDoc = html ?? EMPTY_DOC;

  return (
    <section
      data-testid="live-preview"
      data-viewport={viewport}
      data-dark={dark ? "true" : "false"}
      aria-label="Live preview"
      className="bg-muted/30 relative flex h-full min-w-0 flex-col"
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
          <span className="bg-border h-5 w-px" aria-hidden="true" />
          <ToolbarButton
            label={dark ? "Switch to light" : "Switch to dark"}
            active={dark}
            onClick={() => setDark((d) => !d)}
            testid="vp-theme"
          >
            {dark ? <Moon className="size-3.5" /> : <Sun className="size-3.5" />}
          </ToolbarButton>
        </div>
      </header>

      <div className="flex flex-1 items-start justify-center overflow-auto p-4">
        <div
          className="border-border bg-background h-full border shadow-sm transition-[width]"
          style={{ width: `${width}px`, maxWidth: "100%" }}
          data-testid="preview-frame-container"
        >
          <iframe
            data-testid="preview-iframe"
            title="Live report preview"
            sandbox="allow-same-origin"
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
  children: React.ReactNode;
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
