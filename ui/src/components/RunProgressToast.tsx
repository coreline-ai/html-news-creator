import { CheckCircle2, AlertTriangle, Loader2, X } from "lucide-react";
import type { RunStreamStatus, RunProgressEvent } from "@/hooks/useRunStream";
import { cn } from "@/lib/utils";

export interface RunProgressToastProps {
  status: RunStreamStatus;
  lastEvent: RunProgressEvent | null;
  events: RunProgressEvent[];
  error?: string | null;
  onDismiss?: () => void;
  title?: string;
  actionLabel?: string;
  onAction?: () => void;
}

export function RunProgressToast({
  status,
  lastEvent,
  events,
  error,
  onDismiss,
  title,
  actionLabel,
  onAction,
}: RunProgressToastProps) {
  if (status === "idle") return null;

  const pct = Math.round(
    Math.max(0, Math.min(1, lastEvent?.progress ?? 0)) * 100,
  );
  const defaultTitle =
    status === "running"
      ? "파이프라인 실행 중"
      : status === "done"
        ? "리포트 생성 완료"
        : status === "stalled"
          ? "응답 대기 중"
          : "실행 실패";
  const fallbackMessage =
    status === "running"
      ? "실행 로그를 연결하는 중입니다…"
      : status === "done"
        ? "최신 리포트가 준비되었습니다."
        : status === "stalled"
          ? "서버 응답을 기다리고 있습니다. 잠시 후 자동 복구를 시도합니다."
          : "실행 상태를 확인할 수 없습니다.";

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
        ) : status === "stalled" ? (
          <AlertTriangle
            className="size-4 text-[var(--status-warning)]"
            aria-hidden="true"
          />
        ) : (
          <AlertTriangle
            className="text-destructive size-4"
            aria-hidden="true"
          />
        )}
        <div className="text-foreground text-sm font-medium">
          {title ?? defaultTitle}
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
          fallbackMessage
        )}
      </div>

      {actionLabel && onAction ? (
        <button
          type="button"
          onClick={onAction}
          className="bg-primary text-primary-foreground hover:bg-primary/90 self-start px-2.5 py-1.5 text-[11px] font-semibold"
        >
          {actionLabel}
        </button>
      ) : null}
    </div>
  );
}

export default RunProgressToast;
