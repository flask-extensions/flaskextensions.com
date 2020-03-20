import dataset
from dynaconf import settings
from github import Github

github = Github(settings.GITHUB_TOKEN)

repositories = github.search_repositories(
    query=settings.SEARCH_QUERY, sort="stars"
)

db = dataset.connect(settings.DATABASE_URL, engine_kwargs={"echo": True})
repo = db["repos"]

repo.insert_many(
    [
        dict(
            id=item.id,
            name=item.name,
            full_name=item.full_name,
            html_url=item.html_url,
            description=item.description,
        )
        for item in repositories
    ]
)

print(repo.find_one(name="dynaconf")["name"])
for repo in repo.all():
    print(repo["name"])

# table = repo.table
# statement = table.select(table.c.name.like("%api%"))
# result = db.query(statement)
# print(list(result))
