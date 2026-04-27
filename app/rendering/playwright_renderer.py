from __future__ import annotations
import asyncio
from pathlib import Path
from app.utils.logger import get_logger


class PlaywrightUnavailableError(Exception):
    pass


class PlaywrightRenderer:
    def __init__(self):
        self.logger = get_logger(step="render")
        try:
            from playwright.async_api import async_playwright
            self._playwright_module = async_playwright
        except ImportError:
            self._playwright_module = None

    async def screenshot(self, html_path: str, output_path: str, width: int = 1200, height: int = 630) -> Path:
        """
        Take a PNG screenshot of the HTML file.
        Returns Path to the output file.
        """
        if self._playwright_module is None:
            raise PlaywrightUnavailableError("playwright not installed")

        async with self._playwright_module() as pw:
            browser = await pw.chromium.launch(headless=True)
            page = await browser.new_page(viewport={"width": width, "height": height})

            abs_path = Path(html_path).resolve()
            await page.goto(f"file://{abs_path}")
            await page.wait_for_load_state("networkidle")

            output = Path(output_path)
            output.parent.mkdir(parents=True, exist_ok=True)
            await page.screenshot(path=str(output), full_page=False)
            await browser.close()

        self.logger.info("screenshot_done", path=str(output), size_bytes=output.stat().st_size)
        return output

    async def export_pdf(self, html_path: str, output_path: str) -> Path:
        """Export HTML to PDF using Playwright."""
        if self._playwright_module is None:
            raise PlaywrightUnavailableError("playwright not installed")

        async with self._playwright_module() as pw:
            browser = await pw.chromium.launch(headless=True)
            page = await browser.new_page()

            abs_path = Path(html_path).resolve()
            await page.goto(f"file://{abs_path}")
            await page.wait_for_load_state("networkidle")

            output = Path(output_path)
            output.parent.mkdir(parents=True, exist_ok=True)
            await page.pdf(path=str(output), format="A4")
            await browser.close()

        self.logger.info("pdf_done", path=str(output), size_bytes=output.stat().st_size)
        return output
