# Faz o build do projeto dentro do docker
FROM python:3.8 AS build-env
ARG POETRY_VERSION=1.0.5
RUN pip install poetry=="$POETRY_VERSION"
# Copia o lockfile e pyproject.toml primeiro para cachear melhor a imagem
COPY ./fexapi/pyproject.toml /fexapi/poetry.lock /fexapi/
COPY ./fexapi /fexapi
WORKDIR /fexapi
RUN poetry build

# Instala e roda o projeto já empacotado
FROM python:3.8 AS exec-env 
COPY --from=build-env /fexapi/dist .
RUN ls
RUN pip install *.whl
WORKDIR /fexapi
CMD ["uvicorn", "fexapi.api:app", "--host=0.0.0.0", "--reload"]
