.PHONY: d-homework-i-run
# Make all actions needed for run homework from zero.
d-homework-i-run:
	make d-run

.PHONY: d-homework-i-purge
# Make all actions needed for purge homework related data.
d-homework-i-purge:
	@make d-purge


.PHONY: d-run
# Just run
#Чтобы это работало необходим docker-compose.yaml - это файл конфигурации для docker-compose
#Linux
#d-run:
#	@COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 \
#		docker-compose up --build
#Windows
d-run:
	@set "COMPOSE_DOCKER_CLI_BUILD=1" & set "DOCKER_BUILDKIT=1" & docker-compose build


.PHONY: d-stop
# Stop services
#Linux
#d-stop:
#	@COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 \
#		docker-compose down
#Windows
d-stop:
	@set "COMPOSE_DOCKER_CLI_BUILD=1" & set "DOCKER_BUILDKIT=1" & docker-compose down

.PHONY: d-purge
# Purge all data related with services
#Linux
#d-purge:
#	@COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 \
#		docker-compose down --volumes --remove-orphans --rmi local --timeout 0
#Windows
d-purge:
	@set "COMPOSE_DOCKER_CLI_BUILD=1" & set "DOCKER_BUILDKIT=1" & docker-compose down --volumes --remove-orphans --rmi local --timeout 0


.PHONY: init-dev
# Init environment for development
init-dev:
	@pip install --upgrade pip && \
	pip install --requirement requirements.txt && \
	pre-commit install

.PHONY: homework-i-run
# Run homework.
homework-i-run:
	@python main.py

.PHONY: homework-i-purge
homework-i-purge:
	@echo Goodbye


.PHONY: pre-commit-run
# Run tools for files from commit.
pre-commit-run:
	@pre-commit run

.PHONY: pre-commit-run-all
# Run tools for all files.
pre-commit-run-all:
	@pre-commit run --all-files