
up:
	docker compose \
		-f application/docker-compose.yml \
		-f docker-compose.yml --env-file=application/.env.compose up -d --build
down:
	docker compose \
		-f application/docker-compose.yml \
		-f docker-compose.yml down

# Run application locally, while deploying all other services
local:
	docker compose \
		-f application/docker-compose.yml \
		-f docker-compose.yml \
		-f docker-compose.local.yml --env-file=application/.env.local up -d --build
local-down:
	docker compose \
		-f application/docker-compose.yml \
		-f docker-compose.yml \
		-f docker-compose.local.yml down