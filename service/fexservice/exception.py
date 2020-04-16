"""
Autor - Jairo Matos da Rocha <devjairomr@gmail.com>
As exceções estão organizada por nivel
https://docs.sqlalchemy.org/en/13/core/exceptions.html
https://pygithub.readthedocs.io/en/latest/utilities.html
"""
from github.GithubException import BadAttributeException  # TODO
from github.GithubException import BadUserAgentException  # TODO
from github.GithubException import IncompletableObject  # TODO
from github.GithubException import (BadCredentialsException,
                                    RateLimitExceededException,
                                    TwoFactorException, UnknownObjectException)
from requests.exceptions import ConnectionError  # Error de conexão
from requests.exceptions import ReadTimeout  # Error de conexão
from sqlalchemy.exc import OperationalError

ConsumerWarning = (
    ReadTimeout,
    ConnectionError,
    RateLimitExceededException,
    UnknownObjectException,
)
ConsumerCritical = (
    BadCredentialsException,
    TwoFactorException,
    OperationalError,
    AttributeError,
)
