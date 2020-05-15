from typing import List, Optional

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fexapi import queries
from fexapi.config import settings
from fexapi.db import database, repos
from fexapi.models import PageModel, Repo, Result

app = FastAPI(
    on_startup=[database.connect], on_shutdown=[database.disconnect],
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[settings.CORS_ORIGINS],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/extension/", response_model=Result)
async def read_repos(
    query: Optional[str] = None,
    per_page: Optional[int] = 12,
    page: Optional[int] = 1,
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

    sql += queries.PAGINATION.format(
        limit=per_page, offset=(page - 1) * per_page
    )
    result = await database.fetch_all(
        query=sql.format(fields=queries.FIELDS), values=values
    )

    page = queries.Page(
        items=result, page=page, page_size=per_page, total=total_rows
    )

    return Result(page=PageModel(**page.to_dict()), items=result)
