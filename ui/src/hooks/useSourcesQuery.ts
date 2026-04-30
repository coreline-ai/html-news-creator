import { useQuery, type UseQueryResult } from "@tanstack/react-query";
import { apiFetch } from "@/lib/api";

/**
 * A single source row as returned by `GET /api/sources`. The backend reads
 * this from `data/sources_registry.yaml` so all fields are best-effort and
 * may be absent on legacy entries.
 */
export interface Source {
  name: string;
  source_type?: string | null;
  url?: string | null;
  trust_level?: string | null;
  source_tier?: string | null;
  category?: string | null;
  priority?: number | null;
  max_items?: number | null;
  enabled?: boolean;
  last_run?: string | null;
  item_count?: number | null;
  [key: string]: unknown;
}

export interface SourcesListResponse {
  sources: Source[];
}

export const SOURCES_QUERY_KEY = ["sources"] as const;

/** GET /api/sources — registry-backed list. */
export function useSourcesQuery(): UseQueryResult<Source[], Error> {
  return useQuery<Source[], Error>({
    queryKey: SOURCES_QUERY_KEY,
    queryFn: async () => {
      const data = await apiFetch<SourcesListResponse>("/api/sources");
      return Array.isArray(data?.sources) ? data.sources : [];
    },
  });
}
