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
import { useReports } from "@/hooks/useReports";
import { SIDEBAR_NAV_ICONS } from "@/lib/icons";
import type { ReportSummary } from "@/lib/api";
import { FileText, Plus, RefreshCw, AlertCircle } from "lucide-react";

const DATE_FMT = new Intl.DateTimeFormat("en-CA", {
  year: "numeric",
  month: "2-digit",
  day: "2-digit",
});

function todayKst(): string {
  return DATE_FMT.format(new Date());
}

function formatTime(iso?: string | null): string {
  if (!iso) return "—";
  const d = new Date(iso);
  if (Number.isNaN(d.getTime())) return iso;
  return d.toLocaleString();
}

export function Dashboard() {
  const today = todayKst();
  const { data: reports, isLoading, isError, error, refetch } = useReports({
    limit: 10,
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
        />
        <QuickActionCard
          to="/reports"
          title="Replay yesterday"
          description="Re-render the previous KST date."
          icon={<RefreshCw className="size-4" aria-hidden="true" />}
        />
        <QuickActionCard
          to="/settings"
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

      {/* Recent runs */}
      <section aria-label="Recent runs" className="flex flex-col gap-3">
        <div className="flex items-center justify-between">
          <h2 className="text-foreground text-base font-semibold">
            Recent runs
          </h2>
          <Link
            to="/reports"
            className="text-muted-foreground hover:text-foreground text-xs"
          >
            View all
          </Link>
        </div>

        <Card className="rounded-none gap-0 py-0 shadow-none">
          <CardContent className="px-0">
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
              <RecentRunsTable reports={reports.slice(0, 10)} />
            )}
          </CardContent>
        </Card>
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
}: {
  to: string;
  title: string;
  description: string;
  icon: React.ReactNode;
}) {
  return (
    <Link
      to={to}
      className="border-border bg-card text-card-foreground hover:bg-accent hover:text-accent-foreground flex flex-col gap-2 border p-4 transition-colors"
    >
      <div className="text-muted-foreground flex items-center gap-2">
        {icon}
        <span className="text-foreground text-sm font-medium">{title}</span>
      </div>
      <p className="text-muted-foreground text-xs">{description}</p>
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
