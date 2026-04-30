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

매일 새벽 **50여 개 소스**에서 AI 트렌드를 수집·분류·클러스터링하고,  
편집 정책 기반으로 **개발자 중심 뉴스레터 HTML**을 자동 생성하는 파이프라인입니다.

[데모 →](https://ai-news-5min-kr.netlify.app) · [구조 보기](#-아키텍처) · [빠른 시작](#-빠른-시작)

</div>

---

## ✨ 주요 기능

| 기능 | 설명 |
|------|------|
| 🌐 **멀티 소스 수집** | RSS, GitHub Release, arXiv, Hacker News, Reddit, YouTube 등 50+ 소스 |
| 🤖 **LLM 분류·요약** | AI 관련성 판별, 한국어 팩트 요약, 시사점 생성 |
| 📐 **임베딩 클러스터링** | HDBSCAN으로 동일 주제 기사를 자동 그룹화 |
| 📰 **편집 정책 기반 선정** | 소스 등급·클러스터 크기·토픽 할당량으로 투명한 섹션 선정 |
| 🖼️ **스마트 이미지 선택** | 기자 초상·로고·UI 요소 자동 제외, 기사 대표 이미지 추출 |
| 🌙 **다크/라이트 테마** | Pretendard 폰트, CSS 변수 기반 반응형 HTML |
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
│  50+ 소스        Trafilatura    LLM 판별         HDBSCAN           │
│  RSS/GitHub     본문 추출      AI 관련성         임베딩 클러스터   │
│  arXiv/HN                      점수화                              │
│                                                                     │
│  ⑤ verify   →  ⑥ generate  →  ⑦ render   →  ⑧ publish          │
│     │               │              │               │               │
│  교차 검증       LLM 섹션      Jinja2 HTML     Netlify/S3          │
│  신뢰 점수       생성·요약     다크모드 지원    + Slack 알림       │
└─────────────────────────────────────────────────────────────────────┘
```

### 파이프라인 단계별 상세

```
collect   │ 소스별 컬렉터(RSS/GitHub/arXiv/HN) → DB 저장 (중복 스킵)
extract   │ Trafilatura·Crawl4AI로 본문·OG 이미지·메타데이터 추출
classify  │ LLM으로 AI 관련성 점수(0–1) 산출, 비관련 기사 필터
cluster   │ text-embedding-3-small → HDBSCAN → 주제 클러스터 형성
verify    │ 공식 도메인·GitHub·arXiv와 교차 검증, trust_score 산출
generate  │ 클러스터별 LLM 섹션 생성 (제목·요약·시사점·소스 목록)
render    │ Jinja2 템플릿 → 반응형 HTML 리포트
publish   │ public/news/ 저장 + Netlify 배포
notify    │ Slack Webhook 발송
```

---

## 📁 디렉토리 구조

```
html-news-creator/
├── app/
│   ├── collectors/          # 소스별 수집기
│   │   ├── orchestrator.py  # 컬렉터 통합 실행
│   │   ├── rss_collector.py # RSS / YouTube
│   │   ├── github_collector.py
│   │   ├── arxiv_collector.py
│   │   ├── hackernews_collector.py
│   │   └── website_collector.py
│   ├── editorial/           # 편집 정책 엔진
│   │   ├── policy.py        # YAML 정책 로더
│   │   ├── ranker.py        # 아이템 점수 산출 (순수 함수)
│   │   └── selection.py     # 클러스터 선정·요약
│   ├── extractors/          # 본문 추출기 (Trafilatura 우선)
│   ├── generation/          # LLM 섹션·제목·임베딩 생성
│   ├── models/              # SQLAlchemy ORM (13개 테이블)
│   ├── pipeline/            # 날짜 윈도우 (KST + US 시간대 슬랙)
│   ├── rendering/           # Jinja2 렌더러
│   ├── utils/
│   │   ├── source_images.py # 이미지 URL 검증·필터
│   │   └── generated_images.py # SVG 폴백 생성
│   └── verification/        # 소스 교차 검증
│
├── data/
│   ├── sources_registry.yaml   # 50+ 소스 설정
│   ├── editorial_policy.yaml   # 점수 공식·할당량·티어
│   └── official_domains.yaml   # 공식 도메인 화이트리스트
│
├── templates/
│   ├── report_newsstream.html.j2  # 메인 리포트 템플릿
│   └── section_card.html.j2
│
├── tests/unit/              # 130+ 단위 테스트
├── scripts/
│   └── run_daily.py         # 파이프라인 진입점 (CLI)
├── .github/workflows/
│   ├── daily-report.yml     # 매일 22:00 UTC 자동 실행
│   └── ci.yml               # 푸시/PR 단위 테스트
├── migrations/              # Alembic DB 마이그레이션
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
| ⚪ **community** | Reddit r/MachineLearning, r/LocalLLaMA, Hacker News AI | −4 |

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

### 섹션 할당량 (`max_sections: 10`)

| 토픽 | 최대 섹션 수 |
|------|------------|
| product | 4 |
| tooling | 4 |
| research | 1 |
| industry | 1 |
| policy | 1 |

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
OPENAI_API_KEY=sk-...
OPENAI_MODEL=gpt-4o
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
  --mode TEXT         full | rss-only  [default: full]
  --from-step TEXT    시작 단계 (collect/extract/classify/cluster/verify/
                      image_analyze/generate/render/publish/notify)
  --to-step TEXT      종료 단계
  --dry-run           DB 저장·배포 없이 시뮬레이션
  --source-types TEXT 특정 소스 타입만 수집 (comma-separated)
```

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

**핵심 테이블 13개:** `Source` · `RawItem` · `ExtractedContent` · `MediaAsset` · `AnalysisResult` · `Cluster` · `ClusterItem` · `Verification` · `ImageAnalysis` · `Report` · `ReportSection` · `ReportArtifact` · `JobRun`

---

## 🎨 출력 결과

생성되는 HTML 리포트 특징:

- **파일명**: `public/news/YYYY-MM-DD-trend.html`
- **의존성**: 외부 JS 없음 (테마 토글만 인라인)
- **반응형**: 모바일 최적화, max-width 820px
- **다크모드**: CSS 변수 + `localStorage` 테마 저장
- **폰트**: [Pretendard](https://github.com/orioncactus/pretendard) (한국어 최적화)
- **섹션 구조**: 제목 → 팩트 요약 → 이미지 → 소셜 시그널 → 출처 목록 → 시사점

```
┌──────────────────────────────────────────┐
│  🔥 AI 트렌드 핵심 요약 (2026-04-30)     │
│  [요약 블록]  [통계: 수집 92건 / 18클러스터] │
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
  min_section_score: 35     # 최소 점수 커트라인

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
| **LLM / 임베딩** | openai 1.37 (OpenAI-compatible), tiktoken |
| **클러스터링** | scikit-learn 1.5, numpy 1.26 (HDBSCAN) |
| **수집** | feedparser, PyGithub, arxiv, httpx, aiohttp |
| **본문 추출** | trafilatura 1.12, crawl4ai, playwright |
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
