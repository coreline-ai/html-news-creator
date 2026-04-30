# 01. Design Philosophy

> 우리 디자인 시스템이 무엇을 지향하고 무엇을 거부하는지, 한 페이지에서 결정 근거를 찾을 수 있게.

## 출발점: paperclip의 디자인 DNA

[paperclipai/paperclip](https://github.com/paperclipai/paperclip)은 "zero-human company orchestration" SaaS이며, UI는 shadcn/ui의 **new-york** 스타일을 **monochrome neutral**로 운영합니다. 다섯 가지 특징이 우리 프로젝트와 결이 맞습니다.

### 1. Editorial Sharp — 각진 모서리
```css
--radius-lg: 0px;
--radius-xl: 0px;
--radius-md: 0.5rem;   /* 8px — 작은 요소만 */
--radius-sm: 0.375rem; /* 6px */
```
카드·모달·시트는 **모서리가 0**. 버튼·뱃지·입력만 살짝 둥급니다. SaaS 클리셰인 "둥글둥글한 카드"를 거부하고 신문/잡지의 직각 그리드를 가져옵니다.

### 2. Monochrome Primary — chroma 0
```css
--primary:    oklch(0.205 0 0);   /* 거의 검정, 채도 0 */
--foreground: oklch(0.145 0 0);
--muted:      oklch(0.97  0 0);
--border:     oklch(0.922 0 0);
```
브랜드 컬러를 따로 두지 않고 **검정·흰색·회색만으로 위계를 만듭니다**. 강조색은 데이터 시각화(`--chart-1` ~ `--chart-5`)에만 한정. 기사를 다루는 우리 도메인과 정확히 일치하는 결정.

### 3. Subtle Boundaries — 1px 보더 + shadow-xs
구획은 **얇은 보더 한 줄**과 **거의 보이지 않는 그림자**(`shadow-xs`)로만. 큰 그림자·glow·glass 효과 없음. 화면이 여러 위계가 섞일 때도 시각 잡음 없이 정보가 먼저 보임.

### 4. Density-First Layout
사이드바·브레드크럼·이슈 행·필터바 — paperclip은 데이터를 다루는 워크스페이스이며 **공기보다 정보가 우선**. 행 높이는 36~44px, 패딩은 작게, 정보를 한 화면에 꽉 채웁니다. 여백을 부풀리는 marketing-style UI를 거부.

### 5. OKLCH 색공간
모든 컬러가 `oklch()`. 이유:
- 명도(L)가 직관적이고 일정 — `0.97`은 항상 같은 밝기
- 다크모드에서 색상 보존이 자연스러움
- 라이트 → 다크 전환 시 hue/chroma는 유지하고 L만 반전 가능

---

## 우리 프로젝트(news-creator)와의 매핑

`html-news-creator`는 매일 50+ 소스에서 AI 트렌드를 수집해 **에디토리얼 톤의 HTML 리포트**를 생성하는 파이프라인입니다. 도메인 특성상 paperclip의 DNA가 거의 그대로 적용 가능합니다.

| 영역 | paperclip 결정 | 우리 적용 | 근거 |
|---|---|---|---|
| 컬러 | OKLCH 모노크롬 | 동일 채택 | 뉴스/기사는 색을 잘못 쓰면 신뢰도가 떨어짐. 본문은 흑백, 강조는 1색 |
| Radius | 카드 0, 작은 요소 6~8px | 동일 채택 | 신문 그리드 미학과 자연스러움 |
| Border | 얇은 단색 1px | 동일 채택 | 섹션 구분에 충분 |
| Shadow | shadow-xs 한 단계 | 동일 채택 | 일일 리포트에서 그림자 자체가 잡음 |
| Typography | system + Pretendard 가능 | **Pretendard 유지**(한글 가독성) | 우리 출력은 한국어 우선 |
| Density | 워크스페이스 밀도 | 리포트는 **여유**, 관리자 페이지는 paperclip 밀도 | 독자 경험 vs 운영자 효율 |
| 컴포넌트 | shadcn variants | **동일 variant 어휘 채택** | 향후 Tailwind/React 도입 시 즉시 호환 |

### 두 가지 적용 표면

#### A. 일일 리포트 HTML (현재 출력)
- 사용자: 뉴스레터 독자
- 목표: **읽기**
- 밀도: 여유 (max-width 820, 단락 간 충분한 spacing)
- 색: 거의 흑백, 강조 1색
- 다크모드: localStorage 토글, 시스템 환경설정 자동 감지

#### B. 향후 웹앱 (관리자/대시보드)
- 사용자: 운영자, 편집자
- 목표: **소스 관리, 클러스터 검토, 정책 튜닝**
- 밀도: 높음 (paperclip 수준)
- 컴포넌트: shadcn variant 그대로
- 레이아웃: 좌측 사이드바 + 메인 영역 + 컨텍스트 패널

두 표면은 **동일한 토큰 한 세트**를 공유합니다. 차이는 토큰 선택과 spacing scale 사용 방식뿐.

---

## 디자인 원칙 5조

### 원칙 1. **컨텍스트 우선** (DESIGN.md 4.2 원칙 1)
브랜드/기존 UI가 있으면 무조건 먼저 맞춤. 우리는 paperclip의 토큰 위계를 출발점으로 잡았으므로, 새 화면도 그 위계를 어기지 않습니다.

### 원칙 2. **모노크롬 + 1색**
검정·흰색·회색으로 위계를 만들고, 강조색은 한 번에 하나만. 차트 5색은 **데이터 표현 전용**, UI 강조 금지.

### 원칙 3. **콘텐츠가 형식을 결정**
공간을 채우려고 카드·아이콘·섹션을 만들지 않습니다. 화면이 비어 보인다면 그건 디자인 문제가 아니라 콘텐츠 문제. (DESIGN.md 4.2 원칙 3)

### 원칙 4. **토큰 외 색상 금지**
컴포넌트에서 raw hex나 `oklch()` 직접 사용 금지. 항상 시맨틱 토큰(`--primary`, `--muted-foreground`)을 통해 참조. (DESIGN.md 4.3.3)

### 원칙 5. **반응형은 밀도 변화로**
모바일에서 같은 정보를 줄이지 말고 **밀도와 위계만 재배열**. 사이드바는 시트로, 행은 카드로, 멀티컬럼은 단일컬럼으로.

---

## 거부 패턴 (Anti-patterns)

DESIGN.md 4.2 원칙 5(AI 슬롭 방지)와 paperclip의 시각 결정에서 도출:

- ❌ 그라디언트 배경 / 형광 강조 / 네온
- ❌ 둥글둥글한 카드 (radius > 12px) — `radius-lg=0` 원칙 위반
- ❌ 의미 없는 이모지·이모지 콜아웃
- ❌ 왼쪽 보더 색상 강조 카드 (회색 SaaS 클리셰)
- ❌ Inter / Roboto / system-ui — Pretendard로 통일
- ❌ 데이터 없는 stat card (filler)
- ❌ 여러 강조색 동시 사용 (한 화면에 1색)
- ❌ glass / blur / 반투명 카드 위 카드
- ❌ 큰 SVG 일러스트 — 진짜 자산 또는 placeholder

---

## 결정 로그

| 날짜 | 결정 | 근거 |
|---|---|---|
| 2026-04-30 | 디자인 베이스로 paperclip 채택 | shadcn 표준 + OKLCH + editorial 미학 |
| 2026-04-30 | Pretendard 유지 (system-ui 거부) | 한국어 출력 가독성 |
| 2026-04-30 | 일일 리포트는 여유 밀도, 운영 화면은 고밀도 | 독자/운영자 경험 분리 |
| 2026-04-30 | 강조색은 한 화면에 1색 | 모노크롬 위계 보존 |

향후 결정은 이 표 하단에 추가합니다.
