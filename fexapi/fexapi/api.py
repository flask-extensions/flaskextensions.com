# ?name=nome-da-extensao&last-update=1month
# /extension/1 - {...}
# /extension/?query=...  [{}, ..]  [GET]

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


@app.get("/extension/", response_model=List[Repo])
async def read_repos():
    # /extension/?search="login"
    query = repos.select()
    return await database.fetch_all(query)
