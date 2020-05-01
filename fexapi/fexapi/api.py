from datetime import datetime
from typing import List, Optional

import databases
import sqlalchemy
from dynaconf import settings
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

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


QUERY_TEMPLATE = """
SELECT
    id, name, html_url, description, created_at,
    updated_at, stargazers_count, forks_count
FROM "repos"
WHERE to_tsvector(name || ' ' || description)
@@ plainto_tsquery(:term)
"""


@app.get("/extension/", response_model=List[Repo])
async def read_repos(query: str = None):
    if not query:
        return await database.fetch_all(repos.select())

    return await database.fetch_all(
        query=QUERY_TEMPLATE, values={"term": query}
    )
