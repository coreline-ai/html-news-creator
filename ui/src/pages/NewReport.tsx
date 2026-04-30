import { useCallback, useState } from "react";
import { useNavigate } from "react-router-dom";
import { Play, Save, Sparkles } from "lucide-react";
import { RunOptionsPanel } from "@/components/RunOptionsPanel";
import { LivePreview } from "@/components/LivePreview";
import { RunProgressToast } from "@/components/RunProgressToast";
import { Button } from "@/components/ui/button";
import { useAppStore } from "@/lib/store";
import { usePreview } from "@/hooks/usePreview";
import { useRunStream } from "@/hooks/useRunStream";
import { apiFetch, ApiError } from "@/lib/api";

export function NewReport() {
  const runOptions = useAppStore((s) => s.runOptions);
  const navigate = useNavigate();

  const preview = usePreview(runOptions);

  const [runId, setRunId] = useState<string | null>(null);
  const [submitting, setSubmitting] = useState(false);
  const [actionError, setActionError] = useState<string | null>(null);
  const [toastDismissed, setToastDismissed] = useState(false);

  const stream = useRunStream(runId);

  // Once the stream signals done, navigate to the review page.
  if (stream.status === "done" && runId) {
    // Schedule navigation after current render commit.
    queueMicrotask(() => {
      navigate(`/reports/${runOptions.date}`);
    });
  }

  const handleRun = useCallback(async () => {
    setActionError(null);
    setToastDismissed(false);
    setSubmitting(true);
    try {
      const res = await apiFetch<{ run_id: string }>("/api/runs", {
        method: "POST",
        body: JSON.stringify(runOptions),
      });
      if (!res?.run_id) {
        throw new Error("No run_id returned by /api/runs.");
      }
      setRunId(res.run_id);
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
  }, [runOptions]);

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

  const showToast =
    !toastDismissed && (stream.status !== "idle" || Boolean(actionError));

  const dismissToast = () => {
    setToastDismissed(true);
    if (stream.status !== "running") {
      setRunId(null);
    }
  };

  return (
    <div
      className="grid h-full min-h-0"
      style={{ gridTemplateRows: "1fr auto" }}
      data-testid="new-report-page"
    >
      <div
        className="grid min-h-0"
        style={{ gridTemplateColumns: "minmax(360px, 40%) 1fr" }}
      >
        <RunOptionsPanel />
        <div className="relative flex min-w-0 flex-col">
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
          <div className="min-h-0 flex-1">
            <LivePreview
              html={preview.html}
              isLoading={preview.isLoading}
              error={preview.error}
            />
          </div>
        </div>
      </div>

      <footer
        className="border-border bg-card text-card-foreground sticky bottom-0 flex items-center justify-between gap-2 border-t px-4 py-3"
        data-testid="new-report-actionbar"
      >
        <div className="text-muted-foreground text-xs">
          Target date{" "}
          <span className="text-foreground font-mono">{runOptions.date}</span>
          {" · "}
          {runOptions.target_sections} sections{" · "}
          {runOptions.dry_run ? "dry-run" : "live"}
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
            disabled={submitting || stream.status === "running"}
            data-testid="run-button"
          >
            <Play className="size-3.5" aria-hidden="true" />
            {submitting
              ? "Starting…"
              : stream.status === "running"
                ? "Running…"
                : "Run"}
          </Button>
        </div>
      </footer>

      {showToast ? (
        <RunProgressToast
          status={actionError ? "error" : stream.status}
          lastEvent={stream.lastEvent}
          events={stream.events}
          error={actionError ?? stream.error}
          onDismiss={dismissToast}
        />
      ) : null}
    </div>
  );
}

export default NewReport;
