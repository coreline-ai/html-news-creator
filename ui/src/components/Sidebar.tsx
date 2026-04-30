import { NavLink } from "react-router-dom";
import { Settings } from "lucide-react";
import { SIDEBAR_NAV_ICONS } from "@/lib/icons";
import { cn } from "@/lib/utils";

interface NavEntry {
  to: string;
  label: string;
  iconKey: keyof typeof SIDEBAR_NAV_ICONS;
  /** end=true so `/` is only active for the index route */
  end?: boolean;
}

const NAV: NavEntry[] = [
  { to: "/", label: "Home", iconKey: "home", end: true },
  { to: "/reports", label: "Reports", iconKey: "reports" },
  { to: "/sources", label: "Sources", iconKey: "sources" },
  { to: "/settings", label: "Policy", iconKey: "policy" },
];

export function Sidebar() {
  return (
    <aside
      data-testid="sidebar"
      className="bg-sidebar text-sidebar-foreground border-sidebar-border flex h-screen flex-col border-r"
      style={{ width: 240 }}
      aria-label="Primary"
    >
      <div className="px-4 pt-4 pb-3">
        <div className="text-sidebar-foreground text-sm font-semibold tracking-tight">
          News Studio
        </div>
        <div className="text-muted-foreground text-[11px]">
          AI Trend Report
        </div>
      </div>

      <nav className="flex-1 overflow-y-auto px-2 pb-4">
        <SidebarSectionLabel>Main</SidebarSectionLabel>
        <ul className="flex flex-col gap-0.5">
          {NAV.map((item) => (
            <li key={item.to}>
              <SidebarNavItem entry={item} />
            </li>
          ))}
        </ul>
      </nav>

      <div className="border-sidebar-border border-t p-2">
        <NavLink
          to="/settings"
          className={({ isActive }) =>
            cn(
              "flex h-8 items-center gap-2 rounded-md px-2 text-[13px] transition-colors",
              "hover:bg-sidebar-accent hover:text-sidebar-accent-foreground",
              isActive &&
                "bg-sidebar-primary text-sidebar-primary-foreground hover:bg-sidebar-primary",
            )
          }
          aria-label="Settings"
        >
          <Settings className="size-4 shrink-0" aria-hidden="true" />
          <span>Settings</span>
        </NavLink>
      </div>
    </aside>
  );
}

function SidebarSectionLabel({ children }: { children: React.ReactNode }) {
  return (
    <div className="text-muted-foreground px-2 pt-3 pb-1 text-[11px] font-medium tracking-wider uppercase">
      {children}
    </div>
  );
}

function SidebarNavItem({ entry }: { entry: NavEntry }) {
  const Icon = SIDEBAR_NAV_ICONS[entry.iconKey];
  return (
    <NavLink
      to={entry.to}
      end={entry.end}
      className={({ isActive }) =>
        cn(
          "flex h-8 items-center gap-2 rounded-md px-2 text-[13px] transition-colors",
          "hover:bg-sidebar-accent hover:text-sidebar-accent-foreground",
          isActive &&
            "bg-sidebar-primary text-sidebar-primary-foreground hover:bg-sidebar-primary hover:text-sidebar-primary-foreground",
        )
      }
    >
      <Icon className="size-4 shrink-0" aria-hidden="true" />
      <span>{entry.label}</span>
    </NavLink>
  );
}
