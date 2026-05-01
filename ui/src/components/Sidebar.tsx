import { NavLink } from "react-router-dom";
import { XIcon } from "lucide-react";
import { SIDEBAR_NAV_ICONS } from "@/lib/icons";
import { cn } from "@/lib/utils";
import {
  Sheet,
  SheetClose,
  SheetContent,
  SheetDescription,
  SheetHeader,
  SheetTitle,
} from "@/components/ui/sheet";

interface NavEntry {
  to: string;
  label: string;
  iconKey: keyof typeof SIDEBAR_NAV_ICONS;
  /** end=true so `/` is only active for the index route */
  end?: boolean;
}

const MAIN_NAV: NavEntry[] = [
  { to: "/", label: "Home", iconKey: "home", end: true },
  { to: "/reports", label: "Reports", iconKey: "reports" },
  { to: "/sources", label: "Sources", iconKey: "sources" },
];

const OPERATIONS_NAV: NavEntry[] = [
  { to: "/policy", label: "Policy", iconKey: "policy" },
];

const SettingsIcon = SIDEBAR_NAV_ICONS.settings;

interface SidebarBodyProps {
  /** Optional callback fired when a nav entry is clicked — used to close
   * the mobile sheet automatically. */
  onNavigate?: () => void;
}

function SidebarBody({ onNavigate }: SidebarBodyProps) {
  return (
    <div className="flex h-full flex-col">
      <div className="px-4 pt-4 pb-4">
        <div
          className="text-sidebar-foreground leading-tight font-semibold tracking-tight"
          style={{ fontSize: "1.46rem" }}
        >
          <span className="block">Coreline</span>
          <span className="block">News Studio</span>
        </div>
        <div className="text-muted-foreground text-[11px]">
          AI Trend Report
        </div>
      </div>

      <nav className="flex-1 overflow-y-auto px-2 pb-4">
        <SidebarSectionLabel>Main</SidebarSectionLabel>
        <ul className="flex flex-col gap-0.5">
          {MAIN_NAV.map((item) => (
            <li key={item.to}>
              <SidebarNavItem entry={item} onNavigate={onNavigate} />
            </li>
          ))}
        </ul>

        <SidebarSectionLabel>Operations</SidebarSectionLabel>
        <ul className="flex flex-col gap-0.5">
          {OPERATIONS_NAV.map((item) => (
            <li key={item.to}>
              <SidebarNavItem entry={item} onNavigate={onNavigate} />
            </li>
          ))}
        </ul>
      </nav>

      <div className="border-sidebar-border border-t p-2">
        <NavLink
          to="/settings"
          onClick={onNavigate}
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
          <SettingsIcon className="size-4 shrink-0" aria-hidden="true" />
          <span>Settings</span>
        </NavLink>
      </div>
    </div>
  );
}

/**
 * Desktop sidebar — hidden on viewports under 768px (mobile uses
 * `MobileSidebar`).
 */
export function Sidebar() {
  return (
    <aside
      data-testid="sidebar"
      className="bg-sidebar text-sidebar-foreground border-sidebar-border hidden h-screen flex-col border-r md:flex"
      style={{ width: 240 }}
      aria-label="Primary"
    >
      <SidebarBody />
    </aside>
  );
}

interface MobileSidebarProps {
  open: boolean;
  onOpenChange: (open: boolean) => void;
}

/**
 * Mobile sidebar shown via a `Sheet` drawer. Activated by the hamburger
 * button in `HeaderBar` on viewports < 768px.
 */
export function MobileSidebar({ open, onOpenChange }: MobileSidebarProps) {
  return (
    <Sheet open={open} onOpenChange={onOpenChange}>
      <SheetContent
        side="left"
        className="bg-sidebar text-sidebar-foreground w-64 p-0"
        data-testid="mobile-sidebar"
        showCloseButton={false}
      >
        <SheetClose
          aria-label="Close navigation"
          data-testid="mobile-sidebar-close"
          className={cn(
            "border-sidebar-border bg-sidebar text-sidebar-foreground absolute top-3 right-3 z-10",
            "inline-flex size-9 items-center justify-center rounded-full border shadow-sm",
            "opacity-100 transition-colors hover:bg-sidebar-accent hover:text-sidebar-accent-foreground",
            "focus-visible:ring-ring focus-visible:ring-2 focus-visible:ring-offset-2 focus-visible:outline-none",
          )}
        >
          <XIcon className="size-5 stroke-[2.5]" aria-hidden="true" />
          <span className="sr-only">Close navigation</span>
        </SheetClose>
        <SheetHeader className="sr-only">
          <SheetTitle>Navigation</SheetTitle>
          <SheetDescription>Primary navigation links</SheetDescription>
        </SheetHeader>
        <SidebarBody onNavigate={() => onOpenChange(false)} />
      </SheetContent>
    </Sheet>
  );
}

function SidebarSectionLabel({ children }: { children: React.ReactNode }) {
  return (
    <div className="text-muted-foreground px-2 pt-3 pb-1 text-[11px] font-medium tracking-wider uppercase">
      {children}
    </div>
  );
}

function SidebarNavItem({
  entry,
  onNavigate,
}: {
  entry: NavEntry;
  onNavigate?: () => void;
}) {
  const Icon = SIDEBAR_NAV_ICONS[entry.iconKey];
  return (
    <NavLink
      to={entry.to}
      end={entry.end}
      onClick={onNavigate}
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
