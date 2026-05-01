<div align="center">

<img width="2752" height="1536" alt="똑똑한 AI 뉴스레터 공장" src="https://github.com/user-attachments/assets/89588a1e-7a92-4985-b066-ecf65aecf6d5" /><br>

<img width="1672" height="941" alt="ChatGPT Image 2026년 4월 30일 오후 08_10_05" src="https://github.com/user-attachments/assets/9ac90ff4-3299-4ad3-b024-5df30742d3de" />

# 🔥 HTML News Creator

**AI 트렌드 리포트 자동 생성 엔진**

[![Python](https://img.shields.io/badge/Python-3.11-3776AB?logo=python&logoColor=white)](https://python.org)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16-336791?logo=postgresql&logoColor=white)](https://postgresql.org)
[![OpenAI](https://img.shields.io/badge/OpenAI-Compatible-412991?logo=openai&logoColor=white)](https://openai.com)
[![Netlify](https://img.shields.io/badge/Deploy-Netlify-00C7B7?logo=netlify&logoColor=white)](https://netlify.com)
[![CI](https://github.com/coreline-ai/html-news-creator/actions/workflows/ci.yml/badge.svg)](https://github.com/coreline-ai/html-news-creator/actions)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

매일 새벽 **37개 활성 소스**에서 AI 트렌드를 수집·분류·클러스터링하고,
편집 정책과 image-aware backfill 기반으로 **최대 10개 주제의 개발자 중심 뉴스레터 HTML**을 자동 생성하는 파이프라인입니다.

[데모 →](https://ai-news-5min-kr.netlify.app) · [구조 보기](#-아키텍처) · [빠른 시작](#-빠른-시작)

</div>

---

## ✨ 주요 기능

| 기능 | 설명 |
|------|------|
| 🌐 **멀티 소스 수집** | RSS, GitHub Release, arXiv, Hacker News, Reddit, YouTube 등 37개 활성 소스 |
| 🤖 **LLM 분류·요약** | AI 관련성 판별, 한국어 팩트 요약, 시사점 생성 |
| 📐 **임베딩 클러스터링** | HDBSCAN으로 동일 주제 기사를 자동 그룹화 |
| 📰 **편집 정책 기반 선정** | 소스 등급·클러스터 크기·토픽 할당량·이미지 우선 backfill로 최대 10개 섹션 선정 |
| 🖼️ **스마트 이미지 선택** | 원본 대표 이미지 우선, 기자 초상·로고·UI 요소 자동 제외, 이미지 부재 시 생성형 SVG 카드 대체 |
| 🎨 **3가지 리포트 테마** | 기본 라이트, 다크, `newsroom-white` 공개용 테마 |
| 🖥️ **Coreline News Studio** | 옵션·정책·소스·검토·발행을 처리하는 React + FastAPI 운영 웹앱 |
| 📡 **Run 상태 추적** | SSE history replay + `localStorage` activeRun 복원 + JobRun 종료 이력으로 새로고침/탭 이동 대응 |
| 🚀 **Netlify 자동 배포** | GitHub Actions → Netlify 원클릭 배포 |
| 📢 **Slack 알림** | 생성 완료 후 Webhook 통보 |

---

## 🏗️ 아키텍처

```
┌─────────────────────────────────────────────────────────────────────┐
│                         Daily Pipeline                              │
│                                                                     │
│  ① collect  →  ② extract  →  ③ classify  →  ④ cluster            │
│     │               │              │               │               │
│  37개 활성 소스   Trafilatura    LLM 판별         HDBSCAN           │
│  RSS/GitHub     본문 추출      AI 관련성         임베딩 클러스터   │
│  arXiv/HN                      점수화                              │
│                                                                     │
│  ⑤ verify   →  ⑥ generate  →  ⑦ render   →  ⑧ publish          │
│     │               │              │               │               │
│  교차 검증       LLM 섹션      Jinja2 HTML     Netlify/S3          │
│  신뢰 점수       생성·요약     3테마 지원       + Slack 알림       │
└─────────────────────────────────────────────────────────────────────┘
```

### Coreline News Studio 제어 흐름

```
React SPA (ui/)
  ├─ New Report 옵션 조정 → POST /api/preview      # DB 쓰기 없는 미리보기
  ├─ Run 실행           → POST /api/runs         # subprocess로 CLI 실행
  ├─ 진행률 구독        → GET /api/runs/{id}/stream (SSE)
  ├─ 완료/실패 이력     → GET /api/runs + JobRun
  └─ 검토/발행          → /api/reports/*, /api/sections/*

FastAPI app/admin/*
  → scripts/run_daily.py
  → collect/extract/classify/cluster/verify/generate/render/publish/notify
```

> 웹앱은 파이프라인 내부 함수를 직접 import하지 않고, `scripts/run_daily.py`를 subprocess로 실행하는 운영 UI입니다. CLI 독립 실행 경계를 유지하기 위해 웹앱 옵션은 per-run override로 전달하며, 기본 yaml은 명시적 persist 전까지 자동 변경하지 않습니다.

### 파이프라인 단계별 상세

```
collect   │ 소스별 컬렉터(RSS/GitHub/arXiv/HN) → DB 저장 (중복 스킵)
extract   │ Firecrawl·Crawl4AI·Trafilatura fallback으로 본문·OG 이미지 추출
classify  │ LLM으로 AI 관련성 점수(0–1) 산출, 비관련 기사 필터
cluster   │ text-embedding-3-small → HDBSCAN → 주제 클러스터 형성
verify    │ 공식 도메인·GitHub·arXiv와 교차 검증, trust_score 산출
generate  │ 클러스터별 LLM 섹션 생성 (제목·요약·시사점·소스 목록)
render    │ Jinja2 템플릿 → 반응형 HTML 리포트
publish   │ public/news/ 저장 + Netlify 배포
notify    │ Slack Webhook 발송
```

> OpenAI처럼 Cloudflare challenge로 본문 접근이 차단되는 공식 사이트는
> 무리하게 우회하지 않고, 공식 RSS summary/raw text를
> `rss_summary_fallback` 추출 결과로 저장해 반복 실패와 데이터 누락을 줄입니다.

---

## 📁 디렉토리 구조

```
html-news-creator/
├── app/
│   ├── admin/               # 관리자/운영 API (FastAPI, run_runner/SSE/JobRun)
│   ├── collectors/          # 소스별 수집기
│   │   ├── orchestrator.py  # 컬렉터 통합 실행
│   │   ├── rss_collector.py # RSS / YouTube
│   │   ├── github_collector.py
│   │   ├── arxiv_collector.py
│   │   ├── hackernews_collector.py
│   │   ├── website_collector.py
│   │   └── naver_news_collector.py
│   ├── deployment/          # Netlify 배포 / 정적 publisher
│   ├── editorial/           # 편집 정책 엔진
│   │   ├── policy.py        # YAML 정책 로더
│   │   ├── ranker.py        # 아이템 점수 산출 (순수 함수)
│   │   └── selection.py     # 클러스터 선정·요약 (image-aware backfill 포함)
│   ├── extractors/          # 본문 추출기 (Firecrawl → Crawl4AI → Trafilatura fallback)
│   ├── generation/          # LLM 섹션·제목·임베딩·클러스터링
│   ├── models/              # SQLAlchemy ORM (14개 테이블)
│   ├── pipeline/            # 날짜 윈도우 (KST + US 시간대 슬랙)
│   ├── processors/          # 분류·정규화 처리기
│   ├── rendering/           # Jinja2 렌더러 + Playwright 스크린샷
│   ├── research/            # 리서치/실험 모듈
│   ├── utils/
│   │   ├── source_images.py # 이미지 URL 검증·필터
│   │   └── generated_images.py # SVG 폴백 생성
│   ├── verification/        # 소스 교차 검증
│   └── vision/              # OCR (Surya) / 미디어 다운로더
│
├── ui/                         # Coreline News Studio React SPA
│   ├── src/components/          # Sidebar/Header/LivePreview/RunProgress 등
│   ├── src/pages/               # Dashboard/Reports/NewReport/ReviewReport/Policy/Settings
│   ├── src/lib/                 # API client, Zustand store, theme/run options
│   └── src/__tests__/           # Vitest 컴포넌트·store 테스트
│
├── data/
│   ├── sources_registry.yaml   # 37개 활성 소스 설정
│   ├── editorial_policy.yaml   # 점수 공식·할당량·티어·backfill
│   └── official_domains.yaml   # 공식 도메인 화이트리스트
│
├── templates/
│   ├── base.html.j2               # 베이스 레이아웃
│   ├── report_newsstream.html.j2  # 메인 리포트 템플릿 (현재 사용)
│   ├── section_card.html.j2       # 섹션 카드 부분 템플릿
│   └── daily_report.html.j2       # 레거시 (현재 미사용)
│
├── docs/
│   ├── design/                    # 🎨 디자인 시스템 (토큰·컴포넌트·자동화 명세)
│   ├── additional-dev-docs.md     # 통합 개발 참고 문서
│   └── prd-trd-research-notes.md  # PRD/TRD 기반 리서치 노트
│
├── tests/unit/              # 147개 단위 테스트
├── scripts/
│   └── run_daily.py         # 파이프라인 진입점 (CLI)
├── .github/workflows/
│   ├── daily-report.yml     # 매일 22:00 UTC 자동 실행
│   └── ci.yml               # 푸시/PR 단위 테스트
├── migrations/              # SQL 마이그레이션 (001_initial.sql)
├── dev-plan/                # 작업 계획서·리뷰 노트
├── docker-compose.yml       # PostgreSQL + Redis + MinIO
└── Makefile
```

---

## 📰 소스 구성

### 소스 등급 (37개 활성 소스)

| 등급 | 소스 예시 | 부스트 |
|------|----------|--------|
| 🔴 **official** | OpenAI Blog, Anthropic, Google DeepMind, HuggingFace, NVIDIA, AWS | +18 |
| 🟠 **mainstream** | TechCrunch, The Verge, The Decoder, MIT Tech Review, VentureBeat, AI타임스 | +12 |
| 🟡 **developer_signal** | GitHub (openai / anthropics / google-deepmind / microsoft / meta-llama / huggingface) | +14 |
| 🔵 **research** | arXiv cs.AI / cs.LG / cs.CL / cs.CV | +4 |
| ⚪ **community** | Hacker News AI, Reddit r/MachineLearning, r/artificial, r/OpenAI, r/LocalLLaMA | −4 |

### 소스 유형별 분류

```
RSS       █████████████████████  24개  (OpenAI, Verge, TechCrunch, YouTube, Reddit 피드 등)
GitHub    █████                   6개  (주요 AI org 릴리스)
arXiv     ████                    4개  (cs.AI / cs.LG / cs.CL / cs.CV)
Website   ███                     3개  (커스텀 크롤러)
                                ───
                                 37개
```

> 등급별 분포: official 12 · mainstream 10 · developer_signal 6 · research 4 · community 5

---

## ⚖️ 편집 정책

### 점수 산출 공식

```
editorial_score = min(100, max(0,
  50 (base)
  + source_tier_boost     (official +18 / mainstream +12 / developer_signal +14)
  + official_boost        (+10 if official)
  + mainstream_boost      (+6  if mainstream)
  + product_signal        (+8  if "launch/model/api/release" 키워드)
  + research_signal       (+3  if "paper/benchmark/dataset" 키워드)
  + main_image_signal     (+8  if 유효 대표 이미지 보유)
  + metrics_signal        (stars/points × 0.25, 최대 +10)
  - community_penalty     (−8  if community tier)
  - arxiv_penalty         (−22 if arXiv only)
  - missing_url_penalty   (−40 if URL 없음)
))

cluster_size_bonus = min((항목 수 - 1) × 5, 20)  # 트렌딩 신호
final_score = min(100, editorial_score + cluster_size_bonus)
```

### 토픽 분류 우선순위

```
1. research  ← arXiv URL 또는 "paper/benchmark/dataset"
2. tooling   ← GitHub 소스, 또는 "open source/weights/quantiz/gguf/vllm/lora/ollama"
3. product   ← official 소스 + "launch/announce/model/api"
4. industry  ← mainstream 소스 + 위 키워드
5. policy    ← "regulation/safety/copyright/court"
6. industry  ← 기본값
```

### 섹션 선정 정책 (`max_sections: 10`, `target_sections: 10`)

1차 선정은 아래 토픽 할당량과 소스 캡을 엄격하게 적용합니다.
선택 섹션이 `target_sections`보다 적으면 2차 **image-aware backfill**을 실행해 원본 대표 이미지가 있는 고품질 후보를 우선 보강합니다.

| 토픽 | 최대 섹션 수 |
|------|------------|
| product | 4 |
| tooling | 4 |
| research | 1 |
| industry | 1 |
| policy | 1 |

Backfill 단계에서 유지/완화되는 기준:

| 기준 | 동작 |
|------|------|
| 최소 점수 | `backfill_min_section_score: 35` 유지 |
| 이미지 | 대표 이미지 후보를 우선하되, 없으면 생성형 SVG 카드로 대체 |
| 토픽 할당량 | 부족분 보강 시 완화 |
| 커뮤니티 섹션 | 커뮤니티 단독/우세 후보만 cap 소비, backfill에서는 최대 2개까지 완화 |
| 동일 소스 반복 | 최대 5개까지 완화 |
| arXiv-only | 최대 1개 hard cap 유지 |

> `community` tier가 포함되어도 TechCrunch/The Verge/공식 GitHub처럼 mainstream·official·developer_signal 출처로 함께 확인된 클러스터는 community cap을 소비하지 않습니다. 이 cap은 Reddit/HN 단독 후보가 메인 섹션을 과도하게 차지하지 못하게 하는 용도입니다.

---

## ⚡ 빠른 시작

### 사전 요구사항

- Python 3.11+
- PostgreSQL 16+

### 1. 설치

```bash
git clone https://github.com/coreline-ai/html-news-creator.git
cd html-news-creator

# 의존성 설치
pip install -r requirements.txt
```

### 2. 환경 설정

```bash
cp .env.example .env
```

`.env` 최소 필수 설정:

```env
DATABASE_URL=postgresql+asyncpg://user:pass@localhost:5432/ai_trend
OPENAI_API_KEY=local-proxy
OPENAI_BASE_URL=http://127.0.0.1:4317/openai/v1
OPENAI_MODEL=gpt-5.5
OPENAI_EMBEDDING_MODEL=text-embedding-3-small
TIMEZONE=Asia/Seoul
```

### 3. DB 초기화

```bash
# Docker로 PostgreSQL 실행
docker compose up -d postgres

# 마이그레이션
psql "$DATABASE_URL" -f migrations/001_initial.sql
```

### 4. 실행

```bash
# 오늘자 전체 파이프라인
PYTHONPATH=. python scripts/run_daily.py --mode full

# 특정 날짜
PYTHONPATH=. python scripts/run_daily.py --date 2026-04-30 --mode full

# 특정 단계만 (generate → render)
PYTHONPATH=. python scripts/run_daily.py --date 2026-04-30 --from-step generate --to-step render

# 드라이런 (DB 쓰기 없음)
PYTHONPATH=. python scripts/run_daily.py --mode full --dry-run
```

---

## 🛠️ CLI 레퍼런스

```
Usage: run_daily.py [OPTIONS]

Options:
  --date TEXT         실행 날짜 (YYYY-MM-DD, 기본값: 오늘)
  --mode TEXT         full | rss-only | dry-run  [default: full]
  --from-step TEXT    시작 단계 (collect/extract/classify/cluster/verify/
                      image_analyze/generate/render/publish/notify)
  --to-step TEXT      종료 단계
  --dry-run           DB 저장·배포 없이 시뮬레이션
  --policy-path TEXT  ad-hoc 정책 yaml 경로 (기본 yaml 미수정)
  --policy-override-json TEXT  per-run 정책 deep-merge JSON
  --output-theme TEXT light | dark | newsroom-white
```

> CLI에는 `--source-types` 옵션이 없습니다. 소스 타입 제한은 현재 웹앱/API 실행 시 per-run 정책 오버라이드(`__source_filter`)로 전달됩니다. 순수 CLI에서 특정 소스만 돌릴 때는 별도 정책 파일 또는 코드 레벨 실행 래퍼를 사용하세요.

PDF 변환은 생성된 HTML을 기준으로 별도 실행할 수 있습니다.

```bash
python scripts/export_pdf.py --date 2026-05-01
# → public/news/2026-05-01-trend.pdf
```

브라우저 런타임이 없는 첫 환경에서는 한 번만 Chromium을 설치하세요.

```bash
python -m playwright install chromium
```

웹앱에서는 검토 화면(`/reports/YYYY-MM-DD`)의 **PDF** 버튼이
`GET /api/reports/YYYY-MM-DD/pdf`를 호출합니다. 새로 추가한 PDF 라우트가
404 또는 “사이트에서 사용할 수 없는 파일”로 보이면, 실행 중인 FastAPI 서버가
이전 코드일 가능성이 높으므로 서버를 재시작한 뒤 `http://127.0.0.1:8000`에서
다시 확인하세요.

---

## 🗄️ 데이터 모델

```
Source          ─┐
                 ├─▶ RawItem ──▶ ExtractedContent
ClusterItem ◀───┘         └───▶ AnalysisResult
    │
    ▼
 Cluster ──▶ ReportSection ──▶ Report
    │                │
    └─▶ Verification └─▶ ImageAnalysis
```

**핵심 테이블 14개:** `Source` · `RawItem` · `ExtractedContent` · `MediaAsset` · `AnalysisResult` · `Cluster` · `ClusterItem` · `Verification` · `ImageAnalysis` · `Report` · `ReportSection` · `ReportArtifact` · `JobRun` · `JobLog`

---

## 🎨 출력 결과

생성되는 HTML 리포트 특징:

- **파일명**: `public/news/YYYY-MM-DD-trend.html`
- **PDF 내보내기**: `public/news/YYYY-MM-DD-trend.pdf` (Playwright/Chromium 기반 HTML 그대로 변환)
- **의존성**: 외부 JS 없음 (테마 토글만 인라인)
- **반응형**: 모바일 최적화, max-width 820px
- **테마**: `light → dark → newsroom-white` 3단계 순환, `localStorage` 저장
- **폰트**: [Pretendard](https://github.com/orioncactus/pretendard) (한국어 최적화)
- **섹션 구조**: 제목 → 팩트 요약 → 이미지 → 소셜 시그널 → 출처 목록 → 시사점

```
┌──────────────────────────────────────────┐
│  🔥 AI 트렌드 핵심 요약 (2026-04-30)     │
│  [요약 블록]  [통계: 수집 92건 / 10클러스터] │
├──────────────────────────────────────────┤
│  1. Codex 알파 갱신                       │
│  [팩트 요약] [GitHub OG 이미지]           │
│  [소셜 신호] [출처: openai/codex 🔗]     │
│  [시사점]                                 │
├──────────────────────────────────────────┤
│  2. GPT-5.5 단서     ...                  │
└──────────────────────────────────────────┘
```

### 📸 실제 출력 예시 (2026-04-30)

![AI 트렌드 리포트 2026-04-30](docs/screenshot-2026-04-30.png)

---

## 🎨 디자인 시스템

추가 개발될 운영/관리자/대시보드 웹앱용 디자인 시스템을 [`docs/design/`](docs/design/)에 정의했습니다. shadcn/ui new-york 스타일을 OKLCH 모노크롬으로 운영하는 컨벤션을 베이스로, 고밀도 워크스페이스 UI를 만드는 기준입니다.

> 현재 생성되는 정적 HTML 리포트(`templates/report_newsstream.html.j2`, `public/news/*.html`)의 스타일 가이드는 아닙니다. HTML 리포트는 기존 `light → dark → newsroom-white` 템플릿 스타일을 유지하며, 별도 요청이 있을 때만 디자인 시스템 마이그레이션을 진행합니다.

| 파일 | 다루는 것 |
|------|----------|
| [`README.md`](docs/design/README.md) | 인덱스 + 자동화 개발 사용법 |
| [`01-philosophy.md`](docs/design/01-philosophy.md) | 디자인 DNA, 5원칙, 거부 패턴 |
| [`02-tokens.md`](docs/design/02-tokens.md) | 컬러·radius·shadow·spacing 토큰 명세 |
| [`03-typography.md`](docs/design/03-typography.md) | Pretendard 8단계 type scale |
| [`04-components.md`](docs/design/04-components.md) | Button/Card/Input/Badge 등 12개 컴포넌트 |
| [`05-layout-patterns.md`](docs/design/05-layout-patterns.md) | 워크스페이스 셸 + 반응형, 리포트 구조 참고 |
| [`06-automation-spec.md`](docs/design/06-automation-spec.md) | LLM 코드젠용 기계 가독 명세 |
| [`tokens.css`](docs/design/tokens.css) | 즉시 import 가능한 CSS 변수 |
| [`tokens.json`](docs/design/tokens.json) | W3C design-tokens 포맷 |

**적용 표면**

- **적용 대상**: 운영/관리자/대시보드 웹앱 — 사이드바 240 + 메인 + 컨텍스트 패널, 36~44px 행 밀도
- **비적용 대상**: 현재 정적 HTML 리포트 — 기존 템플릿 스타일 유지

---

## 🖥️ Coreline News Studio 웹앱

CLI(`scripts/run_daily.py`)와 yaml 편집을 반복하는 운영 흐름을 대체하기 위한 단일 사용자 GUI입니다. React 19 + Vite SPA(`ui/`)와 FastAPI(`app/admin/api.py`)로 구성되며, 옵션 변경 → 라이브 미리보기 → Run 상태 추적 → 섹션 검토 → Netlify 발행을 한 흐름에서 처리합니다.

### 시작

```bash
make ui-build && make serve     # http://localhost:8000 (운영)
cd ui && npm run dev            # http://localhost:5173 (개발 HMR, 별도 uvicorn 8000 필요)
```

### 화면 구성

| 이름 | URL | 역할 |
|------|-----|------|
| 대시보드 | `/` | 오늘 카드 · Quick actions · 최근 실행/JobRun 테이블 |
| 리포트 목록 | `/reports` | 생성된 날짜별 리포트 목록과 검토 진입 |
| 신규 리포트 | `/reports/new` | 5그룹 옵션 + 라이브 미리보기 + Run 실행 |
| 검토 | `/reports/:date` | 섹션 reorder · edit · regenerate · PDF 다운로드 · 재렌더 · Publish (Live 모드는 발행된 HTML iframe) |
| 소스 | `/sources` | 37개 소스 토글 · 신규 소스 추가 · registry yaml 반영 |
| 정책 | `/policy` | 점수·할당량·선정 정책 런타임 오버라이드 + `[Persist to yaml]` |
| 설정 | `/settings` | 앱 테마 · 기본 출력 테마 · 브라우저별 Run 기본값 · 발행 기본값 |

### 주요 API 엔드포인트

| 메서드 | 경로 | 용도 |
|------|------|------|
| POST | `/api/runs` | 백그라운드 파이프라인 실행 (옵션 + 정책 오버라이드 전달) |
| GET | `/api/runs` | 메모리 실행 + DB JobRun 이력 병합 조회 |
| GET | `/api/runs/{id}` | 단일 Run 상태 조회 (`trackable` 포함) |
| GET | `/api/runs/{id}/stream` | SSE 진행률 (`{step, progress, message, raw_line}`) + history replay + terminal done |
| POST | `/api/preview` | 옵션만 적용한 in-memory 미리보기 (DB 쓰기 없음) |
| GET | `/api/reports/{date}` | 리포트·섹션·통계 조회 |
| PATCH | `/api/sections/{id}` | 단일 섹션 제목/요약/이미지 등 편집 |
| POST | `/api/sections/{id}/regenerate` | 단일 섹션 LLM 재생성 |
| POST | `/api/reports/{date}/render` | DB 기준 fresh 재렌더 (disabled 섹션 제외, 배포 없음) |
| GET | `/api/reports/{date}/html` | 발행된 HTML 원본 (검토 Live 모드용) |
| GET | `/api/reports/{date}/pdf` | 현재 HTML을 Playwright PDF로 다운로드 (`fresh=true`면 DB 재렌더) |
| POST | `/api/reports/{date}/publish` | 재렌더 후 Netlify 배포 트리거 |
| POST | `/api/sources` | 신규 소스 yaml registry에 atomic append |
| PUT | `/api/sources/{name}` | 소스 활성화/메타데이터 업데이트 |
| PUT | `/api/policy` | 런타임 오버라이드 저장 (메모리, 휘발) |
| POST | `/api/policy/persist` | 런타임 오버라이드를 `editorial_policy.yaml`에 영구 저장 (`*.yaml.bak` 자동 백업) |

> 정책 우선순위: **per-run options > runtime override (`PUT /api/policy`) > yaml**. 오른쪽으로 갈수록 약하며, `/policy`의 `[Persist to yaml]` 버튼이 메모리 오버라이드를 yaml에 머지합니다.

### 단축키 / UX

- `⌘K` / `Ctrl+K` — 명령 팔레트, `R` — 마지막 옵션 재실행, `P` — 발행 (검토 화면 한정)
- HeaderBar 토글 — 앱 크롬 다크 ↔ 라이트 (`localStorage` 영속)
- 전역 Run 토스트 — 새로고침/탭 이동 후에도 `activeRun`을 복원해 SSE에 재연결, 완료 시 `결과 리포트 보기` CTA 제공
- 검토 화면 PDF 버튼 — 현재 HTML을 Playwright/Chromium으로 A4 PDF 다운로드

### 운영 가드

- LLM 호출 60s 하드 타임아웃 + 스톨 감지, `run_runner` 기본 15분 max-runtime으로 장시간 Run 행 멈춤 차단
- SSE는 history replay와 terminal done 합성을 지원해 late subscriber/새로고침 후 진행률 복구
- Run 종료 시 JobRun을 best-effort로 저장해 Dashboard 최근 실행 표와 `/api/runs` 이력에 반영
- 리포트 HTML 응답에 `Cache-Control: no-store`로 stale chunk 방지
- 정책/소스 yaml 저장은 임시파일 → atomic rename + `.bak` 자동 생성

상세 가이드: [`docs/news-studio-usage.md`](docs/news-studio-usage.md) · 디자인 토큰/컴포넌트: [`docs/design/`](docs/design/)

---

## 🔧 개발

```bash
# 단위 테스트
make test
# 또는
PYTHONPATH=. uv run pytest tests/unit/ -v --tb=short

# 린트
make lint
# 또는
ruff check app/ scripts/ tests/
```

### 소스 추가

`data/sources_registry.yaml`에 항목 추가:

```yaml
- name: My AI Blog
  source_type: rss
  url: https://example.com/feed.xml
  trust_level: trusted_media
  source_tier: mainstream
  category: mainstream_media
  priority: 75
  max_items: 10
```

### 편집 정책 조정

`data/editorial_policy.yaml`에서 점수·할당량 튜닝:

```yaml
report_selection:
  max_sections: 10          # 최대 섹션 수
  target_sections: 10       # backfill 목표 섹션 수
  min_section_score: 35     # 최소 점수 커트라인
  backfill_require_image: false  # 이미지 없는 후보도 유지, 생성형 SVG 카드로 대체
  backfill_relax_topic_quotas: true

section_quotas:
  tooling: 4                # 개발도구 섹션 최대 수
  product: 4
```

---

## 🚀 배포 (GitHub Actions)

### 자동 실행

```yaml
# .github/workflows/daily-report.yml
# 매일 22:00 UTC (07:00 KST) 자동 실행
on:
  schedule:
    - cron: "0 22 * * *"
  workflow_dispatch:        # 수동 트리거 지원
```

### 필요 Secrets

| Secret | 설명 |
|--------|------|
| `DATABASE_URL` | PostgreSQL 연결 문자열 |
| `OPENAI_API_KEY` | OpenAI 또는 호환 프록시 키 |
| `NETLIFY_AUTH_TOKEN` | Netlify 배포 토큰 |
| `NETLIFY_SITE_ID` | 배포 대상 사이트 ID |
| `SLACK_WEBHOOK_URL` | 완료 알림 (선택) |
| `GITHUB_TOKEN` | GitHub API 수집용 (선택, 없으면 익명) |

---

## 🧰 기술 스택

| 분류 | 라이브러리 |
|------|-----------|
| **웹 프레임워크** | FastAPI 0.115, SQLAlchemy 2.0 (async) |
| **데이터베이스** | PostgreSQL 16, asyncpg, Alembic |
| **LLM / 임베딩** | openai 1.55 (OpenAI-compatible), tiktoken |
| **클러스터링** | scikit-learn 1.5, numpy 1.26 (HDBSCAN) |
| **수집** | feedparser, PyGithub, arxiv, httpx 0.27, aiohttp 3.10 |
| **본문 추출** | trafilatura 1.12, crawl4ai 0.4, playwright 1.49 |
| **렌더링** | Jinja2 3.1, bleach |
| **스토리지** | boto3 (S3/MinIO), Pillow |
| **모니터링** | structlog, rich |
| **테스트** | pytest 8.3, pytest-asyncio, respx |

---

## 📄 라이선스

[MIT License](LICENSE) © 2026 Coreline AI

---

<div align="center">

Made with ❤️ by [Coreline AI](https://github.com/coreline-ai)

</div>
