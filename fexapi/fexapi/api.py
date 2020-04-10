# ?name=nome-da-extensao&last-update=1month
# /extension/1 - {...}
# /extension/?query=...  [{}, ..]  [GET]

from typing import List, Optional

import databases
import sqlalchemy
from fastapi import FastAPI
from pydantic import BaseModel

# SQLAlchemy specific code, as with any other app
DATABASE_URL = "postgresql://fexservice:password@localhost/fexservice"
# DATABASE_URL = "postgresql://user:password@postgresserver/db"

database = databases.Database(DATABASE_URL)

metadata = sqlalchemy.MetaData()

repos = sqlalchemy.Table(
    "repos",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String),
    sqlalchemy.Column("html_url", sqlalchemy.String),
    sqlalchemy.Column("description", sqlalchemy.Text, nullable=True),
)

engine = sqlalchemy.create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)
# metadata.create_all(engine)


class Repo(BaseModel):
    id: int
    name: str
    html_url: str
    description: Optional[str]


app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


@app.get("/extension/", response_model=List[Repo])
async def read_repos():
    query = repos.select()
    return await database.fetch_all(query)
