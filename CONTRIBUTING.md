# Using Docker
> **recommended**

## requirements

- Docker
- Docker Compose

## Setting up your configuration

copy the file `.example.variables.env` to a file called `.variables.env`

Fill the key `FEXSERVICE_GITHUB_TOKEN` with your own Github access token.

## Building

At the same folder where `docker-compose.yaml` is located run:

```bash
docker-compose build --force-rm
```

## Running

```bash
docker-compose up --force-recreate
```

> **NOTE** you can also put a `-d` at the end of previous command to run as a background daemon.

## Acessing

API is on: http://localhost:8000/docs

web UI is on: http://localhost:5500

You can access the console of the fexservice 

```bash
docker-compose exec fexservice bash
```

# Without Docker

## Requirements

- Python3+
- Poetry
- A running instance of some SQL database (sqlite, postgres, mysql)

## Settings

This are the required environment variables

- **FEXSERVICE_DATABASE_URL**

    e.g: `FEXSERVICE_DATABASE_URL=sqlite:///path/database.db`  

- **FEXAPI_DATABASE_URL**

    e.g: `FEXAPI_DATABASE_URL=sqlite:///path/database.db`  

- **FEXSERVICE_GITHUB_TOKEN**

    e.g: `FEXSERVICE_GITHUB_TOKEN="049854309jvfg8dg7df98gh7"`  

> **NOTE:** You can put those variables in a file called `.env` in the root folder `the same place where `pyproject.toml` is located.

> **NOTE 2:** You can also set those values under each service `settings.toml` file.

## Installing using Poetry

* [Poetry Documentation](https://python-poetry.org/docs/)

Within each package __fexapi__ or __fexservice__:
```
poetry env use 3.8
poetry shell
poetry install 
```

> **NOTE:** In linux you can simply run `make clean-install` that make command will clean your local environment and install those needed environment.

## Running

> Ensure your have either the database service running or that you are using `sqlite`

> Ensure you have configuration set.

### Fex service

This is the service that fetches data from github and stores data on database.

```bash
cd fexservice
poetry run fexservice
```

### FexAPI

This is the API served by FastAPI

```bash
cd fexapi
uvicorn fexapi.api:app --host=0.0.0.0
```

### Fex UI

This is the static website powered by Vue.js

```bash
cd fexui
python3 -m http.server 5500
```

# Generating changelog with Towncrier

* [Link Pypi Towncrier](https://pypi.org/project/towncrier/)

Towncrier has a few standard types of news fragments, signified by the file extension. These are:
```
.feature: Signifying a new feature.
.bugfix: Signifying a bug fix.
.doc: Signifying a documentation improvement.
.removal: Signifying a deprecation or removal of public API.
.misc: A ticket has been closed, but it is not of interest to users.
```
Example a 25.feature file, where 25 is the issue number and .feature and the type of issue, the issue commit goes inside the file.
The version will be read from __init__ within changes

in terminal:
```
towncrier --name packagename
Is it okay if I remove those files? [Y/n]: n
```

# Attention: to always __follow__ the versioning and semantic releases
* [Guide to semantically versioning code](https://semver.org/)
