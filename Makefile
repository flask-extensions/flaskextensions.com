SHELL := /bin/sh
.PHONY: install-requirements build run restart stop logs


install-requirements:
	@curl -fsSL https://get.docker.com -o get-docker.sh && sh get-docker.sh
	pip install docker-compose --user


build:
	@cp -n .example.variables.env .variables.env
	@docker-compose build --force-rm


run:
	@docker-compose -f docker-compose.yml -f docker-compose.dev.yml up --force-recreate -d

restart:
	@docker-compose -f docker-compose.yml -f docker-compose.dev.yml restart -t 0


stop:
	@docker-compose -f docker-compose.yml -f docker-compose.dev.yml down -t 0


logs:
	@docker-compose -f docker-compose.yml -f docker-compose.dev.yml logs -f
