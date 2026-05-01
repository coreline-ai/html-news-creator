/**
 * SIDEBAR_NAV_ICONS — single point of change for sidebar (and related)
 * navigation icons.
 *
 * Rule (per `dev-plan/implement-20260430-news-studio-webapp.md` §7.7):
 * Every navigation icon used in the workspace shell must be imported FROM
 * THIS FILE. Do NOT import lucide-react icons directly elsewhere for
 * navigation entries — swap them here and the change propagates.
 */
import {
  Home,
  FileText,
  Database,
  SlidersHorizontal,
  Calendar,
  Settings,
} from "lucide-react";

export const SIDEBAR_NAV_ICONS = {
  home: Home,
  reports: FileText,
  sources: Database,
  policy: SlidersHorizontal,
  schedule: Calendar,
  settings: Settings,
} as const;

export type SidebarNavIconKey = keyof typeof SIDEBAR_NAV_ICONS;
