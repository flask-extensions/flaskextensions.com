SHELL := /bin/sh
.PHONY: install-requirements build run restart stop logs


install-requirements:
	@curl -fsSL https://get.docker.com -o get-docker.sh && sh get-docker.sh
	pip install docker-compose --user


build:
	@cp -n .example.variables.env .variables.env
	@docker-compose build --force-rm


run:
	@docker-compose up --force-recreate -d


restart:
	@docker-compose restart -t 0


stop:
	@docker-compose down -t 0


logs:
	@docker-compose logs -f

