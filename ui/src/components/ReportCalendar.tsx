import { useMemo } from "react";
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs";
import { Skeleton } from "@/components/ui/skeleton";
import { useAppStore } from "@/lib/store";
import type { ReportSummary } from "@/lib/api";
import { todayKstISO } from "@/lib/kst";
import { ReportCalendarMonthView } from "./ReportCalendar.MonthView";
import { ReportCalendarHeatmapView } from "./ReportCalendar.HeatmapView";

export type CalendarStatus = "published" | "draft" | "failed";

export interface ReportCalendarProps {
  reports: ReportSummary[] | undefined;
  loading?: boolean;
  error?: Error | null;
  todayIso?: string;
  className?: string;
}

/**
 * Map a backend status string to one of the four UI buckets.
 *
 * - "published" / "ready" → published
 * - "failed" / "error" → failed
 * - everything else with a date → draft (treat as in-progress)
 */
function bucket(status: string | null | undefined): CalendarStatus {
  if (status === "published" || status === "ready") return "published";
  if (status === "failed" || status === "error") return "failed";
  return "draft";
}

export function ReportCalendar({
  reports,
  loading = false,
  error = null,
  todayIso,
  className,
}: ReportCalendarProps) {
  const calendarTab = useAppStore((s) => s.calendarTab);
  const setCalendarTab = useAppStore((s) => s.setCalendarTab);

  const today = todayIso ?? todayKstISO();

  const statusByDate = useMemo(() => {
    const m = new Map<string, CalendarStatus>();
    if (!reports) return m;
    for (const r of reports) {
      if (!r.report_date) continue;
      // First-write wins (reports list is newest-first; older duplicates skipped).
      if (!m.has(r.report_date)) {
        m.set(r.report_date, bucket(r.status));
      }
    }
    return m;
  }, [reports]);

  return (
    <div
      data-testid="report-calendar"
      className={["flex flex-col", className].filter(Boolean).join(" ")}
    >
      <Tabs
        value={calendarTab}
        onValueChange={(v) =>
          setCalendarTab(v === "heatmap" ? "heatmap" : "month")
        }
        className="gap-3"
      >
        <div className="px-3 pt-3">
          <TabsList className="grid w-full grid-cols-2">
            <TabsTrigger value="month" data-testid="calendar-tab-month">
              월별
            </TabsTrigger>
            <TabsTrigger value="heatmap" data-testid="calendar-tab-heatmap">
              90일 추세
            </TabsTrigger>
          </TabsList>
        </div>

        {loading ? (
          <div className="flex flex-col gap-2 px-3 pb-3">
            <Skeleton className="h-6 w-32" />
            <Skeleton className="h-40 w-full" />
          </div>
        ) : error ? (
          <div
            role="alert"
            className="text-muted-foreground px-3 pb-3 text-sm"
            data-testid="report-calendar-error"
          >
            달력을 불러오지 못했습니다.
          </div>
        ) : (
          <>
            <TabsContent value="month" className="m-0">
              <ReportCalendarMonthView
                statusByDate={statusByDate}
                todayIso={today}
              />
            </TabsContent>
            <TabsContent value="heatmap" className="m-0">
              <ReportCalendarHeatmapView
                statusByDate={statusByDate}
                todayIso={today}
              />
            </TabsContent>
          </>
        )}
      </Tabs>
    </div>
  );
}

export default ReportCalendar;
