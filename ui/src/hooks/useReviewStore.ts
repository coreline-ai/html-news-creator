import { create } from "zustand";
import { persist, createJSONStorage } from "zustand/middleware";

/**
 * Phase 4 — ReviewReport local state.
 *
 * Intentionally separate from `lib/store.ts` (Phase 3 is editing that file)
 * to avoid merge conflicts. Holds only Review-screen UI state:
 *
 *   - previewMode:     toggle between iframe live preview vs section editor
 *   - selectedSectionId: which section row is being edited (NOT persisted —
 *                        the row may not exist on a future load)
 *   - disabledSectionIds: client-only "off" toggle (DB has no `enabled` col).
 *                         Publish should exclude these.
 *
 * `previewMode` and `disabledSectionIds` survive refresh under the
 * `news-studio-review` localStorage key.
 */

export type ReviewPreviewMode = "live" | "section";

interface ReviewStoreState {
  previewMode: ReviewPreviewMode;
  selectedSectionId: string | null;
  disabledSectionIds: Record<string, boolean>;

  setPreviewMode: (mode: ReviewPreviewMode) => void;
  togglePreviewMode: () => void;
  selectSection: (id: string | null) => void;
  toggleSectionEnabled: (id: string) => void;
  setSectionEnabled: (id: string, enabled: boolean) => void;
  isSectionEnabled: (id: string) => boolean;
  reset: () => void;
}

const REVIEW_PERSIST_VERSION = 1;

interface PersistedReviewState {
  previewMode: ReviewPreviewMode;
  disabledSectionIds: Record<string, boolean>;
}

export const useReviewStore = create<ReviewStoreState>()(
  persist(
    (set, get) => ({
      previewMode: "live",
      selectedSectionId: null,
      disabledSectionIds: {},

      setPreviewMode: (mode) => set({ previewMode: mode }),
      togglePreviewMode: () =>
        set((s) => ({
          previewMode: s.previewMode === "live" ? "section" : "live",
        })),

      selectSection: (id) =>
        set({
          selectedSectionId: id,
          // Selecting a section implicitly switches to the editor pane.
          previewMode: id ? "section" : get().previewMode,
        }),

      toggleSectionEnabled: (id) =>
        set((s) => {
          const next = { ...s.disabledSectionIds };
          if (next[id]) {
            delete next[id];
          } else {
            next[id] = true;
          }
          return { disabledSectionIds: next };
        }),

      setSectionEnabled: (id, enabled) =>
        set((s) => {
          const next = { ...s.disabledSectionIds };
          if (enabled) {
            delete next[id];
          } else {
            next[id] = true;
          }
          return { disabledSectionIds: next };
        }),

      isSectionEnabled: (id) => !get().disabledSectionIds[id],

      reset: () =>
        set({
          previewMode: "live",
          selectedSectionId: null,
          disabledSectionIds: {},
        }),
    }),
    {
      name: "news-studio-review",
      version: REVIEW_PERSIST_VERSION,
      storage: createJSONStorage(() => window.localStorage),
      // selectedSectionId is intentionally omitted — its identity is
      // tied to a single fetched report and should not leak across reloads.
      partialize: (state): PersistedReviewState => ({
        previewMode: state.previewMode,
        disabledSectionIds: state.disabledSectionIds,
      }),
    },
  ),
);
