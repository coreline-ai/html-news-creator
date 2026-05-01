import { ChevronLeft, ChevronRight } from "lucide-react";
import {
  DayPicker,
  type DayPickerProps,
} from "react-day-picker";

import { cn } from "@/lib/utils";
import { buttonVariants } from "@/components/ui/button";

/**
 * shadcn-flavored Calendar primitive built on top of `react-day-picker` v9.
 *
 * Tokens-only — no raw colors. Card radius is 0 by design system rule, but
 * inner buttons (nav, day cells, today highlight) keep `rounded-md`.
 */
function Calendar({
  className,
  classNames,
  showOutsideDays = true,
  ...props
}: DayPickerProps) {
  return (
    <DayPicker
      showOutsideDays={showOutsideDays}
      className={cn("p-3", className)}
      classNames={{
        months: "flex flex-col sm:flex-row gap-2",
        month: "flex flex-col gap-3",
        month_caption: "flex justify-center pt-1 relative items-center w-full",
        caption_label: "text-sm font-medium",
        nav: "flex items-center gap-1 absolute inset-x-0 top-0 justify-between",
        button_previous: cn(
          buttonVariants({ variant: "ghost" }),
          "size-7 bg-transparent p-0 opacity-60 hover:opacity-100",
        ),
        button_next: cn(
          buttonVariants({ variant: "ghost" }),
          "size-7 bg-transparent p-0 opacity-60 hover:opacity-100",
        ),
        month_grid: "w-full border-collapse space-y-1",
        weekdays: "flex",
        weekday:
          "text-muted-foreground w-8 font-medium text-[11px] uppercase tracking-wide",
        week: "flex w-full mt-1",
        day: cn(
          "relative size-8 p-0 text-center text-sm focus-within:relative focus-within:z-20",
        ),
        day_button: cn(
          buttonVariants({ variant: "ghost" }),
          "size-8 p-0 font-normal aria-selected:opacity-100 hover:bg-accent hover:text-accent-foreground rounded-md focus-visible:ring-1 focus-visible:ring-ring",
        ),
        range_start:
          "day-range-start aria-selected:bg-primary aria-selected:text-primary-foreground",
        range_end:
          "day-range-end aria-selected:bg-primary aria-selected:text-primary-foreground",
        selected:
          "bg-primary text-primary-foreground hover:bg-primary hover:text-primary-foreground focus:bg-primary focus:text-primary-foreground",
        today: "ring-1 ring-ring",
        outside:
          "day-outside text-muted-foreground aria-selected:text-muted-foreground",
        disabled: "text-muted-foreground opacity-50",
        range_middle:
          "aria-selected:bg-accent aria-selected:text-accent-foreground",
        hidden: "invisible",
        ...classNames,
      }}
      components={{
        Chevron: ({ orientation, className: cls, ...rest }) => {
          const Icon = orientation === "right" ? ChevronRight : ChevronLeft;
          return (
            <Icon className={cn("size-4", cls)} aria-hidden="true" {...rest} />
          );
        },
      }}
      {...props}
    />
  );
}

export { Calendar };
