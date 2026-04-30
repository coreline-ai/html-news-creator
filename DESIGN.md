# Claude Design Prompt 표준화 가이드

## 목적
이 문서는 `Claude-Design-Sys-Prompt.txt`에 흩어져 있는 운영 규칙, 디자인 원칙, 산출물 규격, 검증 흐름을 **실무용 표준**으로 재구성한 가이드다. 목표는 다음 3가지다.

1. **디자인 가이드 / 스타일 / 테마 적용 기준 통일**
2. **프롬프트 문장 수준 규칙을 운영 가능한 체크리스트로 정리**
3. **모호하거나 충돌하는 규칙을 표준 의사결정 규칙으로 정규화**

---

## 1. 핵심 해석 요약

원문 프롬프트는 크게 4개 층위로 구성된다.

| 층위 | 의미 | 표준화 방향 |
|---|---|---|
| 역할 규정 | 디자이너/매니저 관계, HTML 중심 산출물 | 역할/출력 범위를 명시적으로 분리 |
| 운영 규정 | 질문, 리서치, 파일 구조, 검증 순서 | SOP(표준 작업 절차)로 정리 |
| 구현 규정 | React/Babel, 파일 분할, deck/tweak 규격 | 기술 규격 섹션으로 정리 |
| 디자인 철학 | 브랜드 맥락 우선, 옵션 탐색, AI 슬롭 방지 | 디자인 시스템 원칙으로 승격 |

즉, 이 프롬프트는 단순한 “스타일 가이드”가 아니라 아래를 모두 포함하는 **디자인 에이전트 운영 규약**에 가깝다.

- 디자인 디렉션 원칙
- 산출물 포맷 표준
- 구현 제약
- 리뷰/검증 흐름
- 컨텍스트 수집 방식

따라서 표준화도 **테마 토큰 규칙 + 작업 프로세스 + 구현 규격 + QA 게이트**를 함께 가져가야 한다.

---

## 2. 표준화가 필요한 주요 문제

### 2.1 규칙이 너무 운영 지시문 중심임
원문은 실행 지시가 강하고, 디자인 시스템 자체의 구조는 약하다.

예:
- 질문을 많이 하라
- 검증 전에 특정 절차를 거쳐라
- HTML 파일을 어떻게 나눠라

반면 아래는 약하다.
- 토큰 구조 표준
- 스타일/테마 계층
- 컴포넌트 수준 디자인 계약
- 브랜드 적용 우선순위

### 2.2 규칙 간 충돌 또는 해석 여지가 있음

| 원문 성격 | 충돌/모호성 | 표준 결정 |
|---|---|---|
| “단일 HTML 문서” | “큰 파일 금지, JSX 분리”와 충돌 | **배포 단위는 1개 HTML**, 구현은 분리 가능 |
| “질문을 많이 하라” | “작은 수정은 질문 생략”과 충돌 | 질문 강도를 **작업 유형별 매트릭스**로 분리 |
| “옵션은 3개 이상” | 간단한 수정에는 과도 | 신규 탐색만 3+, 수정은 1~2 대안 허용 |
| “컨텍스트 없으면 시작 금지 수준” | 실제론 빠른 실험이 필요할 수 있음 | **브랜드/시스템 없음 = 임시 시각 시스템 선언 후 진행** |
| “직접 검증하지 말라” | 최소한의 로딩 체크는 필요 | **UI 검증은 정식 게이트에서**, 구현 중 문법/구조 확인은 허용 |

### 2.3 디자인 원칙과 플랫폼 규칙이 섞여 있음
원문에는 아래가 한 문서에 섞여 있다.

- 디자인 미학 원칙
- 컴포넌트 로딩 규칙
- 파일 경로 규칙
- deck navigation 규칙
- tweak 패널 규칙

표준화 시에는 반드시 분리해야 한다.

1. **Design Principles**
2. **Theme & Token Standard**
3. **Artifact Implementation Standard**
4. **Review & Delivery Standard**

---

## 3. 표준 문서 구조 제안

실제 운영용 표준은 아래 5개 문서로 분리하는 것이 가장 안정적이다.

### A. `DESIGN_PRINCIPLES.md`
브랜드, 미학, UX, 컨텐츠 밀도, 옵션 탐색 원칙

### B. `THEME_TOKEN_STANDARD.md`
색상/타이포/간격/반경/그림자/모션/시맨틱 토큰 규칙

### C. `ARTIFACT_IMPLEMENTATION_STANDARD.md`
HTML, JSX, deck, prototype, animation, tweaks, 파일 구조 규칙

### D. `DESIGN_WORKFLOW_STANDARD.md`
질문 → 컨텍스트 수집 → 설계 → 초안 → 검증 → 핸드오프 절차

### E. `DESIGN_QA_CHECKLIST.md`
검증 체크리스트, 금지 패턴, 완료 정의

이 문서에서는 위 5개를 한 번에 사용할 수 있도록 통합 요약본 형태로 정리한다.

---

# 4. 통합 표준 가이드

## 4.1 역할 및 산출물 표준

### 역할 정의
- 시스템은 **디자이너** 역할을 수행한다.
- 사용자는 **매니저/리뷰어** 역할을 가진다.
- 결과물은 설명문이 아니라 **실제 디자인 산출물** 중심이어야 한다.

### 기본 산출물 원칙
- 기본 산출물은 **HTML 엔트리 1개**다.
- 단, 유지보수성을 위해 JS/JSX/CSS 보조 파일 분리는 허용한다.
- 사용자 전달 기준은 “문서 설명”이 아니라 **실행 가능한 결과물**이다.

### 산출물 유형
| 유형 | 기본 포맷 | 목적 |
|---|---|---|
| 비주얼 탐색 | HTML canvas/grid | 정적 옵션 비교 |
| 인터랙티브 프로토타입 | HTML + React/JSX | 흐름/상호작용 검토 |
| 슬라이드/덱 | HTML deck | 발표/스토리텔링 |
| 애니메이션 | HTML timeline | 모션/시퀀스 검토 |
| 문서형 가이드 | Markdown/HTML | 표준, handoff, 운영 문서 |

---

## 4.2 디자인 원칙 표준

### 원칙 1. 컨텍스트 우선
- 기존 브랜드, 디자인 시스템, UI kit, 코드베이스, 스크린샷, Figma가 있으면 **반드시 우선 참조**한다.
- 맥락 없는 디자인은 예외 상황으로 취급한다.
- 기존 UI가 있다면 아래를 먼저 맞춘다.
  - 색상 체계
  - 타이포 계층
  - 간격 밀도
  - radius/shadow 패턴
  - 인터랙션 속도/감도
  - copy tone

### 원칙 2. 탐색은 넓게, 결정은 좁게
- 신규 디자인 탐색은 **최소 3개 방향**을 권장한다.
- 변주는 다음 축에서 만든다.
  - 레이아웃
  - 시각 밀도
  - 상호작용 패턴
  - 컬러 강조 방식
  - 아이코노그래피 사용 유무
  - 타이포그래피 성격

### 원칙 3. 단순함은 내용 절제에서 온다
- 공간을 채우기 위해 섹션, 숫자, 아이콘, 카피를 억지로 추가하지 않는다.
- 디자인 문제를 콘텐츠 부풀리기로 해결하지 않는다.
- 모든 요소는 역할이 있어야 한다.

### 원칙 4. 브랜드 기반 확장
- 가능하면 브랜드 색을 그대로 쓰고,
- 부족할 경우에만 **유사한 톤의 확장색**을 만든다.
- 무작위 새 색상은 금지한다.
- 색상 확장은 가능하면 지각 균형이 좋은 체계로 정의한다.

### 원칙 5. AI 슬롭 방지
다음은 기본 금지 패턴으로 둔다.
- 과도한 그라디언트 배경 남용
- 의미 없는 이모지 남발
- 왼쪽 보더만 강조된 카드 남용
- 불필요한 stats/data filler
- 익숙한 웹 SaaS 클리셰 레이아웃 복제
- 저품질 SVG 일러스트 남발

---

## 4.3 스타일 / 테마 표준

이 부분이 실제 “디자인 가이드 / 스타일 / 테마 적용”에 가장 중요하다.

### 4.3.1 테마 계층
테마는 4단계로 관리한다.

#### Layer 1. Brand Tokens
브랜드 고유 자산
- brand.primary
- brand.secondary
- brand.accent
- brand.logo_usage
- brand.imagery_style
- brand.voice_tone

#### Layer 2. Foundation Tokens
시각 시스템의 기초 단위
- color.*
- typography.*
- spacing.*
- radius.*
- shadow.*
- motion.*

#### Layer 3. Semantic Tokens
역할 중심 토큰
- text.primary / secondary / inverse
- surface.base / elevated / muted
- border.default / strong / subtle
- action.primary / secondary / danger
- feedback.success / warning / error / info
- focus.ring

#### Layer 4. Component Tokens
컴포넌트별 세부 규칙
- button.primary.bg
- button.primary.fg
- card.radius
- input.border.focus
- modal.surface
- badge.info.bg

### 4.3.2 최소 토큰 표준
아래 토큰은 테마 적용 가능성을 위해 **반드시** 있어야 한다.

#### Colors
- `color.bg.base`
- `color.bg.subtle`
- `color.bg.elevated`
- `color.text.primary`
- `color.text.secondary`
- `color.text.inverse`
- `color.border.subtle`
- `color.border.default`
- `color.action.primary`
- `color.action.primaryHover`
- `color.action.secondary`
- `color.feedback.success`
- `color.feedback.warning`
- `color.feedback.error`
- `color.focus.ring`

#### Typography
- `type.family.display`
- `type.family.body`
- `type.size.xl`
- `type.size.lg`
- `type.size.md`
- `type.size.sm`
- `type.weight.regular`
- `type.weight.medium`
- `type.weight.bold`
- `type.leading.tight`
- `type.leading.normal`
- `type.leading.relaxed`

#### Spacing & Shape
- `space.1` ~ `space.8`
- `radius.sm`
- `radius.md`
- `radius.lg`
- `radius.xl`
- `shadow.sm`
- `shadow.md`
- `shadow.lg`

#### Motion
- `motion.fast`
- `motion.base`
- `motion.slow`
- `motion.ease.standard`
- `motion.ease.emphasized`

### 4.3.3 테마 적용 우선순위
1. **브랜드 색상 유지**
2. **시맨틱 토큰 매핑**
3. **컴포넌트별 오버라이드 최소화**
4. **특정 화면용 예외는 theme variant로 분리**

즉, 컴포넌트에서 직접 색을 박지 말고 아래 순서를 지킨다.

- component → semantic token 참조
- semantic token → foundation token 참조
- foundation token → brand token 기반

### 4.3.4 테마 변형 표준
테마 variant는 아래 수준으로만 허용한다.

| 수준 | 예시 | 허용 여부 |
|---|---|---|
| light / dark | 전체 분위기 전환 | 허용 |
| neutral / brand / campaign | 브랜드 강조 강도 | 허용 |
| component-local palette | 컴포넌트마다 임의 색상 | 제한 |
| one-off page-only hacks | 특정 페이지 하드코딩 | 금지 |

---

## 4.4 작업 절차 표준 (SOP)

### Phase 1. Intake
작업 시작 시 최소 확인 항목
- 무엇을 만드는가?
- 최종 산출물 포맷은?
- fidelity 수준은?
- 기존 브랜드/디자인 시스템/코드베이스가 있는가?
- 옵션 탐색이 필요한가?
- 스타일/인터랙션/카피 중 어디를 탐색할 것인가?

### Phase 2. Context Collection
가능한 순서:
1. 기존 코드베이스
2. 디자인 시스템 문서
3. 스크린샷
4. Figma
5. 경쟁/참조 사례

### Phase 3. System Declaration
본격 디자인 전에 아래를 먼저 선언한다.
- 타이포 시스템
- 색상 구조
- 레이아웃 리듬
- 컴포넌트 언어
- 모션 톤
- 변주 축

즉 “무엇을 만들지”보다 “어떤 시스템으로 만들지”를 먼저 잠근다.

### Phase 4. Exploration
- 빠른 초안
- 옵션 3개 이상(신규 탐색 시)
- 정석안 + 실험안 혼합
- placeholder 허용

### Phase 5. Refinement
- 선택된 방향 압축
- tweak 포인트 노출
- 내용 절제
- 실제 컨텍스트에 맞는 copy/spacing 정리

### Phase 6. Verification
완료 전 확인
- 깨지지 않는가
- 레이아웃 밀도가 적정한가
- theme/token 일관성이 유지되는가
- tweak 상태가 정상 반영되는가
- deck/prototype navigation이 동작하는가

---

## 4.5 질문 표준

원문은 질문을 강하게 요구한다. 이를 아래처럼 표준화한다.

### 질문이 필수인 경우
- 신규 제품/신규 흐름 설계
- 브랜드 컨텍스트가 없는 경우
- deck/프로토타입/온보딩/복합 UI
- 옵션 탐색 요구가 있는 경우

### 질문 생략 가능
- 작은 수정
- 텍스트 변경
- 이미 충분한 레퍼런스가 있는 경우
- 기존 시스템 안에서의 한정된 컴포넌트 수정

### 최소 질문 카테고리
1. 목표 사용자/청중
2. 산출물 형식
3. 브랜드/디자인 시스템 유무
4. 탐색 축(비주얼/플로우/모션/카피)
5. 옵션 개수
6. 현실 제약(시간, 범위, 기술)

---

## 4.6 산출물 구현 표준

### 4.6.1 파일 구조
- 사용자에게 전달되는 메인 엔트리는 1개 HTML
- 대형 구현은 보조 JS/JSX/CSS 파일 분리 허용
- 1000라인 이상 파일은 가능하면 분할

### 4.6.2 파일 네이밍
- 사람이 읽을 수 있는 descriptive naming 사용
- 주요 revision은 버전 구분
  - `Landing Page.html`
  - `Landing Page v2.html`

### 4.6.3 기존 UI 편집 시
반드시 먼저 파악할 것:
- visual vocabulary
- spacing rhythm
- interaction patterns
- content tone
- contrast model

### 4.6.4 placeholder 규칙
- 자산이 없으면 placeholder 허용
- 단, 조악한 가짜 final asset은 금지
- placeholder는 “자리/비율/역할”만 설명하면 충분

---

## 4.7 프로토타입 / 덱 / 애니메이션 표준

### 프로토타입
- 제목용 첫 화면을 억지로 만들지 않는다.
- 실제 제품 화면이 바로 보이게 한다.
- 중심 배치 또는 viewport-fit 원칙을 따른다.

### 덱
- 슬라이드 번호는 **사용자 관점 1-indexed**
- 각 슬라이드는 screen label을 가져야 한다.
- speaker notes는 요청 시에만 추가한다.
- 노트 내부 인덱스와 사용자 표시 인덱스는 분리 가능하지만, 표기 규칙은 1-index 기준으로 설명한다.

### 애니메이션
- 장식보다 타이밍 구조가 먼저다.
- 모션은 정보 전달을 강화해야 한다.
- 인터랙티브 프로토타입이면 복잡한 모션보다 상태 전이가 우선이다.

---

## 4.8 Tweaks 표준

원문에서 Tweaks는 “최종 결과 안에서 변형 가능한 제어면”으로 정의된다. 이를 아래처럼 표준화한다.

### 목적
- 옵션을 새 파일로 분기하지 않고 **하나의 메인 산출물 안에서 제어**한다.
- 리뷰 중 빠른 비교를 가능하게 한다.

### tweak 대상 우선순위
1. 테마(색, 폰트, 밀도)
2. 레이아웃(정렬, 폭, 카드형/리스트형)
3. copy 밀도
4. 기능 플래그
5. 모션 강도

### tweak UI 원칙
- 작고 명확해야 한다.
- 기본 상태에서는 숨겨져 있어야 한다.
- 디자인을 망가뜨리지 않고 비교만 가능해야 한다.

### 표준 상태 키 예시
- `themeMode`
- `density`
- `accentStyle`
- `layoutVariant`
- `copyLength`
- `motionLevel`

---

## 4.9 콘텐츠 표준

### 기본 원칙
- filler 금지
- 아이콘 남용 금지
- 숫자 장식 금지
- 사용자 목표와 무관한 섹션 추가 금지

### 텍스트 밀도
- 슬라이드/화면은 “읽는 문서”보다 “즉시 파악되는 구조”를 우선
- 긴 설명은 notes 또는 보조 문서로 분리

### 이미지 사용
- 실제 자산이 있으면 우선 사용
- 없으면 placeholder
- low-quality pseudo-illustration은 지양

---

## 4.10 기술 규격 표준

이 항목은 프롬프트에서 매우 강하게 요구하므로 별도 규격으로 고정하는 것이 좋다.

### React/JSX 사용 시
- 라이브러리 버전 고정
- scope 충돌 방지
- 전역 style object 이름 충돌 금지
- 여러 Babel 파일 간 공유 컴포넌트는 명시적으로 export

### 금지 사항
- 공통 이름의 전역 style 객체 사용 금지
- 근거 없는 module 혼용 금지
- 큰 단일 파일에 모든 것을 밀어넣는 방식 지양

### deck/prototype persistence
- slide/time/state는 복원 가능해야 한다.
- 새로고침 후 진행 상태 손실을 최소화한다.

---

## 4.11 QA / 완료 정의

### 완료 정의 (Definition of Done)
다음이 모두 충족되어야 완료로 본다.

1. 결과물이 열리고 깨지지 않는다.
2. 브랜드/테마 적용 규칙이 일관적이다.
3. 토큰 계층 위반이 없다.
4. 주요 인터랙션이 동작한다.
5. tweak가 있으면 정상 반영되고 저장된다.
6. 옵션 탐색이 요구되었다면 충분한 비교안이 있다.
7. filler 콘텐츠가 없다.
8. 가독성/밀도/대비가 기준 이하가 아니다.

### QA 체크리스트
- [ ] 색상이 semantic token 체계를 따른다
- [ ] 컴포넌트가 직접 raw color에 과도하게 의존하지 않는다
- [ ] type scale이 일관적이다
- [ ] spacing scale이 반복적으로 재사용된다
- [ ] shadow/radius가 시스템 내에서 제한된 수로 유지된다
- [ ] 화면마다 다른 미학 언어가 섞이지 않는다
- [ ] CTA 강조 방식이 일관된다
- [ ] 레이아웃이 콘텐츠를 위해 존재한다
- [ ] 불필요한 장식이 없다
- [ ] 최종 사용자 관점에서 조작이 이해 가능하다

---

## 5. 권장 표준 템플릿

실제 운영에서는 아래 YAML/JSON 형태의 메타 정의를 같이 두면 테마 적용이 쉬워진다.

```yaml
brand:
  name: Sample Brand
  voice: calm / precise / premium
  imagery: minimal / editorial / product-led

theme:
  mode: light
  accent_style: restrained
  density: medium

foundations:
  color:
    bg_base: "#..."
    bg_elevated: "#..."
    text_primary: "#..."
    action_primary: "#..."
  typography:
    display_family: "..."
    body_family: "..."
    size_scale: [12, 14, 16, 20, 24, 32, 48]
  spacing:
    scale: [4, 8, 12, 16, 24, 32, 48, 64]
  radius:
    sm: 8
    md: 12
    lg: 20
  motion:
    fast: 120
    base: 180
    slow: 280

semantics:
  surface:
    base: color.bg_base
    elevated: color.bg_elevated
  text:
    primary: color.text_primary
    secondary: color.text_secondary
  action:
    primary: color.action_primary

components:
  button:
    radius: radius.md
    bg: action.primary
    fg: text.inverse
  card:
    bg: surface.elevated
    radius: radius.lg
```

---

## 6. 원문 기준 수정 권고 사항

표준화 과정에서 아래는 수정 권장 사항이다.

### 6.1 표현/오타 수정
- `TWEAK_DEFAULS` → `TWEAK_DEFAULTS`
- `no questins` → `no questions`
- `largher` → `larger`

### 6.2 규칙 재정의
- “단일 HTML 문서”를 **배포 엔트리 단일화**로 재정의
- “질문 많이”를 **질문 강도 매트릭스**로 재정의
- “3개 이상 옵션”을 **신규 탐색 과제 기준**으로 한정

### 6.3 추가되면 좋은 항목
- 토큰 네이밍 룰
- light/dark 변형 원칙
- 접근성 최소 기준(contrast, hit target)
- component acceptance criteria
- theme override 우선순위

---

## 7. 최종 운영 권장안

가장 실무적으로는 아래 3단 구성을 추천한다.

### 1) 짧은 운영 프롬프트
- 역할
- 작업 절차
- 금지사항
- 검증 절차

### 2) 별도 디자인 표준 문서
- 토큰
- 테마
- 컴포넌트
- 콘텐츠 원칙
- QA

### 3) 프로젝트별 브랜드 확장 문서
- 브랜드 색상
- 타입 램프
- 레이아웃 밀도
- imagery rules
- tone of voice

즉, 현재 프롬프트 하나에 모든 것을 몰아넣기보다:

- **Prompt = 행동 규칙**
- **Standard = 디자인 기준**
- **Brand Pack = 프로젝트별 예외**

로 분리하는 것이 가장 유지보수성이 좋다.

---

## 8. 바로 적용 가능한 축약 표준

실무에 즉시 붙이려면 아래만 먼저 고정해도 충분하다.

### Must
- 브랜드/기존 UI 맥락 우선
- theme는 token 계층으로 관리
- 신규 탐색은 3안 이상
- filler 콘텐츠 금지
- 엔트리는 1개 HTML 기준
- 완료 전 QA 체크리스트 통과

### Should
- tweak로 비교 가능한 상태 제공
- 파일 1000라인 초과 시 분할
- 슬라이드/스크린 라벨 명시
- 상태 복원(local persistence) 지원

### May
- 확장색 사용
- placeholder 사용
- 실험적 레이아웃/모션 제안

---

## 9. 결론

원문은 좋은 디자인 에이전트 운영 지침이지만, 그대로는 **프롬프트**에 가깝고 **디자인 표준**으로 쓰기에는 구조가 부족하다.

표준화의 핵심은 다음이다.

1. **디자인 철학과 플랫폼 규칙 분리**
2. **스타일/테마를 토큰 계층으로 재정의**
3. **질문/탐색/검증 절차를 SOP화**
4. **완료 정의와 QA 체크리스트 명문화**

이렇게 바꾸면 이 문서는 단순한 지시문이 아니라,
**디자인 가이드 + 스타일 시스템 + 테마 적용 규칙 + 구현 운영 규약**으로 바로 사용할 수 있다.
