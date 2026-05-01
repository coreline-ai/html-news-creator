import { describe, it, expect, beforeEach } from "vitest";
import {
  useAppStore,
  DEFAULT_RUN_OPTIONS,
  type RunOptions,
  type ActiveRun,
} from "@/lib/store";
import { useReviewStore } from "@/hooks/useReviewStore";

const APP_KEY = "news-studio-options";
const REVIEW_KEY = "news-studio-review";

beforeEach(() => {
  window.localStorage.clear();
  // Reset stores to defaults so each test sees a known state.
  useAppStore.setState({
    runOptions: { ...DEFAULT_RUN_OPTIONS },
    activeRun: null,
  });
  useReviewStore.setState({
    previewMode: "live",
    selectedSectionId: null,
    disabledSectionIds: {},
  });
});

describe("zustand persist — useAppStore (news-studio-options)", () => {
  it("writes runOptions to localStorage under the configured key", async () => {
    useAppStore.getState().setOption("target_sections", 7);
    useAppStore.getState().setOption("dry_run", true);

    // persist middleware writes synchronously after set() in the JSON storage path.
    const raw = window.localStorage.getItem(APP_KEY);
    expect(raw).toBeTruthy();

    const parsed = JSON.parse(raw!) as {
      version: number;
      state: { runOptions: RunOptions; activeRun: ActiveRun | null };
    };
    expect(parsed.version).toBe(1);
    expect(parsed.state.runOptions.target_sections).toBe(7);
    expect(parsed.state.runOptions.dry_run).toBe(true);
    expect(parsed.state.activeRun).toBeNull();
    // theme must NOT be in the persisted slice — ThemeToggle owns the
    // legacy "theme" key.
    expect(parsed.state).not.toHaveProperty("theme");
    // previewMode must NOT be persisted from this store either.
    expect(parsed.state).not.toHaveProperty("previewMode");
  });

  it("persists activeRun for refresh-safe pipeline tracking", async () => {
    const activeRun: ActiveRun = {
      run_id: "run-abc",
      started_at: "2026-05-01T00:00:00.000Z",
      options: { ...DEFAULT_RUN_OPTIONS, date: "2026-05-01" },
    };

    useAppStore.getState().setActiveRun(activeRun);

    const raw = window.localStorage.getItem(APP_KEY);
    expect(raw).toBeTruthy();
    const parsed = JSON.parse(raw!) as {
      version: number;
      state: { runOptions: RunOptions; activeRun: ActiveRun | null };
    };
    expect(parsed.version).toBe(1);
    expect(parsed.state.activeRun).toEqual(activeRun);

    useAppStore.setState({ activeRun: null });
    window.localStorage.setItem(APP_KEY, raw!);
    await useAppStore.persist.rehydrate();
    expect(useAppStore.getState().activeRun).toEqual(activeRun);
  });

  it("rehydrates runOptions from localStorage on store re-creation", async () => {
    // Simulate a previous session having stored values.
    window.localStorage.setItem(
      APP_KEY,
      JSON.stringify({
        version: 1,
        state: {
          runOptions: {
            ...DEFAULT_RUN_OPTIONS,
            target_sections: 12,
            dry_run: true,
            min_section_score: 50,
          },
        },
      }),
    );

    // Force the store to re-read from storage.
    await useAppStore.persist.rehydrate();
    const opts = useAppStore.getState().runOptions;
    expect(opts.target_sections).toBe(12);
    expect(opts.dry_run).toBe(true);
    expect(opts.min_section_score).toBe(50);
  });

  it("resetOptions reverts to defaults and updates the persisted blob", () => {
    useAppStore.getState().setOption("target_sections", 3);
    expect(useAppStore.getState().runOptions.target_sections).toBe(3);

    useAppStore.getState().resetOptions();
    expect(useAppStore.getState().runOptions.target_sections).toBe(
      DEFAULT_RUN_OPTIONS.target_sections,
    );
    const raw = window.localStorage.getItem(APP_KEY)!;
    const parsed = JSON.parse(raw) as { state: { runOptions: RunOptions } };
    expect(parsed.state.runOptions.target_sections).toBe(
      DEFAULT_RUN_OPTIONS.target_sections,
    );
  });
});

describe("zustand persist — useReviewStore (news-studio-review)", () => {
  it("writes previewMode and disabledSectionIds; omits selectedSectionId", () => {
    useReviewStore.getState().setPreviewMode("section");
    useReviewStore.getState().toggleSectionEnabled("section-42");
    useReviewStore.getState().selectSection("section-99");

    const raw = window.localStorage.getItem(REVIEW_KEY);
    expect(raw).toBeTruthy();

    const parsed = JSON.parse(raw!) as {
      version: number;
      state: {
        previewMode: string;
        disabledSectionIds: Record<string, boolean>;
        selectedSectionId?: string | null;
      };
    };

    expect(parsed.version).toBe(1);
    // selectSection toggles previewMode to "section" too — that's fine here.
    expect(parsed.state.previewMode).toBe("section");
    expect(parsed.state.disabledSectionIds["section-42"]).toBe(true);
    expect(parsed.state).not.toHaveProperty("selectedSectionId");
  });

  it("rehydrates previewMode and disabledSectionIds from a previous session", async () => {
    window.localStorage.setItem(
      REVIEW_KEY,
      JSON.stringify({
        version: 1,
        state: {
          previewMode: "section",
          disabledSectionIds: { "section-7": true },
        },
      }),
    );

    await useReviewStore.persist.rehydrate();

    const s = useReviewStore.getState();
    expect(s.previewMode).toBe("section");
    expect(s.disabledSectionIds["section-7"]).toBe(true);
    // selectedSectionId is intentionally NOT persisted/rehydrated.
    expect(s.selectedSectionId).toBeNull();
  });
});
