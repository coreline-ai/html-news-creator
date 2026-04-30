import { useEffect, useState } from "react";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { Skeleton } from "@/components/ui/skeleton";
import { RefreshCw, Save, Pencil } from "lucide-react";
import type { ReportSection } from "@/lib/api";
import type { SectionPatchPayload } from "@/hooks/useSections";
import { cn } from "@/lib/utils";

export interface SectionEditorProps {
  section: ReportSection | null;
  /** Save handler. Returns the patch that was applied. */
  onSave: (patch: SectionPatchPayload) => Promise<void> | void;
  onRegenerate: () => Promise<void> | void;
  saving?: boolean;
  regenerating?: boolean;
  /** Per-section error (e.g. regenerate failed) */
  error?: string | null;
  className?: string;
}

function getInitialImageUrl(section: ReportSection | null): string {
  if (!section || !section.image_evidence_json) return "";
  const evid = section.image_evidence_json as unknown;
  if (Array.isArray(evid) && evid.length > 0) {
    const first = evid[0] as Record<string, unknown> | string;
    if (typeof first === "string") return first;
    if (first && typeof first === "object" && typeof first.url === "string") {
      return first.url;
    }
  }
  return "";
}

export function SectionEditor({
  section,
  onSave,
  onRegenerate,
  saving = false,
  regenerating = false,
  error = null,
  className,
}: SectionEditorProps) {
  const [title, setTitle] = useState("");
  const [summary, setSummary] = useState("");
  const [implication, setImplication] = useState("");
  const [imageUrl, setImageUrl] = useState("");
  const [manualMode, setManualMode] = useState(false);

  // Reset form when the selected section changes.
  useEffect(() => {
    if (!section) {
      setTitle("");
      setSummary("");
      setImplication("");
      setImageUrl("");
      setManualMode(false);
      return;
    }
    setTitle(section.title ?? "");
    setSummary(section.fact_summary ?? "");
    setImplication(section.inference_summary ?? "");
    setImageUrl(getInitialImageUrl(section));
    setManualMode(false);
  }, [section?.id]); // eslint-disable-line react-hooks/exhaustive-deps

  if (!section) {
    return (
      <div
        className={cn(
          "border-border bg-card text-muted-foreground flex h-full items-center justify-center border p-8 text-sm",
          className,
        )}
        data-testid="section-editor-empty"
      >
        Select a section on the left to edit.
      </div>
    );
  }

  const isLoading = saving || regenerating;
  const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    const patch: SectionPatchPayload = {};
    if (title !== (section.title ?? "")) patch.title = title;
    if (summary !== (section.fact_summary ?? "")) patch.summary_ko = summary;
    if (implication !== (section.inference_summary ?? "")) {
      patch.implication_ko = implication;
    }
    if (imageUrl !== getInitialImageUrl(section)) patch.image_url = imageUrl;
    if (Object.keys(patch).length === 0) return;
    await onSave(patch);
  };

  return (
    <form
      onSubmit={handleSubmit}
      data-testid="section-editor"
      data-section-id={section.id}
      className={cn(
        "border-border bg-card text-card-foreground flex flex-col gap-4 border p-4",
        className,
      )}
    >
      <header className="flex items-start justify-between gap-3">
        <div className="min-w-0">
          <h3 className="text-foreground text-base font-semibold">
            Edit section #{section.section_order + 1}
          </h3>
          <p className="text-muted-foreground text-xs">
            ID: {section.id}
          </p>
        </div>
        <div className="flex shrink-0 gap-2">
          <Button
            type="button"
            size="sm"
            variant="outline"
            onClick={() => setManualMode((v) => !v)}
            data-testid="section-editor-manual-toggle"
          >
            <Pencil className="size-4" aria-hidden="true" />
            {manualMode ? "Auto" : "Manual edit"}
          </Button>
          <Button
            type="button"
            size="sm"
            variant="outline"
            onClick={() => void onRegenerate()}
            disabled={regenerating}
            data-testid="section-editor-regenerate"
          >
            <RefreshCw
              className={cn("size-4", regenerating && "animate-spin")}
              aria-hidden="true"
            />
            Regenerate
          </Button>
        </div>
      </header>

      {regenerating ? (
        <div className="flex flex-col gap-2">
          <Skeleton className="h-8 w-2/3" />
          <Skeleton className="h-20 w-full" />
        </div>
      ) : (
        <div className="flex flex-col gap-3">
          <div className="flex flex-col gap-1.5">
            <Label htmlFor="section-title">Title</Label>
            <Input
              id="section-title"
              value={title}
              onChange={(e) => setTitle(e.target.value)}
              data-testid="section-editor-title"
              disabled={isLoading}
            />
          </div>

          <div className="flex flex-col gap-1.5">
            <Label htmlFor="section-image">Image URL</Label>
            <Input
              id="section-image"
              type="url"
              value={imageUrl}
              onChange={(e) => setImageUrl(e.target.value)}
              data-testid="section-editor-image"
              placeholder="https://…"
              disabled={isLoading}
            />
          </div>

          <div className="flex flex-col gap-1.5">
            <Label htmlFor="section-summary">Summary (요약)</Label>
            <textarea
              id="section-summary"
              value={summary}
              onChange={(e) => setSummary(e.target.value)}
              data-testid="section-editor-summary"
              disabled={isLoading}
              rows={4}
              className="border-input bg-background placeholder:text-muted-foreground focus-visible:border-ring focus-visible:ring-ring/50 aria-invalid:ring-destructive/20 dark:aria-invalid:ring-destructive/40 aria-invalid:border-destructive flex min-h-16 w-full rounded-md border px-3 py-2 text-sm shadow-xs transition-colors outline-none focus-visible:ring-[3px] disabled:cursor-not-allowed disabled:opacity-50"
            />
          </div>

          <div className="flex flex-col gap-1.5">
            <Label htmlFor="section-implication">Implication (시사점)</Label>
            <textarea
              id="section-implication"
              value={implication}
              onChange={(e) => setImplication(e.target.value)}
              data-testid="section-editor-implication"
              disabled={isLoading}
              rows={3}
              className="border-input bg-background placeholder:text-muted-foreground focus-visible:border-ring focus-visible:ring-ring/50 aria-invalid:ring-destructive/20 dark:aria-invalid:ring-destructive/40 aria-invalid:border-destructive flex min-h-16 w-full rounded-md border px-3 py-2 text-sm shadow-xs transition-colors outline-none focus-visible:ring-[3px] disabled:cursor-not-allowed disabled:opacity-50"
            />
          </div>
        </div>
      )}

      {error ? (
        <div
          role="alert"
          className="border-destructive bg-destructive/10 text-destructive border px-3 py-2 text-xs"
          data-testid="section-editor-error"
        >
          {error}
        </div>
      ) : null}

      <footer className="flex items-center justify-end gap-2 border-t pt-3">
        <Button
          type="submit"
          size="sm"
          disabled={isLoading}
          data-testid="section-editor-save"
        >
          <Save className="size-4" aria-hidden="true" />
          {saving ? "Saving…" : "Save"}
        </Button>
      </footer>
    </form>
  );
}

export default SectionEditor;
