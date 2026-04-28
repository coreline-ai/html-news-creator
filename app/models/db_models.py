import uuid
from datetime import datetime
from sqlalchemy import (
    Boolean, Column, Date, DateTime, Float, ForeignKey,
    Integer, String, Text, UniqueConstraint, text,
)
from sqlalchemy.dialects.postgresql import JSONB, UUID, ENUM
from sqlalchemy.orm import relationship
from app.db import Base

# Enum columns use create_type=False — types are already created by migration SQL
_source_type      = ENUM("rss", "website", "github", "arxiv", "x", "manual",
                         name="source_type", create_type=False)
_trust_level      = ENUM("official", "trusted_media", "community", "unknown",
                         name="trust_level", create_type=False)
_verification_st  = ENUM("official_confirmed", "github_confirmed", "paper_confirmed",
                         "trusted_media_only", "social_only", "image_only", "unverified",
                         name="verification_status", create_type=False)
_report_status    = ENUM("draft", "review", "published", "failed", "archived",
                         name="report_status", create_type=False)
_job_status       = ENUM("queued", "running", "completed", "failed", "cancelled",
                         name="job_status", create_type=False)


class Source(Base):
    __tablename__ = "sources"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(Text, nullable=False)
    source_type = Column(_source_type, nullable=False)
    url = Column(Text, nullable=False, unique=True)
    homepage_url = Column(Text)
    trust_level = Column(_trust_level, nullable=False, default="unknown")
    enabled = Column(Boolean, nullable=False, default=True)
    metadata_json = Column(JSONB, nullable=False, default=dict)
    created_at = Column(DateTime(timezone=True), nullable=False, default=datetime.utcnow)
    updated_at = Column(DateTime(timezone=True), nullable=False, default=datetime.utcnow)


class RawItem(Base):
    __tablename__ = "raw_items"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    source_id = Column(UUID(as_uuid=True), ForeignKey("sources.id", ondelete="SET NULL"))
    source_type = Column(_source_type, nullable=False)
    title = Column(Text)
    raw_text = Column(Text)
    url = Column(Text)
    canonical_url = Column(Text)
    canonical_url_hash = Column(Text, unique=True)
    author = Column(Text)
    language = Column(Text)
    published_at = Column(DateTime(timezone=True))
    collected_at = Column(DateTime(timezone=True), nullable=False, default=datetime.utcnow)
    metrics_json = Column(JSONB, nullable=False, default=dict)
    raw_json = Column(JSONB, nullable=False, default=dict)


class MediaAsset(Base):
    __tablename__ = "media_assets"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    raw_item_id = Column(UUID(as_uuid=True), ForeignKey("raw_items.id", ondelete="CASCADE"))
    original_url = Column(Text)
    storage_path = Column(Text)
    media_type = Column(Text, nullable=False, default="image")
    mime_type = Column(Text)
    width = Column(Integer)
    height = Column(Integer)
    sha256 = Column(Text, unique=True)
    metadata_json = Column(JSONB, nullable=False, default=dict)
    created_at = Column(DateTime(timezone=True), nullable=False, default=datetime.utcnow)


class ExtractedContent(Base):
    __tablename__ = "extracted_contents"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    raw_item_id = Column(UUID(as_uuid=True), ForeignKey("raw_items.id", ondelete="CASCADE"))
    extractor = Column(Text, nullable=False)
    extraction_status = Column(Text, nullable=False, default="success")
    title = Column(Text)
    description = Column(Text)
    content_markdown = Column(Text)
    content_text = Column(Text)
    quality_score = Column(Float)
    metadata_json = Column(JSONB, nullable=False, default=dict)
    created_at = Column(DateTime(timezone=True), nullable=False, default=datetime.utcnow)


class AnalysisResult(Base):
    __tablename__ = "analysis_results"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    raw_item_id = Column(UUID(as_uuid=True), ForeignKey("raw_items.id", ondelete="CASCADE"))
    extracted_content_id = Column(UUID(as_uuid=True), ForeignKey("extracted_contents.id", ondelete="SET NULL"))
    is_ai_related = Column(Boolean, nullable=False, default=False)
    ai_relevance_score = Column(Float)
    keywords_json = Column(JSONB, nullable=False, default=list)
    entities_json = Column(JSONB, nullable=False, default=list)
    claim_types_json = Column(JSONB, nullable=False, default=list)
    summary_ko = Column(Text)
    model = Column(Text)
    prompt_version = Column(Text)
    confidence = Column(Float)
    # embedding은 pgvector 타입 — 별도 쿼리로 처리
    created_at = Column(DateTime(timezone=True), nullable=False, default=datetime.utcnow)


class Cluster(Base):
    __tablename__ = "clusters"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    report_date = Column(Date, nullable=False)
    title = Column(Text)
    normalized_topic = Column(Text)
    keywords_json = Column(JSONB, nullable=False, default=list)
    representative_item_id = Column(UUID(as_uuid=True), ForeignKey("raw_items.id", ondelete="SET NULL"))
    importance_score = Column(Float)
    trend_direction = Column(Text)
    created_at = Column(DateTime(timezone=True), nullable=False, default=datetime.utcnow)


class ClusterItem(Base):
    __tablename__ = "cluster_items"
    cluster_id = Column(UUID(as_uuid=True), ForeignKey("clusters.id", ondelete="CASCADE"), primary_key=True)
    raw_item_id = Column(UUID(as_uuid=True), ForeignKey("raw_items.id", ondelete="CASCADE"), primary_key=True)
    similarity_score = Column(Float)


class Verification(Base):
    __tablename__ = "verifications"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    cluster_id = Column(UUID(as_uuid=True), ForeignKey("clusters.id", ondelete="CASCADE"))
    raw_item_id = Column(UUID(as_uuid=True), ForeignKey("raw_items.id", ondelete="SET NULL"))
    entity_name = Column(Text)
    verification_status = Column(_verification_st, nullable=False, default="unverified")
    source_url = Column(Text)
    source_title = Column(Text)
    source_type_label = Column(Text)
    trust_score = Column(Float)
    evidence_summary = Column(Text)
    evidence_json = Column(JSONB, nullable=False, default=list)
    verified_at = Column(DateTime(timezone=True), nullable=False, default=datetime.utcnow)
    model = Column(Text)
    prompt_version = Column(Text)


class ImageAnalysis(Base):
    __tablename__ = "image_analyses"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    media_asset_id = Column(UUID(as_uuid=True), ForeignKey("media_assets.id", ondelete="CASCADE"))
    image_type = Column(Text)
    ocr_text = Column(Text)
    caption_ko = Column(Text)
    verification_level = Column(Text)
    confidence = Column(Float)
    model = Column(Text)
    prompt_version = Column(Text)
    metadata_json = Column(JSONB, nullable=False, default=dict)
    created_at = Column(DateTime(timezone=True), nullable=False, default=datetime.utcnow)


class Report(Base):
    __tablename__ = "reports"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    report_date = Column(Date, nullable=False, unique=True)
    title = Column(Text, nullable=False)
    status = Column(_report_status, nullable=False, default="draft")
    summary_ko = Column(Text)
    stats_json = Column(JSONB, nullable=False, default=dict)
    method_json = Column(JSONB, nullable=False, default=dict)
    created_at = Column(DateTime(timezone=True), nullable=False, default=datetime.utcnow)
    updated_at = Column(DateTime(timezone=True), nullable=False, default=datetime.utcnow)
    published_at = Column(DateTime(timezone=True))


class ReportSection(Base):
    __tablename__ = "report_sections"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    report_id = Column(UUID(as_uuid=True), ForeignKey("reports.id", ondelete="CASCADE"))
    cluster_id = Column(UUID(as_uuid=True), ForeignKey("clusters.id", ondelete="SET NULL"))
    section_order = Column(Integer, nullable=False, default=0)
    title = Column(Text, nullable=False)
    lead = Column(Text)
    fact_summary = Column(Text)
    social_signal_summary = Column(Text)
    inference_summary = Column(Text)
    caution = Column(Text)
    image_evidence_json = Column(JSONB, nullable=False, default=list)
    sources_json = Column(JSONB, nullable=False, default=list)
    confidence = Column(Text)
    importance_score = Column(Float)
    tags_json = Column(JSONB, nullable=False, default=list)
    created_at = Column(DateTime(timezone=True), nullable=False, default=datetime.utcnow)


class ReportArtifact(Base):
    __tablename__ = "report_artifacts"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    report_id = Column(UUID(as_uuid=True), ForeignKey("reports.id", ondelete="CASCADE"))
    artifact_type = Column(Text, nullable=False)  # html|json|pdf|png
    storage_path = Column(Text, nullable=False)
    public_url = Column(Text)
    sha256 = Column(Text)
    created_at = Column(DateTime(timezone=True), nullable=False, default=datetime.utcnow)


class JobRun(Base):
    __tablename__ = "job_runs"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    job_name = Column(Text, nullable=False)
    report_date = Column(Date)
    status = Column(_job_status, nullable=False, default="queued")
    started_at = Column(DateTime(timezone=True))
    completed_at = Column(DateTime(timezone=True))
    error_code = Column(Text)
    error_message = Column(Text)
    metadata_json = Column(JSONB, nullable=False, default=dict)
    created_at = Column(DateTime(timezone=True), nullable=False, default=datetime.utcnow)


class JobLog(Base):
    __tablename__ = "job_logs"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    job_run_id = Column(UUID(as_uuid=True), ForeignKey("job_runs.id", ondelete="CASCADE"))
    step_name = Column(Text, nullable=False)
    level = Column(Text, nullable=False, default="info")
    message = Column(Text, nullable=False)
    context_json = Column(JSONB, nullable=False, default=dict)
    created_at = Column(DateTime(timezone=True), nullable=False, default=datetime.utcnow)
