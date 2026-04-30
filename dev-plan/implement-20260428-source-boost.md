# implement-20260428-source-boost.md

작성 일시: `2026-04-28 KST`  
목적: 소스 다양성 보강, 소셜/포털/동영상 시그널 추가, 이미지 품질 개선

---

## 1. 현황 분석 (직접 검증 결과)

### 1.1 오늘 파이프라인 수집 현황 (2026-04-28)

| 소스 | 파이프라인 결과 | RSS 직접 테스트 | 원인 |
|------|----------------|----------------|------|
| arXiv 4개 | **61건** | — | 정상 (과다) |
| Hugging Face Blog | 1건 | 정상 | 정상 |
| GitHub anthropics | 2건 | — | 정상 |
| TechCrunch AI | **0건** | ✅ 20건 | ⚠️ 파이프라인 날짜 필터 버그 |
| The Verge AI | **0건** | ✅ 10건 | ⚠️ 파이프라인 날짜 필터 버그 |
| The Decoder | **0건** | ✅ 10건 | ⚠️ 파이프라인 날짜 필터 버그 |
| MIT Tech Review | **0건** | ✅ 10건 | ⚠️ 파이프라인 날짜 필터 버그 |
| OpenAI/DeepMind/Meta/MS | 0건 | 0건 | 오늘 발행 없음 (정상) |

### 1.2 신규 소스 검증 — RSS/API

| 소스 | 건수 | 이미지 | 비고 |
|------|------|--------|------|
| Google AI Blog | ✅ 20건 | **있음** | RSS에 media:thumbnail 포함 |
| NVIDIA AI Blog | ✅ 18건 | **있음** | RSS에 media:thumbnail 포함 |
| AWS ML Blog | ✅ 20건 | 없음(본문) | 공식 AWS |
| Ahead of AI | ✅ 20건 | 없음 | Sebastian Raschka 뉴스레터 |
| AI타임스(한국) | ✅ 50건 | 없음(본문) | 한국 AI 전문지 |
| The Batch | ❌ 404 | — | URL 폐기 |

### 1.3 소셜/커뮤니티 소스 검증

| 소스 | 방식 | 건수 | 이미지 | 비고 |
|------|------|------|--------|------|
| Reddit r/artificial | RSS | ✅ 25건 | **있음** (썸네일) | |
| Reddit r/LocalLLaMA | RSS | ✅ 25건 | **있음** (썸네일) | |
| Hacker News API | REST | ✅ 500건 필터 | 없음→원문추출 | |
| Nitter @AnthropicAI | RSS 미러 | ✅ 20건 | 없음 | 불안정 |
| Nitter @OpenAI | RSS 미러 | ✅ 20건 | 없음 | 불안정 |
| X/Twitter 직접 | API | — | — | ❌ $100/월 |

### 1.4 NAVER 검증 결과

| 방법 | 결과 | 비고 |
|------|------|------|
| NAVER RSS 직접 | ❌ 모두 404/302 | RSS 서비스 종료 |
| NAVER IT/과학 페이지 | ✅ 크롤 가능 (200, 275KB) | AI 키워드 95회, 동적 렌더링 필요 |
| **NAVER 뉴스 검색 API** | ✅ **공식 무료 API** | 25,000건/일, API Key 필요 (무료 발급) |

→ **결론**: NAVER는 공식 검색 API로 접근. RSS 없음.

### 1.5 Yahoo 검증 결과

| 방법 | 결과 | 이미지 | 비고 |
|------|------|--------|------|
| Yahoo Finance RSS | ✅ 50건 (AI관련 16건) | **있음** (zenfs/yimg CDN) | 투자/비즈니스 관점 AI 뉴스 |
| Yahoo News RSS | ✅ 50건 (AI관련 18건) | 일부 있음 | 일반 뉴스 혼재 |
| Yahoo Finance AI 전용 | ✅ 20건 | 있음 | `?s=AI&region=US` |

→ **결론**: Yahoo Finance RSS 직접 활용 가능. AI 키워드 필터링 필요.

### 1.6 YouTube 검증 결과

| 방법 | 결과 | 이미지 | 비고 |
|------|------|--------|------|
| YouTube 채널 RSS | ✅ 채널당 15건 | **항상 있음** (hqdefault.jpg) | API Key 불필요 |
| YouTube Data API v3 | ✅ 검색+조회수 정렬 | **항상 있음** | 무료 10,000 units/일, Key 필요 |
| yt-dlp | ✅ 비공식, 조회수 포함 | **항상 있음** | API Key 불필요, 약관 회색지대 |
| Google DeepMind YT | ✅ 15건 | 있음 | 채널 RSS 동작 |
| Hugging Face YT | ✅ 15건 | 있음 | 채널 RSS 동작 |
| Lex Fridman | ✅ 15건 | 있음 | 채널 RSS 동작 |
| Anthropic YT | ❌ 0건 | — | 채널 ID 불일치 |
| OpenAI YT | ❌ 0건 | — | 채널 ID 불일치 |

---

## 2. 개발 목표

### 2.1 수집 목표

| 구분 | 현재 | 목표 |
|------|------|------|
| arXiv 비율 | 95% | < 30% |
| official/mainstream | 3건 | 30건 이상 |
| 소셜/커뮤니티 | 0건 | 20건 이상 |
| 포털(NAVER/Yahoo) | 0건 | 20건 이상 |
| 유튜브 | 0건 | 10건 이상 |
| 이미지 있는 소스 | 1건(HF) | Google/NVIDIA/Reddit/Yahoo/YouTube 포함 |

### 2.2 섹션 구성 목표

```
[현재]                          [목표]
섹션 1: arXiv 논문              섹션 1: 공식 발표 (OpenAI/Anthropic/Google)
섹션 2: arXiv 논문              섹션 2: 뉴스 클러스터 (TechCrunch/Verge/NAVER)
섹션 3: arXiv 논문              섹션 3: 커뮤니티 반응 (Reddit/HN 핫 토픽)
섹션 4: arXiv 논문              섹션 4: 유튜브 주목 영상
                                섹션 5: arXiv 연구 요약 (최대 1개)
```

---

## 3. 범위

**In scope (현재 기본 registry 정리 기준):**
- Phase 0: TechCrunch/The Verge 0건 날짜 필터 버그 수정
- Phase 1: API Key 불필요 RSS 소스 추가 (Google AI, NVIDIA, AWS, AI타임스 등)
- Phase 2: API Key 불필요 Reddit RSS 소셜 시그널
- Phase 3: API Key 불필요 Hacker News 수집/registry
- Phase 5: Yahoo Finance RSS 수집기 (AI 필터링)
- Phase 6 일부: YouTube **채널 RSS만** (API Key 불필요)
- Phase 8: 이미지 선택 로직 통합 정비

**Out of scope / 후속:**
- NAVER 뉴스 검색 API: API Key 필요이므로 기본 registry에서 제외
- YouTube Data API v3 검색: API Key 필요이므로 기본 registry에서 제외; 채널 RSS는 유지 가능
- X/Twitter 직접 API: 유료/API Key 필요이므로 제외
- Nitter(X 미러): API Key는 없지만 불안정하므로 기본 registry에서 제외하고 후속 검토
- yt-dlp (약관 회색지대)
- 실시간 스트리밍
- 전체 UI 리디자인

---

## 4. Phase 의존성

```
Phase 0 (버그 수정) ← 최우선, 독립
    │
    ├── Phase 1 (RSS 추가)             ← 독립, API Key 불필요
    ├── Phase 2 (Reddit RSS)           ← 독립, API Key 불필요
    ├── Phase 3 (HN)                   ← 독립, API Key 불필요
    ├── Phase 5 (Yahoo Finance RSS)    ← 독립, API Key 불필요
    ├── Phase 6a (YouTube 채널 RSS)    ← 독립, API Key 불필요
    └── Phase 8 (이미지 통합)           ← 모든 keyless Phase 완료 후

후속/제외:
    ├── Phase 4 (NAVER API)            ← API Key 필요, 기본 registry 제외
    ├── Phase 6b (YouTube Data API)    ← API Key 필요, 기본 registry 제외
    └── Phase 7 (Nitter)               ← 불안정, 기본 registry 제외
```

---

## 5. 구현 페이즈

---

### Phase 0: TechCrunch/The Verge 0건 날짜 필터 버그 수정
> RSS 자체는 정상인데 파이프라인에서 0건인 원인 파악 및 수정
> **최우선 처리 — 고치면 즉시 +40건**

#### 의심 원인
- `_date_window_utc()`가 UTC 기준으로 날짜 경계를 너무 좁게 설정
- 로컬 `Asia/Seoul` 자정 → UTC 변환 시 이전날 15:00 UTC가 되어 필터 탈락

#### Tasks
- [ ] `app/collectors/rss_collector.py` 날짜 필터 전후 디버그 로그 추가
- [ ] `app/collectors/orchestrator.py`의 `_date_window_utc()` 수정:
  ```python
  # 현재: 로컬 당일 자정 UTC 기준
  # 수정: 6시간 여유 추가 (전날 18:00 KST ~ 익일 06:00 KST)
  date_from = local_midnight - timedelta(hours=6)
  date_to = local_midnight + timedelta(days=1, hours=6)
  ```
- [ ] `published_parsed`가 None인 항목 → 오늘 날짜로 간주해 포함
- [ ] dry_run으로 TechCrunch 5건 이상 수집 확인

#### Success Criteria
- `"source": "TechCrunch AI", "count": N` (N ≥ 5) 로그 출력
- `"source": "The Verge AI", "count": N` (N ≥ 3) 로그 출력

---

### Phase 1: 신규 RSS 소스 추가
> `data/sources_registry.yaml`에 검증된 소스 추가
> Dependencies: Phase 0 완료 후

#### 추가 내용 (`data/sources_registry.yaml`)

```yaml
- name: Google AI Blog
  source_type: rss
  url: https://blog.google/technology/ai/rss/
  trust_level: official
  source_tier: official
  category: official
  priority: 95
  max_items: 15

- name: NVIDIA AI Blog
  source_type: rss
  url: https://blogs.nvidia.com/blog/category/deep-learning/feed/
  trust_level: official
  source_tier: official
  category: official
  priority: 85
  max_items: 10

- name: AWS Machine Learning Blog
  source_type: rss
  url: https://aws.amazon.com/blogs/machine-learning/feed/
  trust_level: official
  source_tier: official
  category: official
  priority: 80
  max_items: 10

- name: Ahead of AI
  source_type: rss
  url: https://magazine.sebastianraschka.com/feed
  trust_level: trusted_media
  source_tier: mainstream
  category: mainstream_media
  priority: 75
  max_items: 8

- name: AI타임스
  source_type: rss
  url: https://www.aitimes.com/rss/allArticle.xml
  language: ko
  trust_level: trusted_media
  source_tier: mainstream
  category: mainstream_media
  priority: 70
  max_items: 15
```

#### Tasks
- [x] `data/sources_registry.yaml` 항목 추가: Google AI Blog, NVIDIA AI Blog, AWS Machine Learning Blog, AI타임스
- [x] The Batch 항목 제거/미등록 유지 (404 폐기)
- [x] YAML 문법 검증: `python3 -c "import yaml; yaml.safe_load(open('data/sources_registry.yaml'))"`
- [ ] Google AI Blog, NVIDIA Blog에서 `media:thumbnail` → `og_image_url` 추출 동작 확인
- [ ] 후속 검토: Ahead of AI는 현재 기본 registry 미등록

---

### Phase 2: Reddit 소셜 시그널
> r/artificial, r/LocalLLaMA — AI 커뮤니티 핫 게시물 수집
> Dependencies: 독립

#### 특성
- **RSS로 접근 가능**, API Key 불필요
- 링크 게시물: `media:thumbnail`에 원문 OG 이미지를 Reddit이 제공
- 이미지 포함 게시물 비율: r/artificial 약 60%, r/LocalLLaMA 약 40%

#### Tasks
- [x] `data/sources_registry.yaml`에 `Reddit LocalLLaMA` 추가
- [x] `data/sources_registry.yaml`에 `Reddit MachineLearning` 추가
- [ ] 후속 검토: `Reddit r/artificial`은 현재 기본 registry 미등록
- [ ] `app/collectors/rss_collector.py`에서 `media_thumbnail` → `raw_json['image_url']` 저장:
  ```python
  media_thumb = entry.get("media_thumbnail", [])
  if media_thumb:
      raw_json["image_url"] = media_thumb[0].get("url", "")
  ```
- [ ] User-Agent 설정: `"html-news-creator/1.0"` (Reddit은 봇 차단 있음)
- [ ] `data/editorial_policy.yaml`: `community` tier `eligible_for_main: false` 유지

---

### Phase 3: Hacker News API 수집기
> HN 상위 스토리 중 AI 관련 필터링, 인기도(score) 기반
> Dependencies: 독립, 신규 `app/collectors/hn_collector.py` 파일 생성

#### HN API 구조
```
GET https://hacker-news.firebaseio.com/v0/topstories.json → 상위 500개 ID
GET https://hacker-news.firebaseio.com/v0/item/{id}.json → 스토리 상세
  반환: title, url, score, descendants(댓글), by(작성자), time
```

#### AI 키워드 필터
```python
AI_KEYWORDS = {
    "ai", "llm", "gpt", "claude", "gemini", "mistral", "llama",
    "neural", "machine learning", "deep learning", "transformer",
    "openai", "anthropic", "deepmind", "hugging face",
    "inference", "training", "fine-tuning", "rag", "agent"
}
```

#### Tasks
- [ ] `app/collectors/hn_collector.py` 신규 생성:
  ```python
  class HNCollector:
      async def collect(self, run_date, max_items=15, min_score=50):
          # topstories 500개 ID → 상위 100개 병렬 fetch
          # AI 키워드 필터링 → score >= min_score
          # RawItem 변환 (source_type="hn")
  ```
- [x] `data/sources_registry.yaml`에 `Hacker News AI` 추가 (`source_type: website`, `collector_type: hackernews`)
- [ ] 참고: 원안의 `source_type: hn` 대신 현재 registry는 특수 website collector 메타데이터 사용
- [ ] 원안 예시:
  ```yaml
  - name: Hacker News AI
    source_type: hn
    trust_level: community
    source_tier: community
    category: social_signal
    priority: 65
    max_items: 15
    min_score: 50
  ```
- [ ] `app/collectors/orchestrator.py`에 `hn` 타입 → `HNCollector` 매핑
- [ ] OG 이미지: `run_extract`에서 원문 URL fetch 시 자동 추출됨

---

### Phase 4: NAVER 뉴스 검색 API 수집기
> 한국어 AI 뉴스 공식 API — 무료, 하루 25,000건
> Dependencies: 독립, 신규 `app/collectors/naver_collector.py`, **API Key 발급 필요**

#### API 스펙
```
GET https://openapi.naver.com/v1/search/news.json
Headers: X-Naver-Client-Id, X-Naver-Client-Secret
Params:
  query: "인공지능 OR AI OR LLM OR ChatGPT OR 생성형AI"
  display: 100 (최대)
  sort: date
응답:
  items[].title, link, description, pubDate
  ※ 이미지 없음 → run_extract에서 원문 URL 크롤해 OG 추출
```

#### 필요 설정
```bash
# .env에 추가
NAVER_CLIENT_ID=xxx
NAVER_CLIENT_SECRET=xxx
# 발급: https://developers.naver.com → 애플리케이션 등록 → 검색 API 선택
```

#### Tasks
- [x] 기본 registry에서 NAVER 뉴스 검색 API 소스 제외(API Key 필요)
- [ ] 후속: `app/config.py`에 `naver_client_id`, `naver_client_secret` 필드 추가
- [ ] 후속: `app/collectors/naver_collector.py` 신규 생성
- [ ] 후속: `data/sources_registry.yaml`에 `NAVER 뉴스 AI` 추가(Key 발급 이후 별도 registry/옵션으로 관리)
- [ ] 후속: `app/collectors/orchestrator.py`에 `naver_news` 타입 매핑
- [ ] 후속: API Key 없을 시 graceful skip (경고 로그만)

#### Success Criteria
- `naver_client_id` 설정 시 AI 관련 한국어 뉴스 최소 20건 수집
- API Key 없으면 skip, 파이프라인 계속 진행

---

### Phase 5: Yahoo Finance RSS 수집기
> AI 투자/비즈니스 관점 뉴스 + 이미지 포함
> Dependencies: 독립

#### 특성
- Yahoo Finance RSS: 50건 중 AI 관련 16~18건 (키워드 필터 후)
- **이미지 있음**: zenfs, yimg CDN 썸네일
- 투자 관점 AI 뉴스: OpenAI 수익, 빅테크 AI 지출, AI 스타트업 투자 등

#### Tasks
- [x] `data/sources_registry.yaml`에 `Yahoo Finance AI` 추가
- [x] `Yahoo Finance AI`에 `ai_filter: true` 설정
- [x] 기본 registry URL은 Yahoo Finance AI 심볼 RSS(`https://finance.yahoo.com/rss/headline?s=AI`) 사용
- [ ] `app/collectors/rss_collector.py`에서 `ai_filter: true` 소스 처리
- [ ] `media:thumbnail` → `raw_json['image_url']` 저장 (Phase 2와 동일 로직)

---

### Phase 6: YouTube 수집기
> AI 관련 영상 — 조회수/최신 순, 썸네일 항상 있음
> Dependencies: 독립. 현재 기본 registry는 API Key 불필요한 채널 RSS만 포함하고, Data API 검색은 후속 제외 항목으로 분리

#### 2가지 수집 방식 (병행 구현)

**방식 A: 채널 RSS (API Key 불필요)**
- 검증 동작: Google DeepMind ✅, Hugging Face ✅, Lex Fridman ✅
- 채널당 최신 15개, 날짜 필터 후 오늘 영상만
- 썸네일: `media:thumbnail` 자동 포함

**방식 B: YouTube Data API v3 (AI 키워드 검색 + 조회수 정렬) — 후속/기본 registry 제외**
- 무료: 10,000 units/일 (검색 1회=100 units)
- `order=viewCount` + `publishedAfter=어제` → 오늘 핫한 AI 영상
- API Key 필요 (Google Cloud Console, 무료 발급)

#### 대상 채널 (방식 A)

| 채널명 | 채널 ID | 특성 |
|--------|---------|------|
| Google DeepMind | UCP7jMXSY2xbc3KCAE0MHQ-A | 공식 연구 영상 |
| Hugging Face | UCHlNU7kIZhRgSbhHvFoy72w | 튜토리얼, 데모 |
| Lex Fridman | UCSHZKyawb77ixDdsGog4iWA | AI 인터뷰 |
| Two Minute Papers | UCbfYPyITQ-7l4upoX8nvctg | 논문 리뷰 |
| Yannic Kilcher | UCZHmQk67mSJgfCCTn7xBfew | 논문 분석 |
| 3Blue1Brown | UCYO_jab_esuFRV4b17AJtAw | ML 교육 |

#### Tasks
- [x] `data/sources_registry.yaml`에 API Key 불필요 YouTube 채널 RSS 등록: Google Cloud Tech YouTube, OpenAI YouTube
- [x] YouTube Data API v3 검색 소스는 API Key 필요 항목으로 기본 registry 제외
- [ ] 후속: `app/collectors/youtube_collector.py` 신규 생성:
  ```python
  class YouTubeCollector:
      RSS_BASE = "https://www.youtube.com/feeds/videos.xml?channel_id={}"
      API_BASE = "https://www.googleapis.com/youtube/v3/search"
      
      async def collect_channels(self, channels, run_date, max_per_channel=3):
          # 채널 RSS → 오늘 발행 영상 필터
          # media:thumbnail → image_url
          # RawItem(source_type="youtube")
      
      async def search_by_keyword(self, query, run_date, max_items=10, order="viewCount"):
          # YouTube Data API v3 검색
          # API Key 없으면 skip
  ```
- [ ] 후속 예시(`YouTube AI Search`는 API Key 필요로 기본 registry 제외):
  ```yaml
  - name: YouTube AI Channels
    source_type: youtube_channel
    trust_level: trusted_media
    source_tier: mainstream
    category: multimedia
    priority: 72
    max_items: 15
    channels:
      - id: UCP7jMXSY2xbc3KCAE0MHQ-A
        name: Google DeepMind
      - id: UCHlNU7kIZhRgSbhHvFoy72w
        name: Hugging Face
      - id: UCbfYPyITQ-7l4upoX8nvctg
        name: Two Minute Papers
      - id: UCZHmQk67mSJgfCCTn7xBfew
        name: Yannic Kilcher
      - id: UCSHZKyawb77ixDdsGog4iWA
        name: Lex Fridman

  - name: YouTube AI Search
    source_type: youtube_search
    trust_level: trusted_media
    source_tier: mainstream
    category: multimedia
    priority: 68
    max_items: 10
    queries:
      - "artificial intelligence 2026"
      - "LLM tutorial"
      - "AI news"
    order: viewCount   # 조회수 순 (또는 date)
    # youtube_api_key는 .env의 YOUTUBE_API_KEY 참조
  ```
- [ ] `app/config.py`에 `youtube_api_key: str = ""` 추가
- [ ] `app/collectors/orchestrator.py`에 `youtube_channel`, `youtube_search` 타입 매핑
- [ ] **섹션 렌더링**: YouTube 아이템은 `sources_json`에 `video_id` 포함 → 템플릿에서 YouTube embed 또는 썸네일+링크로 표시
- [ ] `templates/section_card.html.j2`: YouTube 소스 감지 시 플레이 버튼 오버레이 추가

#### 설정 파일 추가 필요
```bash
# .env에 추가 (선택)
YOUTUBE_API_KEY=AIza...
# 발급: Google Cloud Console → YouTube Data API v3 활성화
```

#### Success Criteria
- Google DeepMind, Hugging Face 채널에서 최신 AI 영상 수집
- 썸네일 이미지 `hqdefault.jpg` 정상 표시
- `youtube_api_key` 없을 시 채널 RSS만 사용 (graceful fallback)

---

### Phase 7: Nitter (X/Twitter 미러) — Optional
> @AnthropicAI, @OpenAI 공식 트윗 수집
> Dependencies: Phase 2 완료 후 구조 재활용

#### 특성
- Nitter 공개 인스턴스: `nitter.net/{handle}/rss`
- @AnthropicAI ✅, @OpenAI ✅ (각 20건), @GoogleDeepMind ❌ (불안정)
- 이미지: 트윗 첨부 이미지 일부 포함
- **불안정**: X의 차단으로 인스턴스 가끔 다운

#### Tasks
- [x] 기본 registry에서 Nitter/X 미러 소스 제외(불안정)
- [ ] 후속 검토: 안정 인스턴스/운영 정책 확정 시 옵션 registry로 추가
- [ ] 후속 검토: `app/collectors/rss_collector.py`에 `fallback_url`, `timeout` 지원 추가
- [ ] 후속 검토: 실패 시 graceful skip (에러 전파 없음)

---

### Phase 8: 이미지 선택 로직 통합 정비
> 소스 유형별 이미지 전략 일원화
> Dependencies: Phase 1~7 완료 후

#### 소스별 이미지 우선순위

| 소스 유형 | 이미지 출처 | 처리 |
|-----------|------------|------|
| 블로그 (HF, Google, NVIDIA) | RSS media:thumbnail / og:image | `raw_json['image_url']` 또는 OG 추출 |
| 뉴스 (TechCrunch, Verge, NAVER) | 기사 og:image | `run_extract`에서 자동 추출 |
| Yahoo Finance | RSS media:thumbnail | `raw_json['image_url']` |
| Reddit | RSS media:thumbnail | `raw_json['image_url']` |
| YouTube | 채널 RSS media:thumbnail | `raw_json['image_url']` (hqdefault.jpg) |
| Nitter | 트윗 첨부 | RSS enclosure |
| HN | 없음 | 원문 URL OG 추출 |
| arXiv | ❌ 사용 안 함 | 생성 SVG 폴백 |

#### Tasks
- [ ] `app/collectors/rss_collector.py`: `media_thumbnail`, `media_content`에서 `image_url` 추출 통일
- [ ] `run_generate`의 이미지 우선순위 확인:
  ```
  1. content_image_urls (블로그 본문) — 비arXiv
  2. raw_json['image_url'] (RSS 썸네일, YouTube 썸네일, Reddit 썸네일)
  3. og_image_url (페이지 OG 태그)
  4. 생성 SVG (arXiv-only 폴백)
  ```
- [ ] `app/utils/source_images.py` 차단 목록 추가:
  - `arxiv.org/static` (arXiv 로고) ← 이미 완료
  - `reddit.com/static` (Reddit UI)
  - `styles.redditmedia.com` (Reddit 광고/UI)
- [ ] `templates/section_card.html.j2`: YouTube 영상 감지 시 썸네일에 플레이 버튼 오버레이

---

## 6. API Key 관리

| 서비스 | 필요 여부 | 무료 한도 | 발급 방법 |
|--------|----------|----------|----------|
| NAVER 검색 API | **필수** | 25,000건/일 | developers.naver.com — 기본 registry 제외 |
| YouTube Data API v3 | 선택 (채널 RSS로 대체 가능) | 10,000 units/일 | console.cloud.google.com — 검색 소스는 기본 registry 제외 |
| X/Twitter API | 제외 | — | $100/월 유료 |
| Nitter | Key 불필요 | — | 불안정 — 기본 registry 제외 |

```bash
# .env에 추가 필요
NAVER_CLIENT_ID=
NAVER_CLIENT_SECRET=
YOUTUBE_API_KEY=      # 없으면 채널 RSS만 사용
```

---

## 7. 수집량 예상 (전체 Phase 완료 후)

| 소스 그룹 | Phase | 예상 건수 | 이미지 |
|-----------|-------|----------|--------|
| 기존 arXiv | — | 61건 | ❌ |
| TechCrunch, Verge, Decoder, MIT TR | Phase 0 수정 | +35건 | 보통 |
| Google AI, NVIDIA, AWS, AI타임스, Ahead of AI | Phase 1 | +50건 | **좋음** |
| Reddit 3개 서브 | Phase 2 | +45건 | **좋음** |
| Hacker News | Phase 3 | +15건 | 원문추출 |
| NAVER 뉴스 | Phase 4 | +30건 | 원문추출 |
| Yahoo Finance | Phase 5 | +20건 | **있음** |
| YouTube (채널 RSS) | Phase 6 | +15건 | **항상 있음** |
| Nitter | Phase 7 | +15건 | 가끔 |
| **합계** | | **~286건** | **arXiv 비율 ~21%** |

---

## 8. editorial_policy.yaml 조정

Phase 완료 후 추가할 내용:

```yaml
section_quotas:
  product: 4
  research: 1         # arXiv-only 최대 1개
  industry: 3
  tooling: 2
  policy: 2
  social: 1           # Reddit/HN 커뮤니티 반응 섹션
  multimedia: 1       # YouTube 영상 섹션 추가

report_selection:
  max_sections: 7     # 6 → 7 (multimedia 추가)
  max_arxiv_only_sections: 1
  max_community_sections: 1
  max_multimedia_sections: 1
```

---

## 9. 리스크

| 리스크 | 영향 | 완화 |
|--------|------|------|
| Nitter 불안정 | X 트윗 0건 | graceful skip, fallback URL |
| Reddit rate limit | 429 에러 | User-Agent 필수, 1초 딜레이 |
| NAVER API Key 미발급 | 한국어 뉴스 없음 | skip, 파이프라인 계속 |
| YouTube API 10,000 units 소진 | 검색 중단 | 채널 RSS로 자동 fallback |
| Yahoo Finance AI 필터 부정확 | 비AI 기사 유입 | 키워드 필터 + classify 단계 |
| 수집량 286건 → 파이프라인 시간 증가 | embed/classify 지연 | arXiv max_items 감축 검토 |

---

## 10. 실행 규칙

1. **Phase 0 먼저** — 기존 소스 버그 수정 후 나머지 진행
2. API Key 필요 Phase (4, 6b)는 기본 registry에 넣지 말고 Key 발급 후 후속으로 진행
3. 각 Phase: dry_run으로 수집 건수 확인 → 실 DB 반영
4. 새 소스 추가 전 직접 URL fetch 테스트 필수
5. Nitter(Phase 7)는 불안정하므로 기본 registry에서 제외하고 후속 검토
6. YouTube는 채널 RSS(Key 없음)만 기본 registry에 포함하고, Data API 검색은 후속 추가
