import { lazy, Suspense, useCallback, useEffect, useState } from "react";
import {
  Outlet,
  Route,
  Routes,
  useLocation,
  useMatch,
  useNavigate,
} from "react-router-dom";
import { Sidebar, MobileSidebar } from "@/components/Sidebar";
import { HeaderBar } from "@/components/HeaderBar";
import { ErrorBoundary } from "@/components/ErrorBoundary";
import { CommandPalette } from "@/components/CommandPalette";
import { Skeleton } from "@/components/ui/skeleton";
import { apiFetch } from "@/lib/api";

// Lazy-load page bundles. All pages export `default` (verified Phase 5).
const Dashboard = lazy(() => import("@/pages/Dashboard"));
const Reports = lazy(() => import("@/pages/Reports"));
const NewReport = lazy(() => import("@/pages/NewReport"));
const ReviewReport = lazy(() => import("@/pages/ReviewReport"));
const Sources = lazy(() => import("@/pages/Sources"));
const Settings = lazy(() => import("@/pages/Settings"));
const NotFound = lazy(() => import("@/pages/NotFound"));

function PageFallback() {
  return (
    <div className="mx-auto flex max-w-[1200px] flex-col gap-4 px-6 py-6">
      <Skeleton className="h-6 w-40" />
      <Skeleton className="h-32 w-full" />
      <Skeleton className="h-32 w-full" />
    </div>
  );
}

interface ShellHandlers {
  onOpenCommandPalette: () => void;
  onOpenMobileSidebar: () => void;
}

function WorkspaceLayout({
  onOpenCommandPalette,
  onOpenMobileSidebar,
}: ShellHandlers) {
  return (
    <div className="bg-background text-foreground grid h-screen grid-cols-1 overflow-hidden md:grid-cols-[240px_1fr]">
      <Sidebar />
      <div className="flex min-w-0 flex-col overflow-hidden">
        <HeaderBar
          onOpenCommandPalette={onOpenCommandPalette}
          onOpenMobileSidebar={onOpenMobileSidebar}
        />
        <main className="flex-1 overflow-y-auto" data-testid="main-outlet">
          <ErrorBoundary>
            <Suspense fallback={<PageFallback />}>
              <Outlet />
            </Suspense>
          </ErrorBoundary>
        </main>
      </div>
    </div>
  );
}

/**
 * Detect macOS reliably across user agents (incl. iPad Pro that reports
 * "MacIntel" with touch). Falls back to platform sniffing in tests.
 */
function isMacPlatform(): boolean {
  if (typeof navigator === "undefined") return false;
  const platform = navigator.platform || "";
  return /Mac|iPhone|iPad|iPod/.test(platform);
}

function App() {
  const navigate = useNavigate();
  const location = useLocation();
  const reviewMatch = useMatch("/reports/:date");

  const [paletteOpen, setPaletteOpen] = useState(false);
  const [mobileSidebarOpen, setMobileSidebarOpen] = useState(false);

  // Close mobile drawer when route changes (covers desktop-resize + nav).
  useEffect(() => {
    setMobileSidebarOpen(false);
  }, [location.pathname]);

  // Re-run last: POST /api/runs. On ReviewReport routes, scope to that date.
  // Elsewhere, route to /reports/new so the user can pick options.
  const rerunLast = useCallback(async () => {
    const date = reviewMatch?.params?.date;
    if (!date) {
      navigate("/reports/new");
      return;
    }
    try {
      await apiFetch("/api/runs", {
        method: "POST",
        body: JSON.stringify({ date, mode: "full" }),
      });
    } catch (err) {
      // eslint-disable-next-line no-console
      console.error("rerun-last failed", err);
    }
  }, [navigate, reviewMatch]);

  // Publish current: only meaningful on ReviewReport. POST publish endpoint.
  const publishCurrent = useCallback(async () => {
    const date = reviewMatch?.params?.date;
    if (!date) return;
    try {
      await apiFetch(
        `/api/reports/${encodeURIComponent(date)}/publish`,
        { method: "POST", body: JSON.stringify({ dry_run: false }) },
      );
    } catch (err) {
      // eslint-disable-next-line no-console
      console.error("publish-current failed", err);
    }
  }, [reviewMatch]);

  // Global keyboard shortcuts: ⌘K palette, R rerun, P publish.
  useEffect(() => {
    const isEditableTarget = (el: EventTarget | null): boolean => {
      if (!(el instanceof HTMLElement)) return false;
      const tag = el.tagName;
      if (tag === "INPUT" || tag === "TEXTAREA" || tag === "SELECT") return true;
      if (el.isContentEditable) return true;
      return false;
    };

    const handler = (e: KeyboardEvent) => {
      const mod = isMacPlatform() ? e.metaKey : e.ctrlKey;

      // ⌘K / Ctrl+K — toggle command palette.
      if (mod && (e.key === "k" || e.key === "K")) {
        e.preventDefault();
        setPaletteOpen((open) => !open);
        return;
      }

      // Single-letter shortcuts: ignore when typing in an input or when a
      // modifier is held, and when the palette dialog is itself open.
      if (paletteOpen) return;
      if (e.metaKey || e.ctrlKey || e.altKey) return;
      if (isEditableTarget(e.target)) return;

      if (e.key === "r" || e.key === "R") {
        e.preventDefault();
        void rerunLast();
        return;
      }
      if (e.key === "p" || e.key === "P") {
        if (!reviewMatch) return;
        e.preventDefault();
        void publishCurrent();
      }
    };

    window.addEventListener("keydown", handler);
    return () => window.removeEventListener("keydown", handler);
  }, [paletteOpen, rerunLast, publishCurrent, reviewMatch]);

  const openPalette = useCallback(() => setPaletteOpen(true), []);
  const openMobileSidebar = useCallback(() => setMobileSidebarOpen(true), []);

  return (
    <>
      <Routes>
        <Route
          element={
            <WorkspaceLayout
              onOpenCommandPalette={openPalette}
              onOpenMobileSidebar={openMobileSidebar}
            />
          }
        >
          <Route index element={<Dashboard />} />
          <Route path="/reports" element={<Reports />} />
          <Route path="/reports/new" element={<NewReport />} />
          <Route path="/reports/:date" element={<ReviewReport />} />
          <Route path="/sources" element={<Sources />} />
          <Route path="/settings" element={<Settings />} />
          <Route path="*" element={<NotFound />} />
        </Route>
      </Routes>

      <MobileSidebar
        open={mobileSidebarOpen}
        onOpenChange={setMobileSidebarOpen}
      />

      <CommandPalette
        open={paletteOpen}
        onOpenChange={setPaletteOpen}
        onRerunLast={rerunLast}
        onPublishCurrent={publishCurrent}
      />
    </>
  );
}

export default App;
