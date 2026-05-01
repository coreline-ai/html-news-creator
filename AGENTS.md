# AGENTS.md — html-news-creator

AI 에이전트(Claude Code, Codex, Copilot 등)가 이 저장소에서 작업할 때 참고하는 규칙·컨텍스트 문서입니다.

---

## 프로젝트 개요

매일 50+ AI 뉴스 소스를 수집·분류·클러스터링해 **개발자 중심 AI 트렌드 HTML 리포트**를 자동 생성하는 파이프라인.  
언어: Python 3.11 / DB: PostgreSQL / LLM: OpenAI-compatible proxy (`gpt-5.5` at `localhost:4317`)

---

## 파이프라인 10단계

```
collect → extract → classify → cluster → verify → image_analyze → generate → render → publish → notify
```

진입점: `scripts/run_daily.py`  
실행: `PYTHONPATH=. uv run python scripts/run_daily.py --date YYYY-MM-DD --mode full`  
부분 실행: `--from-step generate --to-step render`

---

## 핵심 파일 위치

| 파일 | 역할 |
|------|------|
| `scripts/run_daily.py` | 파이프라인 전체 오케스트레이터 (1,200줄) |
| `data/sources_registry.yaml` | 50+ 소스 설정 (RSS / GitHub / arXiv / HN / Reddit) |
| `data/editorial_policy.yaml` | 점수 공식·소스 티어·섹션 할당량 |
| `app/editorial/ranker.py` | 아이템 편집 점수 산출 (순수 함수) |
| `app/editorial/selection.py` | 클러스터 요약 + 섹션 선정 (클러스터 크기 부스트 포함) |
| `app/pipeline/date_window.py` | KST 날짜 윈도우 (`_SLACK_HOURS_BEFORE=1`, `_SLACK_HOURS_AFTER=9`) |
| `app/utils/source_images.py` | 이미지 URL 검증·기자 초상 필터 |
| `app/models/db_models.py` | SQLAlchemy ORM 13개 테이블 |
| `templates/report_newsstream.html.j2` | 최종 HTML 템플릿 (Pretendard, 다크모드) |

---

## 편집 정책 요약

**점수 = 50(base) + tier_boost + 신호 보너스 - 패널티**

| 소스 티어 | 부스트 | main 허용 |
|----------|--------|----------|
| official | +18 (+10 추가) | ✅ |
| mainstream | +12 (+6 추가) | ✅ |
| developer_signal | +14 | ✅ |
| research (arXiv) | +4 (−22 패널티) | ❌ |
| community | −4 | ❌ |

**토픽 분류 우선순위**: research → tooling (GitHub·OSS 키워드) → product → industry → policy  
**클러스터 크기 부스트**: `(항목 수 - 1) × 5`, 최대 +20  
**섹션 최대**: `max_sections: 10` (product 4 / tooling 4 / research 1 / industry 1 / policy 1)

---

## 개발 규칙

### 코드 스타일
- `from __future__ import annotations` 모든 파일 상단
- 타입 힌트 필수 (함수 시그니처)
- 주석: WHY가 비명백한 경우에만, 한 줄로
- 상수는 모듈 레벨에 UPPER_CASE로 선언

### 편집 정책 변경 시
- `data/editorial_policy.yaml` 수정 → 관련 단위 테스트 기댓값 업데이트 필수
- 클러스터 점수가 바뀌면 `tests/unit/test_editorial_selection.py` 확인
- 소스 티어 변경 시 `tests/unit/test_editorial_ranker.py` 확인

### 이미지 필터
- 기자 초상·UI 요소 필터: `app/utils/source_images.py::_is_unsuitable_image_url`
- 새 패턴 추가 시 `_SKIP_PATTERNS` 또는 `_AUTHOR_PORTRAIT_PATTERNS` 튜플에 추가
- `is_usable_representative_image_url()` 가 통과 기준 (HTTP + 비적합 패턴 없음)

### 템플릿
- 현재 사용 템플릿: `report_newsstream.html.j2` (구 `daily_report.html.j2` 사용 안 함)
- Jinja2 autoescaping ON — 사용자 입력 XSS 자동 처리됨
- YouTube play 버튼: `yt-play` 클래스 (CSS `::after` 삼각형)
- 섹션 이미지는 `src.video_id` 필드가 있어야 재생 오버레이 표시

### 디자인 시스템 적용 범위
- `docs/design/**`는 **현재 HTML 리포트용 스타일 가이드가 아니라**, 추가 개발될 웹앱(운영/관리자/대시보드/구독자 UI)을 위한 디자인 시스템이다.
- 현재 생성물인 `templates/report_newsstream.html.j2`와 `public/news/*.html`은 기존 리포트 템플릿 스타일을 유지한다.
- `docs/design`의 토큰·컴포넌트·레이아웃 규칙을 HTML 리포트에 자동/강제 적용하지 말 것.
- 사용자가 명시적으로 “HTML 리포트 디자인 마이그레이션/토큰화”를 요청한 경우에만 별도 개발 계획을 세우고 적용한다.
- 웹앱 UI를 새로 만들 때는 `docs/design/06-automation-spec.md`, `docs/design/tokens.css`, `04-components.md`, `05-layout-patterns.md`를 기준으로 한다.

---

## 테스트

```bash
# 단위 테스트 전체
PYTHONPATH=. uv run pytest tests/unit/ -v --tb=short

# 특정 모듈
PYTHONPATH=. uv run pytest tests/unit/test_editorial_ranker.py -v
```

- 130개+ 단위 테스트, DB 없이 실행 가능
- `@pytest.mark.integration` 태그 테스트는 CI에서 제외
- 편집 점수·선정 로직은 순수 함수 → 모킹 불필요

---

## 소스 추가 방법

`data/sources_registry.yaml`에 아래 형식으로 추가:

```yaml
- name: My Source
  source_type: rss          # rss | github | arxiv | website | hackernews
  url: https://example.com/feed.xml
  trust_level: trusted_media
  source_tier: mainstream   # official | mainstream | developer_signal | research | community
  priority: 75              # 높을수록 우선 수집
  max_items: 10
```

GitHub org 추가 시: `source_type: github`, `org: org-name` (url 불필요)

---

## 주의 사항

- **날짜 윈도우**: KST 기준이지만 미국 기사 포함을 위해 UTC 기준으로 ±슬랙 적용됨. `date_window.py` 직접 수정 시 `_SLACK_HOURS_BEFORE/AFTER` 상수 함께 조정
- **GitHub Rate Limit**: 토큰 없이 실행 시 익명 fallback → `GITHUB_ALLOW_UNAUTHENTICATED=true`
- **Yahoo Finance**: 429 자주 발생 (rate limit), extract 실패는 정상
- **OpenAI**: `localhost:4317` 프록시 사용 중. embedding endpoint 없으면 로컬 fallback (sentence-transformers)
- **섹션 중복 방지**: generate 재실행 시 기존 `ReportSection` 자동 삭제 후 재삽입 (`if db_report: delete(ReportSection)`)
- **SVG 폴백**: 이미지 없는 섹션은 `app/utils/generated_images.py`가 SVG 생성 → `public/assets/generated/`

---

## DB 스키마 핵심

```
Source → RawItem → ExtractedContent
                └→ AnalysisResult
RawItem ←→ Cluster (ClusterItem 조인)
Cluster → ReportSection → Report
```

마이그레이션: `psql "$DATABASE_URL" -f migrations/001_initial.sql`

---

*이 파일은 에이전트 작업 컨텍스트용입니다. 사용자 대상 문서는 README.md를 참조하세요.*
