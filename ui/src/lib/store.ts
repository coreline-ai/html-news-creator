import { create } from "zustand";
import { persist, createJSONStorage } from "zustand/middleware";
import { todayKstISO } from "@/lib/kst";

export type Theme = "dark" | "light";
export type PreviewMode = "live" | "section";
export type RunMode = "full" | "rss-only";
export type OutputTheme = "dark" | "light" | "newsroom-white";
export type SourceType = "rss" | "github" | "arxiv" | "website";
export type DeployTarget = "netlify" | "local-only";
export type CalendarTab = "month" | "heatmap";

export interface SectionQuotas {
  product: number;
  tooling: number;
  research: number;
  industry: number;
  policy: number;
}

/**
 * Run options used by NewReport (Phase 3). Defaults track
 * `data/editorial_policy.yaml` so changing the policy does not silently
 * desync the UI.
 */
export interface RunOptions {
  // ------------------------------------------------------- A. Execution
  date: string; // YYYY-MM-DD KST
  mode: RunMode;
  range_from: string | null;
  range_to: string | null;
  dry_run: boolean;
  source_types: SourceType[];

  // ----------------------------------------------------- B. Editorial
  target_sections: number;
  min_section_score: number;
  quotas: SectionQuotas;
  cluster_bonus: number;
  image_required: boolean;
  arxiv_max: number;
  community_max: number;

  // -------------------------------------------------------- D. Output
  output_theme: OutputTheme;
  language: string;
  format: "html" | "markdown";

  // ----------------------------------------------------- E. Publishing
  deploy_target: DeployTarget;
  slack_notify: boolean;
  publish_at: string | null; // ISO; null = on completion
}

export interface ActiveRun {
  run_id: string;
  started_at: string;
  options: RunOptions;
}

export const DEFAULT_RUN_OPTIONS: RunOptions = {
  date: todayKstISO(),
  mode: "full",
  range_from: null,
  range_to: null,
  dry_run: false,
  source_types: ["rss", "github", "arxiv", "website"],

  target_sections: 10,
  min_section_score: 35,
  quotas: { product: 4, tooling: 4, research: 1, industry: 1, policy: 1 },
  cluster_bonus: 5,
  image_required: false,
  arxiv_max: 1,
  community_max: 1,

  output_theme: "dark",
  language: "ko",
  format: "html",

  deploy_target: "netlify",
  slack_notify: true,
  publish_at: null,
};

interface AppState {
  theme: Theme;
  setTheme: (t: Theme) => void;
  toggleTheme: () => void;

  runOptions: RunOptions;
  setOption: <K extends keyof RunOptions>(key: K, value: RunOptions[K]) => void;
  setQuota: (key: keyof SectionQuotas, value: number) => void;
  resetOptions: () => void;

  previewMode: PreviewMode;
  setPreviewMode: (m: PreviewMode) => void;

  activeRun: ActiveRun | null;
  setActiveRun: (run: ActiveRun | null) => void;

  calendarTab: CalendarTab;
  setCalendarTab: (tab: CalendarTab) => void;
}

// ThemeToggle path persists the preferred theme under this localStorage key.
// We keep the same key here so the two writers stay in sync (single source).
const THEME_STORAGE_KEY = "theme";

// Bumped together with the persisted shape below. If the persisted run
// options shape changes incompatibly, bump this and add a `migrate` hook.
const PERSIST_VERSION = 1;

function readInitialTheme(): Theme {
  if (typeof window === "undefined") return "dark";
  try {
    const stored = window.localStorage.getItem(THEME_STORAGE_KEY);
    if (stored === "light" || stored === "dark") return stored;
  } catch {
    // ignore
  }
  return document.documentElement.classList.contains("dark") ? "dark" : "dark";
}

function applyTheme(theme: Theme) {
  if (typeof document === "undefined") return;
  const root = document.documentElement;
  // Keep the explicit light marker in sync with `.dark`. Design tokens use
  // `:root:not(.light)` for OS-level dark fallback, so merely removing
  // `.dark` is not enough on systems that prefer dark mode.
  root.classList.toggle("dark", theme === "dark");
  root.classList.toggle("light", theme === "light");
  try {
    window.localStorage.setItem(THEME_STORAGE_KEY, theme);
  } catch {
    // ignore
  }
}

/**
 * Slice-shape persisted to `localStorage` under `news-studio-options`.
 * Only fields that should survive refresh — `theme` is intentionally NOT in
 * here because `ThemeToggle`/`applyTheme` already write it under the legacy
 * "theme" key (used by the inline pre-React boot script in `index.html`).
 * `previewMode` is duplicated in `useReviewStore` for the Review screen and
 * is not persisted from here.
 */
interface PersistedAppState {
  runOptions: RunOptions;
  activeRun: ActiveRun | null;
  calendarTab: CalendarTab;
}

export const useAppStore = create<AppState>()(
  persist(
    (set, get) => ({
      theme: readInitialTheme(),
      setTheme: (theme) => {
        applyTheme(theme);
        set({ theme });
      },
      toggleTheme: () => {
        const next: Theme = get().theme === "dark" ? "light" : "dark";
        applyTheme(next);
        set({ theme: next });
      },

      runOptions: { ...DEFAULT_RUN_OPTIONS },
      setOption: (key, value) =>
        set((s) => ({ runOptions: { ...s.runOptions, [key]: value } })),
      setQuota: (key, value) =>
        set((s) => ({
          runOptions: {
            ...s.runOptions,
            quotas: { ...s.runOptions.quotas, [key]: value },
          },
        })),
      resetOptions: () => set({ runOptions: { ...DEFAULT_RUN_OPTIONS } }),

      previewMode: "live",
      setPreviewMode: (previewMode) => set({ previewMode }),

      activeRun: null,
      setActiveRun: (activeRun) => set({ activeRun }),

      calendarTab: "month",
      setCalendarTab: (calendarTab) => set({ calendarTab }),
    }),
    {
      name: "news-studio-options",
      version: PERSIST_VERSION,
      storage: createJSONStorage(() => window.localStorage),
      // Only persist runOptions; theme has its own writer, previewMode is
      // ephemeral (the Review screen has its own persisted store).
      partialize: (state): PersistedAppState => ({
        runOptions: state.runOptions,
        activeRun: state.activeRun,
        calendarTab: state.calendarTab,
      }),
    },
  ),
);
