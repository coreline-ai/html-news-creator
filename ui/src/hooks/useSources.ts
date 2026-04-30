import {
  useMutation,
  useQueryClient,
  type UseMutationResult,
} from "@tanstack/react-query";
import { apiFetch } from "@/lib/api";
import {
  SOURCES_QUERY_KEY,
  type Source,
} from "@/hooks/useSourcesQuery";

/**
 * Fields the registry update endpoint accepts. Mirrors
 * `app/admin/sources_admin.ALLOWED_UPDATE_FIELDS`.
 */
export interface SourcePatch {
  enabled?: boolean;
  priority?: number;
  max_items?: number;
  trust_level?: string;
  source_tier?: string;
  category?: string;
}

export interface UpdateSourceVars {
  name: string;
  patch: SourcePatch;
}

/**
 * PUT /api/sources/{name} — patches a single source. The mutation does an
 * **optimistic** update on the `["sources"]` cache so the toggle flips
 * immediately. On error the previous list is restored.
 */
export function useUpdateSource(): UseMutationResult<
  { source: Source },
  Error,
  UpdateSourceVars,
  { previous: Source[] | undefined }
> {
  const qc = useQueryClient();

  return useMutation<
    { source: Source },
    Error,
    UpdateSourceVars,
    { previous: Source[] | undefined }
  >({
    mutationFn: async ({ name, patch }) => {
      return apiFetch<{ source: Source }>(
        `/api/sources/${encodeURIComponent(name)}`,
        {
          method: "PUT",
          body: JSON.stringify(patch),
        },
      );
    },
    onMutate: async ({ name, patch }) => {
      await qc.cancelQueries({ queryKey: SOURCES_QUERY_KEY });
      const previous = qc.getQueryData<Source[]>(SOURCES_QUERY_KEY);
      if (previous) {
        qc.setQueryData<Source[]>(
          SOURCES_QUERY_KEY,
          previous.map((s) => (s.name === name ? { ...s, ...patch } : s)),
        );
      }
      return { previous };
    },
    onError: (_err, _vars, ctx) => {
      if (ctx?.previous) {
        qc.setQueryData(SOURCES_QUERY_KEY, ctx.previous);
      }
    },
    onSettled: () => {
      void qc.invalidateQueries({ queryKey: SOURCES_QUERY_KEY });
    },
  });
}

export interface NewSourceInput {
  name: string;
  url: string;
  source_type: string;
  source_tier: string;
}

/**
 * POST /api/sources — appends a new source to the registry. The backend
 * endpoint may not exist yet in early phases — callers should treat 404 as
 * a "BE not ready" signal and surface it to the user.
 */
export function useAddSource(): UseMutationResult<
  { source: Source },
  Error,
  NewSourceInput
> {
  const qc = useQueryClient();
  return useMutation<{ source: Source }, Error, NewSourceInput>({
    mutationFn: async (input) => {
      return apiFetch<{ source: Source }>("/api/sources", {
        method: "POST",
        body: JSON.stringify(input),
      });
    },
    onSuccess: () => {
      void qc.invalidateQueries({ queryKey: SOURCES_QUERY_KEY });
    },
  });
}
