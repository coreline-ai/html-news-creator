import { create } from "zustand";

export type Theme = "dark" | "light";
export type PreviewMode = "live" | "section";
export type RunMode = "full" | "rss-only";
export type OutputTheme = "dark" | "light" | "newsroom-white";
export type SourceType = "rss" | "github" | "arxiv" | "website";
export type DeployTarget = "netlify" | "local-only";

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

function todayKstString(): string {
  // KST = UTC+9 — keep simple/local; user will adjust per-run.
  const now = new Date();
  const yyyy = now.getFullYear();
  const mm = String(now.getMonth() + 1).padStart(2, "0");
  const dd = String(now.getDate()).padStart(2, "0");
  return `${yyyy}-${mm}-${dd}`;
}

export const DEFAULT_RUN_OPTIONS: RunOptions = {
  date: todayKstString(),
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
}

const STORAGE_KEY = "theme";

function readInitialTheme(): Theme {
  if (typeof window === "undefined") return "dark";
  try {
    const stored = window.localStorage.getItem(STORAGE_KEY);
    if (stored === "light" || stored === "dark") return stored;
  } catch {
    // ignore
  }
  return document.documentElement.classList.contains("dark") ? "dark" : "dark";
}

function applyTheme(theme: Theme) {
  if (typeof document === "undefined") return;
  document.documentElement.classList.toggle("dark", theme === "dark");
  try {
    window.localStorage.setItem(STORAGE_KEY, theme);
  } catch {
    // ignore
  }
}

export const useAppStore = create<AppState>((set, get) => ({
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
}));
