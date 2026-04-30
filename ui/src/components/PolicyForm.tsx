import { useEffect, useMemo, useState, type ChangeEvent } from "react";
import { Button } from "@/components/ui/button";
import { Label } from "@/components/ui/label";
import { Skeleton } from "@/components/ui/skeleton";
import { EmptyState } from "@/components/EmptyState";
import { usePolicy, useUpdatePolicy, type Policy } from "@/hooks/usePolicy";
import { ApiError } from "@/lib/api";
import { AlertCircle, AlertTriangle, Save, RotateCcw } from "lucide-react";
import { cn } from "@/lib/utils";

/**
 * Built-in defaults — used as hints and for non-numeric fall-backs when the
 * yaml file is missing a key. These match the values shipped in
 * `data/editorial_policy.yaml` at Phase 5 cut.
 */
const DEFAULTS = {
  source_tiers: {
    official: { boost: 18, eligible_for_main: true },
    mainstream: { boost: 12, eligible_for_main: true },
    research: { boost: 4, eligible_for_main: false },
    developer_signal: { boost: 14, eligible_for_main: true },
    community: { boost: -4, eligible_for_main: false },
    unknown: { boost: -18, eligible_for_main: false },
  },
  scoring_weights: {
    base_score: 50,
    source_tier: 1.0,
    official_source_boost: 10,
    mainstream_source_boost: 6,
    product_signal: 8,
    research_signal: 3,
    main_image_signal: 8,
    metrics_signal: 0.25,
    cluster_size_boost_per_item: 5,
    cluster_size_boost_max: 20,
  },
  penalties: {
    obscure_research_penalty: 22,
    arxiv_only_main_penalty: 100,
    community_penalty: 8,
    missing_url_penalty: 40,
    missing_title_penalty: 30,
  },
  quotas: {
    product: 4,
    tooling: 4,
    research: 1,
    industry: 1,
    policy: 1,
  },
  report_selection: {
    max_sections: 10,
    target_sections: 10,
    min_section_score: 35,
    max_arxiv_only_sections: 1,
    max_community_sections: 1,
    max_same_source_name: 2,
    prefer_mainstream_first: true,
    backfill_require_image: true,
  },
} as const;

const TIER_KEYS = [
  "official",
  "mainstream",
  "research",
  "developer_signal",
  "community",
  "unknown",
] as const;

type TierKey = (typeof TIER_KEYS)[number];

interface FormState {
  source_tiers: Record<TierKey, { boost: number; eligible_for_main: boolean }>;
  scoring_weights: Record<keyof typeof DEFAULTS.scoring_weights, number>;
  penalties: Record<keyof typeof DEFAULTS.penalties, number>;
  quotas: Record<keyof typeof DEFAULTS.quotas, number>;
  report_selection: {
    max_sections: number;
    target_sections: number;
    min_section_score: number;
    max_arxiv_only_sections: number;
    max_community_sections: number;
    max_same_source_name: number;
    prefer_mainstream_first: boolean;
    backfill_require_image: boolean;
  };
}

function asNumber(value: unknown, fallback: number): number {
  if (typeof value === "number" && Number.isFinite(value)) return value;
  if (typeof value === "string") {
    const n = Number(value);
    if (Number.isFinite(n)) return n;
  }
  return fallback;
}

function asBool(value: unknown, fallback: boolean): boolean {
  if (typeof value === "boolean") return value;
  return fallback;
}

function buildInitial(policy: Policy | undefined): FormState {
  const root = (policy ?? {}) as Record<string, unknown>;
  const tiers = (root.source_tiers ?? {}) as Record<string, unknown>;
  const sw = (root.scoring_weights ?? {}) as Record<string, unknown>;
  const pen = (root.penalties ?? {}) as Record<string, unknown>;
  const quotas =
    ((root.quotas as Record<string, unknown>) ??
      (root.section_quotas as Record<string, unknown>) ??
      {}) as Record<string, unknown>;
  const sel = (root.report_selection ?? {}) as Record<string, unknown>;

  const tiersOut = {} as FormState["source_tiers"];
  for (const k of TIER_KEYS) {
    const raw = (tiers[k] ?? {}) as Record<string, unknown>;
    tiersOut[k] = {
      boost: asNumber(raw.boost, DEFAULTS.source_tiers[k].boost),
      eligible_for_main: asBool(
        raw.eligible_for_main,
        DEFAULTS.source_tiers[k].eligible_for_main,
      ),
    };
  }

  const swOut = {} as FormState["scoring_weights"];
  (Object.keys(DEFAULTS.scoring_weights) as Array<keyof typeof DEFAULTS.scoring_weights>).forEach(
    (k) => {
      swOut[k] = asNumber(sw[k], DEFAULTS.scoring_weights[k]);
    },
  );

  const penOut = {} as FormState["penalties"];
  (Object.keys(DEFAULTS.penalties) as Array<keyof typeof DEFAULTS.penalties>).forEach((k) => {
    penOut[k] = asNumber(pen[k], DEFAULTS.penalties[k]);
  });

  const qOut = {} as FormState["quotas"];
  (Object.keys(DEFAULTS.quotas) as Array<keyof typeof DEFAULTS.quotas>).forEach((k) => {
    qOut[k] = asNumber(quotas[k], DEFAULTS.quotas[k]);
  });

  const selOut: FormState["report_selection"] = {
    max_sections: asNumber(sel.max_sections, DEFAULTS.report_selection.max_sections),
    target_sections: asNumber(
      sel.target_sections,
      DEFAULTS.report_selection.target_sections,
    ),
    min_section_score: asNumber(
      sel.min_section_score,
      DEFAULTS.report_selection.min_section_score,
    ),
    max_arxiv_only_sections: asNumber(
      sel.max_arxiv_only_sections,
      DEFAULTS.report_selection.max_arxiv_only_sections,
    ),
    max_community_sections: asNumber(
      sel.max_community_sections,
      DEFAULTS.report_selection.max_community_sections,
    ),
    max_same_source_name: asNumber(
      sel.max_same_source_name,
      DEFAULTS.report_selection.max_same_source_name,
    ),
    prefer_mainstream_first: asBool(
      sel.prefer_mainstream_first,
      DEFAULTS.report_selection.prefer_mainstream_first,
    ),
    backfill_require_image: asBool(
      sel.backfill_require_image,
      DEFAULTS.report_selection.backfill_require_image,
    ),
  };

  return {
    source_tiers: tiersOut,
    scoring_weights: swOut,
    penalties: penOut,
    quotas: qOut,
    report_selection: selOut,
  };
}

function toPatch(form: FormState): Policy {
  return {
    source_tiers: form.source_tiers,
    scoring_weights: form.scoring_weights,
    penalties: form.penalties,
    quotas: form.quotas,
    report_selection: form.report_selection,
  };
}

export function PolicyForm() {
  const policyQuery = usePolicy();
  const updatePolicy = useUpdatePolicy();

  const initial = useMemo(
    () => buildInitial(policyQuery.data),
    [policyQuery.data],
  );

  const [form, setForm] = useState<FormState>(initial);
  const [dirty, setDirty] = useState(false);

  // Sync initial state on first successful load.
  useEffect(() => {
    if (policyQuery.data) {
      setForm(initial);
      setDirty(false);
    }
  }, [policyQuery.data, initial]);

  if (policyQuery.isLoading) {
    return (
      <div className="flex flex-col gap-3">
        <Skeleton className="h-8 w-48" />
        <Skeleton className="h-32 w-full" />
        <Skeleton className="h-32 w-full" />
      </div>
    );
  }

  if (policyQuery.isError) {
    return (
      <EmptyState
        icon={AlertCircle}
        title="Could not load policy"
        description={
          policyQuery.error instanceof Error
            ? policyQuery.error.message
            : "Failed to read /api/policy."
        }
        action={
          <Button
            size="sm"
            variant="outline"
            onClick={() => void policyQuery.refetch()}
          >
            Retry
          </Button>
        }
      />
    );
  }

  const updateNumber = (
    section: keyof FormState,
    key: string,
    value: number,
  ) => {
    setForm((prev) => ({
      ...prev,
      [section]: { ...(prev[section] as object), [key]: value },
    }));
    setDirty(true);
  };

  const updateTier = (
    tier: TierKey,
    field: "boost" | "eligible_for_main",
    value: number | boolean,
  ) => {
    setForm((prev) => ({
      ...prev,
      source_tiers: {
        ...prev.source_tiers,
        [tier]: { ...prev.source_tiers[tier], [field]: value },
      },
    }));
    setDirty(true);
  };

  const updateSelectionBool = (
    key: "prefer_mainstream_first" | "backfill_require_image",
    value: boolean,
  ) => {
    setForm((prev) => ({
      ...prev,
      report_selection: { ...prev.report_selection, [key]: value },
    }));
    setDirty(true);
  };

  const onReset = () => {
    setForm(initial);
    setDirty(false);
    updatePolicy.reset();
  };

  const onSave = () => {
    updatePolicy.mutate(
      { patch: toPatch(form) },
      {
        onSuccess: () => {
          setDirty(false);
        },
      },
    );
  };

  const apiError = updatePolicy.error;
  const apiMessage =
    apiError instanceof ApiError
      ? `${apiError.status}: ${typeof apiError.body === "string" ? apiError.body : apiError.message}`
      : apiError?.message;

  return (
    <form
      data-testid="policy-form"
      onSubmit={(e) => {
        e.preventDefault();
        onSave();
      }}
      className="flex flex-col gap-6"
      aria-label="Editorial policy form"
    >
      <VolatileBanner />

      {apiMessage ? (
        <div
          role="alert"
          className="border-destructive bg-destructive/10 text-destructive border px-3 py-2 text-xs"
        >
          Save failed — {apiMessage}
        </div>
      ) : null}

      {updatePolicy.isSuccess && !dirty ? (
        <div
          role="status"
          className="border-border bg-muted text-muted-foreground border px-3 py-2 text-xs"
        >
          Policy override saved (runtime only).
        </div>
      ) : null}

      <Section title="Source tiers" description="Boost per source tier.">
        <div className="grid grid-cols-1 gap-3 md:grid-cols-2">
          {TIER_KEYS.map((tier) => (
            <TierRow
              key={tier}
              tier={tier}
              boost={form.source_tiers[tier].boost}
              eligibleForMain={form.source_tiers[tier].eligible_for_main}
              defaultBoost={DEFAULTS.source_tiers[tier].boost}
              onBoost={(v) => updateTier(tier, "boost", v)}
              onEligible={(v) => updateTier(tier, "eligible_for_main", v)}
            />
          ))}
        </div>
      </Section>

      <Section
        title="Scoring weights"
        description="Linear weights applied to per-section signals."
      >
        <div className="grid grid-cols-1 gap-3 md:grid-cols-2">
          {(Object.keys(DEFAULTS.scoring_weights) as Array<
            keyof typeof DEFAULTS.scoring_weights
          >).map((k) => (
            <NumberField
              key={k}
              id={`weight-${k}`}
              label={prettyLabel(k)}
              value={form.scoring_weights[k]}
              defaultValue={DEFAULTS.scoring_weights[k]}
              step={k === "metrics_signal" || k === "source_tier" ? 0.05 : 1}
              onChange={(v) => updateNumber("scoring_weights", k, v)}
            />
          ))}
        </div>
      </Section>

      <Section title="Penalties" description="Subtract from the score.">
        <div className="grid grid-cols-1 gap-3 md:grid-cols-2">
          {(Object.keys(DEFAULTS.penalties) as Array<
            keyof typeof DEFAULTS.penalties
          >).map((k) => (
            <NumberField
              key={k}
              id={`penalty-${k}`}
              label={prettyLabel(k)}
              value={form.penalties[k]}
              defaultValue={DEFAULTS.penalties[k]}
              step={1}
              onChange={(v) => updateNumber("penalties", k, v)}
            />
          ))}
        </div>
      </Section>

      <Section title="Quotas" description="Topic quotas per report.">
        <div className="grid grid-cols-2 gap-3 md:grid-cols-5">
          {(Object.keys(DEFAULTS.quotas) as Array<keyof typeof DEFAULTS.quotas>).map(
            (k) => (
              <NumberField
                key={k}
                id={`quota-${k}`}
                label={prettyLabel(k)}
                value={form.quotas[k]}
                defaultValue={DEFAULTS.quotas[k]}
                min={0}
                max={20}
                step={1}
                onChange={(v) => updateNumber("quotas", k, v)}
              />
            ),
          )}
        </div>
      </Section>

      <Section
        title="Report selection"
        description="Pipeline thresholds that decide which sections survive ranking."
      >
        <div className="grid grid-cols-1 gap-3 md:grid-cols-2">
          <SliderField
            id="sel-target-sections"
            label="Target sections"
            value={form.report_selection.target_sections}
            defaultValue={DEFAULTS.report_selection.target_sections}
            min={1}
            max={20}
            step={1}
            onChange={(v) => updateNumber("report_selection", "target_sections", v)}
          />
          <SliderField
            id="sel-max-sections"
            label="Max sections"
            value={form.report_selection.max_sections}
            defaultValue={DEFAULTS.report_selection.max_sections}
            min={1}
            max={20}
            step={1}
            onChange={(v) => updateNumber("report_selection", "max_sections", v)}
          />
          <SliderField
            id="sel-min-score"
            label="Min section score"
            value={form.report_selection.min_section_score}
            defaultValue={DEFAULTS.report_selection.min_section_score}
            min={0}
            max={100}
            step={1}
            onChange={(v) =>
              updateNumber("report_selection", "min_section_score", v)
            }
          />
          <NumberField
            id="sel-max-arxiv"
            label="Max arxiv-only sections"
            value={form.report_selection.max_arxiv_only_sections}
            defaultValue={DEFAULTS.report_selection.max_arxiv_only_sections}
            min={0}
            max={5}
            step={1}
            onChange={(v) =>
              updateNumber("report_selection", "max_arxiv_only_sections", v)
            }
          />
          <NumberField
            id="sel-max-community"
            label="Max community sections"
            value={form.report_selection.max_community_sections}
            defaultValue={DEFAULTS.report_selection.max_community_sections}
            min={0}
            max={5}
            step={1}
            onChange={(v) =>
              updateNumber("report_selection", "max_community_sections", v)
            }
          />
          <NumberField
            id="sel-max-same-source"
            label="Max same source name"
            value={form.report_selection.max_same_source_name}
            defaultValue={DEFAULTS.report_selection.max_same_source_name}
            min={1}
            max={10}
            step={1}
            onChange={(v) =>
              updateNumber("report_selection", "max_same_source_name", v)
            }
          />
          <ToggleField
            id="sel-prefer-mainstream"
            label="Prefer mainstream first"
            checked={form.report_selection.prefer_mainstream_first}
            defaultValue={DEFAULTS.report_selection.prefer_mainstream_first}
            onChange={(v) => updateSelectionBool("prefer_mainstream_first", v)}
          />
          <ToggleField
            id="sel-backfill-image"
            label="Backfill: require image"
            checked={form.report_selection.backfill_require_image}
            defaultValue={DEFAULTS.report_selection.backfill_require_image}
            onChange={(v) => updateSelectionBool("backfill_require_image", v)}
          />
        </div>
      </Section>

      <div className="border-border bg-card sticky bottom-0 flex items-center justify-between gap-3 border-t px-4 py-3">
        <span className="text-muted-foreground text-xs">
          {dirty ? "Unsaved changes — runtime override only." : "All changes saved."}
        </span>
        <div className="flex items-center gap-2">
          <Button
            type="button"
            variant="outline"
            size="sm"
            onClick={onReset}
            disabled={!dirty || updatePolicy.isPending}
          >
            <RotateCcw className="size-4" /> Reset
          </Button>
          <Button
            type="submit"
            size="sm"
            disabled={!dirty || updatePolicy.isPending}
          >
            <Save className="size-4" />
            {updatePolicy.isPending ? "Saving…" : "Save policy"}
          </Button>
        </div>
      </div>
    </form>
  );
}

function VolatileBanner() {
  return (
    <div
      role="note"
      data-testid="policy-volatile-banner"
      className="border-amber-500/50 bg-amber-500/10 text-amber-700 dark:text-amber-300 flex items-start gap-2 border px-3 py-2 text-xs"
    >
      <AlertTriangle className="mt-0.5 size-4 shrink-0" aria-hidden="true" />
      <p>
        Runtime override — changes are kept in memory only and{" "}
        <strong>volatile on backend restart</strong>. Persist to{" "}
        <code>data/editorial_policy.yaml</code> manually if needed.
      </p>
    </div>
  );
}

function Section({
  title,
  description,
  children,
}: {
  title: string;
  description?: string;
  children: React.ReactNode;
}) {
  return (
    <section className="border-border bg-card flex flex-col gap-3 rounded-none border p-4">
      <header className="flex flex-col gap-0.5">
        <h2 className="text-foreground text-sm font-semibold">{title}</h2>
        {description ? (
          <p className="text-muted-foreground text-xs">{description}</p>
        ) : null}
      </header>
      {children}
    </section>
  );
}

interface NumberFieldProps {
  id: string;
  label: string;
  value: number;
  defaultValue: number;
  min?: number;
  max?: number;
  step?: number;
  onChange: (n: number) => void;
}

function NumberField({
  id,
  label,
  value,
  defaultValue,
  min,
  max,
  step = 1,
  onChange,
}: NumberFieldProps) {
  return (
    <div className="flex flex-col gap-1.5">
      <Label htmlFor={id} className="text-xs">
        {label}
      </Label>
      <input
        id={id}
        type="number"
        inputMode="decimal"
        value={value}
        min={min}
        max={max}
        step={step}
        onChange={(e: ChangeEvent<HTMLInputElement>) =>
          onChange(Number(e.target.value))
        }
        className="border-input bg-background text-foreground focus-visible:ring-ring/50 h-9 w-full rounded-md border px-3 text-sm focus-visible:ring-[3px] focus-visible:outline-none"
      />
      <p className="text-muted-foreground text-[11px]">
        Default: {defaultValue}
      </p>
    </div>
  );
}

interface SliderFieldProps extends NumberFieldProps {
  min: number;
  max: number;
}

function SliderField({
  id,
  label,
  value,
  defaultValue,
  min,
  max,
  step = 1,
  onChange,
}: SliderFieldProps) {
  return (
    <div className="flex flex-col gap-1.5">
      <Label htmlFor={id} className="text-xs">
        {label}
      </Label>
      <div className="flex items-center gap-3">
        <input
          id={id}
          type="range"
          value={value}
          min={min}
          max={max}
          step={step}
          onChange={(e) => onChange(Number(e.target.value))}
          className="h-2 flex-1 cursor-pointer accent-current"
          aria-valuemin={min}
          aria-valuemax={max}
          aria-valuenow={value}
        />
        <input
          type="number"
          value={value}
          min={min}
          max={max}
          step={step}
          onChange={(e) => onChange(Number(e.target.value))}
          aria-label={`${label} value`}
          className="border-input bg-background text-foreground h-8 w-16 rounded-md border px-2 text-sm focus-visible:outline-none"
        />
      </div>
      <p className="text-muted-foreground text-[11px]">
        Default: {defaultValue}
      </p>
    </div>
  );
}

interface ToggleFieldProps {
  id: string;
  label: string;
  checked: boolean;
  defaultValue: boolean;
  onChange: (v: boolean) => void;
}

function ToggleField({
  id,
  label,
  checked,
  defaultValue,
  onChange,
}: ToggleFieldProps) {
  return (
    <div className="flex flex-col gap-1.5">
      <Label htmlFor={id} className="text-xs">
        {label}
      </Label>
      <label
        className={cn(
          "border-input bg-background text-foreground inline-flex h-9 cursor-pointer items-center gap-2 rounded-md border px-3 text-sm",
        )}
      >
        <input
          id={id}
          type="checkbox"
          checked={checked}
          onChange={(e) => onChange(e.target.checked)}
          className="size-4"
        />
        <span>{checked ? "Enabled" : "Disabled"}</span>
      </label>
      <p className="text-muted-foreground text-[11px]">
        Default: {defaultValue ? "Enabled" : "Disabled"}
      </p>
    </div>
  );
}

interface TierRowProps {
  tier: TierKey;
  boost: number;
  eligibleForMain: boolean;
  defaultBoost: number;
  onBoost: (n: number) => void;
  onEligible: (v: boolean) => void;
}

function TierRow({
  tier,
  boost,
  eligibleForMain,
  defaultBoost,
  onBoost,
  onEligible,
}: TierRowProps) {
  return (
    <div className="border-border flex flex-col gap-2 border p-3">
      <div className="flex items-center justify-between">
        <span className="text-foreground text-xs font-semibold tracking-wide uppercase">
          {tier}
        </span>
        <span className="text-muted-foreground text-[10px]">
          default boost: {defaultBoost}
        </span>
      </div>
      <div className="flex items-center gap-3">
        <input
          aria-label={`${tier} boost`}
          type="range"
          min={-30}
          max={30}
          step={1}
          value={boost}
          onChange={(e) => onBoost(Number(e.target.value))}
          className="h-2 flex-1 cursor-pointer"
        />
        <input
          aria-label={`${tier} boost value`}
          type="number"
          value={boost}
          min={-30}
          max={30}
          step={1}
          onChange={(e) => onBoost(Number(e.target.value))}
          className="border-input bg-background text-foreground h-8 w-16 rounded-md border px-2 text-sm"
        />
      </div>
      <label className="text-muted-foreground inline-flex items-center gap-2 text-xs">
        <input
          type="checkbox"
          checked={eligibleForMain}
          onChange={(e) => onEligible(e.target.checked)}
          className="size-3.5"
        />
        Eligible for main headline
      </label>
    </div>
  );
}

function prettyLabel(key: string): string {
  return key
    .replace(/_/g, " ")
    .replace(/\b\w/g, (c) => c.toUpperCase());
}

export default PolicyForm;
