start:  ## Run containers in the background
	@docker compose up -d

stop: ## Stop Containers
	@docker compose down

build: ## Build Containers
	@docker compose build

restart: stop start ## Restart Containers

init: build start migrations migrate  ## Quickly get up and running (start containers and migrate DB)

ssh: ## SSH into running web container
	@docker compose exec web bash

bash: ## Get a bash shell into the web container
	@docker compose run --rm --no-deps web bash

migrations: ## Create DB migrations in the container
	@docker compose run --rm --no-deps web python manage.py makemigrations

migrate: ## Run DB migrations in the container
	@docker compose run --rm --no-deps web python manage.py migrate

shell: ## Get a Django shell
	@docker compose run --rm --no-deps web python manage.py shell