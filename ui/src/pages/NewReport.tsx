import { useCallback, useState } from "react";
import { Play, Save, Sparkles } from "lucide-react";
import { RunOptionsPanel } from "@/components/RunOptionsPanel";
import { LivePreview } from "@/components/LivePreview";
import { Button } from "@/components/ui/button";
import { useAppStore } from "@/lib/store";
import { usePreview } from "@/hooks/usePreview";
import { apiFetch, ApiError } from "@/lib/api";

export function NewReport() {
  const runOptions = useAppStore((s) => s.runOptions);
  const activeRun = useAppStore((s) => s.activeRun);
  const setActiveRun = useAppStore((s) => s.setActiveRun);

  const preview = usePreview(runOptions);

  const [submitting, setSubmitting] = useState(false);
  const [actionError, setActionError] = useState<string | null>(null);
  const previewTheme = runOptions.output_theme;

  const handleRun = useCallback(async () => {
    setActionError(null);
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
          ? `Run failed: ${err.status} ${err.message}`
          : err instanceof Error
            ? err.message
            : "Run failed.";
      setActionError(msg);
    } finally {
      setSubmitting(false);
    }
  }, [runOptions, setActiveRun]);

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
      style={{ gridTemplateRows: "auto minmax(0, 1fr)" }}
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
            disabled={submitting || Boolean(activeRun)}
            data-testid="run-button"
          >
            <Play className="size-3.5" aria-hidden="true" />
            {submitting
              ? "Starting…"
              : activeRun
                ? "Running…"
                : "Run"}
          </Button>
        </div>
      </header>

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
