import { create } from "zustand";

export type Theme = "dark" | "light";
export type PreviewMode = "live" | "section";

/**
 * Run options used by NewReport (Phase 3). Phase 2 only needs the type to
 * exist so the store interface is stable.
 */
export interface RunOptions {
  target_sections?: number;
  dry_run?: boolean;
  date_kst?: string;
  [key: string]: unknown;
}

interface AppState {
  theme: Theme;
  setTheme: (t: Theme) => void;
  toggleTheme: () => void;

  // Reserved for Phase 3 — declared so callers can wire up early.
  runOptions: RunOptions;
  setOption: <K extends keyof RunOptions>(key: K, value: RunOptions[K]) => void;
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

  runOptions: {},
  setOption: (key, value) =>
    set((s) => ({ runOptions: { ...s.runOptions, [key]: value } })),
  resetOptions: () => set({ runOptions: {} }),

  previewMode: "live",
  setPreviewMode: (previewMode) => set({ previewMode }),
}));
