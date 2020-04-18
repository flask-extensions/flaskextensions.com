# Faz o build do projeto dentro do docker
FROM python:3.8 AS build-env
ARG POETRY_VERSION=1.0.5
RUN pip install poetry=="$POETRY_VERSION"
# Copia o lockfile e pyproject.toml primeiro para cachear melhor a imagem
COPY ./service/pyproject.toml /service/pyproject.toml
COPY ./service/poetry.lock /service/poetry.lock
COPY ./service /service
WORKDIR /service
RUN poetry build

# Instala e roda o projeto já empacotado
FROM python:3.8 AS exec-env
COPY --from=build-env /service/dist .
RUN pip install *.whl
WORKDIR /service
CMD ["fexservice"]
