"""
Autor - Douglas d'Auriol <ddauriol@gmail.com>
Baseado na Live de Python e na documentação do dynaconf
https://dynaconf.readthedocs.io/en/latest/guides/validation.html
"""
from dynaconf import Validator

validators = [
    # Ensure some parameters exists (are required)
    Validator(
        "DATABASE_URL",
        "GITHUB_TOKEN",
        "SEARCH_QUERY",
        "DELAY",
        "PRIORITY",
        must_exist=True,
    ),
    # Ensure some parameter mets a condition
    # conditions: (eq, ne, lt, gt, lte, gte, identity, is_type_of, is_in, is_not_in)
    # Validação de um valor mínimo para o DELAY e a PRIORITY
    Validator("DELAY", gte=10),
    Validator("PRIORITY", gte=100),
    # SQLITE cannot be used in production
    Validator(
        "DATABASE_URL",
        condition=lambda value: "sqlite://" not in value,
        env="PRODUCTION",
    ),
    # GITHUB_TOKEN must have been set by the user
    Validator(
        "GITHUB_TOKEN",
        ne="<Your Real Token Here or in ./fexservice/.secrets.toml>",
    ),
]
