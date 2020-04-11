FROM python:3.8

ARG POETRY_VERSION=1.0.5

RUN pip install poetry=="$POETRY_VERSION"

COPY service /service

WORKDIR /service

RUN poetry install

CMD ["poetry", "run", "fexservice"]
