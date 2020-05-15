import sqlalchemy

import databases
from fexapi.config import settings

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
