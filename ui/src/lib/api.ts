import { QueryClient } from "@tanstack/react-query";

/**
 * Lightweight fetch wrapper. All `/api/*` calls in dev are proxied to
 * FastAPI on port 8000 via vite.config.ts.
 */
export class ApiError extends Error {
  status: number;
  body: unknown;

  constructor(message: string, status: number, body: unknown) {
    super(message);
    this.name = "ApiError";
    this.status = status;
    this.body = body;
  }
}

export async function apiFetch<T = unknown>(
  path: string,
  init?: RequestInit,
): Promise<T> {
  const res = await fetch(path, {
    headers: {
      "Content-Type": "application/json",
      ...(init?.headers ?? {}),
    },
    ...init,
  });

  if (!res.ok) {
    let body: unknown = null;
    try {
      body = await res.json();
    } catch {
      try {
        body = await res.text();
      } catch {
        body = null;
      }
    }
    throw new ApiError(
      `API ${res.status} ${res.statusText} for ${path}`,
      res.status,
      body,
    );
  }

  // 204 / empty body
  if (res.status === 204) {
    return undefined as T;
  }
  const ct = res.headers.get("content-type") ?? "";
  if (ct.includes("application/json")) {
    return (await res.json()) as T;
  }
  return (await res.text()) as unknown as T;
}

/** Shared QueryClient. Defaults are conservative — single-user local app. */
export const queryClient = new QueryClient({
  defaultOptions: {
    queries: {
      staleTime: 30_000,
      gcTime: 5 * 60_000,
      retry: 1,
      refetchOnWindowFocus: false,
    },
  },
});

// ---------------------------------------------------------------------------
// Domain types — keep loose; backend contracts may evolve.
// ---------------------------------------------------------------------------

export interface ReportSummary {
  id: string;
  report_date: string | null;
  title: string | null;
  status: string | null;
  summary_ko?: string | null;
  stats_json?: Record<string, unknown> | null;
  created_at?: string | null;
  updated_at?: string | null;
  published_at?: string | null;
}

export interface ReportDetail extends ReportSummary {
  method_json?: Record<string, unknown> | null;
  sections: ReportSection[];
}

export interface ReportSection {
  id: string;
  section_order: number;
  title: string | null;
  lead?: string | null;
  fact_summary?: string | null;
  social_signal_summary?: string | null;
  inference_summary?: string | null;
  caution?: string | null;
  image_evidence_json?: unknown[] | Record<string, unknown> | null;
  sources_json?: unknown[] | Record<string, unknown> | null;
  confidence?: number | string | null;
  importance_score?: number | null;
  tags_json?: unknown[] | Record<string, unknown> | null;
}

export interface ReportsListResponse {
  reports: ReportSummary[];
}
