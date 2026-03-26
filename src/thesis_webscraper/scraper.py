from __future__ import annotations

from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .config import ScrapeConfig
from .list_crawler import parse_post
from .models import ScrapeResult


class ThesisWebscraper:
    def __init__(self, cfg: ScrapeConfig):
        self.cfg = cfg
        self.driver = self._make_driver()

    def _make_driver(self) -> webdriver.Chrome:
        opts = ChromeOptions()
        if self.cfg.headless:
            opts.add_argument("--headless=new")
        opts.add_argument("--no-sandbox")
        opts.add_argument("--disable-dev-shm-usage")
        opts.add_argument("--window-size=1280,900")

        driver = webdriver.Chrome(options=opts)
        return driver

    def close(self) -> None:
        try:
            self.driver.quit()
        except Exception:
            pass

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, tb):
        self.close()

    def fetch_html(self, url: str) -> str:
        self.driver.get(url)
        WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )
        return self.driver.page_source

    def scrape_thread(self, url: str):
        html = self.fetch_html(url)
        return parse_post(html, url)


def scrape(cfg: ScrapeConfig) -> ScrapeResult:
    result = ScrapeResult()

    # For now, assume cfg.start_urls exists and contains thread URLs.
    with ThesisWebscraper(cfg) as scraper:
        for url in cfg.start_urls:
            try:
                post, comments = scraper.scrape_thread(url)
                result.posts.append(post)
                result.comments.extend(comments)
            except Exception as e:
                result.errors.append(f"{url}: {e}")

    return result
