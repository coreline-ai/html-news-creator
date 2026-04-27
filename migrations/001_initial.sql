-- AI Trend Report Engine initial schema
-- Target: PostgreSQL / Supabase

create extension if not exists pgcrypto;
create extension if not exists vector;

create type source_type as enum ('rss', 'website', 'github', 'arxiv', 'x', 'manual');
create type trust_level as enum ('official', 'trusted_media', 'community', 'unknown');
create type job_status as enum ('queued', 'running', 'completed', 'failed', 'cancelled');
create type verification_status as enum (
  'official_confirmed',
  'github_confirmed',
  'paper_confirmed',
  'trusted_media_only',
  'social_only',
  'image_only',
  'unverified'
);
create type report_status as enum ('draft', 'review', 'published', 'failed', 'archived');

create table if not exists sources (
  id uuid primary key default gen_random_uuid(),
  name text not null,
  source_type source_type not null,
  url text not null,
  homepage_url text,
  trust_level trust_level not null default 'unknown',
  enabled boolean not null default true,
  metadata_json jsonb not null default '{}',
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);

create unique index if not exists sources_url_idx on sources(url);

create table if not exists raw_items (
  id uuid primary key default gen_random_uuid(),
  source_id uuid references sources(id) on delete set null,
  source_type source_type not null,
  title text,
  raw_text text,
  url text,
  canonical_url text,
  canonical_url_hash text,
  author text,
  language text,
  published_at timestamptz,
  collected_at timestamptz not null default now(),
  metrics_json jsonb not null default '{}',
  raw_json jsonb not null default '{}'
);

create unique index if not exists raw_items_canonical_hash_idx on raw_items(canonical_url_hash);
create index if not exists raw_items_published_at_idx on raw_items(published_at);
create index if not exists raw_items_source_type_idx on raw_items(source_type);

create table if not exists media_assets (
  id uuid primary key default gen_random_uuid(),
  raw_item_id uuid references raw_items(id) on delete cascade,
  original_url text,
  storage_path text,
  media_type text not null default 'image',
  mime_type text,
  width int,
  height int,
  sha256 text,
  metadata_json jsonb not null default '{}',
  created_at timestamptz not null default now()
);

create unique index if not exists media_assets_sha256_idx on media_assets(sha256);

create table if not exists extracted_contents (
  id uuid primary key default gen_random_uuid(),
  raw_item_id uuid references raw_items(id) on delete cascade,
  extractor text not null,
  extraction_status text not null default 'success',
  title text,
  description text,
  content_markdown text,
  content_text text,
  quality_score numeric(5,2),
  metadata_json jsonb not null default '{}',
  created_at timestamptz not null default now()
);

create index if not exists extracted_contents_raw_item_idx on extracted_contents(raw_item_id);

create table if not exists analysis_results (
  id uuid primary key default gen_random_uuid(),
  raw_item_id uuid references raw_items(id) on delete cascade,
  extracted_content_id uuid references extracted_contents(id) on delete set null,
  is_ai_related boolean not null default false,
  ai_relevance_score numeric(5,4),
  keywords_json jsonb not null default '[]',
  entities_json jsonb not null default '[]',
  claim_types_json jsonb not null default '[]',
  summary_ko text,
  model text,
  prompt_version text,
  confidence numeric(5,4),
  embedding vector(1536),
  created_at timestamptz not null default now()
);

create index if not exists analysis_results_relevance_idx on analysis_results(ai_relevance_score desc);
create index if not exists analysis_results_raw_item_idx on analysis_results(raw_item_id);

create table if not exists clusters (
  id uuid primary key default gen_random_uuid(),
  report_date date not null,
  title text,
  normalized_topic text,
  keywords_json jsonb not null default '[]',
  representative_item_id uuid references raw_items(id) on delete set null,
  importance_score numeric(5,2),
  trend_direction text,
  created_at timestamptz not null default now()
);

create index if not exists clusters_report_date_idx on clusters(report_date);
create index if not exists clusters_importance_idx on clusters(importance_score desc);

create table if not exists cluster_items (
  cluster_id uuid references clusters(id) on delete cascade,
  raw_item_id uuid references raw_items(id) on delete cascade,
  similarity_score numeric(5,4),
  primary key (cluster_id, raw_item_id)
);

create table if not exists verifications (
  id uuid primary key default gen_random_uuid(),
  cluster_id uuid references clusters(id) on delete cascade,
  raw_item_id uuid references raw_items(id) on delete set null,
  entity_name text,
  verification_status verification_status not null default 'unverified',
  source_url text,
  source_title text,
  source_type_label text,
  trust_score numeric(5,2),
  evidence_summary text,
  evidence_json jsonb not null default '[]',
  verified_at timestamptz not null default now(),
  model text,
  prompt_version text
);

create index if not exists verifications_cluster_idx on verifications(cluster_id);
create index if not exists verifications_status_idx on verifications(verification_status);

create table if not exists image_analyses (
  id uuid primary key default gen_random_uuid(),
  media_asset_id uuid references media_assets(id) on delete cascade,
  image_type text,
  ocr_text text,
  caption_ko text,
  verification_level text,
  confidence numeric(5,4),
  model text,
  prompt_version text,
  metadata_json jsonb not null default '{}',
  created_at timestamptz not null default now()
);

create table if not exists reports (
  id uuid primary key default gen_random_uuid(),
  report_date date not null unique,
  title text not null,
  status report_status not null default 'draft',
  summary_ko text,
  stats_json jsonb not null default '{}',
  method_json jsonb not null default '{}',
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now(),
  published_at timestamptz
);

create table if not exists report_sections (
  id uuid primary key default gen_random_uuid(),
  report_id uuid references reports(id) on delete cascade,
  cluster_id uuid references clusters(id) on delete set null,
  section_order int not null default 0,
  title text not null,
  lead text,
  fact_summary text,
  social_signal_summary text,
  inference_summary text,
  caution text,
  image_evidence_json jsonb not null default '[]',
  sources_json jsonb not null default '[]',
  confidence text,
  importance_score numeric(5,2),
  tags_json jsonb not null default '[]',
  created_at timestamptz not null default now()
);

create index if not exists report_sections_report_idx on report_sections(report_id, section_order);

create table if not exists report_artifacts (
  id uuid primary key default gen_random_uuid(),
  report_id uuid references reports(id) on delete cascade,
  artifact_type text not null, -- html, json, pdf, png
  storage_path text not null,
  public_url text,
  sha256 text,
  created_at timestamptz not null default now()
);

create table if not exists job_runs (
  id uuid primary key default gen_random_uuid(),
  job_name text not null,
  report_date date,
  status job_status not null default 'queued',
  started_at timestamptz,
  completed_at timestamptz,
  error_code text,
  error_message text,
  metadata_json jsonb not null default '{}',
  created_at timestamptz not null default now()
);

create index if not exists job_runs_status_idx on job_runs(status);
create index if not exists job_runs_report_date_idx on job_runs(report_date);

create table if not exists job_logs (
  id uuid primary key default gen_random_uuid(),
  job_run_id uuid references job_runs(id) on delete cascade,
  step_name text not null,
  level text not null default 'info',
  message text not null,
  context_json jsonb not null default '{}',
  created_at timestamptz not null default now()
);

create index if not exists job_logs_job_run_idx on job_logs(job_run_id, created_at);
