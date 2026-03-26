from __future__ import annotations

from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from typing import Optional


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


@dataclass(slots=True)
class PostRecord:
    post_id: str
    url: str
    title: str
    body: str
    author: Optional[str] = None
    created_at: Optional[str] = None
    scraped_at: str = field(default_factory=utc_now_iso)
    source: str = "autohome"


@dataclass(slots=True)
class CommentRecord:
    comment_id: str
    post_id: str
    comment_text: str
    comment_author: Optional[str] = None
    comment_created_at: Optional[str] = None
    parent_comment_id: Optional[str] = None
    scraped_at: str = field(default_factory=utc_now_iso)


@dataclass(slots=True)
class ScrapeResult:
    posts: list[PostRecord] = field(default_factory=list)
    comments: list[CommentRecord] = field(default_factory=list)
    errors: list[str] = field(default_factory=list)

    @property
    def posts_count(self) -> int:
        return len(self.posts)

    @property
    def comments_count(self) -> int:
        return len(self.comments)

    def to_dict(self) -> dict:
        return {
            "posts_count": self.posts_count,
            "comments_count": self.comments_count,
            "errors": self.errors,
            "posts": [asdict(p) for p in self.posts],
            "comments": [asdict(c) for c in self.comments],
        }
