import { Link, useLocation, useParams } from "react-router-dom";
import { Search, User } from "lucide-react";
import { Button } from "@/components/ui/button";
import { ThemeToggle } from "@/components/ThemeToggle";
import { cn } from "@/lib/utils";

interface Crumb {
  label: string;
  to?: string;
}

function buildCrumbs(pathname: string, params: Record<string, string | undefined>): Crumb[] {
  const segs = pathname.split("/").filter(Boolean);
  if (segs.length === 0) return [{ label: "Home" }];

  const crumbs: Crumb[] = [{ label: "Home", to: "/" }];
  let acc = "";
  for (let i = 0; i < segs.length; i++) {
    const seg = segs[i];
    acc += `/${seg}`;
    let label = seg;
    if (seg === "reports") label = "Reports";
    else if (seg === "sources") label = "Sources";
    else if (seg === "settings") label = "Settings";
    else if (params.date && seg === params.date) label = params.date;
    const isLast = i === segs.length - 1;
    crumbs.push({ label, to: isLast ? undefined : acc });
  }
  return crumbs;
}

export function HeaderBar() {
  const location = useLocation();
  const params = useParams();
  const crumbs = buildCrumbs(location.pathname, params);

  return (
    <header
      className="bg-background border-border sticky top-0 z-10 flex shrink-0 items-center justify-between border-b px-4"
      style={{ height: 48 }}
    >
      <nav aria-label="Breadcrumb" className="flex items-center gap-1.5 text-[13px]">
        {crumbs.map((c, i) => {
          const isLast = i === crumbs.length - 1;
          return (
            <span key={`${c.label}-${i}`} className="flex items-center gap-1.5">
              {i > 0 && (
                <span aria-hidden="true" className="text-muted-foreground select-none">
                  /
                </span>
              )}
              {c.to && !isLast ? (
                <Link
                  to={c.to}
                  className="text-muted-foreground hover:text-foreground transition-colors"
                >
                  {c.label}
                </Link>
              ) : (
                <span
                  className={cn(
                    "text-foreground font-medium",
                    !isLast && "text-muted-foreground font-normal",
                  )}
                  aria-current={isLast ? "page" : undefined}
                >
                  {c.label}
                </span>
              )}
            </span>
          );
        })}
      </nav>

      <div className="flex items-center gap-1">
        <Button
          variant="ghost"
          size="sm"
          className="text-muted-foreground hidden h-8 gap-2 px-2 sm:flex"
          aria-label="Open command palette"
          disabled
          title="Command palette (coming in Phase 6)"
        >
          <Search className="size-3.5" aria-hidden="true" />
          <span className="text-xs">Search</span>
          <kbd className="bg-muted text-muted-foreground border-border ml-1 hidden rounded border px-1.5 py-0.5 text-[10px] md:inline-block">
            ⌘K
          </kbd>
        </Button>
        <ThemeToggle />
        <Button
          variant="ghost"
          size="icon"
          aria-label="Account"
          title="Account"
          disabled
        >
          <User className="size-4" aria-hidden="true" />
        </Button>
      </div>
    </header>
  );
}
