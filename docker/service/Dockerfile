# Faz o build do projeto dentro do docker
FROM python:3.8 AS build-env
ARG POETRY_VERSION=1.0.5
RUN pip install poetry=="$POETRY_VERSION"
# Copia o lockfile e pyproject.toml primeiro para cachear melhor a imagem
COPY ./fexservice/pyproject.toml /fexservice/pyproject.toml
COPY ./fexservice/poetry.lock /fexservice/poetry.lock
COPY ./fexservice /fexservice
WORKDIR /fexservice
RUN poetry build

# Instala e roda o projeto já empacotado
FROM python:3.8 AS exec-env
COPY --from=build-env /fexservice/dist .
RUN pip install *.whl
WORKDIR /fexservice
CMD ["fexservice"]
