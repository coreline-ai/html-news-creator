import { useQuery, type UseQueryResult } from "@tanstack/react-query";
import {
  apiFetch,
  type ReportDetail,
  type ReportSummary,
  type ReportsListResponse,
} from "@/lib/api";

export interface UseReportsOptions {
  limit?: number;
}

/** GET /api/reports?limit=N */
export function useReports(
  opts: UseReportsOptions = {},
): UseQueryResult<ReportSummary[], Error> {
  const limit = opts.limit ?? 20;
  return useQuery<ReportSummary[], Error>({
    queryKey: ["reports", { limit }],
    queryFn: async () => {
      const data = await apiFetch<ReportsListResponse>(
        `/api/reports?limit=${limit}`,
      );
      return Array.isArray(data?.reports) ? data.reports : [];
    },
  });
}

/** GET /api/reports/{date_kst} */
export function useReport(
  date: string | null | undefined,
): UseQueryResult<ReportDetail, Error> {
  return useQuery<ReportDetail, Error>({
    queryKey: ["report", date],
    enabled: Boolean(date),
    queryFn: async () => {
      return apiFetch<ReportDetail>(`/api/reports/${date}`);
    },
  });
}
