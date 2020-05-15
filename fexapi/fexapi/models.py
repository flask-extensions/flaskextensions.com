from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel


class Repo(BaseModel):
    id: int
    name: str
    html_url: str
    description: Optional[str]
    created_at: datetime
    updated_at: datetime
    stargazers_count: int
    forks_count: int


class PageModel(BaseModel):
    total: int
    page_size: int
    page: int
    previous: Optional[int]
    next: Optional[int]
    pages: int


class Result(BaseModel):
    page: PageModel
    items: List[Repo]
