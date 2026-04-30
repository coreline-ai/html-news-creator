import { useState, type FormEvent } from "react";
import {
  Dialog,
  DialogContent,
  DialogDescription,
  DialogFooter,
  DialogHeader,
  DialogTitle,
} from "@/components/ui/dialog";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { useAddSource } from "@/hooks/useSources";
import { ApiError } from "@/lib/api";
import { cn } from "@/lib/utils";

export const SOURCE_TYPES = [
  "rss",
  "github",
  "arxiv",
  "website",
] as const;

export const SOURCE_TIERS = [
  "official",
  "mainstream",
  "research",
  "developer_signal",
  "community",
] as const;

const NAME_PATTERN = /^[A-Za-z][A-Za-z0-9 _-]*$/;

interface AddSourceDialogProps {
  open: boolean;
  onOpenChange: (next: boolean) => void;
}

interface FieldErrors {
  name?: string;
  url?: string;
  source_type?: string;
  source_tier?: string;
}

function validate(
  name: string,
  url: string,
  source_type: string,
  source_tier: string,
): FieldErrors {
  const errors: FieldErrors = {};
  const trimmedName = name.trim();
  if (!trimmedName) {
    errors.name = "Name is required.";
  } else if (!NAME_PATTERN.test(trimmedName)) {
    errors.name = "Use letters, digits, spaces, hyphens, or underscores.";
  }

  const trimmedUrl = url.trim();
  if (!trimmedUrl) {
    errors.url = "URL is required.";
  } else {
    try {
      const parsed = new URL(trimmedUrl);
      if (parsed.protocol !== "http:" && parsed.protocol !== "https:") {
        errors.url = "URL must start with http:// or https://.";
      }
    } catch {
      errors.url = "URL must start with http:// or https://.";
    }
  }

  if (!source_type) {
    errors.source_type = "Pick a source type.";
  } else if (!(SOURCE_TYPES as readonly string[]).includes(source_type)) {
    errors.source_type = "Unknown source type.";
  }

  if (!source_tier) {
    errors.source_tier = "Pick a tier.";
  } else if (!(SOURCE_TIERS as readonly string[]).includes(source_tier)) {
    errors.source_tier = "Unknown tier.";
  }

  return errors;
}

export function AddSourceDialog({ open, onOpenChange }: AddSourceDialogProps) {
  const [name, setName] = useState("");
  const [url, setUrl] = useState("");
  const [sourceType, setSourceType] = useState<string>("rss");
  const [sourceTier, setSourceTier] = useState<string>("official");
  const [errors, setErrors] = useState<FieldErrors>({});
  const [submitted, setSubmitted] = useState(false);

  const addSource = useAddSource();

  const reset = () => {
    setName("");
    setUrl("");
    setSourceType("rss");
    setSourceTier("official");
    setErrors({});
    setSubmitted(false);
    addSource.reset();
  };

  const handleOpenChange = (next: boolean) => {
    if (!next) reset();
    onOpenChange(next);
  };

  const onSubmit = (e: FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    setSubmitted(true);
    const next = validate(name, url, sourceType, sourceTier);
    setErrors(next);
    if (Object.keys(next).length > 0) return;

    addSource.mutate(
      {
        name: name.trim(),
        url: url.trim(),
        source_type: sourceType,
        source_tier: sourceTier,
      },
      {
        onSuccess: () => {
          reset();
          onOpenChange(false);
        },
      },
    );
  };

  const apiError = addSource.error;
  const apiMessage =
    apiError instanceof ApiError
      ? `${apiError.status}: ${typeof apiError.body === "string" ? apiError.body : apiError.message}`
      : apiError?.message;

  return (
    <Dialog open={open} onOpenChange={handleOpenChange}>
      <DialogContent
        className="rounded-none"
        data-testid="add-source-dialog"
      >
        <DialogHeader>
          <DialogTitle>Add a new source</DialogTitle>
          <DialogDescription>
            New entries are appended to{" "}
            <code className="text-xs">data/sources_registry.yaml</code> and
            picked up on the next pipeline run.
          </DialogDescription>
        </DialogHeader>

        <form onSubmit={onSubmit} noValidate aria-label="Add source form">
          <div className="flex flex-col gap-4">
            <Field
              id="add-source-name"
              label="Name"
              hint="Short, unique handle. Letters, digits, spaces, hyphens, underscores."
              error={submitted ? errors.name : undefined}
            >
              <Input
                id="add-source-name"
                value={name}
                onChange={(e) => setName(e.target.value)}
                aria-invalid={Boolean(submitted && errors.name)}
                placeholder="e.g. Acme AI Blog"
                autoComplete="off"
              />
            </Field>

            <Field
              id="add-source-url"
              label="URL"
              hint="Must include http:// or https://."
              error={submitted ? errors.url : undefined}
            >
              <Input
                id="add-source-url"
                value={url}
                onChange={(e) => setUrl(e.target.value)}
                aria-invalid={Boolean(submitted && errors.url)}
                placeholder="https://example.com/feed.xml"
                inputMode="url"
                autoComplete="off"
              />
            </Field>

            <div className="grid grid-cols-2 gap-4">
              <Field
                id="add-source-type"
                label="Source type"
                error={submitted ? errors.source_type : undefined}
              >
                <select
                  id="add-source-type"
                  value={sourceType}
                  onChange={(e) => setSourceType(e.target.value)}
                  className="border-input bg-background text-foreground focus-visible:ring-ring/50 h-9 w-full rounded-md border px-3 text-sm focus-visible:ring-[3px] focus-visible:outline-none"
                  aria-invalid={Boolean(submitted && errors.source_type)}
                >
                  {SOURCE_TYPES.map((t) => (
                    <option key={t} value={t}>
                      {t}
                    </option>
                  ))}
                </select>
              </Field>

              <Field
                id="add-source-tier"
                label="Tier"
                error={submitted ? errors.source_tier : undefined}
              >
                <select
                  id="add-source-tier"
                  value={sourceTier}
                  onChange={(e) => setSourceTier(e.target.value)}
                  className="border-input bg-background text-foreground focus-visible:ring-ring/50 h-9 w-full rounded-md border px-3 text-sm focus-visible:ring-[3px] focus-visible:outline-none"
                  aria-invalid={Boolean(submitted && errors.source_tier)}
                >
                  {SOURCE_TIERS.map((t) => (
                    <option key={t} value={t}>
                      {t}
                    </option>
                  ))}
                </select>
              </Field>
            </div>

            {apiMessage ? (
              <div
                role="alert"
                className="border-destructive bg-destructive/10 text-destructive border px-3 py-2 text-xs"
              >
                {apiMessage}
              </div>
            ) : null}
          </div>

          <DialogFooter className="mt-6">
            <Button
              type="button"
              variant="outline"
              onClick={() => handleOpenChange(false)}
              disabled={addSource.isPending}
            >
              Cancel
            </Button>
            <Button type="submit" disabled={addSource.isPending}>
              {addSource.isPending ? "Adding…" : "Add source"}
            </Button>
          </DialogFooter>
        </form>
      </DialogContent>
    </Dialog>
  );
}

interface FieldProps {
  id: string;
  label: string;
  hint?: string;
  error?: string;
  children: React.ReactNode;
}

function Field({ id, label, hint, error, children }: FieldProps) {
  return (
    <div className="flex flex-col gap-1.5">
      <Label htmlFor={id}>{label}</Label>
      {children}
      {error ? (
        <p
          className={cn("text-destructive text-xs")}
          role="alert"
          data-testid={`field-error-${id}`}
        >
          {error}
        </p>
      ) : hint ? (
        <p className="text-muted-foreground text-xs">{hint}</p>
      ) : null}
    </div>
  );
}

export default AddSourceDialog;
