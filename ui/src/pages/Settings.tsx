import { PolicyForm } from "@/components/PolicyForm";

export function Settings() {
  return (
    <div className="mx-auto flex max-w-[1200px] flex-col gap-6 px-6 py-6">
      <header>
        <h1 className="text-foreground text-xl font-semibold tracking-tight">
          Policy &amp; Settings
        </h1>
        <p className="text-muted-foreground text-sm">
          Editorial policy for ranking, scoring, and report selection. Changes
          here apply at runtime only — the on-disk yaml is untouched.
        </p>
      </header>
      <PolicyForm />
    </div>
  );
}

export default Settings;
