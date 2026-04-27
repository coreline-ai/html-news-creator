# AI Trend Report Engine — Additional Development Docs



---

# File: .env.example

# Core
APP_ENV=local
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/ai_trend
REPORT_PUBLIC_BASE_URL=http://localhost:3000

# LLM
OPENAI_API_KEY=
OPENAI_MODEL=gpt-5.5
OPENAI_EMBEDDING_MODEL=text-embedding-3-small

# Web extraction
FIRECRAWL_API_KEY=
CRAWL4AI_ENABLED=true
TRAFILATURA_ENABLED=true

# Supabase optional
SUPABASE_URL=
SUPABASE_ANON_KEY=
SUPABASE_SERVICE_ROLE_KEY=

# GitHub
GITHUB_TOKEN=

# X/Twitter optional
X_BEARER_TOKEN=
X_ENABLED=false

# Object storage
S3_ENDPOINT=http://localhost:9000
S3_ACCESS_KEY=minioadmin
S3_SECRET_KEY=minioadmin
S3_BUCKET=ai-trend-assets
S3_REGION=us-east-1

# Deploy
NETLIFY_AUTH_TOKEN=
NETLIFY_SITE_ID=
VERCEL_TOKEN=

# Runtime
TIMEZONE=Asia/Seoul
LOG_LEVEL=info
MAX_SOURCES_PER_RUN=500
MAX_IMAGES_PER_RUN=50



---

# File: 00_README_IMPLEMENTATION.md

# AI Trend Report Engine — 개발 추가 문서 패키지

이 문서 패키지는 기존 PRD.md / TRD.md를 바로 개발 가능한 형태로 확장하기 위한 실행 문서 모음이다.

## 목표

`AI Trend Report Engine`은 웹/RSS/GitHub/arXiv/X/공식 블로그를 수집하고, 공식 출처 검증과 이미지/OCR 분석을 거쳐 한국어 AI 트렌드 리포트를 생성한 뒤, HTML/PDF/PNG로 발행하는 자동 리포트 엔진이다.

## 문서 구성

| 파일 | 목적 |
|---|---|
| `01_ARCHITECTURE.md` | 전체 아키텍처, 모듈 책임, 데이터 흐름 |
| `02_IMPLEMENTATION_ROADMAP.md` | 단계별 구현 로드맵, 스프린트 계획 |
| `03_BACKLOG.md` | Epic/User Story/Task/Acceptance Criteria |
| `04_API_SPEC.md` | 내부/관리자/API 엔드포인트 계약 |
| `05_DATA_SCHEMA.md` | DB 테이블 설계와 인덱스 전략 |
| `schema.sql` | Supabase/PostgreSQL 초기 DDL |
| `06_PIPELINE_RUNBOOK.md` | 수집·검증·렌더링 파이프라인 운영 절차 |
| `07_PROMPT_PACK.md` | 분류/요약/검증/HTML 생성용 프롬프트 |
| `08_TEST_PLAN.md` | 단위/통합/E2E/시각 회귀/팩트체크 테스트 |
| `09_SECURITY_AND_COMPLIANCE.md` | 보안, 크롤링 정책, 개인정보, RLS |
| `10_DEPLOYMENT_GUIDE.md` | 로컬 실행, Docker, GitHub Actions, Netlify 배포 |
| `11_OBSERVABILITY.md` | 로그, 메트릭, 알림, 품질 대시보드 |
| `.env.example` | 환경 변수 샘플 |
| `docker-compose.yml` | 로컬 개발용 PostgreSQL/Redis/MinIO 구성 초안 |
| `github-actions-daily-report.yml` | 일일 리포트 생성 GitHub Actions 예시 |

## 권장 구현 순서

1. RSS/공식 블로그 수집기 구현
2. Firecrawl/Crawl4AI 기반 본문 추출기 구현
3. GPT Researcher 래퍼 또는 리서치 엔진 구현
4. PostgreSQL/Supabase 데이터 저장
5. Jinja2 기반 HTML 렌더러 구현
6. Playwright 기반 PNG/PDF 생성
7. PaddleOCR/Surya 이미지 분석 추가
8. X/Twitter 수집 추가
9. Astro/생성형 HTML 레이어 추가
10. 관리자 대시보드와 자동 배포 추가

## MVP 성공 기준

- 하루 1회 자동 실행 가능
- 최소 5개 공식 출처에서 AI 관련 문서 수집
- 리포트 섹션 5개 이상 생성
- 각 섹션에 출처 2개 이상 연결
- HTML 파일 생성 및 Netlify/Vercel 배포 가능
- 실패 시 로그와 재시도 포인트 확인 가능



---

# File: 01_ARCHITECTURE.md

# 01. Architecture

## 1. 시스템 개요

AI Trend Report Engine은 다음 7개 계층으로 구성한다.

```mermaid
flowchart TD
    A[Sources: RSS / Web / GitHub / arXiv / X] --> B[Collectors]
    B --> C[Normalizer & Dedupe]
    C --> D[Content Extractors: Firecrawl / Crawl4AI / Trafilatura]
    D --> E[Analysis: Relevance / Entities / Clustering / Scoring]
    E --> F[Verification: Official / GitHub / Paper / Media / Social]
    F --> G[Generation: Summary / Insight / Prompt Pack]
    G --> H[Rendering: Jinja2 / Astro / Generative HTML]
    H --> I[Artifacts: HTML / JSON / PDF / PNG]
    I --> J[Deploy: Netlify / Vercel / GitHub Pages]
```

## 2. 핵심 설계 원칙

### 2.1 사실과 해석 분리

리포트의 모든 문장은 다음 타입 중 하나로 태깅한다.

| 타입 | 의미 |
|---|---|
| `fact` | 공식 출처, 문서, 논문, GitHub, 신뢰 매체에서 확인된 사실 |
| `social_signal` | X/Twitter, Reddit, HN 등 소셜 신호 |
| `inference` | 근거를 바탕으로 한 해석 |
| `unknown` | 확인 불가 또는 낮은 신뢰도 |

### 2.2 검증 우선순위

```text
official_site > official_docs > official_github/huggingface > paper/arxiv > trusted_media > official_social > individual_social > blog/unknown
```

### 2.3 HTML 생성 원칙

- 헤더, 푸터, 출처, 방법론은 고정 템플릿.
- 본문 카드, 이미지 설명, 타임라인, 차트는 생성형 레이아웃 허용.
- 생성형 HTML은 sandbox validator를 통과해야 한다.
- `<script>` 삽입은 기본 금지.
- 외부 리소스는 allowlist 기반으로 제한.

## 3. 모듈 책임

```text
app/
  collectors/          # 원천 데이터 수집
  extractors/          # 웹 본문 추출
  processors/          # 중복 제거, 관련도 분류, 엔티티 추출
  verification/        # 공식 출처 검증, 신뢰도 산정
  vision/              # 이미지 OCR, 캡션, 검증 등급
  research/            # GPT Researcher 연동 또는 자체 리서치 엔진
  generation/          # 섹션 요약, 인사이트, 프롬프트
  rendering/           # HTML/PDF/PNG 생성
  deployment/          # Netlify/Vercel/GitHub Pages 배포
  admin/               # 관리자 API와 UI
```

## 4. 데이터 흐름

### 4.1 수집

```mermaid
sequenceDiagram
    participant Scheduler
    participant Collector
    participant DB
    participant Storage

    Scheduler->>Collector: run_daily(date)
    Collector->>Collector: fetch RSS/GitHub/arXiv/Web/X
    Collector->>Storage: save raw media
    Collector->>DB: insert raw_sources
    Collector->>DB: insert source_media
```

### 4.2 검증

```mermaid
sequenceDiagram
    participant Analyzer
    participant Researcher
    participant Extractor
    participant DB

    Analyzer->>DB: load clusters
    Analyzer->>Researcher: build research query
    Researcher->>Extractor: scrape official candidates
    Extractor-->>Researcher: markdown + metadata
    Researcher-->>Analyzer: evidence set
    Analyzer->>DB: save source_verifications
```

### 4.3 렌더링

```mermaid
sequenceDiagram
    participant Generator
    participant Renderer
    participant Playwright
    participant Deploy

    Generator->>Renderer: report.json
    Renderer->>Renderer: render HTML
    Renderer->>Playwright: screenshot/pdf
    Playwright-->>Renderer: thumbnail.png/report.pdf
    Renderer->>Deploy: publish public/news/date.html
```

## 5. MVP 아키텍처

MVP는 단순성과 안정성을 위해 다음만 구현한다.

```text
RSS + 공식 블로그 수집
→ Firecrawl/Crawl4AI 본문 추출
→ LLM 관련도 분류
→ 공식 출처 검증
→ Jinja2 HTML 렌더링
→ Playwright PNG/PDF 생성
→ Netlify 배포
```

## 6. 확장 아키텍처

Phase 2 이후 확장한다.

```text
X/Twitter 수집
이미지 OCR/비전 캡션
임베딩 클러스터링
GPT Researcher 기반 자동 리서치
OpenGenerativeUI 방식 생성형 HTML
관리자 대시보드
구독자 이메일 발송
```

## 7. 실패 격리 전략

| 실패 지점 | 대응 |
|---|---|
| 특정 RSS 실패 | 해당 소스만 실패 처리, 전체 파이프라인 지속 |
| 크롤링 차단 | Trafilatura fallback, 수동 URL 등록 |
| LLM 요약 실패 | 원문 기반 fallback summary 생성 |
| HTML 생성 실패 | 이전 정상 템플릿 사용 |
| 배포 실패 | 로컬 artifact 보존, 알림 발송 |
| X API 실패 | RSS/공식 블로그만으로 리포트 생성 |

## 8. 저장소 구조 권장안

```text
ai-trend-report-engine/
  app/
    collectors/
    extractors/
    processors/
    verification/
    vision/
    research/
    generation/
    rendering/
    deployment/
  docs/
  templates/
  public/
  data/
    raw/
    processed/
    reports/
  tests/
  scripts/
  migrations/
  .github/workflows/
```



---

# File: 02_IMPLEMENTATION_ROADMAP.md

# 02. Implementation Roadmap

## 1. 개발 전략

처음부터 X/Twitter, 생성형 HTML, 이미지 OCR까지 모두 구현하지 않는다.  
MVP는 공식 출처 기반 리포트 생성으로 시작하고, 이후 소셜 신호와 이미지 분석을 확장한다.

## 2. Phase 계획

### Phase 0. 프로젝트 부트스트랩

**기간:** 1~2일  
**목표:** 개발자가 바로 실행 가능한 저장소 구성

#### 작업

- Python 프로젝트 초기화
- `pyproject.toml` 또는 `requirements.txt` 구성
- `.env.example` 작성
- Docker Compose 구성
- DB 마이그레이션 스크립트 추가
- GitHub Actions skeleton 추가
- 기본 README 작성

#### 완료 기준

- `make dev` 또는 `docker compose up`으로 로컬 의존성 실행
- `python scripts/run_daily.py --dry-run` 실행 가능

---

### Phase 1. MVP 수집/추출/렌더링

**기간:** 1주  
**목표:** RSS/공식 블로그 기반 HTML 리포트 생성

#### 포함 기능

- RSS 수집기
- URL 중복 제거
- Firecrawl 또는 Crawl4AI 본문 추출
- LLM 기반 AI 관련도 분류
- 간단한 섹션 요약
- Jinja2 HTML 렌더링
- JSON artifact 저장

#### 완료 기준

- 최소 5개 소스에서 데이터 수집
- 리포트 섹션 3개 이상 생성
- `/public/news/YYYY-MM-DD-trend.html` 생성
- `/public/news/YYYY-MM-DD-trend.json` 생성

---

### Phase 2. 공식 출처 검증

**기간:** 1~2주  
**목표:** 검증 가능한 출처 기반 리포트 품질 확보

#### 포함 기능

- 공식 도메인 allowlist
- 출처 유형 분류
- 신뢰도 스코어
- 공식/GitHub/논문/뉴스/소셜 구분
- 섹션별 evidence box 생성
- 불확실성 표시

#### 완료 기준

- 모든 핵심 주장에 최소 1개 출처 연결
- `verification_status` 필드가 모든 섹션에 존재
- 확인 불가 항목은 리포트에 명시

---

### Phase 3. 이미지/OCR 분석

**기간:** 1~2주  
**목표:** 최초 이미지와 유사한 “이미지 확인” 블록 자동 생성

#### 포함 기능

- 미디어 다운로드
- 이미지 중복 제거
- PaddleOCR/Surya OCR
- 이미지 유형 분류: chart/ui/logo/person/product/screenshot
- 비전 캡션 생성
- 이미지 검증 등급 A/B/C/D/X 부여

#### 완료 기준

- 이미지 포함 소스에서 썸네일 저장
- 이미지별 caption_ko 생성
- 리포트에 image evidence block 표시

---

### Phase 4. 클러스터링/트렌드 점수

**기간:** 1~2주  
**목표:** 개별 뉴스 나열이 아닌 트렌드 리포트화

#### 포함 기능

- 임베딩 생성
- 유사도 기반 클러스터링
- 키워드 추출
- 트렌드 점수 산식 적용
- 대표 콘텐츠 선정
- TOP 5 키워드 추출

#### 완료 기준

- 동일 이슈 중복 제거
- 중요도 순위 표시
- 리포트 상단 통계 카드 생성

---

### Phase 5. 생성형 HTML 레이어

**기간:** 2주  
**목표:** 콘텐츠 성격에 맞는 카드/차트/갤러리 레이아웃 자동 생성

#### 포함 기능

- layout planner
- section component generator
- HTML sanitizer
- Playwright visual validation
- PDF/PNG export
- fallback template

#### 완료 기준

- 벤치마크 이슈는 표/차트형으로 표시
- 이미지 많은 이슈는 갤러리형으로 표시
- 렌더링 실패 시 고정 템플릿으로 fallback

---

### Phase 6. X/Twitter 통합

**기간:** 2~4주  
**목표:** 소셜 트렌드 기반 리포트로 확장

#### 포함 기능

- X API 또는 Twikit collector
- 트윗 metric 저장
- 이미지/URL 추출
- 계정 신뢰도 점수
- 소셜 신호와 공식 출처 분리

#### 완료 기준

- 일일 500~1,000개 트윗 분석 가능
- AI 관련도 분류 결과 저장
- 소셜 기반 claim은 `social_signal`로 분리

---

## 3. 개발 우선순위

| 우선순위 | 기능 | 이유 |
|---|---|---|
| P0 | RSS/공식 블로그 수집 | 안정적이고 법적 리스크 낮음 |
| P0 | 본문 추출 | 모든 요약의 기반 |
| P0 | HTML 렌더링 | 즉시 결과 확인 가능 |
| P1 | 공식 출처 검증 | 신뢰도 핵심 |
| P1 | 데이터베이스 저장 | 재처리/운영 필수 |
| P2 | 이미지 OCR | 최초 이미지 같은 결과 구현 |
| P2 | 생성형 HTML | 차별화 요소 |
| P3 | X/Twitter | 소셜 트렌드 강화 |
| P3 | 관리자 UI | 운영 편의성 |

## 4. 팀 구성 예상

| 역할 | FTE | 기간 |
|---|---:|---|
| Backend/Automation Engineer | 1.0 | 전체 |
| Frontend/Static Site Engineer | 0.5 | Phase 1~5 |
| ML/LLM Engineer | 0.5 | Phase 2~5 |
| DevOps Engineer | 0.2 | Phase 0, 5, 6 |
| Editor/QA | 0.3 | Phase 2 이후 |

## 5. 핵심 마일스톤

| 마일스톤 | 산출물 |
|---|---|
| M1 | 로컬에서 HTML 리포트 생성 |
| M2 | 공식 출처 검증 표시 |
| M3 | 이미지 확인 블록 생성 |
| M4 | 트렌드 점수 및 클러스터링 |
| M5 | Netlify 자동 배포 |
| M6 | X/Twitter 포함 일일 리포트 |



---

# File: 03_BACKLOG.md

# 03. Product Backlog

## Epic 1. 데이터 수집

### Story 1.1 RSS 수집

**As a** 운영자  
**I want** 공식 블로그와 RSS를 매일 수집하고 싶다  
**So that** 안정적인 공식 출처 기반 리포트를 생성할 수 있다.

#### Tasks

- `feedparser` 기반 RSS collector 작성
- source registry YAML 작성
- 수집 원문 raw_sources에 저장
- URL canonicalization 구현
- 중복 URL 제거

#### Acceptance Criteria

- GIVEN RSS URL 목록이 있을 때
- WHEN daily job이 실행되면
- THEN 각 feed의 신규 아이템이 DB에 저장된다.
- AND 동일 URL은 중복 저장되지 않는다.

---

### Story 1.2 GitHub 릴리즈/트렌딩 수집

#### Tasks

- GitHub API client 구현
- org/repo allowlist 관리
- release, stars, updated_at 수집
- AI 관련 repo 후보 필터링

#### Acceptance Criteria

- 주요 AI repo의 신규 release가 수집된다.
- repo URL과 release URL이 보존된다.

---

### Story 1.3 arXiv 수집

#### Tasks

- arXiv API client 구현
- 카테고리 `cs.AI`, `cs.LG`, `cs.CL`, `cs.CV` 수집
- title/abstract/authors/pdf_url 저장
- 논문 요약 후보 생성

#### Acceptance Criteria

- 최근 24~72시간 논문을 수집한다.
- PDF URL과 arXiv ID가 저장된다.

---

## Epic 2. 웹 본문 추출

### Story 2.1 Firecrawl 추출기

#### Tasks

- Firecrawl client 구현
- scrape 결과 markdown 저장
- title, description, published_at 추출
- 실패 시 retry/backoff

#### Acceptance Criteria

- 공식 블로그 URL을 markdown으로 추출한다.
- 실패 시 error_log에 사유가 저장된다.

---

### Story 2.2 Fallback 추출기

#### Tasks

- Crawl4AI fallback 구현
- Trafilatura fallback 구현
- 본문 품질 점수 계산
- shortest/longest/noise filter 적용

#### Acceptance Criteria

- Firecrawl 실패 시 fallback으로 본문 추출을 시도한다.
- 결과 품질이 낮으면 `extraction_status=low_quality`로 표시한다.

---

## Epic 3. 관련도 분류와 클러스터링

### Story 3.1 AI 관련도 분류

#### Tasks

- keyword prefilter 구현
- LLM relevance classifier prompt 작성
- confidence score 저장
- 제외 사유 저장

#### Acceptance Criteria

- 비AI 콘텐츠는 리포트 후보에서 제외된다.
- 제외 사유가 로그로 남는다.

---

### Story 3.2 엔티티 추출

#### Tasks

- company/product/model/repo/paper 엔티티 추출
- 엔티티 정규화 dictionary 작성
- 오타 교정 규칙 작성

#### Acceptance Criteria

- `NVIDlA C0smos` 같은 OCR 오타를 `NVIDIA Cosmos`로 정규화할 수 있다.

---

### Story 3.3 클러스터링

#### Tasks

- embeddings 생성
- cosine similarity/HDBSCAN 클러스터링
- cluster title 생성
- representative item 선정

#### Acceptance Criteria

- 동일 주제의 여러 글이 하나의 섹션으로 묶인다.
- 대표 출처가 섹션에 연결된다.

---

## Epic 4. 공식 출처 검증

### Story 4.1 Source Trust Scoring

#### Tasks

- official domains registry 작성
- source_type classifier 구현
- trust_score 산식 구현
- evidence 저장

#### Acceptance Criteria

- 각 출처가 official/docs/github/paper/media/social/unknown으로 분류된다.
- 모든 리포트 섹션에 신뢰도 배지가 표시된다.

---

### Story 4.2 GPT Researcher 연동

#### Tasks

- cluster 기반 research query 생성
- GPT Researcher 실행 wrapper 작성
- 결과에서 citations/evidence 추출
- 한국어 summary_ko 생성

#### Acceptance Criteria

- 각 섹션에 공식 출처 또는 확인 불가 표시가 포함된다.
- 출처 없는 주장은 fact로 분류되지 않는다.

---

## Epic 5. 이미지/OCR 분석

### Story 5.1 이미지 저장

#### Tasks

- media URL 다운로드
- SHA256 hash 계산
- 중복 제거
- object storage 저장

#### Acceptance Criteria

- 동일 이미지는 한 번만 저장된다.
- raw source와 media 관계가 보존된다.

---

### Story 5.2 OCR/캡션

#### Tasks

- PaddleOCR 또는 Surya 실행 wrapper
- OCR text 저장
- image_type classifier 구현
- caption_ko 생성 prompt 작성

#### Acceptance Criteria

- 이미지별 OCR 텍스트와 한국어 캡션이 생성된다.
- 낮은 확신도는 `verification_level=D/X`로 표시된다.

---

## Epic 6. HTML 리포트 생성

### Story 6.1 Jinja2 고정 템플릿

#### Tasks

- daily_report.html 템플릿 작성
- section_card.html partial 작성
- CSS 작성
- mobile responsive 구현

#### Acceptance Criteria

- report.json으로 HTML이 생성된다.
- 모바일/데스크톱에서 읽을 수 있다.

---

### Story 6.2 생성형 HTML 섹션

#### Tasks

- layout planner 작성
- 생성형 section prompt 작성
- HTML sanitizer 작성
- fallback 템플릿 작성

#### Acceptance Criteria

- 데이터 유형에 따라 카드/표/타임라인/갤러리 레이아웃이 달라진다.
- 생성 실패 시 고정 템플릿으로 대체된다.

---

### Story 6.3 PDF/PNG Export

#### Tasks

- Playwright screenshot 구현
- PDF export 구현
- visual regression snapshot 저장

#### Acceptance Criteria

- 각 리포트에 thumbnail.png와 report.pdf가 생성된다.
- 빈 화면/렌더링 오류를 감지한다.

---

## Epic 7. 배포/운영

### Story 7.1 GitHub Actions 자동화

#### Tasks

- daily cron workflow 작성
- secrets 설정 문서화
- artifact upload
- 배포 step 추가

#### Acceptance Criteria

- 매일 지정 시간에 자동 실행된다.
- 실패 시 로그를 확인할 수 있다.

---

### Story 7.2 관리자 대시보드

#### Tasks

- draft list
- rerun button
- source health
- manual approve/publish
- issue flagging

#### Acceptance Criteria

- 운영자가 초안을 확인하고 발행할 수 있다.
- 실패한 소스만 재실행할 수 있다.



---

# File: 04_API_SPEC.md

# 04. API Specification

## 1. API 설계 원칙

- API는 내부 파이프라인과 관리자 UI 모두에서 사용 가능해야 한다.
- 모든 응답은 JSON.
- 모든 write API는 admin token 또는 Supabase Auth 필요.
- public API는 발행된 리포트만 조회 가능.

## 2. 공통 응답 포맷

```json
{
  "ok": true,
  "data": {},
  "error": null,
  "meta": {
    "request_id": "req_...",
    "generated_at": "2026-04-27T09:00:00+09:00"
  }
}
```

오류:

```json
{
  "ok": false,
  "data": null,
  "error": {
    "code": "SOURCE_FETCH_FAILED",
    "message": "Failed to fetch RSS source",
    "details": {}
  }
}
```

## 3. Report API

### GET `/api/reports`

발행된 리포트 목록 조회.

#### Query

| 이름 | 타입 | 설명 |
|---|---|---|
| `limit` | number | 기본 20 |
| `offset` | number | 기본 0 |
| `status` | string | `published`, `draft`, `failed` |

#### Response

```json
{
  "ok": true,
  "data": [
    {
      "id": "report_2026_04_27",
      "date": "2026-04-27",
      "title": "오늘의 AI 트렌드",
      "status": "published",
      "html_url": "/news/2026-04-27-trend.html",
      "json_url": "/news/2026-04-27-trend.json",
      "thumbnail_url": "/news/2026-04-27-thumbnail.png",
      "stats": {
        "total_sources": 1240,
        "ai_relevant": 812,
        "verified_links": 43,
        "images_analyzed": 18
      }
    }
  ],
  "error": null
}
```

### GET `/api/reports/{date}`

특정 날짜 리포트 JSON 조회.

### POST `/api/reports/generate`

리포트 생성 job 시작.

#### Request

```json
{
  "date": "2026-04-27",
  "mode": "full",
  "sources": ["rss", "github", "arxiv"],
  "include_images": true,
  "publish": false
}
```

#### Response

```json
{
  "ok": true,
  "data": {
    "job_id": "job_01",
    "status": "queued"
  }
}
```

### POST `/api/reports/{date}/publish`

초안 리포트를 발행 상태로 변경하고 정적 파일 배포.

---

## 4. Source API

### GET `/api/sources`

수집 소스 목록 조회.

### POST `/api/sources`

새 소스 등록.

```json
{
  "name": "OpenAI Blog",
  "source_type": "rss",
  "url": "https://openai.com/news/rss.xml",
  "trust_level": "official",
  "enabled": true
}
```

### PATCH `/api/sources/{id}`

소스 수정.

### POST `/api/sources/{id}/test`

소스 수집 테스트.

---

## 5. Collection API

### POST `/api/jobs/collect`

수집 job 실행.

```json
{
  "date_from": "2026-04-26T00:00:00+09:00",
  "date_to": "2026-04-27T00:00:00+09:00",
  "source_types": ["rss", "github", "arxiv"],
  "dry_run": false
}
```

### GET `/api/jobs/{job_id}`

job 상태 조회.

```json
{
  "ok": true,
  "data": {
    "job_id": "job_01",
    "status": "running",
    "steps": [
      {"name": "collect", "status": "completed"},
      {"name": "extract", "status": "running"},
      {"name": "render", "status": "pending"}
    ],
    "progress": 42
  }
}
```

---

## 6. Verification API

### POST `/api/verify/source`

URL 하나를 검증.

```json
{
  "url": "https://example.com/product",
  "entity_hint": "NVIDIA Cosmos"
}
```

#### Response

```json
{
  "ok": true,
  "data": {
    "url": "https://example.com/product",
    "source_type": "official_site",
    "trust_score": 95,
    "verification_status": "official_confirmed",
    "evidence_summary": "공식 사이트에서 동일 제품명과 설명 확인"
  }
}
```

### POST `/api/verify/cluster`

섹션/클러스터 단위 공식 출처 검증.

---

## 7. Image API

### POST `/api/images/analyze`

이미지 분석 실행.

```json
{
  "media_id": "media_01",
  "run_ocr": true,
  "run_caption": true
}
```

#### Response

```json
{
  "ok": true,
  "data": {
    "media_id": "media_01",
    "image_type": "chart",
    "ocr_text": "...",
    "caption_ko": "벤치마크 성능 비교 차트로 보입니다.",
    "verification_level": "C"
  }
}
```

---

## 8. Render API

### POST `/api/render/html`

report JSON을 HTML로 렌더링.

```json
{
  "report_id": "report_2026_04_27",
  "renderer": "jinja2",
  "generate_pdf": true,
  "generate_png": true
}
```

### POST `/api/render/section`

특정 섹션만 생성형 HTML로 렌더링.

```json
{
  "section_id": "cluster_openai_codex",
  "mode": "generative",
  "layout_hint": "cards"
}
```

---

## 9. Webhook

### POST `/api/webhooks/deploy`

Netlify/Vercel 배포 완료 이벤트 수신.

### POST `/api/webhooks/alert`

실패 알림 수신/중계.

---

## 10. Error Code

| Code | 의미 |
|---|---|
| `SOURCE_FETCH_FAILED` | 소스 수집 실패 |
| `EXTRACTION_FAILED` | 본문 추출 실패 |
| `LLM_TIMEOUT` | LLM 호출 timeout |
| `VERIFICATION_LOW_CONFIDENCE` | 검증 신뢰도 낮음 |
| `HTML_RENDER_FAILED` | HTML 렌더링 실패 |
| `DEPLOY_FAILED` | 배포 실패 |
| `AUTH_REQUIRED` | 인증 필요 |
| `RATE_LIMITED` | 외부 API rate limit |



---

# File: 05_DATA_SCHEMA.md

# 05. Data Schema

## 1. 설계 원칙

- 원본 데이터와 가공 데이터를 분리한다.
- 모든 LLM 결과에는 `model`, `prompt_version`, `confidence`, `created_at`을 저장한다.
- 모든 핵심 주장에는 evidence를 연결한다.
- 리포트는 재생성 가능해야 하므로 중간 산출물을 보존한다.

## 2. 주요 엔티티

```mermaid
erDiagram
    sources ||--o{ raw_items : produces
    raw_items ||--o{ media_assets : has
    raw_items ||--o{ extracted_contents : extracted_from
    extracted_contents ||--o{ analysis_results : analyzed_as
    clusters ||--o{ cluster_items : contains
    raw_items ||--o{ cluster_items : belongs_to
    clusters ||--o{ verifications : verified_by
    reports ||--o{ report_sections : contains
    clusters ||--o{ report_sections : summarized_as
    reports ||--o{ report_artifacts : outputs
```

## 3. 테이블 요약

| 테이블 | 목적 |
|---|---|
| `sources` | 수집 대상 소스 registry |
| `raw_items` | 원본 RSS/URL/트윗/논문/GitHub 아이템 |
| `media_assets` | 이미지/동영상/첨부 자료 |
| `extracted_contents` | Firecrawl/Crawl4AI/Trafilatura 결과 |
| `analysis_results` | 관련도, 엔티티, 키워드, 임베딩 메타 |
| `clusters` | 주제 클러스터 |
| `cluster_items` | 클러스터와 raw item 연결 |
| `verifications` | 출처 검증 결과 |
| `image_analyses` | OCR/비전 캡션 결과 |
| `reports` | 리포트 메타 |
| `report_sections` | 리포트 섹션 |
| `report_artifacts` | HTML/JSON/PDF/PNG 파일 |
| `job_runs` | 파이프라인 실행 기록 |
| `job_logs` | 단계별 로그 |

## 4. 주요 필드 설계

### `sources`

- `source_type`: `rss`, `website`, `github`, `arxiv`, `x`, `manual`
- `trust_level`: `official`, `trusted_media`, `community`, `unknown`
- `enabled`: 수집 활성화 여부

### `raw_items`

- 원본 제목/본문/URL/작성자/발행 시각 저장
- 소셜 지표는 `metrics_json`에 저장
- 중복 방지를 위해 `canonical_url_hash` 사용

### `extracted_contents`

- `extractor`: `firecrawl`, `crawl4ai`, `trafilatura`, `manual`
- `content_markdown`: LLM 입력용 본문
- `quality_score`: 본문 추출 품질

### `analysis_results`

- `is_ai_related`
- `ai_relevance_score`
- `entities_json`
- `keywords_json`
- `summary_ko`
- `claim_type`

### `verifications`

- `verification_status`: `official_confirmed`, `github_confirmed`, `paper_confirmed`, `trusted_media_only`, `social_only`, `image_only`, `unverified`
- `trust_score`: 0~100
- `evidence_json`: 근거 목록

### `report_sections`

- `fact_summary`
- `social_signal_summary`
- `inference_summary`
- `image_evidence_json`
- `sources_json`
- `confidence`

## 5. 인덱스 전략

| 인덱스 | 목적 |
|---|---|
| `raw_items(canonical_url_hash)` | 중복 제거 |
| `raw_items(published_at)` | 날짜별 조회 |
| `raw_items(source_type)` | 소스 타입별 조회 |
| `analysis_results(ai_relevance_score)` | 후보 필터링 |
| `clusters(report_date)` | 일별 클러스터 조회 |
| `reports(report_date)` | 일별 리포트 조회 |
| `job_runs(status)` | 운영 대시보드 |

## 6. 보존 정책

| 데이터 | 보존 기간 |
|---|---|
| raw_items | 180일 |
| extracted_contents | 180일 |
| media_assets | 90일 또는 리포트 연결 시 영구 |
| job_logs | 30일 |
| reports/artifacts | 영구 |
| embeddings | 90일 |



---

# File: 06_PIPELINE_RUNBOOK.md

# 06. Pipeline Runbook

## 1. 일일 파이프라인

```text
01_collect
02_extract
03_classify
04_cluster
05_verify
06_image_analyze
07_generate_report
08_render_artifacts
09_publish
10_notify
```

## 2. 실행 명령 예시

```bash
python scripts/run_daily.py --date 2026-04-27 --mode full
```

드라이런:

```bash
python scripts/run_daily.py --date 2026-04-27 --mode full --dry-run
```

특정 단계만 재실행:

```bash
python scripts/run_daily.py --date 2026-04-27 --from-step verify --to-step render
```

## 3. 단계별 상세

### 3.1 Collect

#### 입력

- source registry
- date range
- source types

#### 출력

- `raw_items`
- `media_assets`

#### 실패 대응

| 오류 | 조치 |
|---|---|
| RSS timeout | 3회 retry 후 skip |
| GitHub rate limit | token 확인, 다음 run으로 이월 |
| X API error | RSS-only mode로 fallback |

---

### 3.2 Extract

#### 입력

- `raw_items.url`

#### 출력

- `extracted_contents`

#### 품질 기준

- 본문 길이 500자 이상
- title 존재
- boilerplate 비율 낮음
- markdown 구조 유지

#### 실패 대응

1. Firecrawl 시도
2. Crawl4AI fallback
3. Trafilatura fallback
4. manual extraction queue로 이동

---

### 3.3 Classify

#### 입력

- extracted text
- source metadata

#### 출력

- `analysis_results`

#### 분류 기준

| score | 처리 |
|---:|---|
| 0.80 이상 | 리포트 후보 |
| 0.50~0.79 | 보조 후보 |
| 0.50 미만 | 제외 |

---

### 3.4 Cluster

#### 입력

- AI 관련 콘텐츠
- embeddings

#### 출력

- `clusters`
- `cluster_items`

#### 운영 기준

- 하루 5~12개 클러스터 권장
- 너무 작은 클러스터는 기타 섹션으로 병합
- 대표 아이템은 trust_score와 relevance_score를 함께 고려

---

### 3.5 Verify

#### 입력

- cluster topic
- entities
- source URLs

#### 출력

- `verifications`

#### 검증 단계

1. 공식 도메인 매칭
2. 공식 문서 검색
3. GitHub/Hugging Face 검색
4. arXiv/논문 검색
5. 신뢰 매체 확인
6. 소셜 신호 분리
7. 불확실성 표시

---

### 3.6 Image Analyze

#### 입력

- `media_assets`

#### 출력

- `image_analyses`

#### 검증 등급

| 등급 | 조건 |
|---|---|
| A | 공식 사이트/공식 계정 이미지 |
| B | 신뢰 계정 또는 문서 이미지 |
| C | 일반 소셜 이미지이나 문맥 일치 |
| D | 이미지 내용만 확인, 출처 불명 |
| X | 판독 불가 |

---

### 3.7 Generate Report

#### 입력

- clusters
- verifications
- image analyses

#### 출력

- report JSON
- report sections

#### 생성 규칙

- fact/social/inference를 분리한다.
- 공식 확인 없는 내용을 사실처럼 쓰지 않는다.
- 과도한 투자/성능/미래 예측을 피한다.
- 불확실한 이미지는 추정이라고 명시한다.

---

### 3.8 Render

#### 출력

- HTML
- JSON
- PDF
- PNG thumbnail

#### 실패 대응

- 생성형 HTML 실패 → Jinja2 fallback
- PDF 실패 → HTML만 배포
- PNG 실패 → 기본 썸네일 사용

---

### 3.9 Publish

#### 배포 대상

```text
public/news/YYYY-MM-DD-trend.html
public/news/YYYY-MM-DD-trend.json
public/news/YYYY-MM-DD-report.pdf
public/news/YYYY-MM-DD-thumbnail.png
```

#### 배포 옵션

- Netlify
- Vercel
- GitHub Pages
- S3/R2 정적 호스팅

---

## 4. 장애 대응

### 리포트가 비어 있음

1. source registry 확인
2. collect job log 확인
3. extraction 품질 점수 확인
4. relevance threshold 임시 하향
5. 수동 source 추가

### 공식 출처가 부족함

1. query_builder 프롬프트 확인
2. official domains registry 업데이트
3. GitHub/arXiv fallback 확인
4. trusted media source 추가

### HTML 렌더링 깨짐

1. report JSON schema validation
2. HTML sanitizer log 확인
3. Playwright screenshot 확인
4. fallback template로 재렌더링

## 5. 운영 지표

| 지표 | 목표 |
|---|---|
| daily job success rate | 95% 이상 |
| report generation time | 30분 이하 |
| official verification coverage | 70% 이상 |
| unverified claim rate | 10% 이하 |
| image analysis success rate | 80% 이상 |
| render success rate | 99% 이상 |



---

# File: 07_PROMPT_PACK.md

# 07. Prompt Pack

## 1. 공통 시스템 프롬프트

```text
너는 AI 기술 뉴스 리서치 편집자다.
목표는 공식 출처와 검증 가능한 근거를 바탕으로 한국어 리포트를 만드는 것이다.

규칙:
1. 공식 출처에서 확인된 사실과 소셜 반응을 구분한다.
2. 확인되지 않은 주장은 절대 사실처럼 쓰지 않는다.
3. 과장된 표현을 피하고, 불확실성은 명시한다.
4. 모든 섹션은 한국어로 작성한다.
5. 출력은 요청된 JSON Schema를 엄격히 따른다.
```

## 2. AI 관련도 분류 프롬프트

### Input

```json
{
  "title": "...",
  "text": "...",
  "source_type": "rss",
  "url": "..."
}
```

### Prompt

```text
다음 콘텐츠가 AI 기술 트렌드 리포트에 포함될 가치가 있는지 판정해라.

판정 기준:
- LLM, AI 모델, 에이전트, 로봇, 반도체, 개발자 도구, 논문, 벤치마크, AI 정책과 직접 관련되면 포함.
- 단순 주가, 마케팅, 일반 IT 뉴스는 낮게 평가.
- 공식 발표, 기술 문서, 논문, GitHub 릴리즈는 높게 평가.

출력 JSON:
{
  "is_ai_related": true,
  "score": 0.0,
  "category": "model|agent|infra|research|product|policy|tool|other",
  "reason_ko": "..."
}
```

## 3. 엔티티 추출 프롬프트

```text
다음 텍스트에서 AI 리포트에 중요한 엔티티를 추출해라.

엔티티 타입:
- company
- product
- model
- repository
- paper
- person
- benchmark
- dataset
- hardware
- framework

출력 JSON:
{
  "entities": [
    {
      "name": "NVIDIA Cosmos",
      "normalized_name": "NVIDIA Cosmos",
      "type": "product",
      "confidence": 0.95
    }
  ],
  "keywords": ["Physical AI", "world model"]
}
```

## 4. 공식 출처 검증 프롬프트

```text
다음 주제와 후보 출처를 검토하고 검증 상태를 판정해라.

주제:
{{ topic }}

후보 출처:
{{ sources }}

검증 기준:
- 공식 회사/프로젝트 사이트면 official_confirmed
- 공식 GitHub/Hugging Face면 github_confirmed
- 논문/arXiv면 paper_confirmed
- 신뢰 매체만 있으면 trusted_media_only
- 소셜 계정만 있으면 social_only
- 이미지 단서만 있으면 image_only
- 확인 근거가 부족하면 unverified

출력 JSON:
{
  "verification_status": "official_confirmed",
  "trust_score": 95,
  "evidence_summary_ko": "...",
  "confirmed_facts": ["..."],
  "unverified_claims": ["..."],
  "source_ranking": [
    {
      "url": "...",
      "type": "official_site",
      "trust_score": 95,
      "reason_ko": "..."
    }
  ]
}
```

## 5. 이미지 캡션 프롬프트

```text
다음 이미지를 AI 트렌드 리포트 관점에서 설명해라.

주의:
- 이미지에서 실제로 보이는 것만 설명한다.
- 로고/텍스트가 흐리면 확정하지 않는다.
- 공식 출처가 없으면 "추정"이라고 표시한다.
- 과장하지 않는다.

출력 JSON:
{
  "image_type": "chart|ui|logo|person|product|screenshot|unknown",
  "visible_elements_ko": ["..."],
  "caption_ko": "...",
  "ocr_keywords": ["..."],
  "verification_level": "A|B|C|D|X",
  "uncertainty_ko": "..."
}
```

## 6. 섹션 요약 프롬프트

```text
다음 클러스터 데이터를 바탕으로 한국어 리포트 섹션을 작성해라.

작성 구조:
1. 제목
2. 한 줄 요약
3. 확인된 사실
4. 소셜 반응
5. 이미지 확인
6. 시사점
7. 주의할 점
8. 해시태그

규칙:
- 확인된 사실과 추정을 분리한다.
- 출처가 없는 내용은 "추정"으로 표시한다.
- 개발자/비즈니스 관점의 시사점을 포함한다.
- 불필요한 수식어를 줄인다.

출력 JSON:
{
  "title": "...",
  "lead": "...",
  "fact_summary": "...",
  "social_signal_summary": "...",
  "image_evidence_summary": "...",
  "insight": "...",
  "caution": "...",
  "hashtags": ["#AI", "#LLM"],
  "confidence": "high|medium|low"
}
```

## 7. 생성형 HTML 프롬프트

```text
다음 리포트 섹션 JSON을 HTML 카드로 렌더링해라.

제약:
- HTML fragment만 출력한다.
- script 태그 금지.
- 외부 JS 금지.
- CSS class는 제공된 디자인 시스템 class만 사용한다.
- 출처 링크는 반드시 sources 배열의 URL만 사용한다.
- 접근성을 위해 img alt를 작성한다.

사용 가능한 컴포넌트:
- trend-card
- badge
- evidence-box
- image-evidence
- source-list
- insight-box
- caution-box
- metric-grid
- timeline

출력:
HTML fragment only.
```

## 8. 팩트체크 프롬프트

```text
다음 리포트 초안을 검토해라.

검토 항목:
1. 공식 출처 없는 주장이 사실처럼 쓰였는가?
2. 수치가 출처와 일치하는가?
3. 이미지 설명이 과장되었는가?
4. 추정과 사실이 분리되었는가?
5. 제목이 지나치게 선정적인가?

출력 JSON:
{
  "pass": true,
  "issues": [
    {
      "severity": "high|medium|low",
      "field": "section.fact_summary",
      "message_ko": "...",
      "suggested_fix_ko": "..."
    }
  ]
}
```

## 9. 제목 생성 프롬프트

```text
다음 리포트의 제목 후보 5개를 생성해라.

조건:
- 한국어
- 과장 금지
- 40자 이하
- 핵심 키워드 1~2개 포함
- 클릭베이트 금지

출력 JSON:
{
  "titles": [
    {"title": "...", "tone": "neutral", "reason_ko": "..."}
  ]
}
```



---

# File: 08_TEST_PLAN.md

# 08. Test Plan

## 1. 테스트 전략

테스트는 다음 6개 레벨로 나눈다.

1. Unit Test
2. Integration Test
3. Pipeline Test
4. LLM Output Validation
5. Visual Regression Test
6. Editorial QA

## 2. Unit Test

### 대상

| 모듈 | 테스트 |
|---|---|
| URL canonicalizer | query/hash/utm 제거 |
| dedupe | 동일 URL/동일 이미지 hash 제거 |
| source classifier | official/docs/github/paper/social 분류 |
| trust scorer | 점수 산식 |
| JSON schema validator | report schema 검증 |
| prompt builder | 필수 변수 누락 검출 |

### 예시

```python
def test_canonicalize_removes_utm():
    url = "https://example.com/a?utm_source=x&id=1"
    assert canonicalize_url(url) == "https://example.com/a?id=1"
```

## 3. Integration Test

### Collect → Extract

- mock RSS feed 사용
- fake HTML page 사용
- extractor fallback 확인

### Extract → Analyze

- 본문이 짧거나 노이즈 많은 경우 quality_score 낮게 표시
- AI 관련도 threshold 확인

### Analyze → Render

- 최소 report.json으로 HTML 생성
- 누락 필드가 있으면 validation error 발생

## 4. Pipeline Test

### 시나리오 A: 정상 실행

```text
given 10 RSS items
when run_daily executes
then report html/json/png/pdf are generated
```

### 시나리오 B: 일부 소스 실패

```text
given 1 source timeout
when pipeline runs
then failed source is logged
and report still generated
```

### 시나리오 C: LLM timeout

```text
given LLM timeout during section summary
when retry fails
then fallback summary is used
```

## 5. LLM Output Validation

모든 LLM 결과는 JSON schema로 검증한다.

### 검증 항목

- JSON parse 가능
- 필수 필드 존재
- enum 값 유효
- confidence 범위 0~1
- 출처 없는 fact 금지

### 실패 대응

1. repair prompt
2. deterministic fallback
3. human review queue

## 6. Visual Regression Test

Playwright 사용.

### 체크

- HTML 렌더링 오류 없음
- 주요 섹션 표시
- 이미지 alt 존재
- 모바일 width 390px 정상
- 데스크톱 width 1440px 정상
- screenshot diff threshold 이하

### 명령 예시

```bash
pytest tests/visual
```

## 7. Editorial QA

### 체크리스트

```text
[ ] 모든 주요 수치에 출처가 있는가?
[ ] 공식 발표와 소셜 반응이 분리되었는가?
[ ] 확인 불가를 명시했는가?
[ ] 이미지 설명이 보이는 내용 이상을 추정하지 않았는가?
[ ] 제목이 과장되지 않았는가?
[ ] 한국어 문장이 자연스러운가?
[ ] 링크가 실제로 열리는가?
```

## 8. 성능 테스트

| 항목 | 목표 |
|---|---|
| 100개 source 처리 | 10분 이하 |
| 1,000개 social item 처리 | 30분 이하 |
| HTML render | 10초 이하 |
| PDF/PNG export | 30초 이하 |
| full daily pipeline | 60분 이하 |

## 9. 보안 테스트

- HTML sanitizer 테스트
- script injection 차단
- SSRF 방지
- admin API 인증
- secret logging 방지
- RLS 정책 확인

## 10. 릴리즈 게이트

릴리즈 전 다음 조건을 만족해야 한다.

```text
[ ] unit test 90% 이상 통과
[ ] integration test 통과
[ ] sample daily report 생성 성공
[ ] visual screenshot 통과
[ ] schema migration 적용 성공
[ ] secrets 문서화
[ ] rollback 절차 문서화
```



---

# File: 09_SECURITY_AND_COMPLIANCE.md

# 09. Security and Compliance

## 1. 보안 원칙

- 외부 웹 데이터는 신뢰하지 않는다.
- 생성형 HTML은 반드시 sanitize한다.
- 관리자 API는 인증과 권한 검사를 거친다.
- 크롤링은 robots.txt, 서비스 약관, rate limit을 준수한다.
- 원본 데이터와 생성 데이터를 분리 저장한다.

## 2. Secrets 관리

### 환경 변수

- `.env`는 커밋 금지
- GitHub Actions Secrets 사용
- Netlify/Vercel 환경 변수 사용
- 로컬은 `.env.example`만 제공

### 주요 Secret

```text
OPENAI_API_KEY
FIRECRAWL_API_KEY
SUPABASE_URL
SUPABASE_SERVICE_ROLE_KEY
SUPABASE_ANON_KEY
GITHUB_TOKEN
X_BEARER_TOKEN
NETLIFY_AUTH_TOKEN
```

## 3. HTML 보안

### 금지

- `<script>`
- inline event handler: `onclick`, `onerror`
- unknown iframe
- 외부 JS
- unknown CSS import
- `javascript:` URL

### 허용

- 제한된 HTML tag
- allowlist class
- allowlist image host
- sanitized anchor tag

## 4. SSRF 방지

크롤러가 내부 네트워크에 접근하지 못하도록 차단한다.

### 차단 대상

```text
localhost
127.0.0.0/8
10.0.0.0/8
172.16.0.0/12
192.168.0.0/16
169.254.0.0/16
metadata.google.internal
169.254.169.254
```

## 5. 크롤링 준수

- robots.txt 확인
- user agent 명시
- rate limit 적용
- 유료/로그인/비공개 콘텐츠 무단 수집 금지
- X/Twitter는 공식 API 우선

## 6. 개인정보 처리

가능한 한 개인정보를 저장하지 않는다.

### 저장 가능

- 공개 계정명
- 공개 게시물 URL
- 공개 게시물 텍스트

### 주의 필요

- 이메일
- 전화번호
- 주소
- 비공개 계정 정보
- 얼굴 이미지
- 의료/금융/민감 정보

### 처리 정책

- 리포트에 불필요한 개인 식별 정보 노출 금지
- 인물 이미지는 맥락 설명만, 신원 추정 금지
- 삭제 요청 대응 절차 마련

## 7. Supabase RLS 권장 정책

### public read

- published reports만 공개 조회 가능

### admin write

- authenticated admin만 write 가능

### service role

- pipeline job에서만 사용
- 클라이언트에 노출 금지

## 8. 출처/저작권

- 긴 원문 복제 금지
- 짧은 인용 또는 요약 중심
- 출처 링크 제공
- 이미지 원본은 가능하면 링크/썸네일 중심
- 공식 이미지와 소셜 이미지는 출처와 검증 등급 표시

## 9. 감사 로그

다음 이벤트는 반드시 저장한다.

- report 생성
- report 발행
- source 추가/수정/삭제
- admin 로그인
- 수동 검증 변경
- 실패한 job 재실행
- 생성형 HTML sanitizer 실패

## 10. 위험과 대응

| 위험 | 대응 |
|---|---|
| 가짜 뉴스 확산 | official verification, confidence 표시 |
| 소셜 루머 단정 | social_signal로 분리 |
| X 약관 위반 | 공식 API 우선, 정책 검토 |
| HTML injection | sanitizer, CSP |
| 비밀키 노출 | secrets manager, log redaction |
| 크롤링 차단 | rate limit, fallback, source health |



---

# File: 10_DEPLOYMENT_GUIDE.md

# 10. Deployment Guide

## 1. 로컬 개발

### 1.1 요구사항

- Python 3.11+
- Node.js 20+
- Docker
- PostgreSQL 또는 Supabase
- Playwright browsers

### 1.2 설치

```bash
git clone <repo>
cd ai-trend-report-engine
cp .env.example .env
pip install -r requirements.txt
npm install
playwright install chromium
docker compose up -d
```

### 1.3 DB 초기화

```bash
psql "$DATABASE_URL" -f schema.sql
```

### 1.4 샘플 실행

```bash
python scripts/run_daily.py --date 2026-04-27 --mode rss-only --dry-run
python scripts/run_daily.py --date 2026-04-27 --mode rss-only
```

## 2. 환경 변수

`.env.example` 참고.

필수:

```text
DATABASE_URL
OPENAI_API_KEY
REPORT_PUBLIC_BASE_URL
```

선택:

```text
FIRECRAWL_API_KEY
SUPABASE_URL
SUPABASE_SERVICE_ROLE_KEY
GITHUB_TOKEN
X_BEARER_TOKEN
NETLIFY_AUTH_TOKEN
```

## 3. Docker Compose

로컬 개발 의존성:

- PostgreSQL
- Redis
- MinIO

```bash
docker compose up -d postgres redis minio
```

## 4. Netlify 배포

### 4.1 정적 파일 경로

```text
public/
  index.html
  news/
    YYYY-MM-DD-trend.html
    YYYY-MM-DD-trend.json
    YYYY-MM-DD-thumbnail.png
    YYYY-MM-DD-report.pdf
```

### 4.2 배포 명령

```bash
npx netlify deploy --prod --dir=public
```

## 5. GitHub Actions

`.github/workflows/daily-report.yml`로 매일 실행한다.

### Secrets

```text
OPENAI_API_KEY
DATABASE_URL
FIRECRAWL_API_KEY
NETLIFY_AUTH_TOKEN
NETLIFY_SITE_ID
```

## 6. Rollback

### 정적 사이트 rollback

- Netlify deploy history에서 이전 배포 선택
- 또는 GitHub Pages 이전 commit revert

### 리포트 rollback

```bash
python scripts/rollback_report.py --date 2026-04-27 --to-version previous
```

## 7. 운영 환경 분리

| 환경 | 목적 |
|---|---|
| local | 개발 |
| staging | 배포 전 검증 |
| production | 실제 발행 |

## 8. 배포 전 체크리스트

```text
[ ] DB migration 적용
[ ] 환경 변수 설정
[ ] source registry 확인
[ ] dry-run 성공
[ ] sample report 생성
[ ] screenshot/PDF 생성
[ ] 링크 검사
[ ] Netlify deploy 성공
```



---

# File: 11_OBSERVABILITY.md

# 11. Observability

## 1. 관측 목표

운영자는 다음 질문에 빠르게 답할 수 있어야 한다.

- 오늘 리포트가 생성되었는가?
- 어느 단계에서 실패했는가?
- 어떤 소스가 자주 실패하는가?
- 공식 출처 검증률은 얼마인가?
- LLM 비용은 얼마인가?
- 생성형 HTML 렌더링은 안정적인가?

## 2. 로그

### 구조화 로그 필드

```json
{
  "timestamp": "2026-04-27T09:00:00+09:00",
  "level": "info",
  "job_id": "job_01",
  "step": "extract",
  "source_id": "src_01",
  "message": "extraction completed",
  "duration_ms": 1234,
  "context": {}
}
```

### 로그 레벨

| Level | 용도 |
|---|---|
| debug | 개발 디버깅 |
| info | 정상 진행 |
| warning | 일부 실패, fallback |
| error | 단계 실패 |
| critical | 전체 job 실패 |

## 3. 메트릭

### Pipeline Metrics

| metric | 설명 |
|---|---|
| `pipeline.duration_seconds` | 전체 실행 시간 |
| `pipeline.success_count` | 성공 job 수 |
| `pipeline.failure_count` | 실패 job 수 |
| `collector.items_count` | 수집 아이템 수 |
| `extractor.success_rate` | 본문 추출 성공률 |
| `verification.coverage_rate` | 검증 커버리지 |
| `render.success_rate` | 렌더링 성공률 |

### Quality Metrics

| metric | 목표 |
|---|---|
| `ai_relevance_precision` | 0.85 이상 |
| `official_source_coverage` | 0.70 이상 |
| `unverified_claim_rate` | 0.10 이하 |
| `image_caption_confidence` | 0.75 이상 |

### Cost Metrics

| metric | 설명 |
|---|---|
| `llm.input_tokens` | 입력 토큰 |
| `llm.output_tokens` | 출력 토큰 |
| `llm.cost_usd` | 추정 비용 |
| `crawl.cost_usd` | 크롤링 비용 |

## 4. 알림

### 알림 조건

| 조건 | 채널 |
|---|---|
| daily job failed | Slack/Email |
| report not generated by deadline | Slack/Email |
| official coverage < 50% | Slack |
| render failed | Slack |
| cost spike > 2x | Slack/Email |

## 5. 대시보드

### 운영 대시보드 섹션

1. 오늘 job 상태
2. 최근 7일 성공률
3. 소스별 실패율
4. 리포트 품질 점수
5. LLM 비용
6. 검증 커버리지
7. 이미지 분석 성공률
8. 렌더링 artifact 링크

## 6. 품질 점수 산식

```text
quality_score =
  official_source_coverage * 0.35
+ extraction_success_rate * 0.20
+ render_success_rate * 0.15
+ low_uncertainty_rate * 0.15
+ editorial_pass_rate * 0.15
```

## 7. 리포트 하단 표시 추천

```text
분석 통계:
- 수집 콘텐츠: 1,240건
- AI 관련: 812건
- 공식 출처 확인: 43건
- 이미지 분석: 18장
- 확인 불가: 6건
- 생성 시각: 2026-04-27 08:30 KST
- 엔진 버전: ai-trend-report-engine v0.1.0
```



---

# File: docker-compose.yml

services:
  postgres:
    image: pgvector/pgvector:pg16
    container_name: ai-trend-postgres
    environment:
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: postgres
      POSTGRES_DB: ai_trend
    ports:
      - "5432:5432"
    volumes:
      - ai_trend_pg_data:/var/lib/postgresql/data

  redis:
    image: redis:7
    container_name: ai-trend-redis
    ports:
      - "6379:6379"

  minio:
    image: minio/minio:latest
    container_name: ai-trend-minio
    command: server /data --console-address ":9001"
    environment:
      MINIO_ROOT_USER: minioadmin
      MINIO_ROOT_PASSWORD: minioadmin
    ports:
      - "9000:9000"
      - "9001:9001"
    volumes:
      - ai_trend_minio_data:/data

volumes:
  ai_trend_pg_data:
  ai_trend_minio_data:



---

# File: github-actions-daily-report.yml

name: Daily AI Trend Report

on:
  schedule:
    - cron: "0 22 * * *" # 07:00 KST
  workflow_dispatch:
    inputs:
      report_date:
        description: "Report date YYYY-MM-DD"
        required: false
      mode:
        description: "Run mode"
        required: false
        default: "full"

jobs:
  build-report:
    runs-on: ubuntu-latest
    timeout-minutes: 90

    steps:
      - uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.11"

      - name: Set up Node
        uses: actions/setup-node@v4
        with:
          node-version: "20"

      - name: Install Python dependencies
        run: pip install -r requirements.txt

      - name: Install Node dependencies
        run: npm ci

      - name: Install Playwright
        run: npx playwright install chromium

      - name: Run daily report
        env:
          DATABASE_URL: ${{ secrets.DATABASE_URL }}
          OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
          FIRECRAWL_API_KEY: ${{ secrets.FIRECRAWL_API_KEY }}
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
          NETLIFY_AUTH_TOKEN: ${{ secrets.NETLIFY_AUTH_TOKEN }}
          NETLIFY_SITE_ID: ${{ secrets.NETLIFY_SITE_ID }}
        run: |
          DATE_INPUT="${{ github.event.inputs.report_date }}"
          MODE_INPUT="${{ github.event.inputs.mode }}"
          if [ -z "$DATE_INPUT" ]; then
            python scripts/run_daily.py --mode "${MODE_INPUT:-full}"
          else
            python scripts/run_daily.py --date "$DATE_INPUT" --mode "${MODE_INPUT:-full}"
          fi

      - name: Upload artifacts
        uses: actions/upload-artifact@v4
        with:
          name: daily-report-artifacts
          path: |
            public/news/
            data/reports/

      - name: Deploy to Netlify
        if: success()
        run: npx netlify deploy --prod --dir=public --site="${{ secrets.NETLIFY_SITE_ID }}"
        env:
          NETLIFY_AUTH_TOKEN: ${{ secrets.NETLIFY_AUTH_TOKEN }}



---

# File: schema.sql

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

