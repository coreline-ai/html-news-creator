import { create } from "zustand";

/**
 * Phase 4 — ReviewReport local state.
 *
 * Intentionally separate from `lib/store.ts` (Phase 3 is editing that file)
 * to avoid merge conflicts. Holds only Review-screen UI state:
 *
 *   - previewMode:     toggle between iframe live preview vs section editor
 *   - selectedSectionId: which section row is being edited
 *   - disabledSectionIds: client-only "off" toggle (DB has no `enabled` col).
 *                         Publish should exclude these.
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

export const useReviewStore = create<ReviewStoreState>((set, get) => ({
  previewMode: "live",
  selectedSectionId: null,
  disabledSectionIds: {},

  setPreviewMode: (mode) => set({ previewMode: mode }),
  togglePreviewMode: () =>
    set((s) => ({ previewMode: s.previewMode === "live" ? "section" : "live" })),

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
}));
