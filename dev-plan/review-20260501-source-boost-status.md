# Review: `implement-20260428-source-boost.md` 코드 현황 매핑 (2026-05-01)

> 원래 계획서는 9 phase, 35 미체크 박스로 표기돼 있었지만, 이후 다른 작업 흐름에서 대부분 처리됐다. 이 노트는 phase별 코드 현황을 한 번 점검한 결과이며, 원본 계획서의 체크박스를 유지하기보다 **현재 진실에 맞는 상태 매트릭스**를 새로 적는다.

---

## 1. Phase별 상태

| Phase | 원안 목표 | 현재 코드 | 상태 |
|---|---|---|---|
| 0 | TechCrunch/The Verge 0건 날짜 필터 버그 | `app/pipeline/date_window.py:14-15` `_SLACK_HOURS_BEFORE=1`, `_SLACK_HOURS_AFTER=9` (KST + US PT 슬랙) | ✅ 해결됨 |
| 1 | Google AI / NVIDIA / AWS / Yahoo Finance / AI타임스 RSS 추가 | `data/sources_registry.yaml`에 5개 모두 등록 | ✅ 완료 |
| 2 | Reddit r/MachineLearning + r/artificial + r/OpenAI + r/LocalLLaMA | 4개 모두 등록, `community` tier, `eligible_for_main: false` 유지 | ✅ 완료 |
| 3 | Hacker News API 수집기 | `app/collectors/hackernews_collector.py`, `Hacker News AI` 등록, `min_score`/`keywords` 필터 | ✅ 완료 |
| 4 | NAVER 뉴스 검색 API 수집기 | `app/collectors/naver_news_collector.py` 존재. 단 `data/sources_registry.yaml` 미등록 (API Key 발급 후 옵션 등록) | 🟡 collector만 완료, registry 등록은 의도적 보류 |
| 5 | Yahoo Finance RSS | `Yahoo Finance AI` 등록, `ai_filter: true` 키워드 필터 | ✅ 완료 |
| 6 | YouTube 수집기 (Two Minute Papers / Lex Fridman / DeepMind / OpenAI / Google Cloud Tech) | RSS 채널 5개 등록, 템플릿 `yt-play` 클래스로 플레이 오버레이 | ✅ 완료 |
| 7 | Nitter (X/Twitter 미러) | `app/collectors/x_collector.py`는 stub. Nitter 인스턴스 미연결 | 🟢 의도적 미실행 (Optional, 안정 인스턴스 부재) |
| 8 | 이미지 선택 로직 통합 정비 | `app/utils/source_images.py`의 `is_usable_representative_image_url` 적용 — main 파이프라인 + admin render 둘 다 (Phase F-Y) | ✅ 완료 |

## 2. 진짜 남은 작업

| 항목 | 위치 | 분류 |
|---|---|---|
| NAVER 뉴스 registry 등록 + 운영 검증 | `data/sources_registry.yaml`, `app/config.py` (이미 `naver_client_id/secret` 필드 있음) | API Key 발급 시 즉시 활성 |
| Nitter 또는 X/Twitter 정식 연결 | `app/collectors/x_collector.py` | 안정 인스턴스/정책 결정 후 |
| `app/collectors/rss_collector.py` 날짜 필터 디버그 로그 | 작은 운영 디버깅 편의 | 가성비 낮음, skip 가능 |
| `published_parsed=None` 항목 → 오늘로 간주 | 현재는 슬랙으로 우회 처리됨 | **재검토 필요 — 슬랙으로 충분한지** |

**결론**: 9 phase 중 7개 ✅, 2개 🟢/🟡 (의도적 보류), **즉시 실행해야 할 미완료 항목 없음**.

## 3. 원본 계획서 처리 권고

`implement-20260428-source-boost.md`는 다음과 같이 다룬다:

- **체크박스는 갱신하지 않는다** — 원안의 35 미체크 항목은 코드와 1:1 매핑이 아니어서 일괄 체크 시 정보 왜곡.
- **이 노트(`review-20260501-source-boost-status.md`)를 정본**으로 사용한다.
- 향후 NAVER 등록·X 연결 작업이 시작되면 별도 implement 계획서를 새로 작성한다 (예: `implement-20260DDD-naver-source-rollout.md`).

## 4. review 메타

- 점검 대상: `dev-plan/implement-20260428-source-boost.md` 9 phase / 35 미체크
- 점검 방법: phase별 키워드 grep + `data/sources_registry.yaml` yaml 파싱
- 점검 결과: 7 완료 · 2 의도적 보류 · 0 즉시 미완료
- 다음 행동: 없음 (현 상태 유지)
