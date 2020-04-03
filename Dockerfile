FROM python:3.8

RUN pip install poetry

COPY service /

WORKDIR /service

RUN poetry install

CMD poetry run fexservice
