import { useState, type ReactNode } from "react";
import { ChevronRight } from "lucide-react";
import { Link } from "react-router-dom";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { Badge } from "@/components/ui/badge";
import { Separator } from "@/components/ui/separator";
import {
  useAppStore,
  type RunOptions,
  type SectionQuotas,
  type SourceType,
  type RunMode,
  type OutputTheme,
  type DeployTarget,
} from "@/lib/store";
import { cn } from "@/lib/utils";

const SOURCE_TYPES: SourceType[] = ["rss", "github", "arxiv", "website"];

const QUOTA_KEYS: (keyof SectionQuotas)[] = [
  "product",
  "tooling",
  "research",
  "industry",
  "policy",
];

interface GroupDef {
  id: "A" | "B" | "C" | "D" | "E";
  label: string;
  description: string;
}

const GROUPS: GroupDef[] = [
  { id: "A", label: "Execution", description: "Date, mode, range, dry-run, source types" },
  { id: "B", label: "Editorial", description: "Sections, scoring, quotas, signals" },
  { id: "C", label: "Sources", description: "Pipeline source registry" },
  { id: "D", label: "Output", description: "Theme, language, format" },
  { id: "E", label: "Publishing", description: "Deploy target, notifications, schedule" },
];

export function RunOptionsPanel() {
  const runOptions = useAppStore((s) => s.runOptions);
  const setOption = useAppStore((s) => s.setOption);
  const setQuota = useAppStore((s) => s.setQuota);
  const resetOptions = useAppStore((s) => s.resetOptions);

  const [open, setOpen] = useState<Record<GroupDef["id"], boolean>>({
    A: true,
    B: true,
    C: false,
    D: false,
    E: false,
  });

  const toggle = (id: GroupDef["id"]) =>
    setOpen((s) => ({ ...s, [id]: !s[id] }));

  return (
    <aside
      data-testid="run-options-panel"
      className="border-border bg-card text-card-foreground flex h-full flex-col border-r"
      aria-label="Run options"
    >
      <div className="border-border flex items-center justify-between border-b px-4 py-3">
        <div>
          <div className="text-foreground text-sm font-semibold">
            Run options
          </div>
          <div className="text-muted-foreground text-[11px]">
            Live preview updates 2s after each change.
          </div>
        </div>
        <button
          type="button"
          onClick={resetOptions}
          className="text-muted-foreground hover:text-foreground text-xs underline-offset-4 hover:underline"
        >
          Reset
        </button>
      </div>

      <div className="flex-1 overflow-y-auto">
        {GROUPS.map((group) => (
          <AccordionGroup
            key={group.id}
            group={group}
            isOpen={open[group.id]}
            onToggle={() => toggle(group.id)}
          >
            {group.id === "A" ? (
              <ExecutionGroup runOptions={runOptions} setOption={setOption} />
            ) : group.id === "B" ? (
              <EditorialGroup
                runOptions={runOptions}
                setOption={setOption}
                setQuota={setQuota}
              />
            ) : group.id === "C" ? (
              <SourcesGroup />
            ) : group.id === "D" ? (
              <OutputGroup runOptions={runOptions} setOption={setOption} />
            ) : (
              <PublishingGroup runOptions={runOptions} setOption={setOption} />
            )}
          </AccordionGroup>
        ))}
      </div>
    </aside>
  );
}

// ---------------------------------------------------------------------------
// Accordion shell
// ---------------------------------------------------------------------------

function AccordionGroup({
  group,
  isOpen,
  onToggle,
  children,
}: {
  group: GroupDef;
  isOpen: boolean;
  onToggle: () => void;
  children: ReactNode;
}) {
  const region = `run-opts-region-${group.id}`;
  const trigger = `run-opts-trigger-${group.id}`;
  return (
    <section
      data-testid={`group-${group.id}`}
      data-group={group.id}
      className="border-border border-b last:border-b-0"
    >
      <button
        id={trigger}
        type="button"
        aria-expanded={isOpen}
        aria-controls={region}
        onClick={onToggle}
        className={cn(
          "hover:bg-accent/40 flex w-full items-center gap-2 px-4 py-3 text-left transition-colors",
        )}
      >
        <span
          aria-hidden="true"
          className={cn(
            "text-muted-foreground inline-flex size-4 items-center justify-center transition-transform",
            isOpen && "rotate-90",
          )}
        >
          <ChevronRight className="size-4" />
        </span>
        <span className="text-muted-foreground w-5 text-[11px] font-mono uppercase">
          {group.id}
        </span>
        <span className="text-foreground text-sm font-medium">
          {group.label}
        </span>
        <span className="text-muted-foreground ml-auto truncate text-[11px]">
          {group.description}
        </span>
      </button>
      {isOpen ? (
        <div
          id={region}
          role="region"
          aria-labelledby={trigger}
          className="flex flex-col gap-4 px-4 pt-1 pb-4"
        >
          {children}
        </div>
      ) : null}
    </section>
  );
}

// ---------------------------------------------------------------------------
// A. Execution
// ---------------------------------------------------------------------------

function ExecutionGroup({
  runOptions,
  setOption,
}: {
  runOptions: RunOptions;
  setOption: <K extends keyof RunOptions>(k: K, v: RunOptions[K]) => void;
}) {
  return (
    <>
      <Field
        id="opt-date"
        label="Date (KST)"
        hint="Target report date in YYYY-MM-DD."
      >
        <Input
          id="opt-date"
          type="date"
          value={runOptions.date}
          onChange={(e) => setOption("date", e.target.value)}
        />
      </Field>

      <Field id="opt-mode" label="Mode" hint="full = run all 9 stages.">
        <select
          id="opt-mode"
          className="bg-background border-input text-foreground h-9 w-full rounded-md border px-3 text-sm"
          value={runOptions.mode}
          onChange={(e) => setOption("mode", e.target.value as RunMode)}
        >
          <option value="full">full</option>
          <option value="rss-only">rss-only</option>
        </select>
      </Field>

      <div className="grid grid-cols-2 gap-3">
        <Field id="opt-range-from" label="Range from">
          <Input
            id="opt-range-from"
            type="date"
            value={runOptions.range_from ?? ""}
            onChange={(e) =>
              setOption("range_from", e.target.value || null)
            }
          />
        </Field>
        <Field id="opt-range-to" label="Range to">
          <Input
            id="opt-range-to"
            type="date"
            value={runOptions.range_to ?? ""}
            onChange={(e) => setOption("range_to", e.target.value || null)}
          />
        </Field>
      </div>

      <Toggle
        id="opt-dry-run"
        label="Dry run"
        hint="Skip DB writes and Netlify deploy."
        checked={runOptions.dry_run}
        onChange={(v) => setOption("dry_run", v)}
      />

      <Field id="opt-source-types" label="Source types">
        <div className="flex flex-wrap gap-2">
          {SOURCE_TYPES.map((t) => {
            const active = runOptions.source_types.includes(t);
            return (
              <button
                key={t}
                type="button"
                role="switch"
                aria-checked={active}
                onClick={() => {
                  const next = active
                    ? runOptions.source_types.filter((x) => x !== t)
                    : [...runOptions.source_types, t];
                  setOption("source_types", next);
                }}
                className={cn(
                  "rounded-md border px-2.5 py-1 text-xs transition-colors",
                  active
                    ? "bg-primary text-primary-foreground border-transparent"
                    : "border-border bg-background text-muted-foreground hover:text-foreground",
                )}
              >
                {t}
              </button>
            );
          })}
        </div>
      </Field>
    </>
  );
}

// ---------------------------------------------------------------------------
// B. Editorial
// ---------------------------------------------------------------------------

function EditorialGroup({
  runOptions,
  setOption,
  setQuota,
}: {
  runOptions: RunOptions;
  setOption: <K extends keyof RunOptions>(k: K, v: RunOptions[K]) => void;
  setQuota: (k: keyof SectionQuotas, v: number) => void;
}) {
  return (
    <>
      <Slider
        id="opt-target-sections"
        label="Target sections"
        min={1}
        max={20}
        value={runOptions.target_sections}
        onChange={(v) => setOption("target_sections", v)}
        hint="Default 10 — editorial_policy.yaml"
      />
      <Slider
        id="opt-min-score"
        label="Min section score"
        min={0}
        max={100}
        value={runOptions.min_section_score}
        onChange={(v) => setOption("min_section_score", v)}
        hint="Default 35"
      />

      <Separator />

      <div className="text-muted-foreground text-[11px] font-medium tracking-wider uppercase">
        Section quotas
      </div>
      <div className="grid grid-cols-2 gap-3">
        {QUOTA_KEYS.map((k) => (
          <Field
            key={k}
            id={`opt-quota-${k}`}
            label={k}
            hint={`Default ${k === "product" || k === "tooling" ? 4 : 1}`}
          >
            <Input
              id={`opt-quota-${k}`}
              type="number"
              min={0}
              max={20}
              value={runOptions.quotas[k]}
              onChange={(e) =>
                setQuota(k, Number.parseInt(e.target.value, 10) || 0)
              }
            />
          </Field>
        ))}
      </div>

      <Separator />

      <Slider
        id="opt-cluster-bonus"
        label="Cluster bonus"
        min={0}
        max={20}
        value={runOptions.cluster_bonus}
        onChange={(v) => setOption("cluster_bonus", v)}
        hint="Default 5"
      />
      <Toggle
        id="opt-image-required"
        label="Require image"
        checked={runOptions.image_required}
        onChange={(v) => setOption("image_required", v)}
      />
      <div className="grid grid-cols-2 gap-3">
        <Field
          id="opt-arxiv-max"
          label="arxiv max"
          hint="Cap arxiv-only sections."
        >
          <Input
            id="opt-arxiv-max"
            type="number"
            min={0}
            max={5}
            value={runOptions.arxiv_max}
            onChange={(e) =>
              setOption(
                "arxiv_max",
                Number.parseInt(e.target.value, 10) || 0,
              )
            }
          />
        </Field>
        <Field
          id="opt-community-max"
          label="community max"
          hint="Cap community-only sections."
        >
          <Input
            id="opt-community-max"
            type="number"
            min={0}
            max={5}
            value={runOptions.community_max}
            onChange={(e) =>
              setOption(
                "community_max",
                Number.parseInt(e.target.value, 10) || 0,
              )
            }
          />
        </Field>
      </div>
    </>
  );
}

// ---------------------------------------------------------------------------
// C. Sources (placeholder summary)
// ---------------------------------------------------------------------------

function SourcesGroup() {
  return (
    <div className="border-border bg-background flex items-center justify-between border px-3 py-2.5">
      <div>
        <div className="text-foreground text-sm font-medium">
          37 sources active
        </div>
        <div className="text-muted-foreground text-[11px]">
          Manage tier, type, and enable/disable.
        </div>
      </div>
      <Link
        to="/sources"
        className="text-foreground hover:underline-offset-4 text-xs underline-offset-2 hover:underline"
      >
        Open Sources →
      </Link>
    </div>
  );
}

// ---------------------------------------------------------------------------
// D. Output
// ---------------------------------------------------------------------------

function OutputGroup({
  runOptions,
  setOption,
}: {
  runOptions: RunOptions;
  setOption: <K extends keyof RunOptions>(k: K, v: RunOptions[K]) => void;
}) {
  const themes: OutputTheme[] = ["dark", "light", "newsroom-white"];
  return (
    <>
      <Field
        id="opt-output-theme"
        label="Output theme"
        previewOnly
      >
        <div className="flex gap-2">
          {themes.map((t) => {
            const active = runOptions.output_theme === t;
            return (
              <button
                key={t}
                type="button"
                onClick={() => setOption("output_theme", t)}
                className={cn(
                  "flex-1 rounded-md border px-2.5 py-1.5 text-xs transition-colors",
                  active
                    ? "bg-primary text-primary-foreground border-transparent"
                    : "border-border bg-background text-muted-foreground hover:text-foreground",
                )}
              >
                {t}
              </button>
            );
          })}
        </div>
      </Field>
      <Field id="opt-language" label="Language">
        <select
          id="opt-language"
          className="bg-background border-input text-foreground h-9 w-full rounded-md border px-3 text-sm"
          value={runOptions.language}
          onChange={(e) => setOption("language", e.target.value)}
        >
          <option value="ko">Korean (ko)</option>
          <option value="en">English (en)</option>
        </select>
      </Field>
      <Field id="opt-format" label="Format" previewOnly>
        <select
          id="opt-format"
          className="bg-background border-input text-foreground h-9 w-full rounded-md border px-3 text-sm"
          value={runOptions.format}
          onChange={(e) =>
            setOption("format", e.target.value as RunOptions["format"])
          }
        >
          <option value="html">html</option>
          <option value="markdown">markdown</option>
        </select>
      </Field>
    </>
  );
}

// ---------------------------------------------------------------------------
// E. Publishing
// ---------------------------------------------------------------------------

function PublishingGroup({
  runOptions,
  setOption,
}: {
  runOptions: RunOptions;
  setOption: <K extends keyof RunOptions>(k: K, v: RunOptions[K]) => void;
}) {
  const targets: DeployTarget[] = ["netlify", "local-only"];
  return (
    <>
      <Field id="opt-deploy-target" label="Deploy target" previewOnly>
        <div className="flex gap-2">
          {targets.map((t) => {
            const active = runOptions.deploy_target === t;
            return (
              <button
                key={t}
                type="button"
                onClick={() => setOption("deploy_target", t)}
                className={cn(
                  "flex-1 rounded-md border px-2.5 py-1.5 text-xs transition-colors",
                  active
                    ? "bg-primary text-primary-foreground border-transparent"
                    : "border-border bg-background text-muted-foreground hover:text-foreground",
                )}
              >
                {t}
              </button>
            );
          })}
        </div>
      </Field>
      <Toggle
        id="opt-slack-notify"
        label="Slack notify"
        checked={runOptions.slack_notify}
        onChange={(v) => setOption("slack_notify", v)}
        previewOnly
      />
      <Field
        id="opt-publish-at"
        label="Publish at"
        hint="Leave blank to publish on completion."
        previewOnly
      >
        <Input
          id="opt-publish-at"
          type="datetime-local"
          value={runOptions.publish_at ?? ""}
          onChange={(e) =>
            setOption("publish_at", e.target.value || null)
          }
        />
      </Field>
      {runOptions.dry_run ? (
        <Badge variant="outline" className="self-start">
          dry run — nothing will be published
        </Badge>
      ) : null}
    </>
  );
}

// ---------------------------------------------------------------------------
// Field shells
// ---------------------------------------------------------------------------

function Field({
  id,
  label,
  hint,
  previewOnly,
  children,
}: {
  id: string;
  label: string;
  hint?: string;
  previewOnly?: boolean;
  children: ReactNode;
}) {
  return (
    <div className="flex flex-col gap-1.5">
      <div className="flex items-center gap-2">
        <Label htmlFor={id} className="text-foreground text-xs font-medium">
          {label}
        </Label>
        {previewOnly ? <PreviewOnlyBadge /> : null}
      </div>
      {children}
      {hint ? (
        <span className="text-muted-foreground text-[11px]">{hint}</span>
      ) : null}
    </div>
  );
}

function PreviewOnlyBadge() {
  return (
    <span
      className="text-muted-foreground text-[10px] tracking-wide uppercase"
      title="UI-only — not yet forwarded to the actual run"
      data-testid="preview-only-badge"
    >
      Preview only
    </span>
  );
}

function Slider({
  id,
  label,
  min,
  max,
  value,
  onChange,
  hint,
}: {
  id: string;
  label: string;
  min: number;
  max: number;
  value: number;
  onChange: (v: number) => void;
  hint?: string;
}) {
  return (
    <div className="flex flex-col gap-1.5">
      <div className="flex items-center justify-between">
        <Label htmlFor={id} className="text-foreground text-xs font-medium">
          {label}
        </Label>
        <span
          className="text-foreground text-xs font-mono"
          aria-live="polite"
          data-testid={`${id}-value`}
        >
          {value}
        </span>
      </div>
      <input
        id={id}
        type="range"
        min={min}
        max={max}
        value={value}
        onChange={(e) => onChange(Number.parseInt(e.target.value, 10))}
        className="accent-primary w-full"
      />
      {hint ? (
        <span className="text-muted-foreground text-[11px]">{hint}</span>
      ) : null}
    </div>
  );
}

function Toggle({
  id,
  label,
  hint,
  checked,
  onChange,
  previewOnly,
}: {
  id: string;
  label: string;
  hint?: string;
  checked: boolean;
  onChange: (v: boolean) => void;
  previewOnly?: boolean;
}) {
  return (
    <div className="flex items-start justify-between gap-3">
      <div className="flex flex-col">
        <div className="flex items-center gap-2">
          <Label htmlFor={id} className="text-foreground text-xs font-medium">
            {label}
          </Label>
          {previewOnly ? <PreviewOnlyBadge /> : null}
        </div>
        {hint ? (
          <span className="text-muted-foreground text-[11px]">{hint}</span>
        ) : null}
      </div>
      <button
        id={id}
        role="switch"
        aria-checked={checked}
        type="button"
        onClick={() => onChange(!checked)}
        className={cn(
          "relative inline-flex h-5 w-9 shrink-0 items-center rounded-full transition-colors",
          checked ? "bg-primary" : "bg-muted",
        )}
      >
        <span
          className={cn(
            "bg-background inline-block size-4 transform rounded-full shadow transition-transform",
            checked ? "translate-x-4" : "translate-x-0.5",
          )}
        />
      </button>
    </div>
  );
}

export default RunOptionsPanel;
