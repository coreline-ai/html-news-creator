import { useEffect, useMemo, useState } from "react";
import { useParams, Link, useNavigate } from "react-router-dom";
import {
  Dialog,
  DialogContent,
  DialogDescription,
  DialogFooter,
  DialogHeader,
  DialogTitle,
} from "@/components/ui/dialog";
import { Button } from "@/components/ui/button";
import { Skeleton } from "@/components/ui/skeleton";
import { EmptyState } from "@/components/EmptyState";
import { SectionList } from "@/components/SectionList";
import { SectionEditor } from "@/components/SectionEditor";
import { useReport } from "@/hooks/useReports";
import {
  usePatchSection,
  usePublishReport,
  useRegenerateSection,
  useReorderSections,
} from "@/hooks/useSections";
import { useReviewStore } from "@/hooks/useReviewStore";
import type { ReportSection } from "@/lib/api";
import { AlertCircle, Download, Eye, FileText, Pencil, Send } from "lucide-react";
import { cn } from "@/lib/utils";

interface Toast {
  id: number;
  message: string;
  url?: string;
  tone?: "success" | "error" | "info";
}

export function ReviewReport() {
  const { date } = useParams<{ date: string }>();
  const navigate = useNavigate();

  const reportQuery = useReport(date);
  const patch = usePatchSection();
  const regen = useRegenerateSection();
  const reorder = useReorderSections();
  const publish = usePublishReport();

  const previewMode = useReviewStore((s) => s.previewMode);
  const setPreviewMode = useReviewStore((s) => s.setPreviewMode);
  const selectedSectionId = useReviewStore((s) => s.selectedSectionId);
  const selectSection = useReviewStore((s) => s.selectSection);
  const disabledSectionIds = useReviewStore((s) => s.disabledSectionIds);
  const toggleSectionEnabled = useReviewStore((s) => s.toggleSectionEnabled);
  const reset = useReviewStore((s) => s.reset);

  const [orderedSections, setOrderedSections] = useState<ReportSection[]>([]);
  const [confirmPublish, setConfirmPublish] = useState(false);
  const [perSectionError, setPerSectionError] = useState<
    Record<string, string>
  >({});
  const [toasts, setToasts] = useState<Toast[]>([]);

  // Reset store when navigating away from the page or to a different date.
  useEffect(() => {
    return () => {
      reset();
    };
  }, [reset]);

  // Hydrate local ordered list whenever the server payload arrives.
  useEffect(() => {
    if (reportQuery.data?.sections) {
      setOrderedSections([...reportQuery.data.sections]);
    }
  }, [reportQuery.data]);

  const selectedSection = useMemo(
    () =>
      orderedSections.find((s) => s.id === selectedSectionId) ?? null,
    [orderedSections, selectedSectionId],
  );

  const pushToast = (t: Omit<Toast, "id">) => {
    const id = Date.now() + Math.random();
    setToasts((prev) => [...prev, { ...t, id }]);
    setTimeout(() => {
      setToasts((prev) => prev.filter((x) => x.id !== id));
    }, 6000);
  };

  if (!date) {
    return (
      <div className="mx-auto max-w-[1200px] px-6 py-6">
        <EmptyState
          title="Missing report date"
          description="Open a report from the dashboard."
          action={
            <Button asChild size="sm" variant="outline">
              <Link to="/">Back to dashboard</Link>
            </Button>
          }
        />
      </div>
    );
  }

  if (reportQuery.isLoading) {
    return (
      <div className="mx-auto grid h-full min-h-0 max-w-[1400px] grid-rows-[auto_minmax(0,1fr)] gap-4 px-6 py-6">
        <Skeleton className="h-8 w-64" />
        <div
          className="grid min-h-0 gap-4"
          style={{ gridTemplateColumns: "40% 60%" }}
        >
          <Skeleton className="h-full min-h-0" />
          <Skeleton className="h-full min-h-0" />
        </div>
      </div>
    );
  }

  if (reportQuery.isError) {
    return (
      <div className="mx-auto max-w-[1200px] px-6 py-6">
        <EmptyState
          icon={AlertCircle}
          title="Could not load report"
          description={
            reportQuery.error instanceof Error
              ? reportQuery.error.message
              : "Backend error."
          }
          action={
            <Button
              size="sm"
              variant="outline"
              onClick={() => void reportQuery.refetch()}
            >
              Retry
            </Button>
          }
        />
      </div>
    );
  }

  const handleReorder = async (newIds: string[]) => {
    // Optimistic UI update
    const byId = new Map(orderedSections.map((s) => [s.id, s]));
    const next = newIds
      .map((id) => byId.get(id))
      .filter((s): s is ReportSection => Boolean(s));
    setOrderedSections(
      next.map((s, i) => ({ ...s, section_order: i })),
    );
    try {
      const res = await reorder.mutateAsync({ date, sectionIds: newIds });
      if (res?.sections) setOrderedSections(res.sections);
    } catch (err) {
      pushToast({
        message:
          err instanceof Error ? err.message : "Reorder failed",
        tone: "error",
      });
      // Roll back from server
      if (reportQuery.data?.sections) {
        setOrderedSections([...reportQuery.data.sections]);
      }
    }
  };

  const handleSave = async (
    patchPayload: Parameters<typeof patch.mutateAsync>[0]["patch"],
  ) => {
    if (!selectedSection) return;
    try {
      const res = await patch.mutateAsync({
        sectionId: selectedSection.id,
        patch: patchPayload,
        date,
      });
      // Merge into local list
      setOrderedSections((prev) =>
        prev.map((s) => (s.id === res.section.id ? res.section : s)),
      );
      pushToast({ message: "Section saved", tone: "success" });
    } catch (err) {
      pushToast({
        message: err instanceof Error ? err.message : "Save failed",
        tone: "error",
      });
    }
  };

  const handleRegenerate = async () => {
    if (!selectedSection) return;
    setPerSectionError((prev) => {
      const { [selectedSection.id]: _omit, ...rest } = prev;
      return rest;
    });
    try {
      const res = await regen.mutateAsync({
        sectionId: selectedSection.id,
        date,
      });
      pushToast({
        message: `Regenerate ${res.status} for section #${selectedSection.section_order + 1}`,
        tone: "info",
      });
    } catch (err) {
      const msg = err instanceof Error ? err.message : "Regenerate failed";
      setPerSectionError((prev) => ({
        ...prev,
        [selectedSection.id]: msg,
      }));
    }
  };

  const handlePublishConfirm = async () => {
    setConfirmPublish(false);
    // Send the operator's "off" toggles so the BE re-render skips them
    // before deploying. The store keeps `disabledSectionIds` as a record
    // (`{[id]: true}`); only ids whose value is truthy count as disabled.
    const disabledIds = Object.entries(disabledSectionIds)
      .filter(([, off]) => off)
      .map(([id]) => id);
    try {
      const res = await publish.mutateAsync({
        date,
        disabledSectionIds: disabledIds,
      });
      const url = res.deployed_url;
      pushToast({
        message: `Published — ${res.status}`,
        url,
        tone: "success",
      });
      // Best-effort copy
      try {
        await navigator.clipboard?.writeText(url);
      } catch {
        // ignore — the toast still surfaces the URL
      }
    } catch (err) {
      pushToast({
        message: err instanceof Error ? err.message : "Publish failed",
        tone: "error",
      });
    }
  };

  const enabledCount = orderedSections.filter(
    (s) => !disabledSectionIds[s.id],
  ).length;

  return (
    <div className="mx-auto grid h-full min-h-0 max-w-[1400px] grid-rows-[auto_minmax(0,1fr)] gap-4 px-6 py-6">
      <header className="flex flex-wrap items-end justify-between gap-3">
        <div>
          <h1 className="text-foreground text-xl font-semibold tracking-tight">
            Review — {reportQuery.data?.title ?? date}
          </h1>
          <p className="text-muted-foreground text-sm">
            {enabledCount}/{orderedSections.length} sections active ·{" "}
            <span className="font-mono">{date}</span>
          </p>
        </div>
        <div className="flex items-center gap-2">
          <div
            role="tablist"
            aria-label="Preview mode"
            className="border-border flex overflow-hidden rounded-md border"
            data-testid="preview-mode-toggle"
          >
            <ModeButton
              active={previewMode === "live"}
              onClick={() => setPreviewMode("live")}
              testId="preview-mode-live"
            >
              <Eye className="size-4" aria-hidden="true" /> Live
            </ModeButton>
            <ModeButton
              active={previewMode === "section"}
              onClick={() => setPreviewMode("section")}
              testId="preview-mode-section"
            >
              <Pencil className="size-4" aria-hidden="true" /> Section
            </ModeButton>
          </div>
          <Button
            type="button"
            size="sm"
            variant="outline"
            onClick={() => navigate("/reports/new")}
          >
            <FileText className="size-4" aria-hidden="true" />
            New report
          </Button>
          <Button asChild size="sm" variant="outline">
            <a
              href={`/api/reports/${encodeURIComponent(date)}/pdf`}
              download={`${date}-trend.pdf`}
              data-testid="pdf-download-button"
            >
              <Download className="size-4" aria-hidden="true" />
              PDF
            </a>
          </Button>
          <Button
            type="button"
            size="sm"
            onClick={() => setConfirmPublish(true)}
            disabled={publish.isPending || enabledCount === 0}
            data-testid="publish-button"
          >
            <Send className="size-4" aria-hidden="true" />
            Publish
          </Button>
        </div>
      </header>

      <div
        className="grid min-h-0 gap-4"
        style={{ gridTemplateColumns: "minmax(0,40%) minmax(0,60%)" }}
      >
        <SectionList
          className="min-h-0 overflow-y-auto pr-1"
          sections={orderedSections}
          selectedSectionId={selectedSectionId}
          disabledSectionIds={disabledSectionIds}
          onSelect={selectSection}
          onToggle={toggleSectionEnabled}
          onReorder={handleReorder}
        />

        <div data-testid="review-right-pane" className="min-h-0">
          {previewMode === "live" ? (
            <div className="border-border bg-card flex h-full min-h-0 flex-col overflow-hidden rounded-md border">
              <div className="border-border text-muted-foreground flex items-center justify-between border-b px-3 py-2 text-xs">
                <span>발행된 HTML — <span className="font-mono">{date}</span></span>
                <a
                  href={`/api/reports/${date}/html`}
                  target="_blank"
                  rel="noreferrer"
                  className="text-primary hover:underline"
                >
                  새 탭에서 열기
                </a>
              </div>
              <iframe
                key={date}
                title={`Published report ${date}`}
                src={`/api/reports/${date}/html`}
                className="min-h-0 flex-1 w-full border-0"
                // Generated report HTML owns the floating 3-theme switcher.
                // Keep the iframe sandboxed, but allow that script to cycle
                // dark/light/newsroom-white in live review.
                sandbox="allow-scripts"
                data-testid="review-live-iframe"
              />
            </div>
          ) : (
            <SectionEditor
              section={selectedSection}
              onSave={handleSave}
              onRegenerate={handleRegenerate}
              saving={patch.isPending}
              regenerating={regen.isPending}
              error={
                selectedSection
                  ? perSectionError[selectedSection.id] ?? null
                  : null
              }
              className="h-full min-h-0 overflow-y-auto"
            />
          )}
        </div>
      </div>

      {/* Publish confirm dialog */}
      <Dialog
        open={confirmPublish}
        onOpenChange={(o) => !publish.isPending && setConfirmPublish(o)}
      >
        <DialogContent data-testid="publish-dialog">
          <DialogHeader>
            <DialogTitle>Publish report for {date}?</DialogTitle>
            <DialogDescription>
              This deploys the rendered HTML to Netlify. Disabled sections (
              {orderedSections.length - enabledCount}) will be excluded on the
              next render.
            </DialogDescription>
          </DialogHeader>
          <DialogFooter>
            <Button
              variant="outline"
              size="sm"
              onClick={() => setConfirmPublish(false)}
              disabled={publish.isPending}
            >
              Cancel
            </Button>
            <Button
              size="sm"
              onClick={() => void handlePublishConfirm()}
              disabled={publish.isPending}
              data-testid="publish-confirm"
            >
              {publish.isPending ? "Publishing…" : "Publish now"}
            </Button>
          </DialogFooter>
        </DialogContent>
      </Dialog>

      {/* Toasts */}
      {toasts.length > 0 ? (
        <div
          className="fixed right-6 bottom-6 z-50 flex flex-col gap-2"
          data-testid="review-toasts"
        >
          {toasts.map((t) => (
            <div
              key={t.id}
              role="status"
              className={cn(
                "border-border bg-card text-card-foreground border px-3 py-2 text-xs shadow-md",
                t.tone === "error" &&
                  "border-destructive bg-destructive/10 text-destructive",
              )}
            >
              <div className="font-medium">{t.message}</div>
              {t.url ? (
                <a
                  className="text-primary mt-1 block break-all underline"
                  href={t.url}
                  target="_blank"
                  rel="noreferrer"
                >
                  {t.url}
                </a>
              ) : null}
            </div>
          ))}
        </div>
      ) : null}
    </div>
  );
}

function ModeButton({
  active,
  onClick,
  children,
  testId,
}: {
  active: boolean;
  onClick: () => void;
  children: React.ReactNode;
  testId?: string;
}) {
  return (
    <button
      type="button"
      role="tab"
      aria-selected={active}
      data-testid={testId}
      data-active={active}
      onClick={onClick}
      className={cn(
        "inline-flex items-center gap-1.5 px-3 py-1.5 text-xs transition-colors",
        active
          ? "bg-primary text-primary-foreground"
          : "text-muted-foreground hover:bg-accent hover:text-foreground",
      )}
    >
      {children}
    </button>
  );
}

export default ReviewReport;
