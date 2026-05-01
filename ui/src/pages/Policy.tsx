import { PolicyForm } from "@/components/PolicyForm";

export function Policy() {
  return (
    <div className="mx-auto flex max-w-[1200px] flex-col gap-6 px-6 py-6">
      <header>
        <h1 className="text-foreground text-xl font-semibold tracking-tight">
          Editorial Policy
        </h1>
        <p className="text-muted-foreground text-sm">
          Ranking, scoring, section quotas, and report selection rules. Save
          applies a runtime override; Persist writes it to the on-disk yaml.
        </p>
      </header>
      <PolicyForm />
    </div>
  );
}

export default Policy;
