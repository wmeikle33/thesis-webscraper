from dataclasses import dataclass
from pathlib import Path

SECTION_URLS = {
    "used-cars": "https://club.autohome.com.cn/...",
    "news": "https://club.autohome.com.cn/...",
}

@dataclass
class ScrapeConfig:
    section: str
    pages: int = 1
    out_dir: Path = Path("data")
    headless: bool = True
    delay_ms: int = 1200
    jitter: float = 0.4
    max_retries: int = 2
    resume: bool = False
    save_raw_html: bool = False
    verbose: bool = False

    @property
    def start_url(self) -> str:
        return SECTION_URLS[self.section]

    @property
    def delay_min_s(self) -> float:
        base = self.delay_ms / 1000.0
        return max(0.0, base * (1.0 - self.jitter))

    @property
    def delay_max_s(self) -> float:
        base = self.delay_ms / 1000.0
        return base * (1.0 + self.jitter)

    def validate(self) -> list[str]:
        errors = []
        if self.section not in SECTION_URLS:
            errors.append(f"Unknown section: {self.section}")
        if self.pages < 1:
            errors.append("pages must be >= 1")
        return errors
