def collect_thread_urls(self, start_url: str, max_pages: int) -> list[str]:
    thread_urls = []

    for page in range(1, max_pages + 1):
        url = self._build_page_url(start_url, page)

        self.driver.get(url)

        links = self.driver.find_elements("css selector", "a[href*='thread']")

        for link in links:
            href = link.get_attribute("href")
            if href:
                thread_urls.append(href)

    return list(set(thread_urls)) 
