import dataset
from dynaconf import settings
from github import Github

github = Github(settings.GITHUB_TOKEN)

db = dataset.connect(settings.DATABASE_URL, engine_kwargs={"echo": True})
repo = db["repos"]


def fetch_github():
    """Fetches Github api and stores in database."""
    repositories = github.search_repositories(
        query=settings.SEARCH_QUERY, sort="stars"
    )

    # print(len(list(repositories)))

    for item in repositories:
        data = dict(
            id=item.id,
            name=item.name,
            full_name=item.full_name,
            html_url=item.html_url,
            description=item.description,
        )
        repo.upsert(data, ["id"])
