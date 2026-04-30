import { Outlet, Route, Routes } from "react-router-dom";
import { Sidebar } from "@/components/Sidebar";
import { HeaderBar } from "@/components/HeaderBar";
import { EmptyState } from "@/components/EmptyState";
import { Dashboard } from "@/pages/Dashboard";
import { SIDEBAR_NAV_ICONS } from "@/lib/icons";

function WorkspaceLayout() {
  return (
    <div
      className="bg-background text-foreground grid h-screen overflow-hidden"
      style={{ gridTemplateColumns: "240px 1fr" }}
    >
      <Sidebar />
      <div className="flex min-w-0 flex-col overflow-hidden">
        <HeaderBar />
        <main className="flex-1 overflow-y-auto" data-testid="main-outlet">
          <Outlet />
        </main>
      </div>
    </div>
  );
}

function ReportsIndexPlaceholder() {
  return (
    <div className="mx-auto max-w-[1200px] px-6 py-6">
      <EmptyState
        icon={SIDEBAR_NAV_ICONS.reports}
        title="Reports list — coming in Phase 4"
        description="The Review screen will list daily reports here."
      />
    </div>
  );
}

function ReportDetailPlaceholder() {
  return (
    <div className="mx-auto max-w-[1200px] px-6 py-6">
      <EmptyState
        icon={SIDEBAR_NAV_ICONS.reports}
        title="Report detail — coming in Phase 4"
        description="Section reorder, edit, publish actions will live here."
      />
    </div>
  );
}

function NewReportPlaceholder() {
  return (
    <div className="mx-auto max-w-[1200px] px-6 py-6">
      <EmptyState
        icon={SIDEBAR_NAV_ICONS.reports}
        title="New Report — coming in Phase 3"
        description="Run options panel + live iframe preview will live here."
      />
    </div>
  );
}

function SourcesPlaceholder() {
  return (
    <div className="mx-auto max-w-[1200px] px-6 py-6">
      <EmptyState
        icon={SIDEBAR_NAV_ICONS.sources}
        title="Sources — coming in Phase 5"
        description="Manage 37 sources, toggle on/off, add new entries."
      />
    </div>
  );
}

function SettingsPlaceholder() {
  return (
    <div className="mx-auto max-w-[1200px] px-6 py-6">
      <EmptyState
        icon={SIDEBAR_NAV_ICONS.policy}
        title="Policy & Settings — coming in Phase 5"
        description="Editorial policy form (scoring, quotas, target sections)."
      />
    </div>
  );
}

function NotFound() {
  return (
    <div className="mx-auto max-w-[1200px] px-6 py-6">
      <EmptyState
        title="Page not found"
        description="The route you requested does not exist."
      />
    </div>
  );
}

function App() {
  return (
    <Routes>
      <Route element={<WorkspaceLayout />}>
        <Route index element={<Dashboard />} />
        <Route path="/reports" element={<ReportsIndexPlaceholder />} />
        <Route path="/reports/new" element={<NewReportPlaceholder />} />
        <Route path="/reports/:date" element={<ReportDetailPlaceholder />} />
        <Route path="/sources" element={<SourcesPlaceholder />} />
        <Route path="/settings" element={<SettingsPlaceholder />} />
        <Route path="*" element={<NotFound />} />
      </Route>
    </Routes>
  );
}

export default App;
