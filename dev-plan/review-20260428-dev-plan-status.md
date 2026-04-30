# 개발 계획서 상태 리뷰 — 2026-04-28

작성 일시: `2026-04-28 23:25:35 KST`

현재 `dev-plan/`의 완료 계획, 신규 계획, 검토 문서를 한 번 더 읽고 상태를 정리했다. 목적은 다음 작업자가 어떤 문서를 기준으로 작업해야 하는지 명확히 하는 것이다.

## 결론

현재 기준의 주 실행 계획은 다음 2개다.

1. `implement-20260428-221438.md` — 이미지/출처/website collector/fallback 이미지 보강 완료
2. `implement-20260428-225829.md` — editorial policy/source tier/mainstream 중심 재실행 품질 개선 완료

새 기능 개발 기준 문서는 다음 1개다.

1. `implement-20260428-source-boost.md` — 추가 소스 확장 후보 계획. 아직 미완료이며, 바로 실행하기 전 범위 축소가 필요하다.

기존 대형 계획 `implement-20260427-221152.md`는 초기 전체 로드맵으로 보관하되, 현재 코드 상태와 맞지 않는 전제가 많아 실행 기준으로 쓰지 않는다.

## 문서별 상태

| 문서 | 상태 | 판단 |
|---|---:|---|
| `implement-20260428-221438.md` | 완료 | 현재 코드에 대부분 반영됨. 출처/이미지/website collector/fallback SVG 기준 문서로 유지 |
| `implement-20260428-225829.md` | 완료 | 현재 주 파이프라인 품질 기준 문서. editorial policy와 mainstream 중심 선별 기준으로 유지 |
| `implement-20260428-source-boost.md` | 신규/미완료 | 아이디어는 유효하지만 범위가 과대. Phase 0~1만 후속 계획으로 잘라야 함 |
| `implement-20260427-215727.md` | 문서 계획 완료/체크박스 미정리 | GPT-5.5 proxy/gpt-image2 맥락 문서. 실제 일부 구현 완료됐으나 문서 체크박스는 미반영 |
| `implement-20260427-221152.md` | 구형 전체 로드맵 | 현재 repo와 맞지 않는 초기 전제 포함. 참조용 archive 성격 |
| `review-20260427-coreline-agent-oauth-proxy.md` | 검토 완료 | proxy 후보/주의사항 문서로 유효 |
| `review-20260427-dev-docs.md` | 검토 완료 | 구형 문서 결함과 P0/P1 권고를 정리한 기준 문서로 유효 |

## 완료 계획 리뷰

### `implement-20260428-221438.md`

완료 내용:

- KST 기준 날짜 window 보강
- `sources` 테이블 upsert 및 `raw_items.source_id` 연결
- RSS/HTML 대표 이미지 추출
- Anthropic/Meta RSS 깨짐을 website/listing collector로 우회
- GitHub anonymous fallback
- 원본 이미지가 없을 때 generated SVG fallback

현재 판단:

- 품질 문제 중 “출처 없음/이미지 없음”은 이 계획으로 큰 틀에서 해결됐다.
- 다만 SVG fallback은 임시 시각 보강이며, 실제 뉴스 이미지가 가능한 경우 원본 이미지를 우선해야 한다.
- source image quality filter는 계속 확장 필요하다. 예: Reddit UI, 광고, tracking pixel 차단.

### `implement-20260428-225829.md`

완료 내용:

- `editorial_policy.yaml` 추가
- source tier 재정의: official/mainstream/research/developer_signal
- mainstream source 추가
- arXiv max_items/priority 제한
- editorial ranker와 selection 적용
- 날짜 스코프 기반 `extract → classify → cluster → generate → render` 재실행
- 현재 HTML 5개 섹션, mainstream 중심으로 개선

현재 판단:

- 이 문서가 현재 프로젝트의 “뉴스 제품 품질 기준”에 가장 가깝다.
- 앞으로 파이프라인 품질 개선은 이 문서의 정책을 기준으로 해야 한다.
- 현재 남은 핵심 개선은 “대중 소스 추가”보다 “소스별 품질/중복/섹션 다양성”이다.

## 신규/미완료 계획 리뷰

### `implement-20260428-source-boost.md`

좋은 점:

- 기존 문제를 정확히 짚는다: arXiv 과다, 대중 소스 부족, 이미지 품질 문제.
- 추가 후보가 현실적이다: Google AI, NVIDIA, AWS, Reddit, HN, NAVER, YouTube 등.
- 이미지 우선순위 정리가 유용하다.

문제:

- 한 계획 안에 RSS, Reddit, HN, NAVER, Yahoo, YouTube, Nitter, 이미지 로직까지 들어 있어 너무 크다.
- API Key가 필요한 Phase가 섞여 있어 즉시 자동 파이프라인에 반영하기 어렵다.
- Reddit/Nitter/YouTube는 신뢰도와 약관/운영 안정성 리스크가 있어 메인 뉴스 출처가 아니라 보조 신호로만 둬야 한다.
- 현재 이미 `implement-20260428-225829.md`에서 mainstream 소스 수집과 arXiv 제한은 상당 부분 해결됐다.

권장 처리:

1. 이 문서는 “아이디어 백로그”로 보관한다.
2. 바로 실행할 후속 계획은 Phase 0~1만 잘라서 새 문서로 만든다.
3. API Key가 필요한 NAVER/YouTube는 별도 계획으로 분리한다.
4. Reddit/HN/Nitter는 메인 기사 출처가 아니라 `community_signal`로만 분류한다.

## 구형 계획 리뷰

### `implement-20260427-215727.md`

상태:

- 문서상 체크박스는 모두 미완료다.
- 실제로는 GPT-5.5 local proxy 설정, preflight, Codex login/test, `gpt-image2` skill 설치 등 일부가 이미 진행됐다.

정리 필요:

- 이 문서는 “초기 proxy/image 전략 문서”로 보관한다.
- 실제 완료 내역은 별도 현황 문서 또는 체크박스 업데이트가 필요하다.
- `backend/src/ai/*` 같은 구형 경로 전제는 현재 `app/` 구조와 맞지 않으므로 신규 구현 기준으로 쓰지 않는다.

### `implement-20260427-221152.md`

상태:

- 초기 전체 구현 로드맵이다.
- “소스코드 0%” 같은 현재와 맞지 않는 전제가 남아 있다.
- 체크박스가 모두 미완료라 현재 진행 상태 추적용으로는 부적합하다.

정리 필요:

- archive/roadmap 용도로만 유지한다.
- 현재 작업 기준은 `implement-20260428-225829.md`와 후속 계획으로 이동한다.
- 장기적으로는 `archive/` 또는 `dev-plan/legacy/` 이동을 검토한다.

## 검토 문서 리뷰

### `review-20260427-dev-docs.md`

유효한 지적:

- 문서와 실제 파일/경로 불일치
- Phase 의존성 충돌
- dry-run/report status 정책 미정
- SSRF/admin auth/sanitizer 기준 부족

현재 반영된 부분:

- 실제 파일과 코드가 많이 추가됨
- source/date/image/editorial 품질 기준은 후속 계획에서 보강됨

아직 남은 부분:

- dry-run 정책 통일
- report status state machine 통일
- admin auth scheme 확정
- SSRF를 DNS resolve/redirect 재검증 수준으로 강화

### `review-20260427-coreline-agent-oauth-proxy.md`

유효한 지적:

- `codex-backend`와 `codex-cli` 재귀 루프 위험 구분
- private backend 의존 리스크 명시
- `/embeddings`는 local fallback 유지 권장

현재 반영된 부분:

- GPT-5.5 proxy preflight가 추가됨
- embeddings는 local fallback으로 실제 스모크에서 정상 동작

## 우선순위 제안

### P0 — 바로 해야 할 정리

1. `implement-20260428-source-boost.md`를 바로 구현하지 말고 범위를 Phase 0~1로 축소한 새 계획을 만든다.
2. `implement-20260427-221152.md`는 legacy roadmap으로 표시한다.
3. `implement-20260427-215727.md`는 실제 완료된 proxy 작업과 문서 체크박스 상태를 맞춘다.

### P1 — 다음 개발 후보

1. 소스 품질 개선
   - Google AI Blog, NVIDIA Blog, AWS AI Blog처럼 공식/대중성이 있는 검증 가능한 RSS 추가
   - VentureBeat처럼 security checkpoint가 걸리는 소스는 제외
2. 섹션 다양성 개선
   - 같은 source/tier/topic이 반복되는 섹션 제한
   - product/policy/safety/research 분포 강화
3. 수집 결과 관측성
   - source별 수집 건수, 실패 원인, image coverage, editorial filtered count를 JSON/HTML에 표시

### P2 — API Key 필요 후속

1. NAVER 뉴스 검색 API
2. YouTube channel RSS/API
3. Hacker News/Reddit community signal

## 최종 권고

현재 기준으로 신규 개발은 `implement-20260428-225829.md`를 기준으로 이어가야 한다.

`implement-20260428-source-boost.md`는 “바로 구현할 계획”이 아니라 “확장 후보 백로그”로 취급하는 것이 안전하다. 다음 실행 단위는 다음처럼 작게 잘라야 한다.

```text
Phase A: 공식/대중 RSS 3~5개 추가 + 검증
Phase B: source별 수집/실패 observability
Phase C: section diversity gate
Phase D: API Key 필요한 NAVER/YouTube 별도
```

