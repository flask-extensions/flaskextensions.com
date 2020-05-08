from datetime import datetime
from typing import List, Optional

import databases
import sqlalchemy
from dynaconf import settings
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from . import queries

database = databases.Database(settings.DATABASE_URL)

metadata = sqlalchemy.MetaData()

repos = sqlalchemy.Table(
    "repos",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String),
    sqlalchemy.Column("html_url", sqlalchemy.String),
    sqlalchemy.Column("description", sqlalchemy.Text, nullable=True),
    sqlalchemy.Column("created_at", sqlalchemy.DateTime, nullable=True),
    sqlalchemy.Column("updated_at", sqlalchemy.DateTime, nullable=True),
    sqlalchemy.Column("stargazers_count", sqlalchemy.Integer),
    sqlalchemy.Column("forks_count", sqlalchemy.Integer),
)


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
    

app = FastAPI()

origins = [settings.CORS_ORIGINS]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


@app.get("/extension/", response_model=Result)
async def read_repos(
    query: Optional[str] = None,
    per_page: Optional[int] = 12,
    page: Optional[int] = 1
):
    sql = queries.BASE
    values = {}
    if query:
        sql += queries.SEARCH
        values["term"] = f"{query}:*"

    total_rows = await database.fetch_one(
        query=sql.format(fields=queries.COUNT)
    )
    total_rows = total_rows.get("total")

    sql += queries.ORDER
    
    
    sql += queries.PAGINATION.format(limit=per_page, offset=(page - 1) * per_page)
    result = await database.fetch_all(
        query=sql.format(fields=queries.FIELDS),
        values=values
    )
    
    page = queries.Page(items=result, page=page, page_size=per_page, total=total_rows)
 
    """
    {
        "pagination": {
            "total": 100,
            "page_size": 1,
            "page": 1,
            "previous": null,
            "next": null,
            "pages": 1
        }
        "items": [
            {"id": ..., "name": ...},
            ...
        ]
    }
    """

    return Result(
        page=PageModel(**page.to_dict()),
        items=result        
    )




