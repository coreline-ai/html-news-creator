import { Link } from "react-router-dom";
import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { Skeleton } from "@/components/ui/skeleton";
import { EmptyState } from "@/components/EmptyState";
import { ReportCalendar } from "@/components/ReportCalendar";
import { useReports } from "@/hooks/useReports";
import { SIDEBAR_NAV_ICONS } from "@/lib/icons";
import { todayKstISO, formatKstDateTime } from "@/lib/kst";
import { cn } from "@/lib/utils";
import type { ReportSummary } from "@/lib/api";
import {
  AlertCircle,
  CalendarClock,
  FileText,
  Plus,
  RefreshCw,
} from "lucide-react";

function formatTime(iso?: string | null): string {
  return formatKstDateTime(iso);
}

export function Dashboard() {
  const today = todayKstISO();
  const { data: reports, isLoading, isError, error, refetch } = useReports({
    limit: 90,
  });

  const todayReport = reports?.find((r) => r.report_date === today);

  return (
    <div className="mx-auto flex max-w-[1200px] flex-col gap-8 px-6 py-6">
      <header className="flex items-end justify-between gap-4">
        <div>
          <h1 className="text-foreground text-xl font-semibold tracking-tight">
            Dashboard
          </h1>
          <p className="text-muted-foreground text-sm">
            Today is{" "}
            <span className="text-foreground font-medium">{today}</span>
          </p>
        </div>
        <Button asChild size="sm" data-testid="dashboard-header-new-report">
          <Link to="/reports/new">
            <FileText className="size-4" aria-hidden="true" />
            New Report
          </Link>
        </Button>
      </header>

      {/* Today + Quick actions */}
      <section
        aria-label="Today and quick actions"
        className="grid gap-4"
        style={{ gridTemplateColumns: "1fr 1fr 1fr 1fr" }}
      >
        <TodayCard report={todayReport} loading={isLoading} />
        <QuickActionCard
          to="/reports/new"
          title="New report"
          description="Run the pipeline with custom options."
          icon={<Plus className="size-4" aria-hidden="true" />}
          featured
          testId="dashboard-new-report-card"
        />
        <QuickActionCard
          to="/reports"
          title="Replay yesterday"
          description="Re-render the previous KST date."
          icon={<RefreshCw className="size-4" aria-hidden="true" />}
        />
        <QuickActionCard
          to="/policy"
          title="Schedule run"
          description="Configure cadence and policy."
          icon={
            <SIDEBAR_NAV_ICONS.schedule
              className="size-4"
              aria-hidden="true"
            />
          }
        />
      </section>

      {/* Run history & Calendar — single split card */}
      <section
        aria-label="Run history and calendar"
        className="flex flex-col gap-3"
      >
        <div
          data-testid="run-history-calendar-card"
          className="border-border bg-card text-card-foreground rounded-none border"
        >
          {/* Card header */}
          <div className="border-border flex items-center justify-between border-b px-6 py-3">
            <h2 className="text-foreground flex items-center gap-2 text-base font-semibold">
              <CalendarClock
                className="text-muted-foreground size-4"
                aria-hidden="true"
              />
              Run history & Calendar
            </h2>
            <span className="text-muted-foreground text-xs">
              Today · {today}
            </span>
          </div>

          {/* Split body: 1fr | 280px on md+, stacked on mobile. */}
          <div className="grid grid-cols-1 md:grid-cols-[1fr_280px]">
            {/* Left — Run history */}
            <div className="flex min-w-0 flex-col">
              {isLoading ? (
                <div className="flex flex-col gap-2 p-4">
                  <Skeleton className="h-8 w-full" />
                  <Skeleton className="h-8 w-full" />
                  <Skeleton className="h-8 w-full" />
                </div>
              ) : isError ? (
                <EmptyState
                  icon={AlertCircle}
                  title="Could not load reports"
                  description={
                    error instanceof Error
                      ? error.message
                      : "API request failed. The backend may be offline."
                  }
                  action={
                    <Button
                      size="sm"
                      variant="outline"
                      onClick={() => {
                        void refetch();
                      }}
                    >
                      Retry
                    </Button>
                  }
                />
              ) : !reports || reports.length === 0 ? (
                <EmptyState
                  icon={FileText}
                  title="아직 리포트가 없습니다"
                  description={`오늘(${today})자 첫 리포트를 만들어보세요. 옵션을 조정하고 Run을 누르면 파이프라인이 실행됩니다.`}
                  action={
                    <div
                      className="flex items-center gap-3"
                      data-testid="dashboard-empty-actions"
                    >
                      <Button asChild size="sm">
                        <Link to="/reports/new">오늘자 첫 리포트 생성</Link>
                      </Button>
                      <Link
                        to="/settings"
                        className="text-muted-foreground hover:text-foreground text-xs underline-offset-4 hover:underline"
                      >
                        도움말 / 정책 보기
                      </Link>
                    </div>
                  }
                />
              ) : (
                <>
                  <div className="border-border flex items-center justify-end border-b px-3 py-2">
                    <Link
                      to="/reports"
                      className="text-muted-foreground hover:text-foreground text-xs font-medium"
                      data-testid="dashboard-view-all-link"
                    >
                      View all
                    </Link>
                  </div>
                  <RecentRunsTable reports={reports.slice(0, 10)} />
                </>
              )}
            </div>

            {/* Right — Calendar / Heatmap (280px on md+) */}
            <div
              className="border-border border-t md:border-l md:border-t-0"
              data-testid="run-history-calendar-pane"
            >
              <ReportCalendar
                reports={reports}
                loading={isLoading}
                error={isError ? (error as Error) : null}
                todayIso={today}
              />
            </div>
          </div>
        </div>
      </section>
    </div>
  );
}

function TodayCard({
  report,
  loading,
}: {
  report: ReportSummary | undefined;
  loading: boolean;
}) {
  return (
    <Card className="rounded-none shadow-none">
      <CardHeader>
        <CardTitle className="text-sm">Today</CardTitle>
        <CardDescription>
          {loading
            ? "Loading…"
            : report
              ? `Status: ${report.status ?? "unknown"}`
              : "No report yet"}
        </CardDescription>
      </CardHeader>
      <CardContent>
        {loading ? (
          <Skeleton className="h-4 w-3/4" />
        ) : report ? (
          <div className="text-foreground line-clamp-2 text-sm">
            {report.title ?? "(untitled)"}
          </div>
        ) : (
          <Button asChild size="sm" variant="outline">
            <Link to="/reports/new">+ Generate</Link>
          </Button>
        )}
      </CardContent>
    </Card>
  );
}

function QuickActionCard({
  to,
  title,
  description,
  icon,
  featured = false,
  testId,
}: {
  to: string;
  title: string;
  description: string;
  icon: React.ReactNode;
  featured?: boolean;
  testId?: string;
}) {
  return (
    <Link
      to={to}
      data-testid={testId}
      className={cn(
        "text-card-foreground flex flex-col gap-2 border p-4 transition-colors",
        featured
          ? "border-primary/40 bg-primary/10 shadow-[inset_0_3px_0_0_var(--primary)] hover:bg-primary/15 dark:border-primary/35 dark:bg-primary/10 dark:hover:bg-primary/15"
          : "border-border bg-card hover:bg-accent hover:text-accent-foreground",
      )}
    >
      <div
        className={cn(
          "flex items-center gap-2",
          featured ? "text-primary" : "text-muted-foreground",
        )}
      >
        {icon}
        <span
          className={cn(
            "text-foreground text-sm font-medium",
            featured && "font-semibold",
          )}
        >
          {title}
        </span>
      </div>
      <p
        className={cn(
          "text-xs",
          featured ? "text-foreground/75" : "text-muted-foreground",
        )}
      >
        {description}
      </p>
    </Link>
  );
}

function RecentRunsTable({ reports }: { reports: ReportSummary[] }) {
  return (
    <table className="w-full text-sm" data-testid="recent-runs-table">
      <thead className="bg-background border-border sticky top-0 border-b">
        <tr>
          <Th>Date</Th>
          <Th>Title</Th>
          <Th>Status</Th>
          <Th>Created</Th>
        </tr>
      </thead>
      <tbody>
        {reports.map((r) => (
          <tr
            key={r.id}
            className="hover:bg-muted border-border border-b transition-colors"
          >
            <td className="px-3 py-2.5">
              {r.report_date ? (
                <Link
                  to={`/reports/${r.report_date}`}
                  className="text-foreground hover:underline"
                >
                  {r.report_date}
                </Link>
              ) : (
                <span className="text-muted-foreground">—</span>
              )}
            </td>
            <td className="text-foreground max-w-[420px] truncate px-3 py-2.5">
              {r.title ?? "(untitled)"}
            </td>
            <td className="px-3 py-2.5">
              <StatusPill status={r.status ?? "unknown"} />
            </td>
            <td className="text-muted-foreground px-3 py-2.5">
              {formatTime(r.created_at)}
            </td>
          </tr>
        ))}
      </tbody>
    </table>
  );
}

function Th({ children }: { children: React.ReactNode }) {
  return (
    <th
      scope="col"
      className="text-muted-foreground px-3 py-2 text-left text-[11px] font-medium tracking-wider uppercase"
    >
      {children}
    </th>
  );
}

function StatusPill({ status }: { status: string }) {
  const tone =
    status === "published" || status === "ready"
      ? "bg-primary text-primary-foreground"
      : status === "failed"
        ? "bg-destructive text-destructive-foreground"
        : "bg-muted text-muted-foreground";
  return (
    <span
      className={`inline-flex h-5 items-center rounded-md px-2 text-[11px] font-medium ${tone}`}
    >
      {status}
    </span>
  );
}

export default Dashboard;
