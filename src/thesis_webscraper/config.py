# src/thesis_webscraper/config.py
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass
class ScrapeConfig:
    start_url: str
    pages: int = 1
    out: Path = Path("data/posts.csv")
    headless: bool = True
    browser: str = "chrome"
    delay_ms: int = 1200
    jitter: float = 0.4
    max_retries: int = 2
    save_raw_html: bool = False
    resume: bool = False
    verbose: bool = False

    @property
    def delay_min_s(self) -> float:
        base = self.delay_ms / 1000.0
        return max(0.0, base * (1.0 - self.jitter))

    @property
    def delay_max_s(self) -> float:
        base = self.delay_ms / 1000.0
        return base * (1.0 + self.jitter)

    def validate(self) -> list[str]:
        problems: list[str] = []

        if not self.start_url:
            problems.append("start_url is required")
        if self.pages < 1:
            problems.append("pages must be >= 1")
        if self.browser not in {"chrome", "edge", "firefox"}:
            problems.append("browser must be one of: chrome, edge, firefox")
        if self.delay_ms < 0:
            problems.append("delay_ms must be >= 0")
        if self.jitter < 0:
            problems.append("jitter must be >= 0")
