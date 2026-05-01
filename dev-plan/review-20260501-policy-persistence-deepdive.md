# Review: Policy & Settings Runtime-only 분석 (코드 레벨 재검증)

> Generated: 2026-05-01 (Phase C 적용 후 재검증)
> Source: 외부 전문가 분석 ("Settings 변경은 메모리 only" + "subprocess 경계에서 끊김")
> Status: 분석 5항 중 4항은 Phase C(`d3e6e95`)로 이미 해결, 1항 + 신규 2항 남음

---

## 1. 외부 분석 요지

> "현재 Policy & Settings 변경값은 FastAPI 메모리에만 저장되고, `data/editorial_policy.yaml`도 DB도 아니고, 서버 재시작 시 사라진다. 더 큰 문제는 `scripts/run_daily.py`(별도 subprocess)가 메모리 override를 모르므로 실제 자동 파이프라인에 반영되지 않을 수 있고, `quotas`/`section_quotas` schema mismatch도 있다."

권고 4건 + 우선순위 가이드 1건이 함께 제시됨.

---

## 2. 코드 레벨 검증 결과

| # | 외부 분석 항목 | 검증 위치 | 상태 |
|---|---|---|---|
| 1 | `PolicyForm.toPatch()`에서 `quotas` 보냄 | `ui/src/components/PolicyForm.tsx:198` | ✅ **이미 `section_quotas`** — Phase C 처리 |
| 2 | run_runner가 runtime override를 subprocess에 전달 안 함 | `app/admin/run_runner.py:159, 196, 200` | ✅ **`_materialize_policy_override()` + `EDITORIAL_POLICY_PATH` env injection** — Phase C 처리 |
| 3 | run_daily.py에 `--policy-path` 옵션 없음 | `scripts/run_daily.py:1306` | ✅ **click option 존재** — Phase C 처리 |
| 4 | load_policy()가 env var를 안 봄 | `app/editorial/policy.py:15, 107` | ✅ **`POLICY_PATH_ENV = "EDITORIAL_POLICY_PATH"`, env 우선** — Phase C 처리 |
| 5 | UI 문구가 "실제 Run 미반영"까지 명확하지 않음 | `ui/src/components/PolicyForm.tsx:343, 516` | ⚠️ **부분만**: "runtime override only" / "Unsaved changes — runtime override only." |

### 진짜 남은 항목 (외부 분석 + 추가 발견)

| # | 항목 | 위치 | 영향 |
|---|---|---|---|
| **R1** | UI 안내 문구가 운영자에게 정확한 의미를 전달 못함 | `PolicyForm.tsx`의 dirty/saved 배너 | 운영자가 "yaml에 저장됐다" / "재시작 후에도 유지된다"고 오해 가능 |
| **R2** | 영구 yaml 저장 옵션 부재 | `app/admin/policy_admin.py`, `PolicyForm.tsx` | 운영자가 정책 영구화하려면 ssh로 yaml 직접 수정 필요 — 운영 도구로서 결함 |
| **R3** | 정책 우선순위 문서 부재 | `docs/news-studio-usage.md`, `dev-plan/` | "yaml < runtime override < per-run options" 우선순위가 어디에도 명문화 안 됨 |

---

## 3. 외부 분석에서 정정할 부분

외부 분석은 "subprocess에 override 전달 없음"이라고 단정했으나, 이는 **Phase C 적용 전 코드** 기준. 현재 코드는:

```
PUT /api/policy
  → policy_admin.set_policy_override(patch)        # in-memory _RUNTIME_OVERRIDE

POST /api/runs
  → run_runner._supervise()
  → _materialize_policy_override()                  # tempfile yaml dump
  → env[EDITORIAL_POLICY_PATH] = tmp_path
  → subprocess: scripts/run_daily.py
  → app.editorial.policy.load_policy()              # env_value 우선
  → 임시 yaml 로드 → DEFAULT_POLICY와 deep-merge
  → 정상 generate
```

즉 **현재는 runtime override가 subprocess까지 전달되며, 다음 Run에 반영된다**.

단, 다음은 여전히 사실:
- `data/editorial_policy.yaml` 파일 자체는 미수정.
- 서버 프로세스 재시작 시 `_RUNTIME_OVERRIDE`는 휘발.
- 영구 보존하려면 yaml을 사람이 직접 수정해야 함.

따라서 외부 분석의 핵심 지적("운영용으로 가려면 영구 저장 옵션이 필요")은 여전히 유효하다.

---

## 4. 권장 정책 우선순위 (확정)

```
data/editorial_policy.yaml          (low — disk truth, 영구 보존)
< Settings runtime override          (mid — 프로세스 메모리, 다음 Run에 자동 반영)
< NewReport per-run policy_override  (high — 단일 Run 임시 적용, 미구현)
```

**해석**:
- yaml: 영구 운영 정책. 변경하려면 명시적 "Save to yaml" 액션 또는 직접 수정.
- runtime override: 운영자가 실험·튜닝 중에 즉시 다음 Run에 반영. 재시작 시 사라짐.
- per-run override: 단일 Run 한정 (예: NewReport에서 옵션 변경 후 Run). 다음 Run에 영향 X — 현재 미구현이지만 향후 phase에서 필요.

---

## 5. 위험도 매트릭스 (재평가)

| 항목 | Phase C 전 | Phase C 후 |
|---|---|---|
| Settings 저장 후 실제 리포트에 반영됐다고 오해 | 🔴 높음 (실제로 반영 안 됨) | 🟡 중간 (반영되지만 "yaml에 저장됐다"고 오해 가능) |
| quota 변경 무시 | 🔴 높음 (schema mismatch) | 🟢 0 (Phase C 통일) |
| 서버 재시작 시 설정 유실 | 🟡 중간 | 🟡 중간 (변경 없음, 운영자 인지가 관건) |
| multi-worker 배포 시 worker별 분리 | 🟡 중간 | 🟡 중간 (변경 없음, 단일 프로세스 가정) |
| 테스트가 실제 pipeline 반영을 못 잡음 | 🔴 높음 | 🟢 낮음 (`test_policy_override_subprocess.py` 8 케이스) |

---

## 6. 권장 후속 작업 (Phase E 후보)

### R1 — UI 안내 정확화 (필수, 15분)
- `PolicyForm.tsx`의 dirty/saved 배너를 다국어 정확화:
  - dirty: "변경 중 — 저장 시 다음 Run부터 반영됩니다 (재시작 시 유실)"
  - saved: "다음 Run에 반영됩니다 · `data/editorial_policy.yaml`은 수정되지 않습니다 · 영구 저장은 [Persist] 버튼"
- 헬프 링크 또는 inline tooltip으로 "정책 우선순위" 설명.

### R2 — 영구 yaml 저장 옵션 (가성비 큼, 30~60분)
- BE: `POST /api/policy/persist` — `_RUNTIME_OVERRIDE`를 yaml에 머지 dump (atomic write, 백업 `*.yaml.bak`).
- FE: PolicyForm 푸터에 `[Persist to yaml]` 버튼 (확인 다이얼로그 필수).
- 단위 테스트 + 라이브 검증.

### R3 — 정책 우선순위 문서화 (10분)
- `docs/news-studio-usage.md`에 "Policy precedence" 섹션 신규.
- `DESIGN.md` 또는 `dev-plan/`에서 "정책 변경 영향 범위" 표 추가.

---

## 7. 결론

외부 분석은 **Phase C 적용 직전 코드** 기준으로는 정확했지만, 현재 main에서는 4/5 항목이 이미 처리됐다. 남은 핵심은 **운영자에게 "현재 동작이 임시 override임"을 더 정확히 전달하고, 영구 저장 경로를 명시적으로 제공**하는 일.

이는 코드 갭이 아니라 **운영 UX 갭**에 가깝다. Phase E로 별도 처리.
