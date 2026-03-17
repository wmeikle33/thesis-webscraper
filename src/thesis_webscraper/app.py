from pathlib import Path


def run_scrape(
    *,
    query: str | None,
    start_url: str | None,
    max_pages: int,
    out_dir: Path,
    headless: bool,
    delay_ms: int,
    retries: int,
    resume: bool,
) -> None:
    raise NotImplementedError("Wire this to your existing scraper entrypoint.")
