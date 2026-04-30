import { CheckCircle2, AlertTriangle, Loader2, X } from "lucide-react";
import type { RunStreamStatus, RunProgressEvent } from "@/hooks/useRunStream";
import { cn } from "@/lib/utils";

export interface RunProgressToastProps {
  status: RunStreamStatus;
  lastEvent: RunProgressEvent | null;
  events: RunProgressEvent[];
  error?: string | null;
  onDismiss?: () => void;
}

export function RunProgressToast({
  status,
  lastEvent,
  events,
  error,
  onDismiss,
}: RunProgressToastProps) {
  if (status === "idle") return null;

  const pct = Math.round(
    Math.max(0, Math.min(1, lastEvent?.progress ?? 0)) * 100,
  );

  return (
    <div
      role="status"
      aria-live="polite"
      data-testid="run-progress-toast"
      data-status={status}
      className={cn(
        "border-border bg-card text-card-foreground fixed right-6 bottom-6 z-50 flex w-80 flex-col gap-2 border p-3 shadow-lg",
      )}
    >
      <div className="flex items-center gap-2">
        {status === "running" ? (
          <Loader2
            className="text-primary size-4 animate-spin"
            aria-hidden="true"
          />
        ) : status === "done" ? (
          <CheckCircle2
            className="text-primary size-4"
            aria-hidden="true"
          />
        ) : (
          <AlertTriangle
            className="text-destructive size-4"
            aria-hidden="true"
          />
        )}
        <div className="text-foreground text-sm font-medium">
          {status === "running"
            ? "Running pipeline"
            : status === "done"
              ? "Run complete"
              : "Run failed"}
        </div>
        {onDismiss ? (
          <button
            type="button"
            onClick={onDismiss}
            aria-label="Dismiss"
            className="text-muted-foreground hover:text-foreground ml-auto"
          >
            <X className="size-3.5" />
          </button>
        ) : null}
      </div>

      <div
        className="bg-muted relative h-1.5 w-full overflow-hidden rounded-full"
        aria-label="Run progress"
      >
        <div
          className={cn(
            "h-full transition-[width]",
            status === "error" ? "bg-destructive" : "bg-primary",
          )}
          style={{ width: `${pct}%` }}
          data-testid="run-progress-bar"
        />
      </div>

      <div className="text-muted-foreground text-[11px]">
        {error ? (
          <span className="text-destructive">{error}</span>
        ) : lastEvent ? (
          <>
            <span className="text-foreground font-mono">{lastEvent.step}</span>
            {lastEvent.message ? ` — ${lastEvent.message}` : null}
            {" · "}
            {events.length} event{events.length === 1 ? "" : "s"}
          </>
        ) : (
          "Waiting for first event…"
        )}
      </div>
    </div>
  );
}

export default RunProgressToast;
