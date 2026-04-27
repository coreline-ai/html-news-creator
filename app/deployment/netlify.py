from __future__ import annotations
import asyncio
import subprocess
from pathlib import Path
from app.utils.logger import get_logger


class NetlifyPublisher:
    def __init__(self, site_id: str = "", auth_token: str = ""):
        self.site_id = site_id
        self.auth_token = auth_token
        self.logger = get_logger(step="publish")

    async def deploy(self, publish_dir: str = "public") -> dict:
        """
        Deploy public/ directory to Netlify using netlify-cli.
        Returns: {status, deploy_url, error}
        """
        cmd = ["netlify", "deploy", "--prod", "--dir", publish_dir]
        if self.site_id:
            cmd += ["--site", self.site_id]
        if self.auth_token:
            cmd += ["--auth", self.auth_token]

        try:
            result = await asyncio.to_thread(
                subprocess.run,
                cmd,
                capture_output=True,
                text=True,
                timeout=120,
            )
            if result.returncode == 0:
                self.logger.info("netlify_deploy_success", stdout=result.stdout[:200])
                return {"status": "success", "deploy_url": "", "stdout": result.stdout}
            else:
                self.logger.error("netlify_deploy_failed", stderr=result.stderr[:200])
                return {"status": "failed", "error": result.stderr}
        except FileNotFoundError:
            self.logger.warning("netlify_cli_not_found", note="Install with: npm i -g netlify-cli")
            return {"status": "skipped", "error": "netlify CLI not installed"}
        except Exception as e:
            self.logger.error("netlify_deploy_error", error=str(e))
            return {"status": "failed", "error": str(e)}
