import type { LucideIcon } from "lucide-react";
import { Inbox } from "lucide-react";
import { cn } from "@/lib/utils";

export interface EmptyStateProps {
  title: string;
  description?: string;
  icon?: LucideIcon;
  action?: React.ReactNode;
  className?: string;
}

export function EmptyState({
  title,
  description,
  icon: Icon = Inbox,
  action,
  className,
}: EmptyStateProps) {
  return (
    <div
      role="status"
      className={cn(
        "border-border bg-card text-card-foreground flex flex-col items-center gap-3 border px-6 py-16 text-center",
        className,
      )}
    >
      <Icon
        className="text-muted-foreground size-8"
        aria-hidden="true"
        strokeWidth={1.5}
      />
      <div className="text-foreground text-base font-medium">{title}</div>
      {description ? (
        <p className="text-muted-foreground max-w-sm text-sm">{description}</p>
      ) : null}
      {action ? <div className="pt-2">{action}</div> : null}
    </div>
  );
}
