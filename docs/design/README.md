# Design System — html-news-creator

이 폴더는 `html-news-creator`의 디자인 가이드, 스타일, 테마 표준을 정의합니다.
출력 HTML 리포트와 향후 웹앱(대시보드/관리자/구독자 페이지) 양쪽에 동일하게 적용할 수 있는 단일 디자인 시스템입니다.

## 출처와 근거

- **시각 베이스**: [shadcn/ui](https://ui.shadcn.com) **new-york** 스타일을 **OKLCH 모노크롬 뉴트럴**로 운영하는 컨벤션. 에디토리얼 미학, 정보 밀도, 정직한 토큰 계층이 우리 프로젝트와 결이 맞아 출발점으로 채택.
- **상위 표준**: 프로젝트 루트의 [`DESIGN.md`](../../DESIGN.md) — 디자인 에이전트 운영 표준. 이 폴더는 그 4개 층위(Brand → Foundation → Semantic → Component)를 실제 토큰과 코드로 채운 결과물.
- **기존 출력물**: [`templates/report_newsstream.html.j2`](../../templates/report_newsstream.html.j2) — 현재 일일 리포트 템플릿. 폰트(Pretendard), 다크모드, max-width 820, 카드 패턴 일부는 여기서 그대로 계승.

## 파일 구성

| # | 파일 | 다루는 것 | 주요 독자 |
|---|---|---|---|
| 00 | [README.md](README.md) | 인덱스·사용법 (이 파일) | 모두 |
| 01 | [01-philosophy.md](01-philosophy.md) | 디자인 DNA, 원칙, 매핑 근거 | 디자이너·PM |
| 02 | [02-tokens.md](02-tokens.md) | 컬러·radius·shadow 토큰 명세 | 개발자·자동화 |
| 03 | [03-typography.md](03-typography.md) | 타입 램프·Pretendard 운영 | 개발자·디자이너 |
| 04 | [04-components.md](04-components.md) | Button/Card/Badge/Input 명세 | 개발자·자동화 |
| 05 | [05-layout-patterns.md](05-layout-patterns.md) | 레이아웃·밀도·반응형 패턴 | 디자이너·개발자 |
| 06 | [06-automation-spec.md](06-automation-spec.md) | LLM/코드젠이 읽는 기계 가독 명세 | 자동화 에이전트 |
| — | [tokens.css](tokens.css) | 즉시 임포트 가능한 CSS 변수 | 코드 |
| — | [tokens.json](tokens.json) | 머신 리더블 토큰 | 코드 |

## 자동화 개발에서 사용하는 방법

### 1. 신규 화면을 만들 때
1. `06-automation-spec.md`를 LLM 프롬프트 컨텍스트로 주입
2. `tokens.css`를 빌드 산출물에 인라인 또는 임포트
3. `04-components.md`의 variant 표를 따라 마크업 생성
4. `05-layout-patterns.md`의 패턴 카탈로그에서 가장 가까운 것 채택

### 2. 일일 리포트(HTML)에 적용할 때
- `templates/report_newsstream.html.j2`의 `<style>` 블록을 점진적으로 `tokens.css` 변수로 치환
- Pretendard는 그대로, 색상·radius·shadow만 토큰화
- 다크모드는 `.dark` 셀렉터 토글로 단일 소스 유지

### 3. 토큰을 바꾸고 싶을 때
1. `tokens.json` 한 곳만 수정
2. 빌드 스크립트로 `tokens.css` 재생성 (TODO: `scripts/build_tokens.py`)
3. 02·03·04 문서의 표는 자동 생성 안 함 — 수치 변경 시 함께 갱신

## 변경 정책

이 디자인 시스템은 **단일 출처 원칙(Single Source of Truth)**을 따릅니다.

- 색·radius·shadow·spacing 수치를 화면 코드에 직접 박지 않습니다.
- 항상 `var(--token-name)` 또는 Tailwind 유틸리티(`bg-primary`, `rounded-md`)로 참조합니다.
- 토큰을 추가·삭제하기 전에 02-tokens.md를 먼저 갱신합니다.

## 라이선스 주의

이 시스템의 OKLCH 토큰 수치는 [shadcn/ui](https://ui.shadcn.com)(MIT 라이선스)의 보편적 디폴트를 출발점으로 삼은 **재해석 결과**이며, 외부 프로젝트의 고유 자산(로고/이미지/카피)은 포함하지 않습니다. 별도 자산을 추가할 때는 출처를 명시합니다.
