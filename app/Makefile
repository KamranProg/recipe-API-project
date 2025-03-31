# -------------------------
# CONFIGURATION
# -------------------------

DOCKER_COMPOSE_DEV = docker compose -f ../docker-compose.dev.yml
DOCKER_COMPOSE_PROD = docker compose -f ../docker-compose.prod.yml

APP_DEV = $(DOCKER_COMPOSE_DEV) run --rm app
APP_PROD = $(DOCKER_COMPOSE_PROD) run --rm app

# -------------------------
# COMMON COMMANDS
# -------------------------

.PHONY: help
help:
	@echo "Makefile Commands:"
	@echo "  make build-dev         - Build dev images"
	@echo "  make build-prod        - Build prod images"
	@echo "  make up-dev            - Start dev environment"
	@echo "  make up-prod           - Start prod environment"
	@echo "  make shell-dev         - Shell into dev container"
	@echo "  make shell-prod        - Shell into prod container"
	@echo "  make migrate           - Run migrations (dev)"
	@echo "  make wait_for_db       - Wait for DB (dev)"
	@echo "  make createsuperuser   - Create superuser (dev)"
	@echo "  make resetdb           - Reset the database with confirmation (dev)"
	@echo "  make resetdb-force     - Reset the database without confirmation (dev)"
	@echo "  make test              - Run tests (dev)"
	@echo "  make lint              - Run flake8 (dev)"
	@echo "  make format            - Format code (black + isort) (dev)"
	@echo "  make check             - Run lint + tests (pre-check) (dev)"
	@echo "  make coverage          - Run tests with coverage report"
	@echo "  make report            - Generate an HTML coverage report"
	@echo "  make requirements      - Freeze pip requirements to requirements.txt"
	@echo "  make clean             - Clean up .pyc and __pycache__ files"
	@echo "  make down              - Stop dev containers"

# -------------------------
# DEVELOPMENT
# -------------------------

createsuperuser:
	$(APP_DEV) python manage.py createsuperuser

resetdb:
	@read -p "⚠️  Are you sure you want to reset the database? This will DELETE all data! (y/N): " confirm && \
	if [ "$$confirm" = "y" ]; then \
		$(APP_DEV) python manage.py flush --no-input && \
		$(APP_DEV) python manage.py migrate; \
	else \
		echo "❌ Reset aborted."; \
	fi

resetdb-force:
	$(APP_DEV) python manage.py flush --no-input && \
	$(APP_DEV) python manage.py migrate

build-dev:
	$(DOCKER_COMPOSE_DEV) build

up-dev:
	$(DOCKER_COMPOSE_DEV) up

shell-dev:
	$(APP_DEV) sh

migrate:
	$(APP_DEV) python manage.py migrate

wait_for_db:
	$(APP_DEV) python manage.py wait_for_db

test:
	$(APP_DEV) pytest -v --tb=short

lint:
	$(APP_DEV) flake8 --config=/app/.flake8

format:
	$(APP_DEV) black . && $(APP_DEV) isort .

check:
	$(MAKE) lint
	$(MAKE) test

coverage:
	$(APP_DEV) pytest --cov=./ --cov-report=term-missing

report:
	$(APP_DEV) pytest --cov=./ --cov-report=html && \
	echo "✅ HTML coverage report generated at htmlcov/index.html"

requirements:
	$(APP_DEV) pip freeze > requirements.txt && \
	echo "✅ requirements.txt updated"

clean:
	find . -name "*.pyc" -delete
	find . -name "__pycache__" -type d -exec rm -r {} + && \
	echo "✅ Cleaned up .pyc and __pycache__ files"

down:
	$(DOCKER_COMPOSE_DEV) down

# -------------------------
# PRODUCTION
# -------------------------

build-prod:
	$(DOCKER_COMPOSE_PROD) build

up-prod:
	$(DOCKER_COMPOSE_PROD) up -d

shell-prod:
	$(APP_PROD) sh
