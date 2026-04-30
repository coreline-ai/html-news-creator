import { useEffect } from "react";
import { useNavigate } from "react-router-dom";
import { Command } from "cmdk";
import {
  Dialog,
  DialogContent,
  DialogDescription,
  DialogTitle,
} from "@/components/ui/dialog";
import { SIDEBAR_NAV_ICONS } from "@/lib/icons";
import {
  FileText,
  Plus,
  RotateCw,
  Send,
  type LucideIcon,
} from "lucide-react";
import { cn } from "@/lib/utils";

export interface CommandPaletteProps {
  open: boolean;
  onOpenChange: (open: boolean) => void;
  /** Re-run last — wired by App. No-op when null. */
  onRerunLast?: () => void;
  /** Publish current — only meaningful from ReviewReport. No-op when null. */
  onPublishCurrent?: () => void;
}

interface CommandItem {
  id: string;
  label: string;
  hint?: string;
  icon: LucideIcon;
  perform: () => void;
}

/**
 * ⌘K command palette. Built on `cmdk` and shadcn `Dialog` so it inherits
 * focus management + dark/light tokens. Items: 4 nav routes + Re-run last +
 * Publish current.
 */
export function CommandPalette({
  open,
  onOpenChange,
  onRerunLast,
  onPublishCurrent,
}: CommandPaletteProps) {
  const navigate = useNavigate();

  // Close on route change initiated from a command.
  const close = () => onOpenChange(false);

  const items: CommandItem[] = [
    {
      id: "go-home",
      label: "Go to Dashboard",
      hint: "/",
      icon: SIDEBAR_NAV_ICONS.home,
      perform: () => {
        navigate("/");
        close();
      },
    },
    {
      id: "go-new-report",
      label: "New report",
      hint: "/reports/new",
      icon: Plus,
      perform: () => {
        navigate("/reports/new");
        close();
      },
    },
    {
      id: "go-sources",
      label: "Sources",
      hint: "/sources",
      icon: SIDEBAR_NAV_ICONS.sources,
      perform: () => {
        navigate("/sources");
        close();
      },
    },
    {
      id: "go-settings",
      label: "Settings",
      hint: "/settings",
      icon: SIDEBAR_NAV_ICONS.policy,
      perform: () => {
        navigate("/settings");
        close();
      },
    },
    {
      id: "rerun-last",
      label: "Re-run last",
      hint: "R",
      icon: RotateCw,
      perform: () => {
        onRerunLast?.();
        close();
      },
    },
    {
      id: "publish-current",
      label: "Publish current",
      hint: "P",
      icon: Send,
      perform: () => {
        onPublishCurrent?.();
        close();
      },
    },
  ];

  // Reset cmdk's internal value each time the dialog opens.
  useEffect(() => {
    if (!open) return;
  }, [open]);

  return (
    <Dialog open={open} onOpenChange={onOpenChange}>
      <DialogContent
        className="overflow-hidden p-0 sm:max-w-[520px]"
        data-testid="command-palette"
      >
        <DialogTitle className="sr-only">Command palette</DialogTitle>
        <DialogDescription className="sr-only">
          Search and run commands across News Studio.
        </DialogDescription>
        <Command
          label="Command palette"
          className="[&_[cmdk-input-wrapper]]:border-border bg-background flex flex-col"
        >
          <div className="border-border flex items-center border-b px-3">
            <FileText
              className="text-muted-foreground mr-2 size-4 shrink-0"
              aria-hidden="true"
            />
            <Command.Input
              data-testid="command-palette-input"
              placeholder="Type a command or search…"
              className="text-foreground placeholder:text-muted-foreground flex h-10 w-full bg-transparent py-3 text-sm outline-none"
            />
          </div>
          <Command.List
            className="max-h-[320px] overflow-y-auto p-1"
            data-testid="command-palette-list"
          >
            <Command.Empty className="text-muted-foreground py-6 text-center text-sm">
              No results found.
            </Command.Empty>

            <Command.Group
              heading="Navigate"
              className="text-muted-foreground [&_[cmdk-group-heading]]:text-muted-foreground [&_[cmdk-group-heading]]:px-2 [&_[cmdk-group-heading]]:pt-2 [&_[cmdk-group-heading]]:pb-1 [&_[cmdk-group-heading]]:text-[11px] [&_[cmdk-group-heading]]:font-medium [&_[cmdk-group-heading]]:tracking-wider [&_[cmdk-group-heading]]:uppercase"
            >
              {items.slice(0, 4).map((item) => (
                <CommandRow key={item.id} item={item} />
              ))}
            </Command.Group>

            <Command.Group
              heading="Actions"
              className="text-muted-foreground [&_[cmdk-group-heading]]:text-muted-foreground [&_[cmdk-group-heading]]:px-2 [&_[cmdk-group-heading]]:pt-2 [&_[cmdk-group-heading]]:pb-1 [&_[cmdk-group-heading]]:text-[11px] [&_[cmdk-group-heading]]:font-medium [&_[cmdk-group-heading]]:tracking-wider [&_[cmdk-group-heading]]:uppercase"
            >
              {items.slice(4).map((item) => (
                <CommandRow key={item.id} item={item} />
              ))}
            </Command.Group>
          </Command.List>
        </Command>
      </DialogContent>
    </Dialog>
  );
}

function CommandRow({ item }: { item: CommandItem }) {
  const Icon = item.icon;
  return (
    <Command.Item
      value={item.label}
      onSelect={item.perform}
      data-testid={`command-item-${item.id}`}
      className={cn(
        "text-foreground aria-selected:bg-accent aria-selected:text-accent-foreground flex cursor-pointer items-center gap-2 rounded-md px-2 py-2 text-sm",
      )}
    >
      <Icon className="text-muted-foreground size-4" aria-hidden="true" />
      <span className="flex-1">{item.label}</span>
      {item.hint ? (
        <kbd className="bg-muted text-muted-foreground border-border rounded border px-1.5 py-0.5 font-mono text-[10px]">
          {item.hint}
        </kbd>
      ) : null}
    </Command.Item>
  );
}

export default CommandPalette;
