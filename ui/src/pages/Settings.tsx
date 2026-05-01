import { type ReactNode } from "react";
import { Link } from "react-router-dom";
import {
  FileSliders,
  Newspaper,
  Palette,
  RotateCcw,
  ShieldCheck,
  UploadCloud,
} from "lucide-react";
import { Button } from "@/components/ui/button";
import {
  Card,
  CardContent,
  CardDescription,
  CardFooter,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";
import { Input } from "@/components/ui/input";
import { cn } from "@/lib/utils";
import {
  useAppStore,
  type DeployTarget,
  type OutputTheme,
  type RunOptions,
  type Theme,
} from "@/lib/store";

const APP_THEMES: Theme[] = ["dark", "light"];
const OUTPUT_THEMES: OutputTheme[] = ["dark", "light", "newsroom-white"];
const DEPLOY_TARGETS: DeployTarget[] = ["netlify", "local-only"];

export function Settings() {
  const theme = useAppStore((s) => s.theme);
  const setTheme = useAppStore((s) => s.setTheme);
  const runOptions = useAppStore((s) => s.runOptions);
  const setOption = useAppStore((s) => s.setOption);
  const resetOptions = useAppStore((s) => s.resetOptions);

  return (
    <div className="mx-auto flex max-w-[1200px] flex-col gap-6 px-6 py-6">
      <header>
        <h1 className="text-foreground text-xl font-semibold tracking-tight">
          Settings
        </h1>
        <p className="text-muted-foreground text-sm">
          Application preferences, report defaults, publishing guidance, and
          operational boundaries. Editorial ranking rules now live under Policy.
        </p>
      </header>

      <div className="grid grid-cols-1 gap-4 lg:grid-cols-2">
        <Card>
          <CardHeader>
            <CardTitle className="flex items-center gap-2 text-base">
              <FileSliders className="text-muted-foreground size-4" aria-hidden="true" />
              Editorial Policy
            </CardTitle>
            <CardDescription>
              Ranking, scoring, source tiers, and section quota controls are
              managed separately from app settings.
            </CardDescription>
          </CardHeader>
          <CardContent>
            <div className="border-border bg-muted/40 text-muted-foreground border px-3 py-2 text-xs">
              Save policy applies a runtime override. Persist to yaml writes the
              override into <code>data/editorial_policy.yaml</code>.
            </div>
          </CardContent>
          <CardFooter>
            <Button asChild size="sm">
              <Link to="/policy">Open Policy</Link>
            </Button>
          </CardFooter>
        </Card>

        <Card>
          <CardHeader>
            <CardTitle className="flex items-center gap-2 text-base">
              <Palette className="text-muted-foreground size-4" aria-hidden="true" />
              Appearance
            </CardTitle>
            <CardDescription>
              Change the app chrome and default report output theme for this
              browser.
            </CardDescription>
          </CardHeader>
          <CardContent className="grid gap-4">
            <SettingField label="App theme" hint="Applied immediately and persisted in this browser.">
              <ButtonGroup
                options={APP_THEMES}
                value={theme}
                onChange={setTheme}
                testIdPrefix="settings-theme"
              />
            </SettingField>
            <SettingField label="Report output theme" hint="Default selected on the New Report screen.">
              <ButtonGroup
                options={OUTPUT_THEMES}
                value={runOptions.output_theme}
                onChange={(value) => setOption("output_theme", value)}
                testIdPrefix="settings-output-theme"
              />
            </SettingField>
          </CardContent>
        </Card>

        <Card>
          <CardHeader>
            <CardTitle className="flex items-center gap-2 text-base">
              <Newspaper className="text-muted-foreground size-4" aria-hidden="true" />
              Report Defaults
            </CardTitle>
            <CardDescription>
              Browser-side defaults used by New Report before each run is
              submitted. Per-run choices can still override them.
            </CardDescription>
          </CardHeader>
          <CardContent className="grid gap-4">
            <SettingField label="Language">
              <select
                data-testid="settings-language"
                className="bg-background border-input text-foreground h-9 w-full rounded-md border px-3 text-sm"
                value={runOptions.language}
                onChange={(e) => setOption("language", e.target.value)}
              >
                <option value="ko">Korean (ko)</option>
                <option value="en">English (en)</option>
              </select>
            </SettingField>
            <SettingField label="Format" hint="Markdown is preview-only until the run pipeline supports it end-to-end.">
              <select
                data-testid="settings-format"
                className="bg-background border-input text-foreground h-9 w-full rounded-md border px-3 text-sm"
                value={runOptions.format}
                onChange={(e) =>
                  setOption("format", e.target.value as RunOptions["format"])
                }
              >
                <option value="html">html</option>
                <option value="markdown">markdown</option>
              </select>
            </SettingField>
            <SettingField label="Target sections" hint="Allowed range follows the New Report control.">
              <Input
                data-testid="settings-target-sections"
                type="number"
                min={1}
                max={12}
                value={runOptions.target_sections}
                onChange={(e) =>
                  setOption("target_sections", Number(e.target.value))
                }
              />
            </SettingField>
          </CardContent>
          <CardFooter className="justify-between gap-3">
            <Button asChild variant="outline" size="sm">
              <Link to="/reports/new">Open New Report</Link>
            </Button>
            <Button
              type="button"
              variant="ghost"
              size="sm"
              data-testid="settings-reset-run-defaults"
              onClick={resetOptions}
            >
              <RotateCcw className="size-4" />
              Reset defaults
            </Button>
          </CardFooter>
        </Card>

        <Card>
          <CardHeader>
            <CardTitle className="flex items-center gap-2 text-base">
              <UploadCloud className="text-muted-foreground size-4" aria-hidden="true" />
              Publishing
            </CardTitle>
            <CardDescription>
              Set browser-side publishing defaults. Secret values remain in the
              backend environment and are never displayed here.
            </CardDescription>
          </CardHeader>
          <CardContent className="grid gap-4">
            <SettingField label="Deploy target">
              <ButtonGroup
                options={DEPLOY_TARGETS}
                value={runOptions.deploy_target}
                onChange={(value) => setOption("deploy_target", value)}
                testIdPrefix="settings-deploy"
              />
            </SettingField>
            <SettingField label="Slack notify">
              <ButtonGroup
                options={["enabled", "disabled"] as const}
                value={runOptions.slack_notify ? "enabled" : "disabled"}
                onChange={(value) => setOption("slack_notify", value === "enabled")}
                testIdPrefix="settings-slack"
              />
            </SettingField>
          </CardContent>
        </Card>
      </div>

      <Card>
        <CardHeader>
          <CardTitle className="flex items-center gap-2 text-base">
            <ShieldCheck className="text-muted-foreground size-4" aria-hidden="true" />
            Operational Boundary
          </CardTitle>
          <CardDescription>
            Settings is intentionally separated from editorial policy so app
            preferences cannot silently change ranking behavior.
          </CardDescription>
        </CardHeader>
        <CardContent>
          <ul className="text-muted-foreground grid gap-2 text-sm md:grid-cols-3">
            <li className="border-border border px-3 py-2">
              Policy changes belong in <strong className="text-foreground">Policy</strong>.
            </li>
            <li className="border-border border px-3 py-2">
              One-off run choices belong in <strong className="text-foreground">New Report</strong>.
            </li>
            <li className="border-border border px-3 py-2">
              Secrets stay in backend <strong className="text-foreground">environment</strong>.
            </li>
          </ul>
        </CardContent>
      </Card>
    </div>
  );
}

function SettingField({
  label,
  hint,
  children,
}: {
  label: string;
  hint?: string;
  children: ReactNode;
}) {
  return (
    <div className="grid gap-1.5">
      <div className="flex items-center justify-between gap-3">
        <span className="text-foreground text-xs font-medium">{label}</span>
        {hint ? <span className="text-muted-foreground text-[11px]">{hint}</span> : null}
      </div>
      {children}
    </div>
  );
}

function ButtonGroup<T extends string>({
  options,
  value,
  onChange,
  testIdPrefix,
}: {
  options: readonly T[];
  value: T;
  onChange: (value: T) => void;
  testIdPrefix: string;
}) {
  return (
    <div className="flex flex-wrap gap-2">
      {options.map((option) => {
        const active = value === option;
        return (
          <button
            key={option}
            type="button"
            data-testid={`${testIdPrefix}-${option}`}
            aria-pressed={active}
            onClick={() => onChange(option)}
            className={cn(
              "rounded-md border px-2.5 py-1.5 text-xs transition-colors",
              active
                ? "bg-primary text-primary-foreground border-transparent"
                : "border-border bg-background text-muted-foreground hover:text-foreground",
            )}
          >
            {option}
          </button>
        );
      })}
    </div>
  );
}

export default Settings;
