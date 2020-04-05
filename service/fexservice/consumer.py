import dataset
from dynaconf import settings
from github import Github
from github.GithubException import BadCredentialsException
from github.GithubException import UnknownObjectException
from github.GithubException import BadUserAgentException # TODO
from github.GithubException import RateLimitExceededException
from github.GithubException import BadAttributeException # TODO
from github.GithubException import TwoFactorException
from github.GithubException import IncompletableObject # TODO
from requests.exceptions import ReadTimeout #Error de conexão
from requests.exceptions import ConnectionError #Error de conexão
from sqlalchemy.exc import OperationalError
from fexservice.logger import create_logger

logger = create_logger(__name__)

try:
    github = Github(settings.GITHUB_TOKEN)
except AttributeError as e:
    logger.critical(e)
    exit(1)


if 'sqlite:' == settings.DATABASE_URL[:7]:
    # Check which is the database system, and if it is sqlite, send an alert that
    # the sqlite database is being used
    logger.warning(
        "Attention you are using the sqlite database, if this is the "+
        "database system you are trying to use also this message"
    )

db = dataset.connect(settings.DATABASE_URL, engine_kwargs={"echo": True})
repo = db["repos"]


class FetchError(Exception):
    ...


def fetch_github():
    """Fetches Github api and stores in database."""
    try:
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
                # TODO: falta colocar: data de ultimo commit/release
                # TODO: quant stars
                # TODO: quant de contribuidores
            )
            repo.upsert(data, ["id"])
    # Erros de Internet
    except ReadTimeout as e:
        logger.warning(e)
    except ConnectionError as e:
        logger.warning(e)
    # Erros no GitHub
    # Git except https://pygithub.readthedocs.io/en/latest/utilities.html
    except RateLimitExceededException as e:
        logger.warning(e)
    except UnknownObjectException as e:
        logger.warning(e)
    except BadCredentialsException  as e:
        # Erro na configuração
        logger.critical(e)
        exit(1)
    except TwoFactorException as e:
        logger.critical(e)
        exit(1)
    # Erros do banco de dados
    # https://docs.sqlalchemy.org/en/13/core/exceptions.html
    except OperationalError as e:
        logger.critical(e)
        exit(1)
    # Erros na Configuração
    except AttributeError as e:
        logger.critical(e)
        exit(1)

    #
