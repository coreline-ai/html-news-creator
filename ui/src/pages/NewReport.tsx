import { useCallback, useState } from "react";
import { Play, Save, Sparkles } from "lucide-react";
import { RunOptionsPanel } from "@/components/RunOptionsPanel";
import { LivePreview } from "@/components/LivePreview";
import { SystemStatusBanner } from "@/components/SystemStatusBanner";
import { Button } from "@/components/ui/button";
import { useAppStore } from "@/lib/store";
import { usePreview } from "@/hooks/usePreview";
import { useSystemStatus } from "@/hooks/useSystemStatus";
import { apiFetch, ApiError } from "@/lib/api";

function apiErrorMessage(err: ApiError): string {
  const detail =
    err.body && typeof err.body === "object" && "detail" in err.body
      ? (err.body as { detail?: unknown }).detail
      : null;

  if (detail && typeof detail === "object" && "message" in detail) {
    const message = (detail as { message?: unknown }).message;
    if (typeof message === "string" && message) return message;
  }
  if (typeof detail === "string" && detail) return detail;
  return `Run failed: ${err.status} ${err.message}`;
}

export function NewReport() {
  const runOptions = useAppStore((s) => s.runOptions);
  const activeRun = useAppStore((s) => s.activeRun);
  const setActiveRun = useAppStore((s) => s.setActiveRun);

  const preview = usePreview(runOptions);
  const systemStatus = useSystemStatus();

  const [submitting, setSubmitting] = useState(false);
  const [actionError, setActionError] = useState<string | null>(null);
  const previewTheme = runOptions.output_theme;
  const canStartRun =
    !submitting && !activeRun && systemStatus.data?.can_generate === true;
  const runBlockedMessage =
    systemStatus.data?.llm?.message ??
    (systemStatus.isLoading
      ? "생성 가능 상태를 확인 중입니다."
      : "시스템 상태를 확인할 수 없어 실행을 막았습니다.");

  const handleRun = useCallback(async () => {
    setActionError(null);
    if (systemStatus.data?.can_generate !== true) {
      setActionError(runBlockedMessage);
      return;
    }
    setSubmitting(true);
    try {
      const res = await apiFetch<{ run_id: string }>("/api/runs", {
        method: "POST",
        body: JSON.stringify(runOptions),
      });
      if (!res?.run_id) {
        throw new Error("No run_id returned by /api/runs.");
      }
      setActiveRun({
        run_id: res.run_id,
        started_at: new Date().toISOString(),
        options: { ...runOptions },
      });
    } catch (err) {
      const msg =
        err instanceof ApiError
          ? apiErrorMessage(err)
          : err instanceof Error
            ? err.message
            : "Run failed.";
      setActionError(msg);
    } finally {
      setSubmitting(false);
    }
  }, [
    runBlockedMessage,
    runOptions,
    setActiveRun,
    systemStatus.data?.can_generate,
  ]);

  const handleSaveDraft = useCallback(() => {
    // Local-only for now: store snapshot in localStorage so closing the tab
    // does not lose tweaks. No server round-trip in Phase 3.
    try {
      window.localStorage.setItem(
        "newsstudio.runOptions.draft",
        JSON.stringify(runOptions),
      );
      setActionError(null);
    } catch {
      setActionError("Could not save draft to localStorage.");
    }
  }, [runOptions]);

  return (
    <div
      className="grid h-full min-h-0 overflow-hidden"
      style={{ gridTemplateRows: "auto auto minmax(0, 1fr)" }}
      data-testid="new-report-page"
    >
      <header
        className="border-border bg-card text-card-foreground sticky top-0 z-20 flex items-center justify-between gap-2 border-b px-4 py-3"
        data-testid="new-report-actionbar"
      >
        <div className="flex flex-col gap-1 text-xs">
          <div className="text-muted-foreground">
            Target date{" "}
            <span className="text-foreground font-mono">{runOptions.date}</span>
            {" · "}
            {runOptions.target_sections} sections{" · "}
            {runOptions.dry_run ? "dry-run" : "live"}
          </div>
          {actionError ? (
            <div
              role="alert"
              className="text-destructive max-w-[60vw] truncate"
              title={actionError}
            >
              {actionError}
            </div>
          ) : null}
        </div>
        <div className="flex items-center gap-2">
          <Button variant="outline" size="sm" onClick={handleSaveDraft}>
            <Save className="size-3.5" aria-hidden="true" />
            Save draft
          </Button>
          <Button
            size="sm"
            onClick={() => {
              void handleRun();
            }}
            disabled={!canStartRun}
            data-testid="run-button"
          >
            <Play className="size-3.5" aria-hidden="true" />
            {submitting
              ? "Starting…"
              : activeRun
                ? "Running…"
                : systemStatus.isLoading
                  ? "Checking…"
                  : systemStatus.data?.can_generate === false
                    ? "Proxy required"
                    : "Run"}
          </Button>
        </div>
      </header>

      <SystemStatusBanner className="border-x-0 border-t-0" />

      <div
        className="grid min-h-0 overflow-hidden"
        style={{ gridTemplateColumns: "minmax(360px, 40%) 1fr" }}
      >
        <RunOptionsPanel />
        <div className="relative flex min-h-0 min-w-0 flex-col overflow-hidden">
          {!preview.html && !preview.error ? (
            <div
              data-testid="new-report-preview-hint"
              role="note"
              className="border-border bg-muted/40 text-muted-foreground flex items-center gap-2 border-b px-4 py-2 text-xs"
            >
              <Sparkles className="size-3.5" aria-hidden="true" />
              <span>
                옵션을 변경하면 미리보기가 생성됩니다.
                {preview.isLoading ? " 첫 렌더 대기 중…" : ""}
              </span>
            </div>
          ) : null}
          <div className="min-h-0 flex-1 overflow-hidden">
            <LivePreview
              html={preview.html}
              isLoading={preview.isLoading}
              error={preview.error}
              theme={previewTheme}
            />
          </div>
        </div>
      </div>
    </div>
  );
}

export default NewReport;
