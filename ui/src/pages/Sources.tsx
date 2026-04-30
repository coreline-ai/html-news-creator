import { useMemo, useState } from "react";
import { Button } from "@/components/ui/button";
import { Badge } from "@/components/ui/badge";
import { Skeleton } from "@/components/ui/skeleton";
import { EmptyState } from "@/components/EmptyState";
import { AddSourceDialog } from "@/components/AddSourceDialog";
import { useSourcesQuery, type Source } from "@/hooks/useSourcesQuery";
import { useUpdateSource } from "@/hooks/useSources";
import { SIDEBAR_NAV_ICONS } from "@/lib/icons";
import { AlertCircle, Plus } from "lucide-react";
import { cn } from "@/lib/utils";

/**
 * The five canonical tiers we render as section headers, in display order.
 * Anything outside this list lands in the trailing `unknown` group.
 */
const TIER_ORDER = [
  "official",
  "mainstream",
  "developer_signal",
  "research",
  "community",
] as const;

type Tier = (typeof TIER_ORDER)[number] | "unknown";

const TIER_LABEL: Record<Tier, string> = {
  official: "Official",
  mainstream: "Mainstream",
  developer_signal: "Developer signal",
  research: "Research",
  community: "Community",
  unknown: "Unknown",
};

function bucketTier(s: Source): Tier {
  const raw = (s.source_tier ?? s.trust_level ?? "") as string;
  if ((TIER_ORDER as readonly string[]).includes(raw)) return raw as Tier;
  if (raw === "trusted_media") return "mainstream";
  if (raw === "official_site" || raw === "official_docs") return "official";
  if (raw === "paper_arxiv" || raw === "arxiv") return "research";
  if (raw === "github" || raw === "developer") return "developer_signal";
  return "unknown";
}

interface Group {
  tier: Tier;
  sources: Source[];
}

function groupSources(sources: Source[]): Group[] {
  const buckets = new Map<Tier, Source[]>();
  for (const tier of TIER_ORDER) buckets.set(tier, []);
  buckets.set("unknown", []);
  for (const s of sources) {
    const t = bucketTier(s);
    buckets.get(t)!.push(s);
  }
  const groups: Group[] = [];
  for (const tier of TIER_ORDER) {
    groups.push({ tier, sources: buckets.get(tier) ?? [] });
  }
  const unknown = buckets.get("unknown") ?? [];
  if (unknown.length > 0) groups.push({ tier: "unknown", sources: unknown });
  return groups;
}

export function Sources() {
  const sourcesQuery = useSourcesQuery();
  const updateSource = useUpdateSource();
  const [addOpen, setAddOpen] = useState(false);
  const [selected, setSelected] = useState<Source | null>(null);

  const groups = useMemo(
    () => groupSources(sourcesQuery.data ?? []),
    [sourcesQuery.data],
  );

  const total = sourcesQuery.data?.length ?? 0;

  return (
    <div className="mx-auto flex max-w-[1200px] flex-col gap-6 px-6 py-6">
      <header className="flex items-end justify-between gap-4">
        <div>
          <h1 className="text-foreground text-xl font-semibold tracking-tight">
            Sources
          </h1>
          <p className="text-muted-foreground text-sm">
            {total} source{total === 1 ? "" : "s"} grouped by tier — toggle to
            include in the next pipeline run.
          </p>
        </div>
        <Button size="sm" onClick={() => setAddOpen(true)}>
          <Plus className="size-4" /> Add source
        </Button>
      </header>

      {sourcesQuery.isLoading ? (
        <div className="flex flex-col gap-2">
          <Skeleton className="h-8 w-full" />
          <Skeleton className="h-8 w-full" />
          <Skeleton className="h-8 w-full" />
        </div>
      ) : sourcesQuery.isError ? (
        <EmptyState
          icon={AlertCircle}
          title="Could not load sources"
          description={
            sourcesQuery.error instanceof Error
              ? sourcesQuery.error.message
              : "API request failed."
          }
          action={
            <Button
              size="sm"
              variant="outline"
              onClick={() => void sourcesQuery.refetch()}
            >
              Retry
            </Button>
          }
        />
      ) : total === 0 ? (
        <EmptyState
          icon={SIDEBAR_NAV_ICONS.sources}
          title="No sources registered yet"
          description="Add your first feed to start ingesting."
          action={
            <Button size="sm" onClick={() => setAddOpen(true)}>
              <Plus className="size-4" /> Add source
            </Button>
          }
        />
      ) : (
        <div
          className="grid gap-6"
          style={{ gridTemplateColumns: selected ? "minmax(0,1fr) 320px" : "1fr" }}
        >
          <div className="flex flex-col gap-6" data-testid="sources-groups">
            {groups.map((group) => (
              <SourceGroup
                key={group.tier}
                group={group}
                onToggle={(name, enabled) =>
                  updateSource.mutate({ name, patch: { enabled } })
                }
                onSelect={(src) => setSelected(src)}
                selectedName={selected?.name}
              />
            ))}
          </div>

          {selected ? (
            <SourceDetailPanel
              source={selected}
              onClose={() => setSelected(null)}
            />
          ) : null}
        </div>
      )}

      <AddSourceDialog open={addOpen} onOpenChange={setAddOpen} />
    </div>
  );
}

interface SourceGroupProps {
  group: Group;
  onToggle: (name: string, enabled: boolean) => void;
  onSelect: (s: Source) => void;
  selectedName?: string;
}

function SourceGroup({ group, onToggle, onSelect, selectedName }: SourceGroupProps) {
  const enabledCount = group.sources.filter((s) => s.enabled !== false).length;
  return (
    <section
      data-testid={`source-group-${group.tier}`}
      className="border-border bg-card flex flex-col rounded-none border"
    >
      <header className="border-border bg-muted/30 flex items-center justify-between border-b px-4 py-2">
        <h2 className="text-foreground text-sm font-semibold tracking-tight">
          {TIER_LABEL[group.tier]}
        </h2>
        <span className="text-muted-foreground text-xs">
          {enabledCount} / {group.sources.length} enabled
        </span>
      </header>
      {group.sources.length === 0 ? (
        <p className="text-muted-foreground px-4 py-6 text-center text-xs">
          No sources in this tier.
        </p>
      ) : (
        <table
          className="w-full text-sm"
          data-testid={`source-table-${group.tier}`}
        >
          <thead className="text-muted-foreground border-border border-b text-[11px] tracking-wider uppercase">
            <tr>
              <Th>Name</Th>
              <Th>Type</Th>
              <Th>Last run</Th>
              <Th>Items</Th>
              <Th className="text-right">Enabled</Th>
            </tr>
          </thead>
          <tbody>
            {group.sources.map((src) => (
              <SourceRow
                key={src.name}
                source={src}
                onToggle={onToggle}
                onSelect={onSelect}
                selected={selectedName === src.name}
              />
            ))}
          </tbody>
        </table>
      )}
    </section>
  );
}

function Th({
  children,
  className,
}: {
  children: React.ReactNode;
  className?: string;
}) {
  return (
    <th
      scope="col"
      className={cn(
        "px-3 py-2 text-left text-[11px] font-medium tracking-wider uppercase",
        className,
      )}
    >
      {children}
    </th>
  );
}

interface SourceRowProps {
  source: Source;
  onToggle: (name: string, enabled: boolean) => void;
  onSelect: (s: Source) => void;
  selected: boolean;
}

function SourceRow({ source, onToggle, onSelect, selected }: SourceRowProps) {
  const enabled = source.enabled !== false;
  return (
    <tr
      data-testid={`source-row-${source.name}`}
      className={cn(
        "border-border hover:bg-muted/40 border-b transition-colors",
        selected && "bg-muted/60",
      )}
    >
      <td className="px-3 py-2.5">
        <button
          type="button"
          onClick={() => onSelect(source)}
          className="text-foreground hover:underline focus-visible:underline focus-visible:outline-none"
        >
          {source.name}
        </button>
        {source.url ? (
          <p className="text-muted-foreground line-clamp-1 text-[11px]">
            {source.url}
          </p>
        ) : null}
      </td>
      <td className="px-3 py-2.5">
        <Badge variant="outline" className="rounded-none">
          {source.source_type ?? "unknown"}
        </Badge>
      </td>
      <td className="text-muted-foreground px-3 py-2.5 text-xs">
        {source.last_run ?? "—"}
      </td>
      <td className="text-muted-foreground px-3 py-2.5 text-xs">
        {source.item_count != null ? source.item_count : "—"}
      </td>
      <td className="px-3 py-2.5 text-right">
        <label className="inline-flex cursor-pointer items-center gap-2">
          <span className="text-muted-foreground text-[11px]">
            {enabled ? "On" : "Off"}
          </span>
          <input
            data-testid={`source-toggle-${source.name}`}
            aria-label={`Toggle ${source.name}`}
            type="checkbox"
            checked={enabled}
            onChange={(e) => onToggle(source.name, e.target.checked)}
            className="size-4"
          />
        </label>
      </td>
    </tr>
  );
}

function SourceDetailPanel({
  source,
  onClose,
}: {
  source: Source;
  onClose: () => void;
}) {
  return (
    <aside
      data-testid="source-detail-panel"
      className="border-border bg-card flex h-fit flex-col gap-3 rounded-none border p-4"
    >
      <div className="flex items-start justify-between gap-2">
        <div>
          <p className="text-muted-foreground text-[11px] tracking-wider uppercase">
            {TIER_LABEL[bucketTier(source)]}
          </p>
          <h3 className="text-foreground text-sm font-semibold">
            {source.name}
          </h3>
        </div>
        <Button size="sm" variant="ghost" onClick={onClose}>
          Close
        </Button>
      </div>

      <DetailRow label="Type" value={source.source_type ?? "—"} />
      <DetailRow label="URL" value={source.url ?? "—"} mono />
      <DetailRow
        label="Priority"
        value={source.priority != null ? String(source.priority) : "—"}
      />
      <DetailRow
        label="Max items"
        value={source.max_items != null ? String(source.max_items) : "—"}
      />
      <DetailRow label="Trust level" value={source.trust_level ?? "—"} />
      <DetailRow label="Category" value={source.category ?? "—"} />
      <DetailRow label="Last run" value={source.last_run ?? "—"} />
      <DetailRow
        label="Item count"
        value={source.item_count != null ? String(source.item_count) : "—"}
      />
    </aside>
  );
}

function DetailRow({
  label,
  value,
  mono = false,
}: {
  label: string;
  value: string;
  mono?: boolean;
}) {
  return (
    <div className="flex flex-col gap-0.5">
      <span className="text-muted-foreground text-[10px] tracking-wider uppercase">
        {label}
      </span>
      <span
        className={cn(
          "text-foreground break-words text-xs",
          mono && "font-mono",
        )}
      >
        {value}
      </span>
    </div>
  );
}

export default Sources;
