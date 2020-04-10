import dataset
from dynaconf import settings, Validator
from github import Github
from github.GithubException import BadAttributeException  # TODO
from github.GithubException import BadUserAgentException  # TODO
from github.GithubException import IncompletableObject  # TODO
from github.GithubException import (BadCredentialsException,
                                    RateLimitExceededException,
                                    TwoFactorException, UnknownObjectException)
from requests.exceptions import ConnectionError  # Error de conexão
from requests.exceptions import ReadTimeout  # Error de conexão
from sqlalchemy.exc import OperationalError

import fexservice.validator
from fexservice.logger import create_logger

logger = create_logger(__name__)

# Fire the validator settings
settings.validators.validate()

try:
    github = Github(settings.GITHUB_TOKEN)
except AttributeError as e:
    logger.critical(e)
    exit(1)

# TODO: Usar dynaconf Validators
if "sqlite:" == settings.DATABASE_URL[:7]:
    # Check which is the database system, and if it is sqlite, send an alert that
    # the sqlite database is being used
    logger.warning(
        "Attention you are using the sqlite database, if this is the "
        + "database system you are trying to use also this message"
    )

# TODO: ConnectionError
db = dataset.connect(settings.DATABASE_URL, engine_kwargs={"echo": True})
repo = db["repos"]


def fetch_github():
    """Fetches Github api and stores in database."""
    try:
        repositories = github.search_repositories(
            query=settings.SEARCH_QUERY, sort="stars"
        )

        for item in repositories:
            data = dict(
                id=item.id,
                name=item.name,
                full_name=item.full_name,
                html_url=item.html_url,
                description=item.description,
                created_at=item.created_at,
                updated_at=item.updated_at,
                stargazers_count=item.stargazers_count,
                forks_count=item.forks_count
            )
            repo.upsert(data, ["id"])
    # Erros de Internet
    except (ConnectionError, ReadTimeout) as e:
        logger.warning(e)
    # Erros no GitHub
    # Git except https://pygithub.readthedocs.io/en/latest/utilities.html
    except (UnknownObjectException, RateLimitExceededException) as e:
        logger.warning(e)
    except (TwoFactorException, BadCredentialsException) as e:
        # Erro na configuração
        logger.critical(e)
        exit(1)
    # Erros do banco de dados
    # https://docs.sqlalchemy.org/en/13/core/exceptions.html
    except OperationalError as e:
        logger.critical(e)
        exit(1)