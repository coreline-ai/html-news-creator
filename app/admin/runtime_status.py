"""Runtime dependency checks for News Studio.

The dashboard uses these checks to fail before a pipeline subprocess is queued.
"""
from __future__ import annotations

import asyncio
import shlex
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

import httpx

from app.config import settings

PIPELINE_STEPS: tuple[str, ...] = (
    "collect",
    "extract",
    "classify",
    "cluster",
    "verify",
    "image_analyze",
    "generate",
    "render",
    "publish",
    "notify",
)
LLM_REQUIRED_STEPS: frozenset[str] = frozenset({"classify", "verify", "generate"})
LOCAL_PROXY_HOSTS: frozenset[str] = frozenset({"127.0.0.1", "localhost"})
LOCAL_PROXY_PORT = 4317
PROXY_HEALTH_TIMEOUT_SEC = 2.0
PROXY_RECOVERY_POLL_ATTEMPTS = 8
PROXY_RECOVERY_POLL_INTERVAL_SEC = 1.0
PROJECT_ROOT = Path(__file__).resolve().parents[2]
PROXY_RECOVERY_LOG_PATH = PROJECT_ROOT / ".logs" / "llm_proxy_recovery.log"

_RECOVERY_LOCK = asyncio.Lock()
_RECOVERY_PROCESS: asyncio.subprocess.Process | None = None


class RuntimeDependencyError(RuntimeError):
    """Raised when an operator tries to start a run without dependencies."""

    def __init__(self, payload: dict[str, Any]) -> None:
        self.payload = payload
        message = str(payload.get("message") or "runtime dependency unavailable")
        super().__init__(message)


def local_proxy_health_url(openai_base_url: str) -> str | None:
    """Return the health URL when the configured OpenAI base URL is local proxy."""
    parsed = urlparse(openai_base_url)
    if parsed.hostname not in LOCAL_PROXY_HOSTS:
        return None
    if parsed.port != LOCAL_PROXY_PORT:
        return None
    return f"{parsed.scheme}://{parsed.netloc}/api/v1/health"


def _normalise_step(value: Any, fallback: str) -> str:
    step = str(value or fallback)
    return step if step in PIPELINE_STEPS else fallback


def steps_for_run_options(options: dict[str, Any] | None) -> list[str]:
    """Mirror the CLI step slice enough to decide if LLM access is needed."""
    opts = dict(options or {})
    mode = str(opts.get("mode") or "full")
    from_step = _normalise_step(opts.get("from_step"), "collect")
    to_step = _normalise_step(opts.get("to_step"), "notify")
    from_idx = PIPELINE_STEPS.index(from_step)
    to_idx = PIPELINE_STEPS.index(to_step)
    if from_idx > to_idx:
        from_idx, to_idx = to_idx, from_idx
    steps = list(PIPELINE_STEPS[from_idx : to_idx + 1])
    if mode == "rss-only":
        steps = [step for step in steps if step in {"collect", "render"}]
    return steps


def run_requires_llm(options: dict[str, Any] | None) -> bool:
    return any(step in LLM_REQUIRED_STEPS for step in steps_for_run_options(options))


async def _check_proxy_health(health_url: str) -> tuple[bool, dict[str, Any] | None, str | None]:
    try:
        async with httpx.AsyncClient(timeout=PROXY_HEALTH_TIMEOUT_SEC) as client:
            response = await client.get(health_url)
            response.raise_for_status()
            payload = response.json()
        if not isinstance(payload, dict):
            return False, None, "health payload was not a JSON object"
        if payload.get("ok") is not True:
            return False, payload, f"unexpected health payload: {payload}"
        return True, payload, None
    except Exception as exc:  # pragma: no cover - exact httpx subtype is not useful here.
        return False, None, str(exc)


def _llm_unavailable_message(health_url: str) -> str:
    return (
        "LLM 프록시가 꺼져 있어 classify/verify/generate 단계가 포함된 "
        f"뉴스 생성 실행을 시작할 수 없습니다. health={health_url}"
    )


def _recovery_scenarios(health_url: str | None) -> list[dict[str, str]]:
    if not health_url or not settings.news_studio_llm_proxy_start_command:
        return []
    return [
        {
            "code": "local_make_proxy",
            "label": "로컬 LLM 프록시 시작",
            "command": settings.news_studio_llm_proxy_start_command,
            "description": "FastAPI 서버가 프로젝트 루트에서 설정된 프록시 시작 명령을 실행합니다.",
        }
    ]


async def get_system_status() -> dict[str, Any]:
    """Return dashboard-safe runtime status without throwing on proxy outages."""
    health_url = local_proxy_health_url(settings.openai_base_url)
    llm: dict[str, Any] = {
        "openai_base_url": settings.openai_base_url,
        "openai_model": settings.openai_model,
        "proxy_required": bool(health_url),
        "proxy_health_url": health_url,
        "proxy_reachable": True,
        "status": "external",
        "message": "외부 OpenAI-compatible endpoint 설정입니다. 로컬 프록시 상태 확인은 생략합니다.",
        "start_command": None,
        "recovery_supported": False,
        "recovery_endpoint": None,
        "recovery_scenarios": [],
    }

    if not health_url:
        return {"can_generate": True, "llm": llm}

    ok, payload, error = await _check_proxy_health(health_url)
    llm.update(
        {
            "proxy_reachable": ok,
            "status": "ready" if ok else "unavailable",
            "message": (
                "LLM 프록시가 정상 응답 중입니다. 뉴스 생성 실행이 가능합니다."
                if ok
                else _llm_unavailable_message(health_url)
            ),
            "start_command": settings.news_studio_llm_proxy_start_command,
            "recovery_supported": bool(settings.news_studio_llm_proxy_start_command),
            "recovery_endpoint": (
                "/api/system/proxy/recover"
                if settings.news_studio_llm_proxy_start_command
                else None
            ),
            "recovery_scenarios": _recovery_scenarios(health_url),
            "health_payload": payload,
            "last_error": error,
        }
    )
    return {"can_generate": ok, "llm": llm}


async def _launch_proxy_start_command(command: str) -> int:
    argv = shlex.split(command)
    if not argv:
        raise RuntimeError("LLM proxy start command is empty")

    global _RECOVERY_PROCESS
    PROXY_RECOVERY_LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    with PROXY_RECOVERY_LOG_PATH.open("ab") as log_file:
        process = await asyncio.create_subprocess_exec(
            *argv,
            cwd=str(PROJECT_ROOT),
            stdout=log_file,
            stderr=asyncio.subprocess.STDOUT,
            start_new_session=True,
        )
    _RECOVERY_PROCESS = process
    return int(process.pid or 0)


async def recover_local_proxy() -> dict[str, Any]:
    """Best-effort recovery for the local OpenAI-compatible proxy."""
    async with _RECOVERY_LOCK:
        before = await get_system_status()
        llm = before.get("llm") if isinstance(before.get("llm"), dict) else {}
        if before.get("can_generate") is True:
            return {
                "status": "ready",
                "action": "noop",
                "started": False,
                "message": "LLM 프록시가 이미 정상 응답 중입니다.",
                "system_status": before,
            }

        command = str(llm.get("start_command") or "").strip()
        health_url = llm.get("proxy_health_url")
        if not health_url or not command:
            return {
                "status": "unsupported",
                "action": "none",
                "started": False,
                "message": "현재 설정에서는 자동 프록시 복구를 지원하지 않습니다.",
                "system_status": before,
            }

        pid = await _launch_proxy_start_command(command)
        for _ in range(PROXY_RECOVERY_POLL_ATTEMPTS):
            await asyncio.sleep(PROXY_RECOVERY_POLL_INTERVAL_SEC)
            current = await get_system_status()
            if current.get("can_generate") is True:
                return {
                    "status": "ready",
                    "action": "started",
                    "started": True,
                    "pid": pid,
                    "message": "LLM 프록시 복구가 완료되었습니다.",
                    "system_status": current,
                    "log_path": str(PROXY_RECOVERY_LOG_PATH.relative_to(PROJECT_ROOT)),
                }

            if _RECOVERY_PROCESS and _RECOVERY_PROCESS.returncode is not None:
                return {
                    "status": "failed",
                    "action": "started",
                    "started": True,
                    "pid": pid,
                    "message": "프록시 시작 명령이 조기 종료되었습니다. 복구 로그를 확인하세요.",
                    "system_status": current,
                    "log_path": str(PROXY_RECOVERY_LOG_PATH.relative_to(PROJECT_ROOT)),
                }

        current = await get_system_status()
        return {
            "status": "starting",
            "action": "started",
            "started": True,
            "pid": pid,
            "message": "프록시 시작 명령을 실행했습니다. 아직 health check 응답을 기다리는 중입니다.",
            "system_status": current,
            "log_path": str(PROXY_RECOVERY_LOG_PATH.relative_to(PROJECT_ROOT)),
        }


async def ensure_can_start_run(options: dict[str, Any] | None) -> None:
    """Raise a 409-mappable error when an LLM run would fail immediately."""
    opts = dict(options or {})
    if not run_requires_llm(opts):
        return
    status = await get_system_status()
    if status.get("can_generate") is True:
        return
    llm = status.get("llm") if isinstance(status.get("llm"), dict) else {}
    raise RuntimeDependencyError(
        {
            "code": "llm_proxy_unavailable",
            "message": llm.get("message") or "LLM 프록시가 준비되지 않았습니다.",
            "requires_action": True,
            "system_status": status,
        }
    )
