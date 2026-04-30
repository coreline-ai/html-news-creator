import { useMutation, useQueryClient, type UseMutationResult } from "@tanstack/react-query";
import { apiFetch, type ReportSection } from "@/lib/api";

// ---------------------------------------------------------------------------
// Types
// ---------------------------------------------------------------------------

export interface SectionPatchPayload {
  title?: string;
  summary_ko?: string;
  implication_ko?: string;
  image_url?: string;
}

export interface SectionPatchVariables {
  sectionId: string;
  patch: SectionPatchPayload;
  /** Optional date for query invalidation */
  date?: string;
}

export interface SectionRegenerateVariables {
  sectionId: string;
  date?: string;
}

export interface ReorderVariables {
  date: string;
  sectionIds: string[];
}

export interface PublishVariables {
  date: string;
  dryRun?: boolean;
}

export interface PublishResponse {
  status: string;
  deployed_url: string;
  report_date: string;
  details?: Record<string, unknown>;
}

export interface RegenerateResponse {
  status: string;
  section_id: string;
  note?: string;
}

export interface ReorderResponse {
  report_date: string;
  sections: ReportSection[];
}

// ---------------------------------------------------------------------------
// Mutations
// ---------------------------------------------------------------------------

/** PATCH /api/sections/{id} */
export function usePatchSection(): UseMutationResult<
  { section: ReportSection },
  Error,
  SectionPatchVariables
> {
  const qc = useQueryClient();
  return useMutation({
    mutationFn: async ({ sectionId, patch }) => {
      return apiFetch<{ section: ReportSection }>(
        `/api/sections/${encodeURIComponent(sectionId)}`,
        {
          method: "PATCH",
          body: JSON.stringify(patch),
        },
      );
    },
    onSuccess: (_data, vars) => {
      if (vars.date) {
        void qc.invalidateQueries({ queryKey: ["report", vars.date] });
      }
    },
  });
}

/** POST /api/sections/{id}/regenerate */
export function useRegenerateSection(): UseMutationResult<
  RegenerateResponse,
  Error,
  SectionRegenerateVariables
> {
  const qc = useQueryClient();
  return useMutation({
    mutationFn: async ({ sectionId }) => {
      return apiFetch<RegenerateResponse>(
        `/api/sections/${encodeURIComponent(sectionId)}/regenerate`,
        { method: "POST", body: "{}" },
      );
    },
    onSuccess: (_data, vars) => {
      if (vars.date) {
        void qc.invalidateQueries({ queryKey: ["report", vars.date] });
      }
    },
  });
}

/** POST /api/reports/{date}/reorder */
export function useReorderSections(): UseMutationResult<
  ReorderResponse,
  Error,
  ReorderVariables
> {
  const qc = useQueryClient();
  return useMutation({
    mutationFn: async ({ date, sectionIds }) => {
      return apiFetch<ReorderResponse>(
        `/api/reports/${encodeURIComponent(date)}/reorder`,
        {
          method: "POST",
          body: JSON.stringify({ section_ids: sectionIds }),
        },
      );
    },
    onSuccess: (_data, vars) => {
      void qc.invalidateQueries({ queryKey: ["report", vars.date] });
    },
  });
}

/** POST /api/reports/{date}/publish */
export function usePublishReport(): UseMutationResult<
  PublishResponse,
  Error,
  PublishVariables
> {
  const qc = useQueryClient();
  return useMutation({
    mutationFn: async ({ date, dryRun = false }) => {
      return apiFetch<PublishResponse>(
        `/api/reports/${encodeURIComponent(date)}/publish`,
        {
          method: "POST",
          body: JSON.stringify({ dry_run: dryRun }),
        },
      );
    },
    onSuccess: (_data, vars) => {
      void qc.invalidateQueries({ queryKey: ["report", vars.date] });
      void qc.invalidateQueries({ queryKey: ["reports"] });
    },
  });
}
