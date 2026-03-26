from __future__ import annotations

from bs4 import BeautifulSoup

from .models import Post


def parse_list(html: str) -> list[str]:
    soup = BeautifulSoup(html, "html.parser")

    urls: list[str] = []
    for a in soup.select("a[href]"):
        href = a.get("href")
        if not href:
            continue

        # tighten this rule to match your real Autohome post URLs
        if href.startswith("http"):
            urls.append(href)

    # preserve order, remove duplicates
    return list(dict.fromkeys(urls))


def parse_post(html: str, url: str) -> Post:
    soup = BeautifulSoup(html, "html.parser")

    title_el = soup.select_one(".post-title")
    title = title_el.get_text(strip=True) if title_el else ""

    body_el = soup.select_one(".tz-paragraph")
    body = body_el.get_text("\n", strip=True) if body_el else ""

    comments = [
        el.get_text(strip=True)
        for el in soup.select(".reply-detail")
        if el.get_text(strip=True)
    ]

    subcomments = [
        el.get_text(strip=True)
        for el in soup.select(".reply-sub-front")
        if el.get_text(strip=True)
    ]

    return Post(
        url=url,
        title=title,
        body=body,
        comments=comments,
        subcomments=subcomments,
    )
