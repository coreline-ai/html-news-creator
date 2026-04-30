import { useMemo } from "react";
import {
  DndContext,
  KeyboardSensor,
  PointerSensor,
  closestCenter,
  useSensor,
  useSensors,
  type DragEndEvent,
} from "@dnd-kit/core";
import {
  SortableContext,
  arrayMove,
  sortableKeyboardCoordinates,
  useSortable,
  verticalListSortingStrategy,
} from "@dnd-kit/sortable";
import { CSS } from "@dnd-kit/utilities";
import { GripVertical } from "lucide-react";
import type { ReportSection } from "@/lib/api";
import { cn } from "@/lib/utils";

export interface SectionListProps {
  sections: ReportSection[];
  selectedSectionId: string | null;
  disabledSectionIds: Record<string, boolean>;
  onSelect: (id: string) => void;
  onToggle: (id: string) => void;
  onReorder: (orderedIds: string[]) => void;
  className?: string;
}

export function SectionList({
  sections,
  selectedSectionId,
  disabledSectionIds,
  onSelect,
  onToggle,
  onReorder,
  className,
}: SectionListProps) {
  const sensors = useSensors(
    useSensor(PointerSensor, {
      // Distance >= 8px before drag starts — keeps tap/click usable on touch.
      activationConstraint: { distance: 8 },
    }),
    useSensor(KeyboardSensor, {
      coordinateGetter: sortableKeyboardCoordinates,
    }),
  );

  const ids = useMemo(() => sections.map((s) => s.id), [sections]);

  const handleDragEnd = (event: DragEndEvent) => {
    const { active, over } = event;
    if (!over || active.id === over.id) return;
    const oldIndex = ids.indexOf(String(active.id));
    const newIndex = ids.indexOf(String(over.id));
    if (oldIndex < 0 || newIndex < 0) return;
    const next = arrayMove(ids, oldIndex, newIndex);
    onReorder(next);
  };

  if (sections.length === 0) {
    return (
      <div
        className={cn(
          "border-border bg-card text-muted-foreground border p-6 text-sm",
          className,
        )}
        data-testid="section-list-empty"
      >
        No sections to review.
      </div>
    );
  }

  return (
    <div
      className={cn("flex flex-col gap-2", className)}
      data-testid="section-list"
    >
      <DndContext
        sensors={sensors}
        collisionDetection={closestCenter}
        onDragEnd={handleDragEnd}
      >
        <SortableContext items={ids} strategy={verticalListSortingStrategy}>
          <ul className="flex flex-col gap-2" role="list">
            {sections.map((section) => (
              <SortableSectionRow
                key={section.id}
                section={section}
                selected={selectedSectionId === section.id}
                enabled={!disabledSectionIds[section.id]}
                onSelect={onSelect}
                onToggle={onToggle}
              />
            ))}
          </ul>
        </SortableContext>
      </DndContext>
    </div>
  );
}

interface SortableSectionRowProps {
  section: ReportSection;
  selected: boolean;
  enabled: boolean;
  onSelect: (id: string) => void;
  onToggle: (id: string) => void;
}

function SortableSectionRow({
  section,
  selected,
  enabled,
  onSelect,
  onToggle,
}: SortableSectionRowProps) {
  const {
    attributes,
    listeners,
    setNodeRef,
    transform,
    transition,
    isDragging,
  } = useSortable({ id: section.id });

  const style: React.CSSProperties = {
    transform: CSS.Transform.toString(transform),
    transition,
    opacity: isDragging ? 0.7 : 1,
  };

  return (
    <li
      ref={setNodeRef}
      style={style}
      data-testid={`section-row-${section.id}`}
      data-section-id={section.id}
      data-selected={selected}
      data-enabled={enabled}
      className={cn(
        "border-border bg-card text-card-foreground flex items-center gap-2 border px-2 py-2 transition-colors",
        selected && "border-primary bg-accent",
        !enabled &&
          "bg-[repeating-linear-gradient(135deg,var(--muted)_0_8px,transparent_8px_16px)] text-muted-foreground",
      )}
    >
      {/* Drag handle */}
      <button
        type="button"
        aria-label={`Drag handle for ${section.title ?? "section"}`}
        data-testid={`section-handle-${section.id}`}
        className="text-muted-foreground hover:text-foreground flex size-7 shrink-0 cursor-grab items-center justify-center active:cursor-grabbing"
        {...attributes}
        {...listeners}
      >
        <GripVertical className="size-4" aria-hidden="true" />
      </button>

      {/* Body — clicking selects */}
      <button
        type="button"
        onClick={() => onSelect(section.id)}
        className="flex min-w-0 flex-1 flex-col items-start gap-0.5 text-left"
      >
        <span className="text-foreground line-clamp-1 text-sm font-medium">
          {section.section_order + 1}. {section.title ?? "(untitled)"}
        </span>
        {section.fact_summary ? (
          <span className="text-muted-foreground line-clamp-1 text-xs">
            {section.fact_summary}
          </span>
        ) : null}
      </button>

      {/* On/off toggle */}
      <label
        className="text-muted-foreground flex shrink-0 items-center gap-2 text-xs"
        onClick={(e) => e.stopPropagation()}
      >
        <input
          type="checkbox"
          checked={enabled}
          onChange={() => onToggle(section.id)}
          aria-label={
            enabled
              ? `Disable section ${section.title ?? section.id}`
              : `Enable section ${section.title ?? section.id}`
          }
          data-testid={`section-toggle-${section.id}`}
          className="accent-primary size-4 cursor-pointer"
        />
        <span className="hidden md:inline">
          {enabled ? "On" : "Off"}
        </span>
      </label>
    </li>
  );
}

export default SectionList;
